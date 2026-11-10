from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Main Title
    ax.text(6, 7.0, "Users of Accounting Information", ha='center', va='center',
            fontsize=18, fontweight='bold', color=INK)

    # Left Container: Internal Users (Green box)
    rect_internal = patches.FancyBboxPatch(
        (0.6, 1.2), 3.2, 5.2,
        boxstyle="round,pad=0.2,rounding_size=0.3",
        facecolor=CREAM, edgecolor=DEEP["green"], linewidth=2.5
    )
    ax.add_patch(rect_internal)
    ax.text(2.2, 6.0, "Internal Users", ha='center', va='center',
            fontsize=16, fontweight='bold', color=DEEP["green"])

    # Internal user items
    internal_users = ["Management", "Employees"]
    y_internal = [4.5, 2.7]
    for text, y in zip(internal_users, y_internal):
        box = patches.FancyBboxPatch(
            (0.9, y - 0.55), 2.6, 1.1,
            boxstyle="round,pad=0.1,rounding_size=0.2",
            facecolor="white", edgecolor=DEEP["green"], linewidth=1.5
        )
        ax.add_patch(box)
        ax.text(2.2, y, text, ha='center', va='center',
                fontsize=15, fontweight='bold', color=INK)

    # Right Container: External Users (Blue box)
    rect_external = patches.FancyBboxPatch(
        (8.2, 0.4), 3.2, 6.0,
        boxstyle="round,pad=0.2,rounding_size=0.3",
        facecolor=CREAM, edgecolor=DEEP["blue"], linewidth=2.5
    )
    ax.add_patch(rect_external)
    ax.text(9.8, 6.05, "External Users", ha='center', va='center',
            fontsize=16, fontweight='bold', color=DEEP["blue"])

    # External user items
    external_users = ["Investors", "Banks", "Government / FIRS", "Creditors", "Public"]
    y_external = [5.1, 4.0, 2.9, 1.8, 0.75]
    for text, y in zip(external_users, y_external):
        box = patches.FancyBboxPatch(
            (8.4, y - 0.4), 2.8, 0.8,
            boxstyle="round,pad=0.1,rounding_size=0.2",
            facecolor="white", edgecolor=DEEP["blue"], linewidth=1.5
        )
        ax.add_patch(box)
        ax.text(9.8, y, text, ha='center', va='center',
                fontsize=14, fontweight='bold', color=INK)

    # Center Circle: Accounting Information
    center_circle = patches.Circle(
        (6.0, 3.7), 1.45,
        facecolor=LAV, edgecolor=DEEP["lav"], linewidth=2.5, zorder=3
    )
    ax.add_patch(center_circle)
    ax.text(6.0, 3.7, "Accounting\nInformation", ha='center', va='center',
            fontsize=16, fontweight='bold', color=INK, zorder=4)

    # Outward Arrows to Internal Users
    for y in y_internal:
        ax.annotate(
            '', xy=(3.5, y), xytext=(4.6, 3.7),
            arrowprops=dict(
                arrowstyle="-|>", color=DEEP["green"],
                lw=2.2, mutation_scale=18, shrinkA=8, shrinkB=6
            )
        )

    # Outward Arrows to External Users
    for y in y_external:
        ax.annotate(
            '', xy=(8.4, y), xytext=(7.4, 3.7),
            arrowprops=dict(
                arrowstyle="-|>", color=DEEP["blue"],
                lw=2.2, mutation_scale=18, shrinkA=8, shrinkB=6
            )
        )

    save(fig, out)
