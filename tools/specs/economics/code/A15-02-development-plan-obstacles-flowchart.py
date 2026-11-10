from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    # Canvas setup
    fig = canvas(12, 11)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Top Goal Box
    goal_box = patches.FancyBboxPatch(
        (15, 84), 70, 11,
        boxstyle="round,pad=1.0",
        fc=BLUE, ec=DEEP["blue"], lw=2.5
    )
    ax.add_patch(goal_box)
    ax.text(50, 91.5, "Development Plan Goals", ha="center", va="center",
            fontsize=17, weight="bold", color=INK)
    ax.text(50, 86.5, "(Job creation, Infrastructure, Education)", ha="center", va="center",
            fontsize=14, style="italic", color=INK)

    # Four Hurdles (Red / Pink Bricks blocking the path)
    hurdles = [
        "Corruption",
        "Lack of\nAccurate Data",
        "Policy\nSomersault",
        "Reliance on\nOil Revenue"
    ]
    xs = [7, 29.5, 52, 74.5]
    brick_w = 18.5
    brick_h = 9.5
    brick_y = 63.5

    for i, (hx, text) in enumerate(zip(xs, hurdles)):
        # Arrow pointing down from Top Box towards implementation, interrupted/blocked at brick
        ax.annotate("", xy=(hx + brick_w / 2, brick_y + brick_h),
                    xytext=(hx + brick_w / 2, 84),
                    arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=2.2, mutation_scale=16))

        # Brick patch
        brick = patches.Rectangle(
            (hx, brick_y), brick_w, brick_h,
            fc=PINK, ec=DEEP["pink"], lw=2.5
        )
        ax.add_patch(brick)
        ax.text(hx + brick_w / 2, brick_y + brick_h / 2, text,
                ha="center", va="center", fontsize=14, weight="bold", color=INK)

        # Blocked / severed path below brick (dashed red line with an 'X' block symbol)
        ax.plot([hx + brick_w / 2, hx + brick_w / 2], [brick_y, 45],
                color=DEEP["pink"], lw=2, ls="--")
        ax.text(hx + brick_w / 2, 53, "✕", color=DEEP["pink"],
                ha="center", va="center", fontsize=18, weight="bold", bbox=dict(fc="white", ec="none", pad=1))

    # Implementation Phase Box
    imp_box = patches.FancyBboxPatch(
        (25, 33), 50, 9,
        boxstyle="round,pad=0.8",
        fc=CREAM, ec=ORANGE, lw=2.5, ls="--"
    )
    ax.add_patch(imp_box)
    ax.text(50, 37.5, "Implementation Phase", ha="center", va="center",
            fontsize=16, weight="bold", color=INK)

    # Arrow from Implementation to Stalled Outcome
    ax.annotate("", xy=(50, 21), xytext=(50, 33),
                arrowprops=dict(arrowstyle="-|>", color=GREY, lw=2.5, mutation_scale=18))

    # Broken Gear Helper Function
    def draw_broken_gear(cx, cy, r_out=7.5, r_in=5.0, teeth=10):
        angles = np.linspace(0, 2 * np.pi, teeth * 2, endpoint=False)
        pts = []
        for i, a in enumerate(angles):
            r = r_out if (i % 2 == 0) else r_in
            pts.append([cx + r * np.cos(a), cy + r * np.sin(a)])
        pts = np.array(pts)
        
        # Split gear into two cracked halves
        poly_left = []
        poly_right = []
        for pt in pts:
            if pt[0] < cx - 0.4:
                poly_left.append(pt)
            elif pt[0] > cx + 0.4:
                poly_right.append(pt)
        
        # Left half
        poly1 = patches.Polygon(np.array(poly_left), closed=False, fc=LAV, ec=DEEP["lav"], lw=2.5)
        # Right half
        poly2 = patches.Polygon(np.array(poly_right), closed=False, fc=LAV, ec=DEEP["lav"], lw=2.5)
        ax.add_patch(poly1)
        ax.add_patch(poly2)

        # Center cracked hole
        ax.plot([cx, cx - 1.5, cx + 1.2, cx], [cy + 7, cy + 2, cy - 2, cy - 7],
                color=DEEP["pink"], lw=3)

    draw_broken_gear(30, 12, r_out=6.5, r_in=4.5, teeth=10)

    # Bottom Label: Stalled Economic Development
    stalled_box = patches.FancyBboxPatch(
        (42, 6.5), 45, 11,
        boxstyle="round,pad=0.8",
        fc=LAV, ec=DEEP["lav"], lw=2.5
    )
    ax.add_patch(stalled_box)
    ax.text(64.5, 12, "Stalled Economic Development", ha="center", va="center",
            fontsize=15, weight="bold", color=INK)

    save(fig, out)
