from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 6.2)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title / Column Headers
    ax.text(2.6, 6.6, "Onset", fontsize=18, fontweight="bold", color=INK, ha="center", va="center")
    ax.text(5.6, 6.6, "Rhyme", fontsize=18, fontweight="bold", color=INK, ha="center", va="center")

    # Word rows configuration
    # (word label, onset text, onset width, rhyme text)
    # Total rhyme block: x from 4.2 to 7.0 (width 2.8)
    # The onset block is immediately to the left of the rhyme block: x starts at 4.2 - onset_w
    rows = [
        ("cat", "/k/", 2.4, 5.0),
        ("hat", "/h/", 2.4, 3.6),
        ("flat", "/fl/", 2.8, 2.2)
    ]

    block_h = 0.95
    rhyme_x0 = 4.2
    rhyme_w = 2.8

    for word, onset_ph, onset_w, y_center in rows:
        y0 = y_center - block_h / 2

        # Word label on the far left
        ax.text(0.9, y_center, f'"{word}"', fontsize=17, fontweight="bold", color=INK, ha="center", va="center")

        # Onset block (pale blue)
        onset_x0 = rhyme_x0 - onset_w
        rect_onset = patches.FancyBboxPatch(
            (onset_x0, y0), onset_w - 0.05, block_h,
            boxstyle="round,pad=0.04,rounding_size=0.18",
            facecolor=BLUE, edgecolor=DEEP["blue"], linewidth=2.0
        )
        ax.add_patch(rect_onset)
        ax.text(onset_x0 + (onset_w - 0.05) / 2, y_center, onset_ph,
                fontsize=16, color=INK, ha="center", va="center")

        # Rhyme block (soft orange)
        rect_rhyme = patches.FancyBboxPatch(
            (rhyme_x0, y0), rhyme_w, block_h,
            boxstyle="round,pad=0.04,rounding_size=0.18",
            facecolor=ORANGE, edgecolor=DEEP["orange"], linewidth=2.0
        )
        ax.add_patch(rect_rhyme)
        ax.text(rhyme_x0 + rhyme_w / 2, y_center, "/æt/",
                fontsize=16, color=INK, ha="center", va="center")

    # Curved bracket joining the three orange blocks on the right
    # Top rhyme y=5.0, Bottom rhyme y=2.2, Midpoint y=3.6
    # Parametric smooth curly bracket along x = 7.35
    t = np.linspace(-1, 1, 200)
    y_bracket = 3.6 + 1.45 * t
    # S-curve displacement to make a classic bracket shape
    # Using a piecewise smooth expression for a clean right curly bracket '}'
    bx = 7.35 + 0.18 * (1.0 - (np.abs(t)) ** 0.5)
    # Draw bracket line
    bracket_x = []
    bracket_y = []
    for yi in np.linspace(2.15, 5.05, 150):
        # distance from center (3.6), normalized to [-1, 1]
        ny = (yi - 3.6) / 1.45
        # Bracket shape pointing right at center ny=0, and inward at ends ny=+-1
        val = np.clip(1.0 - np.abs(ny), 0, 1)
        # Classic bracket tip
        shift = 0.22 * (val ** 1.8)
        bracket_x.append(7.35 + shift)
        bracket_y.append(yi)

    ax.plot(bracket_x, bracket_y, color=INK, lw=2.2, solid_capstyle="round")

    # Bracket annotation label
    ax.text(7.8, 3.6, "Same rhyme =\nwords rhyme",
            fontsize=15, color=INK, ha="left", va="center",
            linespacing=1.3,
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=GREY, lw=1.2))

    save(fig, out)
