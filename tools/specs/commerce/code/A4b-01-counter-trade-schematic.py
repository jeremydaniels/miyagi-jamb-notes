from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Circle

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(6, 7.0, "Counter Trade (Barter Agreement)", fontsize=18, fontweight="bold",
            ha="center", va="center", color=INK)

    # Country maps/polygons (schematic / real poly)
    # Get nigeria and brazil polygons
    nig_polys = country_polys("Nigeria")
    bra_polys = country_polys("Brazil")

    # If country_polys works, we transform coordinates to fit into our diagram boxes
    # Nigeria bounding box roughly [2.6, 14.7] E, [4.2, 13.9] N
    # Brazil bounding box roughly [-73.9, -34.7] W, [-33.7, 5.2] S/N
    def plot_transformed_poly(polys, target_cx, target_cy, target_scale, fc, ec):
        # Find global bounds of the provided polygons
        all_pts = np.vstack([p for p in polys if len(p) > 0])
        min_x, max_x = np.min(all_pts[:, 0]), np.max(all_pts[:, 0])
        min_y, max_y = np.min(all_pts[:, 1]), np.max(all_pts[:, 1])
        cx = (min_x + max_x) / 2
        cy = (min_y + max_y) / 2
        max_dim = max(max_x - min_x, max_y - min_y)
        
        for p in polys:
            if len(p) == 0: continue
            tx = (p[:, 0] - cx) / max_dim * target_scale + target_cx
            ty = (p[:, 1] - cy) / max_dim * target_scale + target_cy
            poly = Polygon(np.column_stack([tx, ty]), closed=True, facecolor=fc, edgecolor=ec, lw=1.5, zorder=2)
            ax.add_patch(poly)

    if nig_polys:
        plot_transformed_poly(nig_polys, target_cx=2.3, target_cy=3.6, target_scale=3.0, fc=GREEN, ec=DEEP["green"])
    else:
        # Fallback simplified shape
        ax.add_patch(FancyBboxPatch((0.8, 2.2), 3.0, 2.8, boxstyle="round,pad=0.2", fc=GREEN, ec=DEEP["green"], lw=2))

    if bra_polys:
        plot_transformed_poly(bra_polys, target_cx=9.7, target_cy=3.6, target_scale=3.2, fc=BLUE, ec=DEEP["blue"])
    else:
        # Fallback simplified shape
        ax.add_patch(FancyBboxPatch((8.2, 2.1), 3.0, 3.0, boxstyle="round,pad=0.2", fc=BLUE, ec=DEEP["blue"], lw=2))

    # Country Labels
    ax.text(2.3, 1.6, "NIGERIA", fontsize=16, fontweight="bold", ha="center", va="center", color=INK)
    ax.text(9.7, 1.6, "BRAZIL", fontsize=16, fontweight="bold", ha="center", va="center", color=INK)

    # Oil Derrick Icon over Nigeria
    # Base center at (2.3, 3.2)
    ox, oy = 2.3, 3.1
    derrick_pts = np.array([
        [ox - 0.45, oy],
        [ox - 0.12, oy + 1.2],
        [ox + 0.12, oy + 1.2],
        [ox + 0.45, oy]
    ])
    # Legs
    ax.plot([ox - 0.45, ox - 0.12], [oy, oy + 1.2], color=INK, lw=2.5, zorder=4)
    ax.plot([ox + 0.45, ox + 0.12], [oy, oy + 1.2], color=INK, lw=2.5, zorder=4)
    # Cross bars
    ax.plot([ox - 0.38, ox + 0.22], [oy + 0.35, oy + 0.85], color=INK, lw=1.8, zorder=4)
    ax.plot([ox + 0.38, ox - 0.22], [oy + 0.35, oy + 0.85], color=INK, lw=1.8, zorder=4)
    ax.plot([ox - 0.36, ox + 0.36], [oy + 0.4, oy + 0.4], color=INK, lw=1.8, zorder=4)
    ax.plot([ox - 0.23, ox + 0.23], [oy + 0.85, oy + 0.85], color=INK, lw=1.8, zorder=4)
    # Top block
    ax.plot([ox - 0.16, ox + 0.16], [oy + 1.2, oy + 1.2], color=INK, lw=3, zorder=4)
    ax.plot([ox, ox], [oy + 1.2, oy + 1.45], color=INK, lw=2.5, zorder=4)
    ax.text(ox, oy - 0.35, "Oil Derrick", fontsize=14, ha="center", va="center", color=INK,
            bbox=dict(fc="white", ec="none", pad=1.5))

    # Tractor Icon over Brazil
    tx, ty = 9.7, 3.4
    # Wheels
    rear_wheel = Circle((tx - 0.35, ty), 0.36, facecolor=GREY, edgecolor=INK, lw=2, zorder=4)
    front_wheel = Circle((tx + 0.45, ty - 0.14), 0.22, facecolor=GREY, edgecolor=INK, lw=2, zorder=4)
    ax.add_patch(rear_wheel)
    ax.add_patch(front_wheel)
    # Tractor body
    ax.plot([tx - 0.35, tx + 0.45], [ty, ty - 0.05], color=INK, lw=3, zorder=4) # axle line
    ax.plot([tx - 0.2, tx + 0.5, tx + 0.5, tx + 0.05, tx - 0.2, tx - 0.2],
            [ty + 0.2, ty + 0.2, ty + 0.45, ty + 0.45, ty + 0.6, ty + 0.2],
            color=DEEP["orange"], lw=2.5, zorder=4)
    # Exhaust pipe
    ax.plot([tx + 0.35, tx + 0.35], [ty + 0.45, ty + 0.75], color=INK, lw=2, zorder=4)
    ax.text(tx, ty - 0.65, "Tractor", fontsize=14, ha="center", va="center", color=INK,
            bbox=dict(fc="white", ec="none", pad=1.5))

    # Curved trade arrows
    # Top Arrow: Nigeria to Brazil (Crude Oil Export)
    ax.annotate(
        "", xy=(8.2, 5.3), xytext=(3.8, 5.3),
        arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.7",
                        connectionstyle="arc3,rad=-0.22",
                        color=DEEP["orange"], lw=3.5),
        zorder=3
    )
    ax.text(6.0, 6.1, "Crude Oil Export", fontsize=15, fontweight="bold",
            ha="center", va="center", color=DEEP["orange"],
            bbox=dict(fc="white", ec=DEEP["orange"], lw=1.5, boxstyle="round,pad=0.35"))

    # Bottom Arrow: Brazil to Nigeria (Tractor Import)
    ax.annotate(
        "", xy=(3.8, 2.2), xytext=(8.2, 2.2),
        arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.7",
                        connectionstyle="arc3,rad=-0.22",
                        color=DEEP["green"], lw=3.5),
        zorder=3
    )
    ax.text(6.0, 1.4, "Tractor Import", fontsize=15, fontweight="bold",
            ha="center", va="center", color=DEEP["green"],
            bbox=dict(fc="white", ec=DEEP["green"], lw=1.5, boxstyle="round,pad=0.35"))

    # Big text bubble in the middle
    ax.text(6.0, 3.8, "NO MONEY EXCHANGED,\nDIRECT SWAP", fontsize=15, fontweight="bold",
            ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.6,rounding_size=0.4",
                      facecolor=CREAM, edgecolor=DEEP["pink"], lw=2.5, zorder=5))

    save(fig, out)
