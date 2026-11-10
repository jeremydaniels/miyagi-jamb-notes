from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(11, 10.5)
    ax = fig.add_subplot(111)
    
    # Base map of Nigeria
    polys = nigeria_poly()
    if isinstance(polys, np.ndarray) and polys.ndim == 2:
        polys_list = [polys]
    elif isinstance(polys, (list, tuple)):
        if len(polys) > 0 and isinstance(polys[0], np.ndarray) and polys[0].ndim == 2:
            polys_list = polys
        elif len(polys) == 2 and isinstance(polys[0], np.ndarray) and polys[0].ndim == 1:
            polys_list = [np.column_stack((polys[0], polys[1]))]
        else:
            polys_list = [np.asarray(p) for p in polys if np.asarray(p).ndim == 2]
    else:
        polys_list = []

    for poly in polys_list:
        ax.fill(poly[:, 0], poly[:, 1], color=CREAM, ec=DEEP["blue"], lw=1.8, zorder=1)
    
    # Setup axis limits around Nigeria
    ax.set_xlim(2.2, 15.0)
    ax.set_ylim(3.8, 15.0)  # Increased top limit to fit the title
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Industry data: (Longitude, Latitude, label_offset)
    cement = {
        "Sokoto": (5.23, 13.06, (15, 0)),
        "Obajana": (6.43, 7.92, (15, 6)),
        "Ewekoro": (3.21, 6.93, (-25, 15)),  # Cement
        "Nkalagu": (7.77, 6.47, (15, -6))
    }
    
    textiles = {
        "Kano": (8.52, 12.00, (15, 5)),
        "Kaduna": (7.44, 10.52, (-60, 5))
    }
    
    petroleum = {
        "Port Harcourt": (7.01, 4.82, (15, -12)),
        "Warri": (5.75, 5.52, (-50, -18)),
        "Kaduna": (7.44, 10.52, (15, -15)),
        "Lagos": (3.39, 6.45, (-15, -20))  # Petroleum
    }
    
    steel = {
        "Ajaokuta": (6.66, 7.56, (-65, -8)),
        "Aladja": (5.78, 5.51, (15, 6))
    }

    # Style specs
    styles = {
        "Cement": {"marker": "s", "color": DEEP["orange"], "size": 130, "label": "Cement factories"},
        "Textile": {"marker": "^", "color": DEEP["green"], "size": 140, "label": "Textile mills"},
        "Petroleum": {"marker": "o", "color": DEEP["pink"], "size": 130, "label": "Petroleum refineries"},
        "Steel": {"marker": "D", "color": DEEP["lav"], "size": 110, "label": "Iron & Steel"}
    }
    
    # Plot Cement
    for name, (lon, lat, offset) in cement.items():
        ax.scatter(lon, lat, marker=styles["Cement"]["marker"], color=styles["Cement"]["color"],
                   s=styles["Cement"]["size"], edgecolor=INK, linewidth=1.2, zorder=5)
        ax.annotate(name, (lon, lat), xytext=offset, textcoords="offset points",
                    fontsize=14, color=INK, fontweight='medium',
                    bbox=dict(fc="white", ec="none", pad=1.5, alpha=0.85), zorder=6)
        
    # Plot Textiles
    for name, (lon, lat, offset) in textiles.items():
        x_pt, y_pt = (lon - 0.14, lat) if name == "Kaduna" else (lon, lat)
        ax.scatter(x_pt, y_pt, marker=styles["Textile"]["marker"], color=styles["Textile"]["color"],
                   s=styles["Textile"]["size"], edgecolor=INK, linewidth=1.2, zorder=5)
        if name != "Kaduna":
            ax.annotate(name, (lon, lat), xytext=offset, textcoords="offset points",
                        fontsize=14, color=INK, fontweight='medium',
                        bbox=dict(fc="white", ec="none", pad=1.5, alpha=0.85), zorder=6)

    # Plot Petroleum
    for name, (lon, lat, offset) in petroleum.items():
        x_pt, y_pt = (lon + 0.14, lat) if name == "Kaduna" else (lon, lat)
        ax.scatter(x_pt, y_pt, marker=styles["Petroleum"]["marker"], color=styles["Petroleum"]["color"],
                   s=styles["Petroleum"]["size"], edgecolor=INK, linewidth=1.2, zorder=5)
        label_text = "Kaduna (Textile & Refinery)" if name == "Kaduna" else name
        ax.annotate(label_text, (lon, lat), xytext=offset, textcoords="offset points",
                    fontsize=14, color=INK, fontweight='medium',
                    bbox=dict(fc="white", ec="none", pad=1.5, alpha=0.85), zorder=6)

    # Plot Iron & Steel
    for name, (lon, lat, offset) in steel.items():
        x_pt, y_pt = (lon, lat + 0.14) if name == "Aladja" else (lon, lat)
        ax.scatter(x_pt, y_pt, marker=styles["Steel"]["marker"], color=styles["Steel"]["color"],
                   s=styles["Steel"]["size"], edgecolor=INK, linewidth=1.2, zorder=5)
        ax.annotate(name, (lon, lat), xytext=offset, textcoords="offset points",
                    fontsize=14, color=INK, fontweight='medium',
                    bbox=dict(fc="white", ec="none", pad=1.5, alpha=0.85), zorder=6)

    # Title - shifted up and centered
    ax.text(8.6, 14.5, "Major Manufacturing Industries in Nigeria",
            ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

    # Legend elements
    legend_handles = [
        plt.Line2D([0], [0], marker=s["marker"], color='w', markerfacecolor=s["color"],
                   markeredgecolor=INK, markersize=12, label=s["label"])
        for s in styles.values()
    ]
    
    # Legend
    leg = ax.legend(handles=legend_handles, loc="center right", frameon=True,
                    facecolor="white", edgecolor=GREY, fontsize=14, borderpad=0.8,
                    title="Industry Type", title_fontsize=15)
    leg.get_title().set_fontweight('bold')
    
    # Caption
    ax.text(2.6, 4.0, "Sketch map: zones are approximate",
            fontsize=14, fontstyle="italic", color=INK)

    save(fig, out)
