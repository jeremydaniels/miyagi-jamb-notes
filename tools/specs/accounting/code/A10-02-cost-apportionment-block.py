import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Polygon
from style import *

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Helper function to draw a stylized coin stack
    def draw_stack(cx, cy, num_coins, r_w=0.9, r_h=0.15, step=0.18, face_col=CREAM, edge_col=DEEP["orange"]):
        for i in range(num_coins):
            y = cy + i * step
            # Cylinder side/body
            rect = Rectangle((cx - r_w, y), 2 * r_w, step, fc=face_col, ec=edge_col, lw=1.5)
            ax.add_patch(rect)
            # Elliptical top
            theta = np.linspace(0, 2 * np.pi, 50)
            ex = cx + r_w * np.cos(theta)
            ey = y + step + r_h * np.sin(theta)
            ax.fill(ex, ey, color=face_col)
            ax.plot(ex, ey, color=edge_col, lw=1.5)

    # 1. Total Rent Stack (Left)
    draw_stack(2.0, 1.8, num_coins=9, r_w=0.85, r_h=0.15, step=0.22, face_col=CREAM, edge_col=DEEP["orange"])
    
    ax.text(2.0, 4.4, "Total Rent\n₦60,000", ha="center", va="bottom", fontsize=16, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2))

    # 2. Floor Plan Diagram (Middle)
    # Total area: 600 sq m (400 Factory : 200 Office -> 2:1 ratio)
    fp_x, fp_y, fp_w, fp_h = 4.3, 2.0, 3.2, 3.5
    
    # Factory: lower 2/3 (or split left/right, let's split horizontally: top Factory 2/3, bottom Office 1/3)
    # Let's do Factory (h = 2.3) and Office (h = 1.2)
    fact_h = fp_h * (2/3)
    off_h = fp_h * (1/3)

    # Office rectangle (bottom)
    rect_off = Rectangle((fp_x, fp_y), fp_w, off_h, fc=BLUE, ec=DEEP["blue"], lw=2)
    ax.add_patch(rect_off)
    ax.text(fp_x + fp_w/2, fp_y + off_h/2, "Office\n(200 sq m)", ha="center", va="center", fontsize=14, weight="bold", color=INK)

    # Factory rectangle (top)
    rect_fact = Rectangle((fp_x, fp_y + off_h), fp_w, fact_h, fc=GREEN, ec=DEEP["green"], lw=2)
    ax.add_patch(rect_fact)
    ax.text(fp_x + fp_w/2, fp_y + off_h + fact_h/2, "Factory\n(400 sq m)", ha="center", va="center", fontsize=15, weight="bold", color=INK)

    # Floor plan overall title & ratio badge
    ax.text(fp_x + fp_w/2, fp_y + fp_h + 0.3, "Floor Plan (600 sq m)", ha="center", va="bottom", fontsize=15, weight="bold", color=INK)
    ax.text(fp_x + fp_w/2, fp_y - 0.45, "Ratio 2 : 1", ha="center", va="center", fontsize=15, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc=LAV, ec=DEEP["lav"], lw=1.5))

    # Arrow from Total Stack to Floor Plan
    ax.annotate("", xy=(fp_x - 0.15, fp_y + fp_h/2), xytext=(2.95, fp_y + fp_h/2),
                arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", color=INK, lw=2.5))
    ax.text((2.95 + fp_x - 0.15)/2, fp_y + fp_h/2 + 0.3, "Apportioned\nby area", ha="center", va="bottom", fontsize=14, color=INK)

    # 3. Two Split Piles (Right)
    # Factory Pile (Upper Right) - 6 coins
    fact_stack_x, fact_stack_y = 10.2, 4.0
    draw_stack(fact_stack_x, fact_stack_y, num_coins=6, r_w=0.75, r_h=0.12, step=0.2, face_col=GREEN, edge_col=DEEP["green"])
    ax.text(fact_stack_x, fact_stack_y + 6 * 0.2 + 0.4, "Factory: ₦40,000", ha="center", va="bottom", fontsize=15, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["green"], lw=1.5))

    # Arrow Factory -> Factory Pile
    ax.annotate("", xy=(fact_stack_x - 0.9, fact_stack_y + 0.6), xytext=(fp_x + fp_w + 0.1, fp_y + off_h + fact_h/2),
                arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", color=DEEP["green"], lw=2.5))
    ax.text(8.75, 4.95, "400/600 (⅔)", ha="center", va="center", fontsize=14, color=DEEP["green"], weight="bold",
            bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none"))

    # Office Pile (Lower Right) - 3 coins
    off_stack_x, off_stack_y = 10.2, 1.2
    draw_stack(off_stack_x, off_stack_y, num_coins=3, r_w=0.75, r_h=0.12, step=0.2, face_col=BLUE, edge_col=DEEP["blue"])
    ax.text(off_stack_x, off_stack_y + 3 * 0.2 + 0.4, "Office: ₦20,000", ha="center", va="bottom", fontsize=15, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["blue"], lw=1.5))

    # Arrow Office -> Office Pile
    ax.annotate("", xy=(off_stack_x - 0.9, off_stack_y + 0.4), xytext=(fp_x + fp_w + 0.1, fp_y + off_h/2),
                arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", color=DEEP["blue"], lw=2.5))
    ax.text(8.75, 2.05, "200/600 (⅓)", ha="center", va="center", fontsize=14, color=DEEP["blue"], weight="bold",
            bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none"))

    # Main Title
    ax.text(6.0, 6.55, "Cost Apportionment by Floor Area", ha="center", va="center", fontsize=18, weight="bold", color=INK)

    save(fig, out)
