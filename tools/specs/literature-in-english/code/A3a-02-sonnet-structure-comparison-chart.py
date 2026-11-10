from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(13, 10.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10.5)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.9, "Comparison of Sonnet Structures", fontsize=18, fontweight='bold', ha='center', va='center', color=INK)

    # Column Titles
    ax.text(3.3, 9.2, "Shakespearean Sonnet", fontsize=16, fontweight='bold', ha='center', va='center', color=INK)
    ax.text(9.7, 9.2, "Petrarchan Sonnet", fontsize=16, fontweight='bold', ha='center', va='center', color=INK)

    # Line height parameters
    # 14 lines total. Map line 1 (top) to line 14 (bottom).
    y_start = 8.4
    line_h = 0.5

    def line_y(line_num):
        # line_num from 1 to 14
        return y_start - (line_num - 1) * line_h

    # Colors
    c_q = BLUE
    c_c = ORANGE
    c_oct = GREEN
    c_ses = LAV

    # Shakespearean Blocks (x from 1.0 to 4.2)
    # Quatrain 1: lines 1-4
    # Quatrain 2: lines 5-8
    # Quatrain 3: lines 9-12
    # Couplet: lines 13-14

    # Outer bracket / block for Quatrains 1-3
    q13_top = line_y(1) + 0.22
    q13_bot = line_y(12) - 0.22
    rect_q = plt.Rectangle((1.0, q13_bot), 3.2, q13_top - q13_bot, facecolor=c_q, edgecolor=DEEP["blue"], lw=1.5, alpha=0.35, zorder=1)
    ax.add_patch(rect_q)

    # Couplet block
    c_top = line_y(13) + 0.22
    c_bot = line_y(14) - 0.22
    rect_c = plt.Rectangle((1.0, c_bot), 3.2, c_top - c_bot, facecolor=c_c, edgecolor=DEEP["orange"], lw=1.5, alpha=0.35, zorder=1)
    ax.add_patch(rect_c)

    # Labels for Shakespearean blocks
    ax.text(1.2, (q13_top + q13_bot)/2, "Quatrains 1-3\n(12 lines)", fontsize=14, fontweight='bold', va='center', ha='left', color=INK)
    ax.text(1.2, (c_top + c_bot)/2, "Couplet\n(2 lines)", fontsize=14, fontweight='bold', va='center', ha='left', color=INK)

    # Rhyme schemes Shakespearean: abab cdcd efef gg
    sh_rhymes = ['a', 'b', 'a', 'b', 'c', 'd', 'c', 'd', 'e', 'f', 'e', 'f', 'g', 'g']
    for i in range(14):
        y = line_y(i + 1)
        # Line indicator bar
        ax.plot([2.7, 3.7], [y, y], color=DEEP["blue"] if i < 12 else DEEP["orange"], lw=2.5, solid_capstyle='round')
        # Rhyme letter
        ax.text(4.0, y, sh_rhymes[i], fontsize=14, fontfamily='monospace', fontweight='bold', ha='center', va='center', color=INK)

    # Shakespeare rhyme scheme label / bracket
    ax.text(2.6, 0.7, "Rhyme scheme:\nabab cdcd efef gg", fontsize=14, ha='center', va='top', color=INK,
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.4'))

    # Petrarchan Blocks (x from 7.4 to 10.6)
    # Octave: lines 1-8
    # Sestet: lines 9-14
    oct_top = line_y(1) + 0.22
    oct_bot = line_y(8) - 0.22
    rect_oct = plt.Rectangle((7.4, oct_bot), 3.2, oct_top - oct_bot, facecolor=c_oct, edgecolor=DEEP["green"], lw=1.5, alpha=0.35, zorder=1)
    ax.add_patch(rect_oct)

    ses_top = line_y(9) + 0.22
    ses_bot = line_y(14) - 0.22
    rect_ses = plt.Rectangle((7.4, ses_bot), 3.2, ses_top - ses_bot, facecolor=c_ses, edgecolor=DEEP["lav"], lw=1.5, alpha=0.35, zorder=1)
    ax.add_patch(rect_ses)

    # Labels for Petrarchan blocks
    ax.text(7.6, (oct_top + oct_bot)/2, "Octave\n(8 lines)", fontsize=14, fontweight='bold', va='center', ha='left', color=INK)
    ax.text(7.6, (ses_top + ses_bot)/2, "Sestet\n(6 lines)", fontsize=14, fontweight='bold', va='center', ha='left', color=INK)

    # Rhyme schemes Petrarchan: abbaabba cdecde
    pet_rhymes = ['a', 'b', 'b', 'a', 'a', 'b', 'b', 'a', 'c', 'd', 'e', 'c', 'd', 'e']
    for i in range(14):
        y = line_y(i + 1)
        # Line indicator bar
        ax.plot([9.1, 10.1], [y, y], color=DEEP["green"] if i < 8 else DEEP["lav"], lw=2.5, solid_capstyle='round')
        # Rhyme letter
        ax.text(10.4, y, pet_rhymes[i], fontsize=14, fontfamily='monospace', fontweight='bold', ha='center', va='center', color=INK)

    # Petrarchan rhyme scheme label / bracket
    ax.text(9.0, 0.7, "Rhyme scheme:\nabbaabba cdecde", fontsize=14, ha='center', va='top', color=INK,
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.4'))

    # Line numbers down the sides or middle
    # Center divider with line numbers
    for i in range(14):
        y = line_y(i + 1)
        ax.text(0.5, y, f"L{i+1}", fontsize=14, color=GREY, ha='right', va='center')
        ax.text(12.3, y, f"L{i+1}", fontsize=14, color=GREY, ha='left', va='center')

    # Volta annotation pointing to line 9 on Petrarchan and line 13 on Shakespearean
    # Shakespearean line 13 y: line_y(13)
    # Petrarchan line 9 y: line_y(9)
    y_sh_volta = line_y(13)
    y_pet_volta = line_y(9)

    # Central Volta label
    volta_x = 5.8
    volta_y = 3.6
    ax.text(volta_x, volta_y, "Volta\n(the turn in thought)", fontsize=14, fontweight='bold', ha='center', va='center', color=INK,
            bbox=dict(fc=CREAM, ec=DEEP["pink"], boxstyle='round,pad=0.5', lw=2))

    # Arrow to Shakespearean Line 13
    ax.annotate("",
                xy=(4.3, y_sh_volta), xytext=(volta_x - 0.9, volta_y - 0.4),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.2,
                                connectionstyle="arc3,rad=-0.15"))

    # Arrow to Petrarchan Line 9
    ax.annotate("",
                xy=(7.3, y_pet_volta), xytext=(volta_x + 0.9, volta_y + 0.4),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.2,
                                connectionstyle="arc3,rad=-0.15"))

    # Small indicators at arrow endpoints
    ax.plot([4.3], [y_sh_volta], 'o', color=DEEP["pink"], markersize=5)
    ax.plot([7.3], [y_pet_volta], 'o', color=DEEP["pink"], markersize=5)

    save(fig, out)
