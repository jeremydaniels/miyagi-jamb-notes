from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 9)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # Titles
    ax.text(3.5, 8.2, "Inductive Reasoning\n(Bottom-Up)", fontsize=18, fontweight="bold",
            color=INK, ha="center", va="center")
    ax.text(10.5, 8.2, "Deductive Reasoning\n(Top-Down)", fontsize=18, fontweight="bold",
            color=INK, ha="center", va="center")

    # Box coordinates and definitions
    # Inductive steps from bottom (y=1.0) to top (y=6.4)
    inductive_steps = [
        "Specific Observations & Data",
        "Detecting Patterns",
        "Formulating a Hypothesis",
        "General Theory"
    ]
    
    # Deductive steps from top (y=6.4) to bottom (y=1.0)
    deductive_steps = [
        "General Theory",
        "Hypothesis",
        "Observation & Testing",
        "Specific Conclusion"
    ]

    y_levels = [1.3, 3.0, 4.7, 6.4]  # Bottom to top levels

    box_w = 4.4
    box_h = 0.9

    # Draw Inductive Boxes (Left: center x = 3.5)
    for i, text in enumerate(inductive_steps):
        yc = y_levels[i]
        rect = patches.FancyBboxPatch(
            (3.5 - box_w / 2, yc - box_h / 2),
            box_w, box_h,
            boxstyle="round,pad=0.1,rounding_size=0.2",
            facecolor=BLUE,
            edgecolor=DEEP["blue"],
            linewidth=2.0
        )
        ax.add_patch(rect)
        ax.text(3.5, yc, text, fontsize=15, fontweight="semibold",
                color=INK, ha="center", va="center")

    # Draw Inductive Connecting Arrows (Upward)
    for i in range(3):
        y_start = y_levels[i] + box_h / 2 + 0.08
        y_end = y_levels[i+1] - box_h / 2 - 0.08
        ax.annotate(
            "",
            xy=(3.5, y_end),
            xytext=(3.5, y_start),
            arrowprops=dict(
                arrowstyle="-|>",
                color=DEEP["blue"],
                lw=3,
                mutation_scale=22
            )
        )

    # Draw Deductive Boxes (Right: center x = 10.5)
    # Deductive goes top-down: y_levels[3], y_levels[2], y_levels[1], y_levels[0]
    for i, text in enumerate(deductive_steps):
        yc = y_levels[3 - i]
        rect = patches.FancyBboxPatch(
            (10.5 - box_w / 2, yc - box_h / 2),
            box_w, box_h,
            boxstyle="round,pad=0.1,rounding_size=0.2",
            facecolor=ORANGE,
            edgecolor=DEEP["orange"],
            linewidth=2.0
        )
        ax.add_patch(rect)
        ax.text(10.5, yc, text, fontsize=15, fontweight="semibold",
                color=INK, ha="center", va="center")

    # Draw Deductive Connecting Arrows (Downward)
    for i in range(3):
        y_start = y_levels[3 - i] - box_h / 2 - 0.08
        y_end = y_levels[2 - i] + box_h / 2 + 0.08
        ax.annotate(
            "",
            xy=(10.5, y_end),
            xytext=(10.5, y_start),
            arrowprops=dict(
                arrowstyle="-|>",
                color=DEEP["orange"],
                lw=3,
                mutation_scale=22
            )
        )

    # Dividing separator line in the middle
    ax.plot([7.0, 7.0], [0.8, 8.6], color=GREY, lw=1.5, linestyle="--")

    save(fig, out)
