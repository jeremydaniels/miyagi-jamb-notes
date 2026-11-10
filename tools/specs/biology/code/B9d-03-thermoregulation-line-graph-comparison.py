from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)

    # Grid and limits
    ax.set_xlim(0, 42)
    ax.set_ylim(0, 48)
    ax.set_xticks(np.arange(0, 45, 10))
    ax.set_yticks(np.arange(0, 50, 10))
    ax.tick_params(colors=INK, labelsize=14)

    # Style spines
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_color(INK)
        ax.spines[spine].set_linewidth(1.5)

    # Gridlines
    ax.grid(True, linestyle='--', alpha=0.4, color=GREY)

    # Axis Labels
    ax.set_xlabel("temperature of surroundings (°C)", fontsize=15, color=INK, labelpad=8)
    ax.set_ylabel("body temperature (°C)", fontsize=15, color=INK, labelpad=8)

    # Data curves
    x = np.linspace(0, 40, 100)
    # Endotherm: constant body temperature at ~37 °C
    y_endo = np.full_like(x, 37.0)
    # Ectotherm: rises steadily with surroundings, slightly above ambient at low temps, roughly y = x + 1
    y_ecto = x + 1.0

    # Plot lines
    ax.plot(x, y_endo, color=DEEP["pink"], lw=3.5, label="endotherm (e.g. human)")
    ax.plot(x, y_ecto, color=DEEP["blue"], lw=3.5, label="ectotherm (e.g. lizard)")

    # 37°C guideline / marker
    ax.axhline(37, color=DEEP["pink"], linestyle=':', alpha=0.3, lw=1.2)

    # Annotations / labels for curves
    ax.text(20, 39.5, "endotherm (e.g. human)", fontsize=15, fontweight="bold",
            color=DEEP["pink"], ha="center", va="bottom",
            bbox=dict(fc="white", ec="none", pad=2))
    ax.text(20, 34.0, "constant body temperature", fontsize=14,
            fontstyle="italic", color=INK, ha="center", va="top",
            bbox=dict(fc="white", ec="none", pad=2))

    # Ectotherm label positioned along diagonal
    ax.text(27, 24, "ectotherm (e.g. lizard)", fontsize=15, fontweight="bold",
            color=DEEP["blue"], ha="left", va="top", rotation=36,
            bbox=dict(fc="white", ec="none", pad=2))
    ax.text(28.5, 20.5, "body temperature changes\nwith surroundings", fontsize=14,
            fontstyle="italic", color=INK, ha="left", va="top",
            bbox=dict(fc="white", ec="none", pad=2))

    # Legend / Clean up layout
    fig.tight_layout()
    save(fig, out)
