from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 6.5)
    ax = fig.add_subplot(111)
    
    # 0 to 13 on x axis, 0 to 10 on y axis
    axes_clean(ax, "time", "number of organisms", 13.0, 9.6)
    
    # Coupled oscillations
    # Period: T = 2*pi / omega = 2*pi / 1.3 ≈ 4.83
    # Peaks for prey: x ≈ 1.21, 6.04, 10.87
    # Peaks for predator (lag 0.85 rad ≈ 0.65 units): x ≈ 1.86, 6.70, 11.53
    omega = 1.3
    x = np.linspace(0.2, 10.2, 400)
    
    prey = 5.0 + 2.7 * np.sin(omega * x)
    predator = 3.0 + 1.7 * np.sin(omega * x - 0.85)
    
    color_prey = DEEP["blue"]
    color_pred = DEEP["pink"]  # soft red/pink tone
    
    ax.plot(x, prey, color=color_prey, lw=3.2)
    ax.plot(x, predator, color=color_pred, lw=3.2)
    
    # Peak annotations showing phase lag
    t_prey_peak1 = (np.pi / 2) / omega
    y_prey_peak1 = 5.0 + 2.7
    
    t_pred_peak1 = (np.pi / 2 + 0.85) / omega
    y_pred_peak1 = 3.0 + 1.7
    
    # Vertical dashed lines down from first peaks to illustrate the lag
    ax.plot([t_prey_peak1, t_prey_peak1], [0, y_prey_peak1], color=color_prey, ls="--", lw=1.2, alpha=0.6)
    ax.plot([t_pred_peak1, t_pred_peak1], [0, y_pred_peak1], color=color_pred, ls="--", lw=1.2, alpha=0.6)
    
    ax.scatter([t_prey_peak1], [y_prey_peak1], color=color_prey, s=35, zorder=4)
    ax.scatter([t_pred_peak1], [y_pred_peak1], color=color_pred, s=35, zorder=4)
    
    # Horizontal bracket / arrow showing lag and annotation
    ax.annotate(
        "", 
        xy=(t_pred_peak1, 8.3), 
        xytext=(t_prey_peak1, 8.3),
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.4)
    )
    ax.text(
        t_prey_peak1, 8.6,
        "predator peak follows prey peak",
        fontsize=12,
        color=INK,
        ha="left",
        va="bottom",
        bbox=dict(fc="white", ec="none", pad=2)
    )
    
    # Direct curve labels (placed along curves away from icons)
    ax.text(
        4.6, 6.2, 
        "prey population", 
        color=color_prey, 
        fontsize=12.5, 
        fontweight="bold",
        bbox=dict(fc="white", ec="none", pad=2)
    )
    
    ax.text(
        5.2, 2.2, 
        "predator population", 
        color=color_pred, 
        fontsize=12.5, 
        fontweight="bold",
        bbox=dict(fc="white", ec="none", pad=2)
    )
    
    # Clean dedicated side panel for icons and labels on the right (x > 10.4)
    # Icon for prey (grasshopper) beside prey line extension at top right
    gh_x, gh_y = 10.9, 7.3
    # Body
    ax.plot([gh_x - 0.25, gh_x + 0.25], [gh_y - 0.05, gh_y + 0.1], color=color_prey, lw=2.2)
    # Head & antenna
    ax.plot([gh_x + 0.25, gh_x + 0.35], [gh_y + 0.1, gh_y + 0.15], color=color_prey, lw=2.0)
    ax.plot([gh_x + 0.32, gh_x + 0.42], [gh_y + 0.15, gh_y + 0.35], color=color_prey, lw=1.2)
    # Bent jumping leg
    ax.plot([gh_x - 0.05, gh_x - 0.15, gh_x - 0.3], [gh_y + 0.05, gh_y + 0.32, gh_y - 0.2], color=color_prey, lw=1.8)
    # Front legs
    ax.plot([gh_x + 0.1, gh_x + 0.15], [gh_y, gh_y - 0.2], color=color_prey, lw=1.3)
    ax.plot([gh_x + 0.2, gh_x + 0.28], [gh_y + 0.05, gh_y - 0.18], color=color_prey, lw=1.3)
    
    ax.text(gh_x + 0.52, gh_y, "prey\n(e.g. grasshopper)", color=color_prey, fontsize=11.5, va="center", fontweight="bold")
    
    # Icon for predator (owl silhouette sketch) beside predator line at lower right
    owl_x, owl_y = 10.9, 2.5
    theta = np.linspace(0, 2*np.pi, 30)
    # Body
    ax.plot(owl_x + 0.2 * np.cos(theta), owl_y + 0.3 * np.sin(theta), color=color_pred, lw=1.8)
    # Ear tufts
    ax.plot([owl_x - 0.14, owl_x - 0.18], [owl_y + 0.24, owl_y + 0.4], color=color_pred, lw=1.6)
    ax.plot([owl_x + 0.14, owl_x + 0.18], [owl_y + 0.24, owl_y + 0.4], color=color_pred, lw=1.6)
    # Wings
    ax.plot([owl_x - 0.18, owl_x - 0.38, owl_x - 0.1], [owl_y + 0.15, owl_y + 0.22, owl_y - 0.18], color=color_pred, lw=1.5)
    ax.plot([owl_x + 0.18, owl_x + 0.38, owl_x + 0.1], [owl_y + 0.15, owl_y + 0.22, owl_y - 0.18], color=color_pred, lw=1.5)
    # Beak
    ax.plot([owl_x - 0.05, owl_x, owl_x + 0.05], [owl_y + 0.16, owl_y + 0.08, owl_y + 0.16], color=color_pred, lw=1.5)
    
    ax.text(owl_x + 0.52, owl_y, "predator\n(e.g. owl)", color=color_pred, fontsize=11.5, va="center", fontweight="bold")

    save(fig, out)
