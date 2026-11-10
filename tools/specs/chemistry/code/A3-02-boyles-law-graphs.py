from style import *
import numpy as np

def draw(out):
    fig = canvas(15, 5.5)

    # Subplot 1: P vs V (hyperbola)
    ax1 = fig.add_subplot(1, 3, 1)
    axes_clean(ax1, "V", "P", 10, 10)
    v = np.linspace(1.2, 9.2, 200)
    p = 8.5 / v
    ax1.plot(v, p, color=DEEP["blue"], lw=3.5)
    ax1.set_title("P against V", fontsize=16, color=INK, pad=15)
    ax1.text(5.5, 4.5, r"$P \propto \frac{1}{V}$", fontsize=16, color=INK,
             bbox=dict(fc="white", ec="none", pad=2))

    # Subplot 2: P vs 1/V (straight line from origin)
    ax2 = fig.add_subplot(1, 3, 2)
    axes_clean(ax2, "1/V", "P", 10, 10)
    inv_v = np.linspace(0, 8.5, 200)
    p2 = 0.95 * inv_v
    ax2.plot(inv_v, p2, color=DEEP["blue"], lw=3.5)
    ax2.set_title("P against 1/V", fontsize=16, color=INK, pad=15)
    ax2.text(3.5, 6.5, r"Linear through origin", fontsize=15, color=INK,
             bbox=dict(fc="white", ec="none", pad=2))

    # Subplot 3: PV vs P (horizontal constant line)
    ax3 = fig.add_subplot(1, 3, 3)
    axes_clean(ax3, "P", "PV", 10, 10)
    p3 = np.linspace(0.5, 9.0, 200)
    pv = np.full_like(p3, 5.0)
    ax3.plot(p3, pv, color=DEEP["blue"], lw=3.5)
    ax3.set_title("PV against P", fontsize=16, color=INK, pad=15)
    ax3.text(4.5, 6.2, r"$PV = \mathrm{constant}$", fontsize=16, color=INK,
             bbox=dict(fc="white", ec="none", pad=2))

    fig.tight_layout(pad=3.0)
    save(fig, out)
