from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(6.0, 7.0, "Two-Sector Circular Flow of Income", 
            ha="center", va="center", fontsize=18, weight="bold", color=INK)

    # Box dimensions
    box_w, box_h = 2.4, 3.0
    y_box = 2.0
    x_hh = 0.8
    x_firm = 8.8

    # Households box
    hh_rect = patches.FancyBboxPatch((x_hh, y_box), box_w, box_h,
                                     boxstyle="round,pad=0.15,rounding_size=0.2",
                                     facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5)
    ax.add_patch(hh_rect)
    ax.text(x_hh + box_w / 2, y_box + box_h / 2, "Households",
            ha="center", va="center", fontsize=16, weight="bold", color=INK)

    # Firms box
    firm_rect = patches.FancyBboxPatch((x_firm, y_box), box_w, box_h,
                                       boxstyle="round,pad=0.15,rounding_size=0.2",
                                       facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2.5)
    ax.add_patch(firm_rect)
    ax.text(x_firm + box_w / 2, y_box + box_h / 2, "Firms",
            ha="center", va="center", fontsize=16, weight="bold", color=INK)

    # Arrow definitions
    # Flow coordinates:
    x_start_r = x_hh + box_w + 0.15
    x_end_r = x_firm - 0.15

    # 1. Top outer arrow (Money flow): Firms -> Households (Factor Incomes)
    y_top_outer = 5.7
    arrow1 = patches.FancyArrow(x_end_r, y_top_outer, -(x_end_r - x_start_r), 0,
                                 width=0.04, head_width=0.22, head_length=0.35,
                                 length_includes_head=True, fc=DEEP["pink"], ec=DEEP["pink"])
    ax.add_patch(arrow1)
    ax.text(6.0, y_top_outer + 0.35, "Factor Incomes (Wages, Rent, etc.)",
            ha="center", va="center", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # 2. Top inner arrow (Real flow): Households -> Firms (Factors of Production)
    y_top_inner = 4.4
    arrow2 = patches.FancyArrow(x_start_r, y_top_inner, (x_end_r - x_start_r), 0,
                                 width=0.04, head_width=0.22, head_length=0.35,
                                 length_includes_head=True, fc=DEEP["green"], ec=DEEP["green"])
    ax.add_patch(arrow2)
    ax.text(6.0, y_top_inner + 0.35, "Factors of Production",
            ha="center", va="center", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # 3. Bottom inner arrow (Real flow): Firms -> Households (Goods and Services)
    y_bot_inner = 2.6
    arrow3 = patches.FancyArrow(x_end_r, y_bot_inner, -(x_end_r - x_start_r), 0,
                                 width=0.04, head_width=0.22, head_length=0.35,
                                 length_includes_head=True, fc=DEEP["green"], ec=DEEP["green"])
    ax.add_patch(arrow3)
    ax.text(6.0, y_bot_inner - 0.35, "Goods and Services",
            ha="center", va="center", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # 4. Bottom outer arrow (Money flow): Households -> Firms (Consumption Expenditure)
    y_bot_outer = 1.3
    arrow4 = patches.FancyArrow(x_start_r, y_bot_outer, (x_end_r - x_start_r), 0,
                                 width=0.04, head_width=0.22, head_length=0.35,
                                 length_includes_head=True, fc=DEEP["pink"], ec=DEEP["pink"])
    ax.add_patch(arrow4)
    ax.text(6.0, y_bot_outer - 0.35, "Consumption Expenditure",
            ha="center", va="center", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # Legend / Key at bottom
    leg_y = 0.4
    # Real flows key
    ax.plot([2.5, 3.2], [leg_y, leg_y], color=DEEP["green"], lw=3)
    ax.text(3.4, leg_y, "Real flows", va="center", ha="left", fontsize=14, color=INK)

    # Money flows key
    ax.plot([6.8, 7.5], [leg_y, leg_y], color=DEEP["pink"], lw=3)
    ax.text(7.7, leg_y, "Money flows", va="center", ha="left", fontsize=14, color=INK)

    save(fig, out)
