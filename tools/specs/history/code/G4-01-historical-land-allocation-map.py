from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # Base South Africa landmass
    sa_polys = country_polys("South Africa")
    for poly in sa_polys:
        ax.fill(poly[:, 0], poly[:, 1], color=CREAM, ec=INK, lw=1.5, zorder=1)

    # Lesotho and Eswatini (Swaziland) inside SA
    try:
        lesotho_polys = country_polys("Lesotho")
        for poly in lesotho_polys:
            ax.fill(poly[:, 0], poly[:, 1], color="#EEEEEE", ec=GREY, lw=1.2, ls="--", zorder=2)
            ax.text(np.mean(poly[:, 0]), np.mean(poly[:, 1]), "Basutoland\n(Lesotho)", 
                    fontsize=14, color=GREY, ha="center", va="center", style="italic", zorder=4)
    except Exception:
        pass

    try:
        eswatini_polys = country_polys("eSwatini")
        for poly in eswatini_polys:
            ax.fill(poly[:, 0], poly[:, 1], color="#EEEEEE", ec=GREY, lw=1.2, ls="--", zorder=2)
            ax.text(np.mean(poly[:, 0]), np.mean(poly[:, 1]), "Swaziland", 
                    fontsize=14, color=GREY, ha="center", va="center", style="italic", zorder=4)
    except Exception:
        pass

    # Schematic "Native Reserves" (~13% allocated under 1913/1936 Land Acts)
    reserves_coords = [
        [[27.8, -31.5], [29.8, -31.0], [30.1, -31.8], [28.5, -33.0], [27.5, -32.5]], # Transkei
        [[26.6, -32.8], [27.5, -32.7], [27.6, -33.4], [26.8, -33.3]],                # Ciskei
        [[31.2, -28.8], [32.3, -27.5], [32.8, -27.8], [32.1, -29.2]],                # Zululand
        [[30.4, -30.0], [30.9, -29.5], [31.2, -30.2]],                               # Natal fragment
        [[24.5, -27.3], [25.5, -27.1], [25.3, -27.8], [24.3, -27.7]],                # North West fragment 1
        [[25.1, -25.8], [26.0, -25.5], [25.8, -26.2], [24.8, -26.3]],                # North West fragment 2
        [[27.3, -25.4], [28.2, -25.1], [28.0, -25.7], [27.1, -25.8]],                # North West fragment 3
        [[29.3, -24.3], [30.5, -23.8], [30.2, -24.7], [29.1, -24.8]],                # Northern Transvaal
        [[29.8, -23.1], [30.8, -22.8], [30.6, -23.4]],                               # Venda area
        [[30.8, -24.8], [31.5, -24.5], [31.4, -25.3], [30.7, -25.2]],                # Eastern Transvaal
        [[28.7, -28.5], [29.1, -28.4], [28.9, -28.8]],                               # Free State fragment
    ]

    for pts in reserves_coords:
        patch = patches.Polygon(pts, closed=True, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.3, zorder=3)
        ax.add_patch(patch)

    # Major cities & mines
    cities = [
        ("Cape Town", (18.42, -33.92), (15.5, -34.5)),
        ("Kimberley\n(Diamonds)", (24.76, -28.74), (22.0, -29.2)),
        ("Johannesburg\n(Gold Reef)", (28.04, -26.20), (28.04, -27.6)),
        ("Durban", (31.02, -29.86), (33.2, -30.5)),  # Pointer clearly points to East Coast
        ("Pretoria", (28.23, -25.75), (28.23, -24.3)),
    ]

    for name, pt, text_pt in cities:
        ax.plot(pt[0], pt[1], marker="o", color=DEEP["blue"], markersize=7, zorder=6)
        ax.annotate(
            name, xy=pt, xytext=text_pt,
            fontsize=14, color=INK, weight="bold", zorder=7, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.9),
            arrowprops=dict(arrowstyle="-", color=INK, lw=1.2)
        )

    # Ocean labels
    ax.text(15.5, -31.5, "ATLANTIC\nOCEAN", fontsize=15, color=GREY, ha="center", style="italic")
    ax.text(33.8, -33.5, "INDIAN\nOCEAN", fontsize=15, color=GREY, ha="center", style="italic")

    # Title & Subtitle (Top Left)
    ax.text(14.5, -21.4, "Land Allocation in South Africa (1913–1936)", fontsize=18, weight="bold", color=INK)
    ax.text(14.5, -22.2, "Segregation under the Natives Land Acts", fontsize=15, color=DEEP["blue"])

    # Legend / Key (Moved to bottom left to avoid intersecting map boundaries)
    l_x, l_y = 14.5, -36.0
    r1 = patches.Rectangle((l_x, l_y), 1.3, 0.8, facecolor=CREAM, edgecolor=INK, lw=1.2, zorder=5)
    ax.add_patch(r1)
    ax.text(l_x + 1.8, l_y + 0.4, '87% "White areas"\n(Major cities, mines & fertile farmland)',
            fontsize=14, va="center", color=INK)

    r2 = patches.Rectangle((l_x, l_y - 1.6), 1.3, 0.8, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.2, zorder=5)
    ax.add_patch(r2)
    ax.text(l_x + 1.8, l_y - 1.2, '13% "Native Reserves"\n(Allocated for African population)',
            fontsize=14, va="center", color=INK)

    # Note
    ax.text(14.5, -38.3, "Sketch map: zones are approximate", fontsize=14, color=GREY, style="italic")

    ax.set_xlim(14.0, 35.5)
    ax.set_ylim(-38.8, -20.5)

    save(fig, out)
