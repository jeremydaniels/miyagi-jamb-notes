from style import *
import numpy as np

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Triangular glass prism coordinates
    prism_pts = np.array([
        [4.8, 5.8],  # apex
        [2.8, 1.6],  # bottom left
        [6.8, 1.6]   # bottom right
    ])
    prism = plt.Polygon(prism_pts, closed=True, facecolor="#EBF3F9", edgecolor=DEEP["blue"], lw=2.2, zorder=2)
    ax.add_patch(prism)
    ax.text(4.8, 2.2, "Glass Prism", fontsize=15, color=DEEP["blue"], ha="center", va="center", weight="bold")

    # Screen on the right
    screen_x = 10.2
    ax.plot([screen_x, screen_x], [1.0, 5.5], color=GREY, lw=4, solid_capstyle='round', zorder=2)
    ax.text(screen_x, 5.8, "Screen", fontsize=15, color=INK, ha="center", va="bottom", weight="bold")

    # Incident white light beam
    # Hits the left face at around (3.6, 3.28)
    p_hit = np.array([3.6, 3.28])
    p_start = np.array([0.8, 2.3])
    
    # White light ray representation: a light grey thick beam with black border/arrow
    ax.annotate("", xy=(p_hit[0], p_hit[1]), xytext=(p_start[0], p_start[1]),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5, mutation_scale=18), zorder=4)
    ax.text(1.8, 3.1, "Beam of\nwhite light", fontsize=15, color=INK, ha="center", va="bottom",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # Colours of spectrum (from Red down to Violet)
    # Inside prism: slight deviation and spread to right face
    # Red undergoes least refraction, Violet most refraction
    spectrum_colors = [
        ("#D9383A", "Red (least deviated)"),   # Red
        ("#E76F24", ""),                        # Orange
        ("#EAB308", ""),                        # Yellow
        ("#22C55E", ""),                        # Green
        ("#0EA5E9", ""),                        # Blue
        ("#4338CA", ""),                        # Indigo
        ("#7E22CE", "Violet (most deviated)")  # Violet
    ]

    n_rays = len(spectrum_colors)
    
    # Right face of prism goes from (4.8, 5.8) to (6.8, 1.6)
    # Linear equation: x - 4.8 = (6.8 - 4.8)/(1.6 - 5.8) * (y - 5.8) => x = 4.8 - (2.0/4.2)*(y - 5.8)
    
    # Exit points along right face
    y_exits = np.linspace(3.7, 3.1, n_rays)
    # Screen arrival points
    y_screens = np.linspace(4.8, 1.7, n_rays)

    for i, (col, label) in enumerate(spectrum_colors):
        y_exit = y_exits[i]
        x_exit = 4.8 - (2.0 / 4.2) * (y_exit - 5.8)
        p_exit = np.array([x_exit, y_exit])
        
        y_screen = y_screens[i]
        p_screen = np.array([screen_x, y_screen])
        
        # Ray inside prism
        ax.plot([p_hit[0], p_exit[0]], [p_hit[1], p_exit[1]], color=col, lw=1.8, zorder=3)
        
        # Ray from prism to screen
        ax.plot([p_exit[0], p_screen[0]], [p_exit[1], p_screen[1]], color=col, lw=2.0, zorder=3)
        
        # Mid-arrow on rays outside towards screen (for middle ray or outer rays)
        if i == 0 or i == n_rays - 1 or i == 3:
            mid = 0.55 * p_exit + 0.45 * p_screen
            ax.annotate("", xy=(mid[0] + 0.1, mid[1] + 0.1 * (p_screen[1] - p_exit[1]) / (p_screen[0] - p_exit[0])),
                        xytext=(mid[0], mid[1]),
                        arrowprops=dict(arrowstyle="->", color=col, lw=2.0, mutation_scale=14), zorder=4)

        # Labels for Red and Violet
        if label:
            # Draw line/text for the specific ray label
            ha = "left"
            ax.annotate(label, xy=(p_screen[0], p_screen[1]), xytext=(screen_x + 0.4, y_screen),
                        fontsize=14, color=INK, va="center", ha=ha,
                        arrowprops=dict(arrowstyle="->", color=GREY, lw=1.2),
                        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # Label the spectrum on the screen
    ax.annotate("Spectrum", xy=(screen_x + 0.05, 3.25), xytext=(screen_x + 0.8, 3.25),
                fontsize=15, color=INK, weight="bold", va="center", ha="left")

    save(fig, out)
