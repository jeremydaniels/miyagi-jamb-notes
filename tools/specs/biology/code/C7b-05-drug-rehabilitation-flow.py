from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    # Canvas setup
    fig = canvas(12, 12)
    ax = fig.add_subplot(111)
    ax.set_xlim(-6.2, 6.2)
    ax.set_ylim(-6.2, 6.2)
    ax.axis("off")

    # Title
    ax.text(0, 5.5, "The Drug Rehabilitation Process", fontsize=18, fontweight="bold",
            ha="center", va="center", color=INK)

    # 7 Steps definitions
    # Angles: Step 1 at top (90 deg), moving clockwise
    # 90, 90 - 360/7, etc.
    n_steps = 7
    r_center = 3.6
    angles_deg = [90 - i * (360.0 / n_steps) for i in range(n_steps)]

    steps_data = [
        {
            "num": "1",
            "title": "Seeking help",
            "desc": "Person talking to\na family member",
            "color": CREAM,
            "border": DEEP["orange"],
        },
        {
            "num": "2",
            "title": "Assessment",
            "desc": "Doctor evaluation\n& clinical plan",
            "color": BLUE,
            "border": DEEP["blue"],
        },
        {
            "num": "3",
            "title": "Detoxification",
            "desc": "Medical detox in\nsupervised care",
            "color": PINK,
            "border": DEEP["pink"],
        },
        {
            "num": "4",
            "title": "Counselling\nand therapy",
            "desc": "Individual & group\ntherapy sessions",
            "color": LAV,
            "border": DEEP["lav"],
        },
        {
            "num": "5",
            "title": "Skills training",
            "desc": "Vocational skills &\nproductive habits",
            "color": GREEN,
            "border": DEEP["green"],
        },
        {
            "num": "6",
            "title": "Reintegration",
            "desc": "Welcomed home by\nfamily & community",
            "color": CREAM,
            "border": DEEP["orange"],
        },
        {
            "num": "7",
            "title": "After-care\nand support",
            "desc": "Support group &\nrelapse prevention",
            "color": BLUE,
            "border": DEEP["blue"],
        },
    ]

    # Draw central hub circle (soft decorative motif)
    central_circle = patches.Circle((0, 0), 1.6, facecolor="#F8FAFC", edgecolor=GREY, lw=1.5, linestyle="--")
    ax.add_patch(central_circle)
    ax.text(0, 0.25, "Continuous\nRecovery", fontsize=16, fontweight="bold", ha="center", va="center", color=INK)
    ax.text(0, -0.5, "Journey", fontsize=14, ha="center", va="center", color=GREY)

    # Draw curved connecting arrows along the circle
    # Radius for arrows slightly outside or on the circle path
    arrow_r = 3.6
    for i in range(n_steps):
        a_start = angles_deg[i] - 18
        a_end = angles_deg[(i + 1) % n_steps] + 18
        
        # Draw arc with arrow
        arc_patch = patches.Arc(
            (0, 0), arrow_r * 2, arrow_r * 2,
            angle=0, theta1=a_end, theta2=a_start,
            color=GREY, lw=2.5, linestyle="-"
        )
        ax.add_patch(arc_patch)
        
        # Arrowhead at end of arc (clockwise direction)
        tip_rad = np.radians(a_end + 1)
        tip_x = arrow_r * np.cos(tip_rad)
        tip_y = arrow_r * np.sin(tip_rad)
        # Tangent vector for clockwise motion (-sin, cos)
        tangent_rad = tip_rad - np.pi / 2
        dx = 0.2 * np.cos(tangent_rad)
        dy = 0.2 * np.sin(tangent_rad)
        ax.annotate(
            "",
            xy=(tip_x + dx, tip_y + dy),
            xytext=(tip_x - dx * 0.1, tip_y - dy * 0.1),
            arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5, mutation_scale=18)
        )

    # Draw step nodes
    for i, data in enumerate(steps_data):
        deg = angles_deg[i]
        rad = np.radians(deg)
        cx = r_center * np.cos(rad)
        cy = r_center * np.sin(rad)

        # Card / Box dimensions
        box_w = 2.4
        box_h = 1.7  # Increased height to fit two-line titles

        # Rounded rectangle for step content
        rect = patches.FancyBboxPatch(
            (cx - box_w / 2, cy - box_h / 2),
            box_w, box_h,
            boxstyle="round,pad=0.12,rounding_size=0.25",
            facecolor=data["color"],
            edgecolor=data["border"],
            lw=2.2,
            zorder=4
        )
        ax.add_patch(rect)

        # Step number badge
        badge_y = cy + box_h / 2 + 0.1
        badge = patches.Circle((cx, badge_y), 0.28, facecolor=data["border"], edgecolor="white", lw=2, zorder=5)
        ax.add_patch(badge)
        ax.text(cx, badge_y, data["num"], fontsize=14, fontweight="bold", ha="center", va="center", color="white", zorder=6)

        # Title text
        ax.text(
            cx, cy + 0.35, data["title"],
            fontsize=14, fontweight="bold", ha="center", va="center",
            color=INK, zorder=5, linespacing=1.1
        )

        # Description text
        ax.text(
            cx, cy - 0.3, data["desc"],
            fontsize=14, ha="center", va="center",
            color=INK, zorder=5, linespacing=1.1
        )

    save(fig, out)
