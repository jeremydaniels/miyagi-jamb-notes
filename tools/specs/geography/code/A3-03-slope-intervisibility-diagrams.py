from style import *
import numpy as np

def draw_stick_figure(ax, x, y, scale=1.0, color=INK):
    # Base height of figure is around 0.9 * scale
    h = scale
    # Body line
    ax.plot([x, x], [y + 0.35 * h, y + 0.7 * h], color=color, lw=1.8, solid_capstyle='round')
    # Head
    head = plt.Circle((x, y + 0.85 * h), 0.12 * h, edgecolor=color, facecolor='white', lw=1.8, zorder=5)
    ax.add_patch(head)
    # Legs
    ax.plot([x, x - 0.15 * h], [y + 0.35 * h, y], color=color, lw=1.8, solid_capstyle='round')
    ax.plot([x, x + 0.15 * h], [y + 0.35 * h, y], color=color, lw=1.8, solid_capstyle='round')
    # Arms
    ax.plot([x - 0.18 * h, x + 0.18 * h], [y + 0.55 * h, y + 0.55 * h], color=color, lw=1.8, solid_capstyle='round')

def draw(out):
    fig = canvas(18, 6.5)
    
    # Left subplot: Concave slope
    ax1 = fig.add_subplot(1, 3, 1)
    # Middle subplot: Convex slope
    ax2 = fig.add_subplot(1, 3, 2)
    # Right subplot: Intervening ridge
    ax3 = fig.add_subplot(1, 3, 3)

    for ax in [ax1, ax2, ax3]:
        ax.set_xlim(-0.5, 10.5)
        ax.set_ylim(-0.5, 9.5)
        ax.set_aspect('equal')
        ax.axis('off')

    # --- 1. CONCAVE SLOPE ---
    ax1.set_title("Concave Slope\n(Intervisible)", fontsize=16, color=INK, pad=15, weight='bold')
    x1 = np.linspace(0, 10, 200)
    # Gentle at bottom (x=0 to 5), steep at top (x=5 to 10)
    y1 = 1.0 + 5.5 * (x1 / 10.0)**2.5
    ax1.fill_between(x1, y1, color=GREEN, alpha=0.35)
    ax1.plot(x1, y1, color=DEEP['green'], lw=3.5)

    # Figures: bottom at x=1, top at x=9
    y_bot1 = 1.0 + 5.5 * (1.0 / 10.0)**2.5
    y_top1 = 1.0 + 5.5 * (9.0 / 10.0)**2.5
    draw_stick_figure(ax1, 1.0, y_bot1, scale=1.1)
    draw_stick_figure(ax1, 9.0, y_top1, scale=1.1)

    # Eyes at y + 0.85 * scale
    eye_bot1 = (1.0, y_bot1 + 0.93)
    eye_top1 = (9.0, y_top1 + 0.93)
    ax1.plot([eye_bot1[0], eye_top1[0]], [eye_bot1[1], eye_top1[1]], 
             color=DEEP['blue'], lw=2.2, linestyle='--', zorder=6)

    ax1.text(5.0, 5.8, "Line of sight clear", color=DEEP['blue'], fontsize=14, 
             ha='center', va='bottom', rotation=28,
             bbox=dict(fc='white', ec='none', pad=2.0))
    ax1.text(1.5, 0.2, "Gentle slope", fontsize=14, color=INK, ha='left')
    ax1.text(8.8, 4.0, "Steep\nslope", fontsize=14, color=INK, ha='right')

    # --- 2. CONVEX SLOPE ---
    ax2.set_title("Convex Slope\n(Not Intervisible)", fontsize=16, color=INK, pad=15, weight='bold')
    x2 = np.linspace(0, 10, 200)
    # Steep at bottom (x=0), gentle at top (x=10)
    y2 = 1.0 + 5.5 * (1.0 - (1.0 - x2 / 10.0)**2.5)
    ax2.fill_between(x2, y2, color=ORANGE, alpha=0.35)
    ax2.plot(x2, y2, color=DEEP['orange'], lw=3.5)

    y_bot2 = 1.0 + 5.5 * (1.0 - (1.0 - 1.0 / 10.0)**2.5)
    y_top2 = 1.0 + 5.5 * (1.0 - (1.0 - 9.0 / 10.0)**2.5)
    draw_stick_figure(ax2, 1.0, y_bot2, scale=1.1)
    draw_stick_figure(ax2, 9.0, y_top2, scale=1.1)

    eye_bot2 = (1.0, y_bot2 + 0.93)
    eye_top2 = (9.0, y_top2 + 0.93)
    ax2.plot([eye_bot2[0], eye_top2[0]], [eye_bot2[1], eye_top2[1]], 
             color=DEEP['pink'], lw=2.2, linestyle='--', zorder=2)

    ax2.annotate("Sight line blocked\nby hill bulge", 
                 xy=(5.0, eye_bot2[1] + (eye_top2[1] - eye_bot2[1]) * 0.5), 
                 xytext=(5.0, 2.2),
                 fontsize=14, color=DEEP['pink'], ha='center',
                 arrowprops=dict(arrowstyle="->", color=DEEP['pink'], lw=1.5),
                 bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3'))
    ax2.text(1.2, 3.8, "Steep\nslope", fontsize=14, color=INK, ha='left')
    ax2.text(8.5, 7.0, "Gentle slope", fontsize=14, color=INK, ha='right')

    # --- 3. TWO PEAKS WITH INTERVENING RIDGE ---
    ax3.set_title("Intervening High Ground\n(Not Intervisible)", fontsize=16, color=INK, pad=15, weight='bold')
    x3 = np.linspace(0, 10, 300)
    # Two peaks around x=1.5 and x=8.5, higher ridge around x=5.0
    p1 = 3.6 * np.exp(-((x3 - 1.5) / 1.5)**2)
    p2 = 3.6 * np.exp(-((x3 - 8.5) / 1.5)**2)
    ridge = 5.6 * np.exp(-((x3 - 5.0) / 1.8)**2)
    y3 = 1.0 + p1 + p2 + ridge
    ax3.fill_between(x3, y3, color=LAV, alpha=0.35)
    ax3.plot(x3, y3, color=DEEP['lav'], lw=3.5)

    y_bot3 = 1.0 + 3.6 * np.exp(-((1.5 - 1.5) / 1.5)**2) + 5.6 * np.exp(-((1.5 - 5.0) / 1.8)**2)
    y_top3 = 1.0 + 3.6 * np.exp(-((8.5 - 8.5) / 1.5)**2) + 5.6 * np.exp(-((8.5 - 5.0) / 1.8)**2)
    draw_stick_figure(ax3, 1.5, y_bot3, scale=1.1)
    draw_stick_figure(ax3, 8.5, y_top3, scale=1.1)

    eye_p1 = (1.5, y_bot3 + 0.93)
    eye_p2 = (8.5, y_top3 + 0.93)
    ax3.plot([eye_p1[0], eye_p2[0]], [eye_p1[1], eye_p2[1]], 
             color=DEEP['pink'], lw=2.2, linestyle='--', zorder=2)

    ax3.annotate("Intervening ridge\nblocks sight line", 
                 xy=(5.0, eye_p1[1]), 
                 xytext=(5.0, 8.0),
                 fontsize=14, color=DEEP['pink'], ha='center',
                 arrowprops=dict(arrowstyle="->", color=DEEP['pink'], lw=1.5),
                 bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3'))
    ax3.text(1.5, 0.4, "Peak A", fontsize=14, color=INK, ha='center', weight='bold')
    ax3.text(8.5, 0.4, "Peak B", fontsize=14, color=INK, ha='center', weight='bold')
    ax3.text(5.0, 0.4, "Higher Ridge", fontsize=14, color=INK, ha='center', weight='bold')

    plt.tight_layout()
    save(fig, out)
