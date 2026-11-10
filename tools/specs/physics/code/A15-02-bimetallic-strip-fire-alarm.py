from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 11)
    
    # 3 subplots vertically
    ax1 = fig.add_axes([0.05, 0.70, 0.90, 0.25])
    ax2 = fig.add_axes([0.05, 0.38, 0.90, 0.27])
    ax3 = fig.add_axes([0.05, 0.04, 0.90, 0.30])
    
    for ax in [ax1, ax2, ax3]:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
    brass_color = "#E5B83B" # gold / brass
    iron_color = "#A8B2BA"  # grey / iron
    support_color = "#4A5568"
    
    # --- PANEL 1: Room Temperature ---
    ax1.text(0.5, 8.5, "room temperature", fontsize=16, fontweight='bold', color=INK,
             bbox=dict(fc="white", ec="none", pad=2))
    
    # Fixed support wall on the left
    ax1.fill_between([1.5, 2.0], 1.5, 7.5, color=support_color)
    for y in np.linspace(2.0, 7.0, 6):
        ax1.plot([1.2, 1.5], [y - 0.3, y], color=INK, lw=1.5)
        
    # Brass strip (top)
    rect_brass1 = patches.Rectangle((2.0, 4.5), 4.5, 0.8, fc=brass_color, ec=INK, lw=1.5)
    # Iron strip (bottom)
    rect_iron1 = patches.Rectangle((2.0, 3.7), 4.5, 0.8, fc=iron_color, ec=INK, lw=1.5)
    ax1.add_patch(rect_brass1)
    ax1.add_patch(rect_iron1)
    
    # Rivets / bonding line
    ax1.plot([2.0, 6.5], [4.5, 4.5], color=INK, lw=1)
    
    # Labels for Panel 1
    ax1.annotate("brass (higher expansivity)", xy=(4.5, 5.3), xytext=(5.5, 7.5),
                 fontsize=15, color=INK, fontweight='medium',
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
                 
    ax1.annotate("iron (lower expansivity)", xy=(4.5, 3.7), xytext=(5.5, 1.8),
                 fontsize=15, color=INK, fontweight='medium',
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    # --- PANEL 2: Heated Strip ---
    ax2.text(0.5, 8.5, "heated", fontsize=16, fontweight='bold', color=INK,
             bbox=dict(fc="white", ec="none", pad=2))
             
    # Support wall
    ax2.fill_between([1.5, 2.0], 2.5, 8.5, color=support_color)
    for y in np.linspace(3.0, 8.0, 6):
        ax2.plot([1.2, 1.5], [y - 0.3, y], color=INK, lw=1.5)
        
    # Curved strip (bending downwards, brass on outside/top, convex downwards curve)
    # y = y0 - k * x^2
    x_curve = np.linspace(2.0, 6.2, 100)
    dx = x_curve - 2.0
    y_mid = 5.5 - 0.12 * (dx ** 2)
    
    # Brass (top layer)
    y_top = y_mid + 0.4
    y_bond = y_mid - 0.4
    y_bot = y_mid - 1.2
    
    ax2.fill_between(x_curve, y_bond, y_top, color=brass_color, ec=INK, lw=1.5)
    ax2.fill_between(x_curve, y_bot, y_bond, color=iron_color, ec=INK, lw=1.5)
    
    # End cap line
    ax2.plot([x_curve[-1], x_curve[-1]], [y_bot[-1], y_top[-1]], color=INK, lw=1.5)
    
    # Heat flame indication
    ax2.text(3.5, 1.2, "🔥 Heat applied", fontsize=15, color=DEEP["orange"],
             bbox=dict(fc=CREAM, ec=ORANGE, boxstyle="round,pad=0.3"))
    ax2.text(6.8, 4.5, "Brass expands more than iron,\nforcing strip to bend downwards",
             fontsize=14, color=INK, style='italic',
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # --- PANEL 3: Fire Alarm Circuit ---
    ax3.text(0.5, 8.8, "Fire alarm circuit", fontsize=16, fontweight='bold', color=INK,
             bbox=dict(fc="white", ec="none", pad=2))
             
    # Support block (metal / conducting terminal)
    ax3.fill_between([1.5, 2.0], 3.5, 8.0, color=support_color)
    
    # Bent strip touching contact point
    x_c3 = np.linspace(2.0, 6.0, 100)
    dx3 = x_c3 - 2.0
    y_mid3 = 5.5 - 0.13 * (dx3 ** 2)
    y_top3 = y_mid3 + 0.35
    y_bond3 = y_mid3 - 0.35
    y_bot3 = y_mid3 - 1.05
    
    ax3.fill_between(x_c3, y_bond3, y_top3, color=brass_color, ec=INK, lw=1.5)
    ax3.fill_between(x_c3, y_bot3, y_bond3, color=iron_color, ec=INK, lw=1.5)
    ax3.plot([x_c3[-1], x_c3[-1]], [y_bot3[-1], y_top3[-1]], color=INK, lw=1.5)
    
    contact_x = x_c3[-1]
    contact_y = y_bot3[-1]
    
    # Contact screw/point
    ax3.plot([contact_x - 0.2, contact_x + 0.2], [contact_y - 0.15, contact_y - 0.15], color=INK, lw=4)
    ax3.plot([contact_x, contact_x], [contact_y - 0.15, 1.5], color=INK, lw=2)
    ax3.plot([contact_x - 0.4, contact_x + 0.4], [1.5, 1.5], color=support_color, lw=4)
    
    ax3.annotate("contact point", xy=(contact_x, contact_y), xytext=(6.7, 2.5),
                 fontsize=15, color=INK, fontweight='medium',
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
                 
    # Circuit wiring
    # From contact point at bottom (contact_x, 1.5) -> wire down, right, up to bell and battery
    # Path: (contact_x, 1.5) -> (8.5, 1.5) -> (8.5, 4.0) -> Bell -> (8.5, 6.5) -> Battery -> (8.5, 8.2) -> (1.75, 8.2) -> (1.75, 7.5)
    
    # Wire segment 1: contact base to right corner
    ax3.plot([contact_x, 8.5], [1.5, 1.5], color=DEEP["blue"], lw=2.5)
    ax3.plot([8.5, 8.5], [1.5, 3.5], color=DEEP["blue"], lw=2.5)
    
    # Bell symbol at (8.5, 4.3)
    bell_cx, bell_cy = 8.5, 4.3
    # Bell dome (half circle)
    dome = patches.Wedge((bell_cx, bell_cy), 0.6, 0, 180, fc=LAV, ec=INK, lw=2)
    ax3.add_patch(dome)
    ax3.plot([bell_cx - 0.6, bell_cx + 0.6], [bell_cy, bell_cy], color=INK, lw=2)
    # Bell base gong / striker
    ax3.plot([bell_cx, bell_cx], [bell_cy, bell_cy - 0.5], color=INK, lw=2)
    # Sound waves
    ax3.text(bell_cx + 0.8, bell_cy + 0.1, "RING!", fontsize=14, fontweight='bold', color=DEEP["pink"])
    ax3.text(bell_cx - 2.0, bell_cy - 0.1, "bell", fontsize=15, color=INK, fontweight='medium',
             bbox=dict(fc="white", ec="none", pad=1))
    
    # Wire from bell to battery
    ax3.plot([8.5, 8.5], [bell_cy + 0.6, 5.8], color=DEEP["blue"], lw=2.5)
    
    # Battery symbol at (8.5, 6.5)
    # Long plate (positive), short thick plate (negative)
    bat_y = 6.4
    ax3.plot([7.8, 9.2], [bat_y + 0.3, bat_y + 0.3], color=INK, lw=3)   # long
    ax3.plot([8.1, 8.9], [bat_y - 0.3, bat_y - 0.3], color=INK, lw=5)   # short
    ax3.text(9.4, bat_y, "battery", fontsize=15, color=INK, va='center', fontweight='medium',
             bbox=dict(fc="white", ec="none", pad=1))
    ax3.text(9.4, bat_y + 0.3, "+", fontsize=14, color=INK, va='center')
    ax3.text(9.4, bat_y - 0.3, "-", fontsize=16, color=INK, va='center')
    
    # Wire from battery to top left support block
    ax3.plot([8.5, 8.5], [bat_y + 0.3, 8.2], color=DEEP["blue"], lw=2.5)
    ax3.plot([8.5, 1.75], [8.2, 8.2], color=DEEP["blue"], lw=2.5)
    ax3.plot([1.75, 1.75], [8.2, 7.5], color=DEEP["blue"], lw=2.5)
    
    # Current arrows
    ax3.annotate("", xy=(5.0, 8.2), xytext=(5.5, 8.2),
                 arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2))
    ax3.annotate("", xy=(7.5, 1.5), xytext=(7.0, 1.5),
                 arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2))

    save(fig, out)
