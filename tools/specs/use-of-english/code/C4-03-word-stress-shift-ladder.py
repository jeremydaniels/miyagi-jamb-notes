from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

def draw(out):
    fig = canvas(10, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # Title
    ax.text(5.0, 7.8, "The stress moves when the word grows", 
            ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

    # Ladder steps data
    # Each step: (x_step_start, y_step_base, width_step, syllables_list, stressed_index)
    steps_data = [
        # Step 1: PHO-to-graph
        {"sylls": ["PHO", "to", "graph"], "stress": 0, "x_center": 2.2, "y_base": 1.2},
        # Step 2: pho-TO-gra-pher
        {"sylls": ["pho", "TO", "gra", "pher"], "stress": 1, "x_center": 4.1, "y_base": 2.7},
        # Step 3: pho-TO-gra-phy
        {"sylls": ["pho", "TO", "gra", "phy"], "stress": 1, "x_center": 6.0, "y_base": 4.2},
        # Step 4: pho-to-GRA-phic
        {"sylls": ["pho", "to", "GRA", "phic"], "stress": 2, "x_center": 7.9, "y_base": 5.7},
    ]

    # Draw ladder staircase structure in background
    stair_x = [0.8, 0.8, 3.1, 3.1, 5.0, 5.0, 6.9, 6.9, 9.2, 9.2]
    stair_y = [0.4, 1.0, 1.0, 2.5, 2.5, 4.0, 4.0, 5.5, 5.5, 0.4]
    ax.fill(stair_x, stair_y, color=CREAM, alpha=0.5, zorder=1)
    ax.plot(stair_x[:-1], stair_y[:-1], color=GREY, lw=2, zorder=2)

    block_h = 0.65
    block_w = 0.95
    gap = 0.08

    for step_num, step in enumerate(steps_data, 1):
        sylls = step["sylls"]
        n_syll = len(sylls)
        stress_idx = step["stress"]
        total_w = n_syll * block_w + (n_syll - 1) * gap
        
        # Calculate horizontal starting position
        x_start = step["x_center"] - total_w / 2.0
        y_bottom = step["y_base"] + 0.35

        # Step label to the left of the step
        ax.text(x_start - 0.25, y_bottom + block_h / 2.0, f"Step {step_num}", 
                ha="right", va="center", fontsize=14, fontweight="bold", color=INK)

        # Draw syllables
        stress_center_x = 0
        for i, syll in enumerate(sylls):
            bx = x_start + i * (block_w + gap)
            is_stressed = (i == stress_idx)

            fc = DEEP["orange"] if is_stressed else "#EAEAEA"
            ec = DEEP["orange"] if is_stressed else GREY
            text_color = "white" if is_stressed else INK
            weight = "bold" if is_stressed else "normal"

            rect = FancyBboxPatch((bx, y_bottom), block_w, block_h,
                                  boxstyle="round,pad=0.03,rounding_size=0.08",
                                  fc=fc, ec=ec, lw=1.5, zorder=3)
            ax.add_patch(rect)

            ax.text(bx + block_w / 2.0, y_bottom + block_h / 2.0, syll,
                    ha="center", va="center", fontsize=15, fontweight=weight,
                    color=text_color, zorder=4)

            if is_stressed:
                stress_center_x = bx + block_w / 2.0

        # Small arrow pointing up to the stressed block
        arrow_y_start = y_bottom - 0.22
        arrow_y_end = y_bottom - 0.03
        ax.annotate("", xy=(stress_center_x, arrow_y_end), xytext=(stress_center_x, arrow_y_start),
                    arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2, mutation_scale=14),
                    zorder=5)

    save(fig, out)
