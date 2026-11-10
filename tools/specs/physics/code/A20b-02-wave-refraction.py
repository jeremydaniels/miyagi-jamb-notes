from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Boundary is a horizontal line at y = 3.5
    y_b = 3.5

    # Shading regions
    # Deep water on top (y > 3.5), Shallow water on bottom (y < 3.5)
    ax.fill_between([0, 10], y_b, 7, color=BLUE, alpha=0.25)
    ax.fill_between([0, 10], 0, y_b, color=CREAM, alpha=0.45)

    # Boundary line
    ax.plot([0.5, 9.5], [y_b, y_b], color=INK, lw=2.5)

    # Normal line at x = 5.0
    x_norm = 5.0
    ax.plot([x_norm, x_norm], [1.0, 6.0], color=GREY, lw=2, linestyle="--")
    ax.text(x_norm + 0.15, 5.8, "Normal", fontsize=14, color=INK, fontstyle="italic")

    # Wave parameters
    # Deep water: wave direction angle with normal theta_1 = 45 deg
    # Ray travels downwards and rightwards: unit vector d1 = (sin 45, -cos 45) = (1/sqrt2, -1/sqrt2)
    # Wavefronts are perpendicular to ray: vector parallel to wavefronts is w1 = (cos 45, sin 45) = (1/sqrt2, 1/sqrt2)
    # Wavelength lambda_1 = 1.0
    # Snell's law: sin(theta_1) / lambda_1 = sin(theta_2) / lambda_2
    # Let lambda_2 = 0.55. Then sin(theta_2) = 0.55 * sin(45) = 0.55 * 0.7071 = 0.3889 => theta_2 approx 22.88 deg
    theta_1 = np.radians(45.0)
    theta_2 = np.arcsin(0.55 * np.sin(theta_1))
    
    # Boundary intercept spacing L_b = lambda_1 / sin(theta_1) = lambda_2 / sin(theta_2)
    L_b = 1.0 / np.sin(theta_1)  # approx 1.414

    # Wavefront intercepts along boundary
    # Center around x = 5.0
    k_vals = np.arange(-3, 4)
    x_intercepts = x_norm + k_vals * L_b

    # Draw wavefronts
    for xi in x_intercepts:
        # Deep water segment: line passing through (xi, y_b)
        # Ray direction: (sin theta_1, -cos theta_1).
        # Wavefront normal is ray direction.
        # Wavefront line equation: (x - xi)*sin(theta_1) + (y - y_b)*(-cos(theta_1)) = 0
        # => y - y_b = tan(theta_1) * (x - xi) = 1.0 * (x - xi)
        # For deep water (y >= y_b):
        y_top = 6.6
        x_top = xi + (y_top - y_b) / np.tan(theta_1)
        ax.plot([xi, x_top], [y_b, y_top], color=DEEP["blue"], lw=2.5)

        # Shallow water segment: y <= y_b
        # Ray direction: (sin theta_2, -cos theta_2).
        # Wavefront line: (x - xi)*sin(theta_2) + (y - y_b)*(-cos(theta_2)) = 0
        # => y - y_b = tan(theta_2) * (x - xi)
        y_bot = 0.5
        x_bot = xi + (y_bot - y_b) / np.tan(theta_2)
        ax.plot([x_bot, xi], [y_bot, y_b], color=DEEP["blue"], lw=2.5)

    # Direction of travel (Rays)
    # Ray 1: Deep water towards normal intersection (5.0, y_b)
    # Ray goes along (sin theta_1, -cos theta_1)
    # Path: from (5.0 - 2.8*sin(theta_1), y_b + 2.8*cos(theta_1)) to (5.0, y_b)
    r1_start = (x_norm - 2.8 * np.sin(theta_1), y_b + 2.8 * np.cos(theta_1))
    ax.annotate(
        "", xy=(x_norm, y_b), xytext=r1_start,
        arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", color=DEEP["orange"], lw=3.5)
    )

    # Ray 2: Shallow water, bending towards normal
    # Path: from (5.0, y_b) to (5.0 + 2.6*sin(theta_2), y_b - 2.6*cos(theta_2))
    r2_end = (x_norm + 2.6 * np.sin(theta_2), y_b - 2.6 * np.cos(theta_2))
    ax.annotate(
        "", xy=r2_end, xytext=(x_norm, y_b),
        arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", color=DEEP["orange"], lw=3.5)
    )

    # Text annotations and labels
    # Deep water region labels
    ax.text(1.0, 6.2, "Deep water", fontsize=18, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=3))
    ax.text(1.0, 5.5, "Fast, long wavelength", fontsize=15, color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Shallow water region labels
    ax.text(1.0, 1.8, "Shallow water", fontsize=18, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=3))
    ax.text(1.0, 1.1, "Slow, short wavelength", fontsize=15, color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Boundary label
    ax.text(8.2, y_b + 0.15, "Boundary", fontsize=15, color=INK, ha="center",
            bbox=dict(fc="white", ec="none", pad=2))

    # Ray description annotations
    ax.text(3.3, 4.8, "Wave direction", fontsize=14, color=DEEP["orange"], fontweight="bold",
            rotation=-45, ha="center", va="bottom",
            bbox=dict(fc="white", ec="none", pad=1))
    
    deg2 = np.degrees(theta_2)
    ax.text(5.9, 2.2, "Bends towards\nnormal line", fontsize=14, color=DEEP["orange"],
            fontweight="bold", ha="left", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Wavelength indicators
    # In deep water: between wavefront at xi=5.0 and xi=5.0 - L_b
    # Draw double arrow perpendicular to wavefronts (along ray direction)
    wl1_mid = (x_norm - 1.2 * np.sin(theta_1), y_b + 1.2 * np.cos(theta_1))
    d_perp = 0.5 * 1.0
    p1 = (wl1_mid[0] - d_perp * np.sin(theta_1), wl1_mid[1] + d_perp * np.cos(theta_1))
    p2 = (wl1_mid[0] + d_perp * np.sin(theta_1), wl1_mid[1] - d_perp * np.cos(theta_1))
    ax.annotate("", xy=p1, xytext=p2,
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5))
    ax.text(wl1_mid[0] - 0.5, wl1_mid[1] + 0.1, "λ₁", fontsize=16, color=INK,
            bbox=dict(fc="white", ec="none", pad=1))

    # In shallow water:
    wl2_mid = (x_norm + 1.2 * np.sin(theta_2), y_b - 1.2 * np.cos(theta_2))
    d2_perp = 0.5 * 0.55
    q1 = (wl2_mid[0] - d2_perp * np.sin(theta_2), wl2_mid[1] + d2_perp * np.cos(theta_2))
    q2 = (wl2_mid[0] + d2_perp * np.sin(theta_2), wl2_mid[1] - d2_perp * np.cos(theta_2))
    ax.annotate("", xy=q1, xytext=q2,
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5))
    ax.text(wl2_mid[0] - 0.45, wl2_mid[1] - 0.05, "λ₂", fontsize=16, color=INK,
            bbox=dict(fc="white", ec="none", pad=1))

    save(fig, out)
