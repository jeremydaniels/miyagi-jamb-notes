from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 6.8)
    ax = fig.add_subplot(111)
    axes_clean(ax, "Quantity (Q)", "Average Cost", 10.5, 9.5)

    # Long-Run Average Cost (LRAC) - broad U-shaped envelope curve
    # Minimum around Q = 5.2, Cost = 2.8
    x_lrac = np.linspace(1.2, 9.2, 300)
    y_lrac = 0.28 * (x_lrac - 5.2)**2 + 2.8
    ax.plot(x_lrac, y_lrac, color=DEEP["blue"], lw=3.8, label="LRAC (Envelope Curve)", zorder=3)

    # SRAC curves touching LRAC at different points:
    srac_params = [
        {"x_tangent": 2.4, "label": "SRAC1", "x_min": 1.2, "x_max": 3.7, "curv": 2.2, "color": DEEP["orange"]},
        {"x_tangent": 4.2, "label": "SRAC2", "x_min": 3.0, "x_max": 5.4, "curv": 2.4, "color": DEEP["green"]},
        {"x_tangent": 6.2, "label": "SRAC3", "x_min": 5.0, "x_max": 7.4, "curv": 2.4, "color": DEEP["pink"]},
        {"x_tangent": 8.0, "label": "SRAC4", "x_min": 6.7, "x_max": 9.2, "curv": 2.2, "color": DEEP["lav"]}
    ]

    for i, p in enumerate(srac_params):
        x0 = p["x_tangent"]
        y0 = 0.28 * (x0 - 5.2)**2 + 2.8
        slope0 = 2 * 0.28 * (x0 - 5.2)
        curv = p["curv"]
        
        xs = np.linspace(p["x_min"], p["x_max"], 150)
        # Quadratic sharing tangent (value & 1st derivative) with LRAC at x0:
        ys = y0 + slope0 * (xs - x0) + curv * (xs - x0)**2
        
        ax.plot(xs, ys, color=p["color"], lw=2.4, ls="--", zorder=4)
        
        # Determine label position manually to avoid overlaps
        if i < 2:
            lbl_x = p["x_min"] + 0.1
            lbl_y = ys[0] + 0.4
        else:
            lbl_x = p["x_max"] - 0.1
            lbl_y = ys[-1] + 0.4
            
        # Specific tweak for SRAC4 to ensure it stays well clear of the curve
        if p["label"] == "SRAC4":
            lbl_x = p["x_max"] - 0.2
            lbl_y = ys[-1] + 0.5
            
        ax.text(lbl_x, min(lbl_y, 9.2), p["label"], color=p["color"],
                fontsize=14, weight="bold", ha="center", va="bottom",
                bbox=dict(fc="white", ec="none", pad=1.5), zorder=5)

    # Label the LRAC curve
    ax.text(9.2, y_lrac[-1] + 0.1, "LRAC\n(Envelope Curve)", color=DEEP["blue"],
            fontsize=15, weight="bold", ha="left", va="center",
            bbox=dict(fc="white", ec="none", pad=2), zorder=5)

    # Economies of Scale annotation (downward-sloping section)
    ax.annotate("Economies of Scale",
                xy=(2.8, 4.4), xytext=(2.0, 8.2),
                fontsize=15, weight="bold", color=INK,
                ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8,
                                connectionstyle="arc3,rad=-0.15"),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"), zorder=5)

    # Diseconomies of Scale annotation (upward-sloping section)
    ax.annotate("Diseconomies of Scale",
                xy=(7.6, 4.6), xytext=(7.8, 8.2),
                fontsize=15, weight="bold", color=INK,
                ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8,
                                connectionstyle="arc3,rad=0.15"),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"), zorder=5)

    # Minimum Efficient Scale helper (subtle dash at bottom)
    min_x = 5.2
    min_y = 2.8
    ax.plot([min_x, min_x], [0, min_y], color=GREY, ls=":", lw=1.5, zorder=1)
    ax.plot([0, min_x], [min_y, min_y], color=GREY, ls=":", lw=1.5, zorder=1)
    ax.text(min_x, -0.6, "Q*", color=INK, fontsize=14, ha="center")
    ax.text(-0.35, min_y, "AC*", color=INK, fontsize=14, ha="right", va="center")

    save(fig, out)
