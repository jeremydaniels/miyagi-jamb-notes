from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(14, 5.5)
    
    # 4 subplots for the 4 patterns
    axes = [fig.add_subplot(1, 4, i+1) for i in range(4)]
    
    ridge_color = "#333333"
    delta_color = DEEP["orange"]
    core_color = DEEP["blue"]
    lw = 1.8

    for ax in axes:
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1.25)
        ax.set_aspect('equal')
        ax.axis('off')

    # Shared x array for straight-through ridges
    x = np.linspace(-0.85, 0.85, 200)

    # -------------------------------------------------------------
    # 1. Plain Arch
    # -------------------------------------------------------------
    ax1 = axes[0]
    ax1.set_title("Arch", fontsize=14, fontweight="bold", pad=12, color=INK)

    for y0 in np.linspace(-0.85, 0.75, 17):
        h = 0.35 * np.exp(-((y0 - 0.0) / 0.6)**2)
        y = y0 + h * np.exp(-(x / 0.35)**2)
        mask = (x**2 / 0.85**2 + y**2 / 0.95**2) < 0.96
        ax1.plot(x[mask], y[mask], color=ridge_color, lw=lw)

    ax1.annotate("ridges", xy=(-0.45, 0.22), xytext=(-0.55, 0.78),
                 fontsize=11.5, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    # -------------------------------------------------------------
    # 2. Loop
    # -------------------------------------------------------------
    ax2 = axes[1]
    ax2.set_title("Loop", fontsize=14, fontweight="bold", pad=12, color=INK)

    # Baseline ridges at the bottom
    for y0 in np.linspace(-0.85, -0.42, 6):
        y = y0 + 0.08 * np.sin(np.pi * (x + 0.85) / 1.7)
        mask = (x**2 / 0.85**2 + y**2 / 0.95**2) < 0.96
        ax2.plot(x[mask], y[mask], color=ridge_color, lw=lw)

    # Loop ridges smoothly parameterized from bottom-left to top-left
    core_x, core_y = -0.05, 0.08
    for r in np.linspace(0.08, 0.58, 9):
        # Continuous parameter s from -1 (bottom-left) around bend (s=0) to +1 (top-left)
        s = np.linspace(-1.0, 1.0, 180)
        # Hairpin bend around the core, extending out to the left margin
        rx = core_x + r * 0.9 * np.cos(s * np.pi / 2) - 0.9 * (s**2)
        ry = core_y + r * np.sin(s * np.pi / 2) + 0.08 * s
        mask = (rx >= -0.85) & ((rx**2 / 0.85**2 + ry**2 / 0.95**2) < 0.96)
        ax2.plot(rx[mask], ry[mask], color=ridge_color, lw=lw)

    # Outer enclosing ridges arching over the top
    for y0 in np.linspace(0.7, 0.88, 3):
        y = y0 - 0.16 * (x - 0.05)**2
        mask = (x**2 / 0.85**2 + y**2 / 0.95**2) < 0.96
        ax2.plot(x[mask], y[mask], color=ridge_color, lw=lw)

    # Delta on right side
    dx, dy = 0.52, -0.32
    ax2.plot([dx-0.08, dx+0.08, dx, dx-0.08], [dy-0.07, dy-0.07, dy+0.07, dy-0.07],
             color=delta_color, lw=2.2)
    # Core marker
    ax2.plot(core_x, core_y, marker='o', markersize=4.5, color=core_color)

    # Annotations
    ax2.annotate("core", xy=(core_x, core_y), xytext=(core_x - 0.25, core_y + 0.65),
                 fontsize=11.5, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
    
    ax2.annotate("delta", xy=(dx, dy), xytext=(dx + 0.22, dy + 0.38),
                 fontsize=11.5, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    # -------------------------------------------------------------
    # 3. Whorl
    # -------------------------------------------------------------
    ax3 = axes[2]
    ax3.set_title("Whorl", fontsize=14, fontweight="bold", pad=12, color=INK)

    # Concentric rings / spiral in centre
    w_core_x, w_core_y = 0.0, 0.05
    for r in np.linspace(0.06, 0.52, 8):
        theta = np.linspace(0, 2*np.pi, 150)
        wx = w_core_x + r * 1.05 * np.cos(theta)
        wy = w_core_y + r * 0.88 * np.sin(theta)
        ax3.plot(wx, wy, color=ridge_color, lw=lw)

    # Lower framing ridges
    for y0 in np.linspace(-0.85, -0.48, 5):
        y = y0 + 0.12 * np.cos(x * 2.5)
        mask = (x**2 / 0.85**2 + y**2 / 0.95**2) < 0.96
        ax3.plot(x[mask], y[mask], color=ridge_color, lw=lw)

    # Upper framing ridges
    for y0 in np.linspace(0.55, 0.85, 4):
        y = y0 + 0.12 * (1 - x**2)
        mask = (x**2 / 0.85**2 + y**2 / 0.95**2) < 0.96
        ax3.plot(x[mask], y[mask], color=ridge_color, lw=lw)

    # Deltas on left and right
    dl_x, dl_y = -0.58, -0.35
    dr_x, dr_y = 0.58, -0.35
    ax3.plot([dl_x-0.07, dl_x+0.07, dl_x, dl_x-0.07], [dl_y-0.06, dl_y-0.06, dl_y+0.06, dl_y-0.06],
             color=delta_color, lw=2.2)
    ax3.plot([dr_x-0.07, dr_x+0.07, dr_x, dr_x-0.07], [dr_y-0.06, dr_y-0.06, dr_y+0.06, dr_y-0.06],
             color=delta_color, lw=2.2)
    
    # Core point
    ax3.plot(w_core_x, w_core_y, marker='o', markersize=4.5, color=core_color)

    # Annotations
    ax3.annotate("core", xy=(w_core_x, w_core_y), xytext=(w_core_x, w_core_y + 0.65),
                 fontsize=11.5, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
    
    ax3.annotate("delta", xy=(dl_x, dl_y), xytext=(dl_x - 0.05, dl_y + 0.38),
                 fontsize=11.5, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    ax3.annotate("delta", xy=(dr_x, dr_y), xytext=(dr_x + 0.05, dr_y + 0.38),
                 fontsize=11.5, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    # -------------------------------------------------------------
    # 4. Composite (double loop)
    # -------------------------------------------------------------
    ax4 = axes[3]
    ax4.set_title("Composite (double loop)", fontsize=13, fontweight="bold", pad=12, color=INK)

    for shift in np.linspace(-0.25, 0.25, 7):
        s_y = np.linspace(-0.7, 0.75, 140)
        s_x = 0.32 * np.sin(s_y * np.pi / 0.5) + shift * 0.7
        mask = (s_x**2 / 0.85**2 + s_y**2 / 0.95**2) < 0.94
        ax4.plot(s_x[mask], s_y[mask], color=ridge_color, lw=lw)

    for r in np.linspace(0.18, 0.42, 4):
        # loop 1 (top right)
        th1 = np.linspace(-np.pi/3, np.pi, 80)
        ax4.plot(0.15 + r*np.cos(th1), 0.28 + r*0.75*np.sin(th1), color=ridge_color, lw=lw)
        # loop 2 (bottom left)
        th2 = np.linspace(2*np.pi/3, 2*np.pi, 80)
        ax4.plot(-0.15 + r*np.cos(th2), -0.22 + r*0.75*np.sin(th2), color=ridge_color, lw=lw)

    for y0 in [-0.82, -0.65, 0.7, 0.85]:
        y = y0 + 0.08 * np.sin(x * 3)
        mask = (x**2 / 0.85**2 + y**2 / 0.95**2) < 0.96
        ax4.plot(x[mask], y[mask], color=ridge_color, lw=lw)

    # Deltas on both sides
    cdl_x, cdl_y = -0.58, 0.22
    cdr_x, cdr_y = 0.58, -0.28
    ax4.plot([cdl_x-0.07, cdl_x+0.07, cdl_x, cdl_x-0.07], [cdl_y-0.06, cdl_y-0.06, cdl_y+0.06, cdl_y-0.06],
             color=delta_color, lw=2.2)
    ax4.plot([cdr_x-0.07, cdr_x+0.07, cdr_x, cdr_x-0.07], [cdr_y-0.06, cdr_y-0.06, cdr_y+0.06, cdr_y-0.06],
             color=delta_color, lw=2.2)

    ax4.annotate("delta", xy=(cdl_x, cdl_y), xytext=(cdl_x + 0.05, cdl_y + 0.38),
                 fontsize=11.5, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    ax4.annotate("delta", xy=(cdr_x, cdr_y), xytext=(cdr_x - 0.05, cdr_y + 0.38),
                 fontsize=11.5, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    # Subtle card borders for all 4 pattern windows
    for ax in axes:
        rect = plt.Rectangle((-0.88, -0.95), 1.76, 1.9, fill=False,
                             edgecolor=GREY, linewidth=1.5, linestyle="--",
                             joinstyle="round")
        ax.add_patch(rect)

    plt.tight_layout()
    save(fig, out)
