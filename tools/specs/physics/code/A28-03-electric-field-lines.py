from style import *
import numpy as np

def draw_charge(ax, x, y, sign="+", radius=0.35):
    # Charge body
    color = DEEP["orange"] if sign == "+" else DEEP["blue"]
    bg_color = PINK if sign == "+" else BLUE
    circle = plt.Circle((x, y), radius, facecolor=bg_color, edgecolor=color, lw=2.5, zorder=10)
    ax.add_patch(circle)
    symbol = "+" if sign == "+" else "−"
    ax.text(x, y, symbol, color=INK, fontsize=20, fontweight="bold",
            ha="center", va="center", zorder=11)

def draw(out):
    fig = canvas(12, 10)
    
    # Create 4 panels (2x2 grid)
    # [Panel 1, Panel 2]
    # [Panel 3, Panel 4]
    
    # ---------------- PANEL 1: Isolated Positive Charge ----------------
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax1.set_title("Isolated positive charge", fontsize=15, pad=12, color=INK, fontweight="bold")
    
    draw_charge(ax1, 0, 0, sign="+")
    angles = np.linspace(0, 2 * np.pi, 12, endpoint=False)
    for th in angles:
        r_start = 0.4
        r_end = 2.4
        x0, y0 = r_start * np.cos(th), r_start * np.sin(th)
        x1, y1 = r_end * np.cos(th), r_end * np.sin(th)
        ax1.annotate("", xy=(x1, y1), xytext=(x0, y0),
                     arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.45",
                                     color=DEEP["orange"], lw=2.0))
        
    # ---------------- PANEL 2: Isolated Negative Charge ----------------
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-3, 3)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title("Isolated negative charge", fontsize=15, pad=12, color=INK, fontweight="bold")
    
    draw_charge(ax2, 0, 0, sign="-")
    for th in angles:
        r_start = 2.4
        r_end = 0.4
        x0, y0 = r_start * np.cos(th), r_start * np.sin(th)
        x1, y1 = r_end * np.cos(th), r_end * np.sin(th)
        ax2.annotate("", xy=(x1, y1), xytext=(x0, y0),
                     arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.45",
                                     color=DEEP["blue"], lw=2.0))

    # ---------------- PANEL 3: Opposite Charges (+ and -) ----------------
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.set_xlim(-3, 3)
    ax3.set_ylim(-2.5, 2.5)
    ax3.set_aspect("equal")
    ax3.axis("off")
    ax3.set_title("Opposite charges (+ and −)", fontsize=15, pad=12, color=INK, fontweight="bold")
    
    d = 1.2
    # Streamlines using physics dipole potential/field
    Y, X = np.mgrid[-2.5:2.5:200j, -3:3:200j]
    # Field of + at (-d, 0) and - at (+d, 0)
    r1_sq = (X + d)**2 + Y**2
    r2_sq = (X - d)**2 + Y**2
    r1 = np.sqrt(r1_sq)
    r2 = np.sqrt(r2_sq)
    
    Ex = (X + d) / (r1**3 + 1e-4) - (X - d) / (r2**3 + 1e-4)
    Ey = Y / (r1**3 + 1e-4) - Y / (r2**3 + 1e-4)
    
    # Specific starting points for clean aesthetic lines
    start_angles = np.linspace(-np.pi * 0.85, np.pi * 0.85, 12)
    start_points = np.array([[-d + 0.38 * np.cos(a), 0.38 * np.sin(a)] for a in start_angles])
    
    ax3.streamplot(X, Y, Ex, Ey, color=DEEP["pink"], linewidth=1.8,
                   arrowsize=1.4, arrowstyle="->",
                   start_points=start_points, density=2,
                   integration_direction='forward', minlength=0.2)
    
    draw_charge(ax3, -d, 0, sign="+")
    draw_charge(ax3, d, 0, sign="-")

    # ---------------- PANEL 4: Like Positive Charges (+ and +) ----------------
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.set_xlim(-3, 3)
    ax4.set_ylim(-2.5, 2.5)
    ax4.set_aspect("equal")
    ax4.axis("off")
    ax4.set_title("Like positive charges (+ and +)", fontsize=15, pad=12, color=INK, fontweight="bold")
    
    # Field of + at (-d, 0) and + at (+d, 0)
    Ex4 = (X + d) / (r1**3 + 1e-4) + (X - d) / (r2**3 + 1e-4)
    Ey4 = Y / (r1**3 + 1e-4) + Y / (r2**3 + 1e-4)
    
    angles_like = np.linspace(0, 2 * np.pi, 14, endpoint=False)
    pts1 = [[-d + 0.38 * np.cos(a), 0.38 * np.sin(a)] for a in angles_like]
    pts2 = [[d + 0.38 * np.cos(a), 0.38 * np.sin(a)] for a in angles_like]
    all_starts = np.vstack([pts1, pts2])
    
    ax4.streamplot(X, Y, Ex4, Ey4, color=DEEP["orange"], linewidth=1.8,
                   arrowsize=1.4, arrowstyle="->",
                   start_points=all_starts, density=2,
                   integration_direction='forward', minlength=0.2)
    
    draw_charge(ax4, -d, 0, sign="+")
    draw_charge(ax4, d, 0, sign="+")
    
    # Neutral point 'N'
    ax4.text(0, 0, "N", fontsize=18, fontweight="bold", color=INK,
             ha="center", va="center",
             bbox=dict(boxstyle="circle,pad=0.25", facecolor=CREAM, edgecolor=GREY, lw=1.5),
             zorder=12)

    plt.tight_layout()
    save(fig, out)
