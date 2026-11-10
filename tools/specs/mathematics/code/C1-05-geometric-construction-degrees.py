from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 8)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.5, 6.5)
    ax.set_ylim(-1.0, 6.2)

    # Origin and key parameters
    O = np.array([2.0, 0.0])
    R = 2.8  # Main compass radius

    # Helper function for arcs
    def draw_arc(center, r, theta1_deg, theta2_deg, color=GREY, lw=1.5, ls='-'):
        t = np.linspace(np.radians(theta1_deg), np.radians(theta2_deg), 100)
        x = center[0] + r * np.cos(t)
        y = center[1] + r * np.sin(t)
        ax.plot(x, y, color=color, lw=lw, ls=ls)

    # Baseline AB
    ax.plot([-0.5, 5.8], [0.0, 0.0], color=INK, lw=2.5)
    ax.plot(O[0], O[1], 'o', color=INK, ms=5)

    # 1. Main arc from baseline
    draw_arc(O, R, 0, 135, color=DEEP["blue"], lw=1.8)

    # Key points on the main arc
    P_0 = O + np.array([R, 0.0])
    rad60 = np.radians(60)
    rad120 = np.radians(120)
    rad75 = np.radians(75)

    P_60 = O + R * np.array([np.cos(rad60), np.sin(rad60)])
    P_120 = O + R * np.array([np.cos(rad120), np.sin(rad120)])
    P_90 = O + np.array([0.0, R])

    # 2. Construction arcs cutting 60° and 120° on the main arc (radius R)
    # Arc from P_0 intersecting main arc at 60°
    draw_arc(P_0, R, 110, 130, color=GREY, lw=1.4)
    # Arc from P_60 intersecting main arc at 120°
    draw_arc(P_60, R, 110, 130, color=GREY, lw=1.4)

    # 3. Intersecting arcs above for 90°
    # Distance between P_60 and P_120 is R. Intersection point at 90°:
    # y = sqrt(R^2 - (R/2)^2) + R*sin(60) = R*sqrt(3)/2 + R*sqrt(3)/2 = R*sqrt(3)
    # Let's verify: center P_60=(R/2, R*sqrt(3)/2), center P_120=(-R/2, R*sqrt(3)/2).
    # Midpoint is (0, R*sqrt(3)/2). Distance to both is R/2, height above midpoint is sqrt(R^2 - R^2/4) = R*sqrt(3)/2.
    # Total y = R*sqrt(3).
    # From P_60: vector to intersection is (-R/2, R*sqrt(3)/2) -> angle is 120°.
    # From P_120: vector to intersection is (R/2, R*sqrt(3)/2) -> angle is 60°.
    draw_arc(P_60, R, 105, 135, color=GREY, lw=1.4)
    draw_arc(P_120, R, 45, 75, color=GREY, lw=1.4)

    # Dotted 90° line through the intersection
    I_90 = O + np.array([0.0, R * np.sqrt(3)])
    ax.plot([O[0], O[0]], [O[1], I_90[1] + 0.3], color=GREY, lw=1.8, ls=':')

    # Faint guide line for 60°
    P_60_ext = O + 3.8 * np.array([np.cos(rad60), np.sin(rad60)])
    ax.plot([O[0], P_60_ext[0]], [O[1], P_60_ext[1]], color=GREY, lw=1.4, ls='--')

    # 4. Construction arcs bisecting the space between 60° and 90° (from P_60 and P_90)
    # Distance between P_60 and P_90 on circle of radius R:
    # theta_diff = 30° => chord length d = 2*R*sin(15°) ≈ 0.5176 * R ≈ 1.45
    # Choose compass radius r_bisect = 1.6
    r_bisect = 1.6
    # Midpoint of P_60 and P_90 is at angle 75°, distance R*cos(15°) from O
    mid_60_90 = 0.5 * (P_60 + P_90)
    half_chord = R * np.sin(np.radians(15))
    h_bisect = np.sqrt(r_bisect**2 - half_chord**2)
    # Bisector intersection point (outer one):
    dir_75 = np.array([np.cos(rad75), np.sin(rad75)])
    I_75 = mid_60_90 + h_bisect * dir_75

    # Angles from centers to I_75:
    v_from_60 = I_75 - P_60
    ang_from_60 = np.degrees(np.arctan2(v_from_60[1], v_from_60[0]))
    v_from_90 = I_75 - P_90
    ang_from_90 = np.degrees(np.arctan2(v_from_90[1], v_from_90[0]))

    # Draw arcs cleanly crossing at I_75
    draw_arc(P_60, r_bisect, ang_from_60 - 20, ang_from_60 + 20, color=DEEP["pink"], lw=1.8)
    draw_arc(P_90, r_bisect, ang_from_90 - 20, ang_from_90 + 20, color=DEEP["pink"], lw=1.8)

    # 5. Solid final line for 75° passing through the intersection I_75
    P_75_end = O + 5.0 * dir_75
    ax.plot([O[0], P_75_end[0]], [O[1], P_75_end[1]], color=DEEP["green"], lw=3.0)

    # 75° angle arc indicator near O
    draw_arc(O, 1.0, 0, 75, color=DEEP["green"], lw=2.0)

    # Highlight the intersection points
    ax.plot(I_75[0], I_75[1], 'o', color=DEEP["pink"], ms=4)
    ax.plot(I_90[0], I_90[1], 'o', color=GREY, ms=4)
    ax.plot(P_60[0], P_60[1], 'o', color=GREY, ms=3.5)
    ax.plot(P_90[0], P_90[1], 'o', color=GREY, ms=3.5)

    # Labels and Annotations
    ax.text(O[0] - 0.15, -0.35, "O", fontsize=16, color=INK, fontweight="bold", ha="center")
    ax.text(-0.4, -0.35, "A", fontsize=16, color=INK, ha="center")
    ax.text(5.6, -0.35, "B", fontsize=16, color=INK, ha="center")

    # Angle annotations
    ax.text(P_60[0] + 0.35, P_60[1] - 0.15, "60°", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=1))
    ax.text(P_120[0] - 0.45, P_120[1] - 0.15, "120°", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=1))
    ax.text(O[0] - 0.35, P_90[1] + 0.1, "90°", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=1))

    # Angle arc label 75°
    ax.text(O[0] + 0.65, 1.25, "75°", fontsize=16, color=DEEP["green"], fontweight="bold",
            bbox=dict(fc="white", ec="none", pad=1))

    # Ray label at top of 75° line
    ax.text(P_75_end[0] + 0.1, P_75_end[1] + 0.1, "75°", fontsize=16,
            color=DEEP["green"], fontweight="bold")

    # Title with comfortable margin above top construction
    ax.text(2.5, 5.8, "Construction of a 75° Angle", fontsize=18,
            fontweight="bold", color=INK, ha="center")

    save(fig, out)
