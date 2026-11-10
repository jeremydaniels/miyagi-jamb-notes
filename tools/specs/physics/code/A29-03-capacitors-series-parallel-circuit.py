from style import *
import numpy as np

def draw_capacitor_h(ax, cx, cy, d=0.28, h=0.8, lw=2.5, color=INK):
    """Horizontal capacitor: two vertical parallel plates."""
    ax.plot([cx - d/2, cx - d/2], [cy - h/2, cy + h/2], color=color, lw=lw, solid_capstyle='round')
    ax.plot([cx + d/2, cx + d/2], [cy - h/2, cy + h/2], color=color, lw=lw, solid_capstyle='round')

def draw_capacitor_v(ax, cx, cy, d=0.28, w=0.8, lw=2.5, color=INK):
    """Vertical capacitor: two horizontal parallel plates."""
    ax.plot([cx - w/2, cx + w/2], [cy + d/2, cy + d/2], color=color, lw=lw, solid_capstyle='round')
    ax.plot([cx - w/2, cx + w/2], [cy - d/2, cy - d/2], color=color, lw=lw, solid_capstyle='round')

def draw_battery_h(ax, cx, cy, d=0.32, h_long=0.9, h_short=0.45, lw=2.5, color=INK):
    """Horizontal battery: long plate on left (+), short thicker plate on right (-)."""
    # Long plate (+)
    ax.plot([cx - d/2, cx - d/2], [cy - h_long/2, cy + h_long/2], color=color, lw=lw, solid_capstyle='round')
    # Short plate (-)
    ax.plot([cx + d/2, cx + d/2], [cy - h_short/2, cy + h_short/2], color=color, lw=lw * 1.8, solid_capstyle='round')
    ax.text(cx - d/2 - 0.35, cy, "+", ha="center", va="center", fontsize=16, color=color, weight="bold")
    ax.text(cx + d/2 + 0.35, cy, "−", ha="center", va="center", fontsize=16, color=color, weight="bold")
    ax.text(cx, cy - 0.75, "V", ha="center", va="center", fontsize=16, weight="bold", color=color)

def draw_battery_v(ax, cx, cy, d=0.32, w_long=0.9, w_short=0.45, lw=2.5, color=INK):
    """Vertical battery: long plate on top (+), short thicker plate on bottom (-)."""
    # Long plate (+)
    ax.plot([cx - w_long/2, cx + w_long/2], [cy + d/2, cy + d/2], color=color, lw=lw, solid_capstyle='round')
    # Short plate (-)
    ax.plot([cx - w_short/2, cx + w_short/2], [cy - d/2, cy - d/2], color=color, lw=lw * 1.8, solid_capstyle='round')
    ax.text(cx - 0.55, cy + d/2, "+", ha="center", va="center", fontsize=16, color=color, weight="bold")
    ax.text(cx - 0.55, cy - d/2, "−", ha="center", va="center", fontsize=16, color=color, weight="bold")
    ax.text(cx - 0.95, cy, "V", ha="center", va="center", fontsize=16, weight="bold", color=color)

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    wire_color = INK
    lw = 2.5
    cap_color = DEEP["blue"]

    # ================== LEFT SIDE: SERIES CONNECTION ==================
    # Titles & Formulas
    ax.text(4.0, 9.2, "Series Connection", ha="center", va="center", fontsize=18, weight="bold", color=INK)
    ax.text(4.0, 8.35, r"$\frac{1}{C} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3}$", 
            ha="center", va="center", fontsize=16, color=DEEP["blue"],
            bbox=dict(fc=CREAM, ec="none", boxstyle="round,pad=0.35"))

    # Series circuit loop coordinates
    c_series_x = [2.5, 4.0, 5.5]
    y_top = 6.4
    y_bot = 3.0
    x_left = 1.0
    x_right = 7.0
    d_cap = 0.28
    d_bat = 0.32

    # Top wire segments between series capacitors
    ax.plot([x_left, c_series_x[0] - d_cap/2], [y_top, y_top], color=wire_color, lw=lw)
    ax.plot([c_series_x[0] + d_cap/2, c_series_x[1] - d_cap/2], [y_top, y_top], color=wire_color, lw=lw)
    ax.plot([c_series_x[1] + d_cap/2, c_series_x[2] - d_cap/2], [y_top, y_top], color=wire_color, lw=lw)
    ax.plot([c_series_x[2] + d_cap/2, x_right], [y_top, y_top], color=wire_color, lw=lw)

    # Capacitors
    for i, cx in enumerate(c_series_x):
        draw_capacitor_h(ax, cx, y_top, d=d_cap, h=0.8, lw=lw, color=cap_color)
        ax.text(cx, y_top + 0.65, f"$C_{i+1}$", ha="center", va="center", fontsize=16, weight="bold", color=INK)

    # Side wires
    ax.plot([x_left, x_left], [y_bot, y_top], color=wire_color, lw=lw)
    ax.plot([x_right, x_right], [y_bot, y_top], color=wire_color, lw=lw)

    # Bottom wire segments with battery at (4.0, y_bot)
    ax.plot([x_left, 4.0 - d_bat/2], [y_bot, y_bot], color=wire_color, lw=lw)
    ax.plot([4.0 + d_bat/2, x_right], [y_bot, y_bot], color=wire_color, lw=lw)
    draw_battery_h(ax, 4.0, y_bot, d=d_bat, h_long=0.9, h_short=0.45, lw=lw, color=INK)

    # ================== MIDDLE DIVIDER ==================
    ax.plot([8.0, 8.0], [1.2, 9.2], color=GREY, lw=1.5, linestyle="--")

    # ================== RIGHT SIDE: PARALLEL CONNECTION ==================
    # Titles & Formulas
    ax.text(12.2, 9.2, "Parallel Connection", ha="center", va="center", fontsize=18, weight="bold", color=INK)
    ax.text(12.2, 8.35, r"$C = C_1 + C_2 + C_3$", 
            ha="center", va="center", fontsize=16, color=DEEP["blue"],
            bbox=dict(fc=CREAM, ec="none", boxstyle="round,pad=0.35"))

    # Parallel circuit geometry
    x_bat = 9.4
    y_mid = 4.7
    branch_x = [11.2, 12.8, 14.4]

    # Horizontal bus rails: top and bottom
    ax.plot([x_bat, branch_x[-1]], [y_top, y_top], color=wire_color, lw=lw)
    ax.plot([x_bat, branch_x[-1]], [y_bot, y_bot], color=wire_color, lw=lw)

    # Leftmost vertical branch: Voltage Source (properly broken wire, no short-circuit)
    ax.plot([x_bat, x_bat], [y_top, y_mid + d_bat/2], color=wire_color, lw=lw)
    ax.plot([x_bat, x_bat], [y_mid - d_bat/2, y_bot], color=wire_color, lw=lw)
    draw_battery_v(ax, x_bat, y_mid, d=d_bat, w_long=0.9, w_short=0.45, lw=lw, color=INK)

    # Vertical branches with capacitors
    for i, bx in enumerate(branch_x):
        # Upper wire segment
        ax.plot([bx, bx], [y_top, y_mid + d_cap/2], color=wire_color, lw=lw)
        # Lower wire segment
        ax.plot([bx, bx], [y_mid - d_cap/2, y_bot], color=wire_color, lw=lw)
        # Capacitor symbol
        draw_capacitor_v(ax, bx, y_mid, d=d_cap, w=0.8, lw=lw, color=cap_color)
        # Capacitor label
        ax.text(bx, y_top + 0.65, f"$C_{i+1}$", ha="center", va="center", fontsize=16, weight="bold", color=INK)
        # Junction dots on bus rails
        ax.plot(bx, y_top, "o", color=INK, markersize=5.5)
        ax.plot(bx, y_bot, "o", color=INK, markersize=5.5)

    save(fig, out)
