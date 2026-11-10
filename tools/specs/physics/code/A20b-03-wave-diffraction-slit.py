from style import *
import numpy as np

def draw(out):
    fig = canvas(14, 7)
    
    # Create two subplots side-by-side
    ax1 = fig.add_axes([0.05, 0.1, 0.42, 0.78])
    ax2 = fig.add_axes([0.53, 0.1, 0.42, 0.78])
    
    barrier_x = 0.0
    wavelength = 1.0
    wave_color = DEEP["blue"]
    barrier_color = INK
    barrier_width = 7.0
    
    # ------------------ LEFT PANEL: Wide Gap ------------------
    ax1.set_xlim(-5, 6)
    ax1.set_ylim(-5.5, 5.5)
    ax1.set_aspect("equal")
    ax1.axis("off")
    
    gap_wide = 3.6  # Much wider than wavelength = 1.0
    
    # Barriers
    ax1.plot([barrier_x, barrier_x], [gap_wide / 2, 5.5], color=barrier_color, lw=barrier_width, solid_capstyle='round')
    ax1.plot([barrier_x, barrier_x], [-5.5, -gap_wide / 2], color=barrier_color, lw=barrier_width, solid_capstyle='round')
    
    # Incident plane waves (left side)
    for x in np.arange(-4.5, barrier_x, wavelength):
        ax1.plot([x, x], [-5.0, 5.0], color=wave_color, lw=2.5)
        
    # Emerging waves (right side) - straight in middle, slight curving at edges
    # For each wavefront at distance r from barrier:
    for n in range(1, 6):
        r = n * wavelength
        # Middle flat section: y from -(gap_wide/2 - 0.2) to (gap_wide/2 - 0.2)
        y_straight = gap_wide / 2 - 0.3
        
        # Upper edge curve (arc curving back towards barrier)
        th_top = np.linspace(0, np.pi / 3, 30)
        x_top = barrier_x + r * np.cos(th_top)
        y_top = y_straight + r * np.sin(th_top)
        
        # Lower edge curve
        th_bot = np.linspace(-np.pi / 3, 0, 30)
        x_bot = barrier_x + r * np.cos(th_bot)
        y_bot = -y_straight + r * np.sin(th_bot)
        
        # Straight segment
        x_mid = [barrier_x + r, barrier_x + r]
        y_mid = [-y_straight, y_straight]
        
        # Stitch together
        x_full = np.concatenate([x_bot, x_mid, x_top])
        y_full = np.concatenate([y_bot, y_mid, y_top])
        
        ax1.plot(x_full, y_full, color=wave_color, lw=2.5)
        
    # Propagation direction arrows
    ax1.annotate("", xy=(-1.2, 0), xytext=(-2.8, 0),
                 arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5, mutation_scale=18))
    ax1.annotate("", xy=(3.8, 0), xytext=(2.2, 0),
                 arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5, mutation_scale=18))
    
    # Gap width indicator
    ax1.annotate("", xy=(barrier_x, gap_wide / 2), xytext=(barrier_x, -gap_wide / 2),
                 arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5, mutation_scale=12))
    ax1.text(barrier_x - 0.3, 0, "gap > $\lambda$", ha="right", va="center", fontsize=14,
             bbox=dict(fc="white", ec="none", pad=1))
    
    ax1.set_title("Wide gap: minimal diffraction", fontsize=16, pad=15, color=INK, weight="bold")
    
    # ------------------ RIGHT PANEL: Narrow Gap ------------------
    ax2.set_xlim(-5, 6)
    ax2.set_ylim(-5.5, 5.5)
    ax2.set_aspect("equal")
    ax2.axis("off")
    
    gap_narrow = 1.0  # Roughly equal to wavelength = 1.0
    
    # Barriers
    ax2.plot([barrier_x, barrier_x], [gap_narrow / 2, 5.5], color=barrier_color, lw=barrier_width, solid_capstyle='round')
    ax2.plot([barrier_x, barrier_x], [-5.5, -gap_narrow / 2], color=barrier_color, lw=barrier_width, solid_capstyle='round')
    
    # Incident plane waves (left side)
    for x in np.arange(-4.5, barrier_x, wavelength):
        ax2.plot([x, x], [-5.0, 5.0], color=wave_color, lw=2.5)
        
    # Emerging waves (right side) - semicircles centered at (0, 0)
    theta = np.linspace(-np.pi / 2, np.pi / 2, 100)
    for n in range(1, 6):
        r = n * wavelength
        x_arc = barrier_x + r * np.cos(theta)
        y_arc = r * np.sin(theta)
        ax2.plot(x_arc, y_arc, color=wave_color, lw=2.5)
        
    # Propagation direction arrows
    ax2.annotate("", xy=(-1.2, 0), xytext=(-2.8, 0),
                 arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5, mutation_scale=18))
    for ang in [-np.pi / 4, 0, np.pi / 4]:
        r_start = 2.2
        r_end = 3.8
        ax2.annotate("", xy=(barrier_x + r_end * np.cos(ang), r_end * np.sin(ang)),
                     xytext=(barrier_x + r_start * np.cos(ang), r_start * np.sin(ang)),
                     arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.0, mutation_scale=15))
    
    # Gap width indicator
    ax2.annotate("", xy=(barrier_x + 0.35, gap_narrow / 2), xytext=(barrier_x + 0.35, -gap_narrow / 2),
                 arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5, mutation_scale=12))
    ax2.text(barrier_x + 0.6, 0, "gap $\\approx \lambda$", ha="left", va="center", fontsize=14,
             bbox=dict(fc="white", ec="none", pad=1))
    
    # Barrier labels
    ax2.text(barrier_x, 4.2, "Barrier", ha="center", va="center", fontsize=14,
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    ax1.text(barrier_x, 4.2, "Barrier", ha="center", va="center", fontsize=14,
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    
    ax2.set_title("Narrow gap: maximum diffraction", fontsize=16, pad=15, color=INK, weight="bold")
    
    save(fig, out)
