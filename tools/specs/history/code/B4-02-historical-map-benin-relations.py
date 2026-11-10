from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # Spatial extent representing southern/central Nigeria
    ax.set_xlim(4.2, 8.6)
    ax.set_ylim(4.5, 8.9)

    # Simplified coastline of the Bight of Benin / Niger Delta
    coast_x = np.linspace(4.2, 8.6, 100)
    coast_y = 5.35 - 0.25 * np.sin((coast_x - 4.2) * 1.5) - 0.15 * (coast_x - 6.0)**2 / 4.0
    ax.fill_between(coast_x, 4.3, coast_y, color=BLUE, alpha=0.35, zorder=1)
    ax.plot(coast_x, coast_y, color=DEEP["blue"], lw=1.8, zorder=2)
    ax.text(4.7, 4.95, "Gulf of Guinea / Bight of Benin", fontsize=14, color=DEEP["blue"], style="italic")

    # Schematic Niger River course
    # Terminate below the title area (stops at y=8.2) so it does not cross any title
    niger_pts = np.array([
        [6.75, 8.15],
        [6.80, 7.8],
        [6.82, 7.2],
        [6.75, 6.6],
        [6.65, 6.2],
        [6.4, 5.7],
        [6.1, 5.3]
    ])
    t = np.linspace(0, 1, len(niger_pts))
    t_fine = np.linspace(0, 1, 100)
    rx = np.interp(t_fine, t, niger_pts[:, 0])
    ry = np.interp(t_fine, t, niger_pts[:, 1])
    ax.plot(rx, ry, color=DEEP["blue"], lw=3.5, zorder=3, alpha=0.8)

    # River label along its course
    ax.text(7.05, 6.9, "Niger River", fontsize=15, color=DEEP["blue"], weight="bold",
            rotation=-75, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85), zorder=4)

    # Region shading for Benin Core Kingdom / Empire
    benin_poly = plt.Circle((5.7, 6.35), 0.65, color=ORANGE, alpha=0.3, ec=DEEP["orange"], lw=2.2, zorder=2)
    ax.add_patch(benin_poly)

    # Center label: Benin Empire
    ax.text(5.7, 6.35, "Benin\nEmpire", fontsize=16, fontweight="bold", color=INK,
            ha="center", va="center", bbox=dict(boxstyle="round,pad=0.35", fc=CREAM, ec=DEEP["orange"], lw=2), zorder=6)

    # Distinct outward arrows from Benin to neighbouring regions
    # (start_pt, end_pt, color)
    arrows = [
        # West towards Akure and Ekiti (Yorubaland)
        ((5.25, 6.65), (4.75, 7.05), DEEP["green"]),
        # North towards Nupe
        ((5.85, 6.85), (6.10, 7.85), DEEP["lav"]),
        # North towards Afenmai
        ((5.65, 6.85), (5.55, 7.35), DEEP["lav"]),
        # Northeast towards Esan (Ishan)
        ((6.15, 6.65), (6.70, 6.95), DEEP["pink"]),
        # East across Niger River towards Western Igbo (Asaba/Agbor)
        # Starts east of Benin center (6.25, 6.35) and points across river (rx~6.7) to (7.25, 6.35)
        ((6.25, 6.35), (7.15, 6.35), DEEP["blue"]),
        # South-west towards Itsekiri
        ((5.40, 5.95), (4.95, 5.65), DEEP["green"]),
        # South towards Urhobo / Niger Delta
        ((5.80, 5.85), (5.95, 5.45), DEEP["orange"]),
    ]

    for start, end, col in arrows:
        ax.annotate(
            "",
            xy=end,
            xytext=start,
            arrowprops=dict(
                arrowstyle="-|>,head_width=0.45,head_length=0.7",
                color=col,
                lw=2.8,
                mutation_scale=15
            ),
            zorder=5
        )

    # Region Labels with white bounding boxes
    ax.text(4.55, 7.3, "Yorubaland\n(Akure & Ekiti)", fontsize=15, ha="center", va="center",
            fontweight="bold", color=INK, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2), zorder=6)

    ax.text(6.15, 8.1, "Nupe", fontsize=15, ha="center", va="center",
            fontweight="bold", color=INK, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2), zorder=6)

    ax.text(5.5, 7.55, "Afenmai", fontsize=15, ha="center", va="center",
            fontweight="bold", color=INK, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2), zorder=6)

    ax.text(7.1, 7.25, "Esan", fontsize=15, ha="center", va="center",
            fontweight="bold", color=INK, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2), zorder=6)

    ax.text(7.85, 6.35, "Western Igbo\n(Asaba / Agbor)", fontsize=15, ha="center", va="center",
            fontweight="bold", color=INK, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2), zorder=6)

    ax.text(4.65, 5.5, "Itsekiri", fontsize=15, ha="center", va="center",
            fontweight="bold", color=INK, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2), zorder=6)

    ax.text(6.25, 5.25, "Urhobo\n(Niger Delta)", fontsize=15, ha="center", va="center",
            fontweight="bold", color=INK, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2), zorder=6)

    # Title & Caption (Title placed high at y=8.65, completely clear of any river lines or labels)
    ax.text(6.4, 8.65, "Kingdom of Benin & Regional Relations (mid-19th C.)",
            fontsize=16, fontweight="bold", ha="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.95))

    ax.text(4.35, 4.65, "Sketch map: zones are approximate",
            fontsize=14, fontstyle="italic", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85))

    save(fig, out)
