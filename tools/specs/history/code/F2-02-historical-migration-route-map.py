from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, PathPatch
import matplotlib.path as mpath

def draw(out):
    fig = canvas(9, 10)
    ax = fig.add_subplot(111)
    
    # Range covering Southern Africa: Longitude 14 to 38 E, Latitude -36 to -10 S
    lon_min, lon_max = 14, 38
    lat_min, lat_max = -36, -10
    
    ax.set_xlim(lon_min, lon_max)
    ax.set_ylim(lat_min, lat_max)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw Africa continent base
    africa = continent_polys('Africa')
    for p in africa:
        poly_pts = np.array(p)
        poly = Polygon(poly_pts, closed=True, facecolor='#f7f9fa', edgecolor=GREY, lw=1.2, zorder=1)
        ax.add_patch(poly)

    # Rivers / Lakes schematic (Lake Malawi)
    # Approximate Lake Malawi polygon: ~34-35 E, -14.5 to -10 S
    malawi_lats = np.linspace(-14.5, -10, 20)
    malawi_lons = 34.0 + 0.8 * np.sin((malawi_lats + 14.5) / 4.5 * np.pi)
    malawi_poly_pts = np.vstack([
        np.column_stack([malawi_lons, malawi_lats]),
        np.column_stack([malawi_lons[::-1] + 0.6, malawi_lats[::-1]])
    ])
    lake = Polygon(malawi_poly_pts, closed=True, facecolor='#dce9f5', edgecolor=DEEP['blue'], lw=1.0, zorder=2)
    ax.add_patch(lake)
    ax.text(35.2, -12.5, "Lake\nMalawi", fontsize=14, color=DEEP['blue'], ha='left', va='center', style='italic')

    # Cape Colony shaded region in southwest
    cape_poly_pts = np.array([
        [17.5, -32.5],
        [18.4, -34.4],
        [20.0, -34.8],
        [24.0, -34.2],
        [26.5, -33.5],
        [26.0, -31.5],
        [21.0, -31.0],
        [18.5, -30.5],
        [17.5, -32.5]
    ])
    cape_patch = Polygon(cape_poly_pts, closed=True, facecolor='#fceed1', edgecolor=DEEP['orange'], lw=1.5, alpha=0.7, zorder=2)
    ax.add_patch(cape_patch)
    ax.text(21.5, -32.8, "Cape Colony", fontsize=15, color=INK, ha='center', va='center', weight='bold')

    # Zulu Kingdom core area (eastern coast: roughly lon 30.6-32.8, lat -29.5 to -27.2)
    zulu_pts = np.array([
        [30.8, -29.5],
        [32.2, -29.0],
        [32.8, -27.5],
        [31.8, -27.2],
        [30.6, -28.2],
        [30.8, -29.5]
    ])
    zulu_patch = Polygon(zulu_pts, closed=True, facecolor=PINK, edgecolor=DEEP['pink'], lw=2.0, zorder=3)
    ax.add_patch(zulu_patch)
    
    # Label Zulu Kingdom
    ax.annotate("Zulu Kingdom\n(under Shaka)", 
                xy=(31.8, -28.5), xytext=(34.3, -28.5),
                fontsize=14, weight='bold', color=DEEP['pink'], ha='left', va='center',
                arrowprops=dict(arrowstyle="->", color=DEEP['pink'], lw=1.5),
                bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=DEEP['pink'], lw=1.2),
                zorder=6)

    # Mountainous interior region (Sotho / Drakensberg)
    sotho_pts = np.array([
        [27.0, -29.8],
        [28.5, -30.3],
        [29.3, -29.2],
        [28.5, -28.5],
        [27.3, -28.8]
    ])
    sotho_patch = Polygon(sotho_pts, closed=True, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5, ls='--', alpha=0.6, zorder=2)
    ax.add_patch(sotho_patch)

    # Migration Arrows helper
    def draw_curved_arrow(start, control, end, col):
        path = mpath.Path([start, control, end], [mpath.Path.MOVETO, mpath.Path.CURVE3, mpath.Path.CURVE3])
        patch = PathPatch(path, facecolor='none', edgecolor=col, lw=3.2, zorder=4)
        ax.add_patch(patch)
        
        # Tangent vector at the end of quadratic Bezier: B'(1) = 2*(P2 - P1)
        dx = end[0] - control[0]
        dy = end[1] - control[1]
        length = np.hypot(dx, dy)
        dx, dy = dx / length, dy / length
        
        ax.annotate("", xy=end, xytext=(end[0] - 0.05 * dx, end[1] - 0.05 * dy),
                    arrowprops=dict(arrowstyle="-|>", color=col, mutation_scale=22, lw=0),
                    zorder=5)

    # 1. Moshoeshoe (Sotho) - into mountainous interior
    draw_curved_arrow((31.0, -28.8), (29.5, -29.0), (28.2, -29.3), DEEP['green'])
    ax.text(26.2, -27.8, "Moshoeshoe (Sotho)", fontsize=14, color=INK, weight='bold', ha='center',
            bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=DEEP['green'], lw=1.2), zorder=6)

    # 2. Soshangane (Gaza) - pointing north into Mozambique
    draw_curved_arrow((32.0, -27.5), (33.5, -24.5), (34.0, -21.0), DEEP['lav'])
    ax.text(34.8, -23.0, "Soshangane\n(Gaza)", fontsize=14, color=INK, weight='bold', ha='left',
            bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=DEEP['lav'], lw=1.2), zorder=6)

    # 3. Zwangendaba (Ngoni) - pointing far north towards Lake Malawi
    draw_curved_arrow((31.5, -27.2), (32.5, -20.0), (33.8, -14.2), DEEP['blue'])
    ax.text(31.2, -16.0, "Zwangendaba\n(Ngoni)", fontsize=14, color=INK, weight='bold', ha='right',
            bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=DEEP['blue'], lw=1.2), zorder=6)

    # 4. Mzilikazi (Ndebele) - pointing west then north into modern Zimbabwe
    draw_curved_arrow((30.8, -27.8), (27.0, -26.0), (28.0, -23.0), DEEP['orange'])
    draw_curved_arrow((28.0, -23.0), (28.5, -21.5), (29.0, -19.5), DEEP['orange'])
    ax.text(25.5, -21.5, "Mzilikazi\n(Ndebele)", fontsize=14, color=INK, weight='bold', ha='center',
            bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=DEEP['orange'], lw=1.2), zorder=6)

    # Geographical Context Labels
    ax.text(33.0, -32.5, "INDIAN OCEAN", fontsize=15, color=GREY, style='italic', weight='bold')
    ax.text(15.5, -28.0, "ATLANTIC\nOCEAN", fontsize=15, color=GREY, ha='center', style='italic', weight='bold')

    # Title & Subtitle
    ax.text(15.0, -11.2, "The Mfecane Migrations", fontsize=18, weight='bold', color=INK, ha='left')
    ax.text(15.0, -12.3, "Southern Africa, early 19th century", fontsize=14, color=GREY, ha='left')

    # Legend / Caption
    caption = "Sketch map: zones are approximate"
    ax.text(37.5, -35.2, caption, fontsize=14, color=GREY, ha='right', style='italic')

    save(fig, out)
