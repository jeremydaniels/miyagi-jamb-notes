from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)

    # Set up axes
    axes_clean(ax, "Frequency (f)", "Current (I)", 10, 10)

    # Generate resonance curve (Lorentzian-like / RLC current response)
    f = np.linspace(0.5, 9.5, 400)
    f0 = 5.0
    gamma = 1.0  # bandwidth parameter
    # Current response I(f)
    I_max = 8.5
    I = I_max / np.sqrt(1 + ((f**2 - f0**2) / (gamma * f))**2)

    # Shading under curve
    ax.fill_between(f, I, color=BLUE, alpha=0.25)

    # Plot resonance curve
    ax.plot(f, I, color=DEEP["blue"], lw=3.5)

    # Dotted vertical line from peak to x-axis
    peak_y = np.max(I)
    ax.plot([f0, f0], [0, peak_y], color=DEEP["pink"], lw=2.5, linestyle="--")

    # Mark the peak point
    ax.plot(f0, peak_y, marker='o', markersize=8, color=DEEP["blue"])

    # Labels and annotations
    ax.text(f0, -0.6, "Resonant Frequency ($f_0$)", ha="center", va="top",
            fontsize=15, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # Title / label for the curve
    ax.text(f0, peak_y + 0.4, "Resonance Peak ($I_{max}$)", ha="center", va="bottom",
            fontsize=15, color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Title of the graph
    ax.text(5.0, 9.6, "Resonance Curve", ha="center", va="center",
            fontsize=18, fontweight="bold", color=INK)

    save(fig, out)
