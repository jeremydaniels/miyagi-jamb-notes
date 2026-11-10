from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    curve_color = DEEP["blue"]
    stressed_color = DEEP["orange"]

    # ================= TOP SECTION: FALLING TUNE =================
    # Title / Tune label
    ax.text(
        0.8, 9.2,
        "Falling tune (Tune 1): statements, wh-questions, commands",
        fontsize=15, weight="bold", color=INK, ha="left", va="center"
    )

    # Pitch reference guides (subtle dotted lines)
    ax.axhline(8.1, xmin=0.08, xmax=0.92, color=GREY, ls=":", lw=1, alpha=0.6)
    ax.axhline(6.8, xmin=0.08, xmax=0.92, color=GREY, ls=":", lw=1, alpha=0.6)
    ax.text(0.75, 8.1, "High", fontsize=11, color=GREY, ha="right", va="center")
    ax.text(0.75, 6.8, "Low", fontsize=11, color=GREY, ha="right", va="center")

    # Curve for Falling Tune
    # "I bought a new" stays relatively flat / mid-high, then rises slightly on "CAR" and falls steeply
    x1 = np.linspace(1.2, 8.2, 300)
    # Piecewise or smooth formula:
    # 1.2 to 6.2: flat around 7.6
    # 6.2 to 7.0: rises to 8.2
    # 7.0 to 8.2: falls steeply to 6.8
    y1 = np.piecewise(
        x1,
        [x1 < 6.0, (x1 >= 6.0) & (x1 < 7.1), x1 >= 7.1],
        [
            lambda x: 7.6 + 0.05 * np.sin((x - 1.2) * 1.5),
            lambda x: 7.6 + 0.55 * np.sin((x - 6.0) / 1.1 * (np.pi / 2)),
            lambda x: 6.8 + 1.35 * (1 - (x - 7.1) / 1.1)
        ]
    )
    ax.plot(x1, y1, color=curve_color, lw=3.5, solid_capstyle="round")

    # Down arrow at the end of the falling tune
    ax.annotate(
        "", xy=(8.3, 6.6), xytext=(8.0, 7.0),
        arrowprops=dict(arrowstyle="->", color=curve_color, lw=3.5, mutation_scale=20)
    )

    # Words for Top Sentence: "I bought a new CAR."
    # Positions aligned under the curve
    ax.text(1.5, 5.9, "I", fontsize=17, color=INK, ha="center", va="center")
    ax.text(2.8, 5.9, "bought", fontsize=17, color=INK, ha="center", va="center")
    ax.text(4.2, 5.9, "a", fontsize=17, color=INK, ha="center", va="center")
    ax.text(5.5, 5.9, "new", fontsize=17, color=INK, ha="center", va="center")
    ax.text(7.4, 5.9, "CAR.", fontsize=18, weight="bold", color=stressed_color, ha="center", va="center")


    # ================= BOTTOM SECTION: RISING TUNE =================
    # Title / Tune label
    ax.text(
        0.8, 4.4,
        "Rising tune (Tune 2): yes/no questions, uncertainty",
        fontsize=15, weight="bold", color=INK, ha="left", va="center"
    )

    # Pitch reference guides (subtle dotted lines)
    ax.axhline(3.3, xmin=0.08, xmax=0.92, color=GREY, ls=":", lw=1, alpha=0.6)
    ax.axhline(2.0, xmin=0.08, xmax=0.92, color=GREY, ls=":", lw=1, alpha=0.6)
    ax.text(0.75, 3.3, "High", fontsize=11, color=GREY, ha="right", va="center")
    ax.text(0.75, 2.0, "Low", fontsize=11, color=GREY, ha="right", va="center")

    # Curve for Rising Tune
    # "Are you" starts flat and low (~2.1), then rises steeply on "COMING?" up to ~3.3
    x2 = np.linspace(1.2, 7.8, 300)
    y2 = np.piecewise(
        x2,
        [x2 < 4.8, x2 >= 4.8],
        [
            lambda x: 2.1 + 0.03 * np.sin((x - 1.2) * 1.5),
            lambda x: 2.1 + 1.15 * ((x - 4.8) / 3.0)**1.5
        ]
    )
    ax.plot(x2, y2, color=curve_color, lw=3.5, solid_capstyle="round")

    # Up arrow at the end of the rising tune
    ax.annotate(
        "", xy=(8.0, 3.45), xytext=(7.65, 3.1),
        arrowprops=dict(arrowstyle="->", color=curve_color, lw=3.5, mutation_scale=20)
    )

    # Words for Bottom Sentence: "Are you COMING?"
    ax.text(1.8, 1.2, "Are", fontsize=17, color=INK, ha="center", va="center")
    ax.text(3.5, 1.2, "you", fontsize=17, color=INK, ha="center", va="center")
    ax.text(6.4, 1.2, "COMING?", fontsize=18, weight="bold", color=stressed_color, ha="center", va="center")

    save(fig, out)
