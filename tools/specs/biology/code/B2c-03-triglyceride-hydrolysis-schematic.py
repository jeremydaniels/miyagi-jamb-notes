from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Helper function to generate zig-zag coords
    def make_zigzag(x_start, y_val, x_end, n_zigs=6, amp=0.18):
        xs = np.linspace(x_start, x_end, n_zigs * 2 + 1)
        ys = np.full_like(xs, y_val)
        for i in range(1, len(ys)):
            ys[i] += amp if i % 2 == 1 else -amp
        ys[0] = y_val
        ys[-1] = y_val
        return xs, ys

    # --- TOP: Triglyceride Molecule ---
    # Glycerol backbone (left bar)
    gly_rect_top = patches.FancyBboxPatch((3.0, 4.0), 0.7, 1.8, 
                                          boxstyle="round,pad=0.08", 
                                          fc=LAV, ec=DEEP["lav"], lw=2)
    ax.add_patch(gly_rect_top)
    ax.text(3.35, 4.9, "glycerol", ha="center", va="center", 
            rotation=90, fontsize=14, fontweight="bold", color=INK)

    # 3 Fatty acid tails (top)
    y_tails_top = [5.4, 4.9, 4.4]
    for y in y_tails_top:
        # Link line from glycerol
        ax.plot([3.75, 4.2], [y, y], color=DEEP["orange"], lw=2.5)
        # Zig-zag tail
        zx, zy = make_zigzag(4.2, y, 7.0, n_zigs=7, amp=0.14)
        ax.plot(zx, zy, color=DEEP["orange"], lw=2.5)
        # Label each tail
        ax.text(7.3, y, "fatty acid", ha="left", va="center", 
                fontsize=13, color=INK)

    # --- MIDDLE: Reaction Arrow ---
    # Downward arrow showing hydrolysis
    ax.annotate("", xy=(5.0, 2.7), xytext=(5.0, 3.6),
                arrowprops=dict(arrowstyle="->", lw=3, color=DEEP["blue"], mutation_scale=20))
    
    # Text next to arrow
    ax.text(5.3, 3.15, "hydrolysis (digestion by lipase)", 
            ha="left", va="center", fontsize=13, color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1))

    # --- BOTTOM: Separated Products ---
    # Separated Glycerol
    gly_rect_bot = patches.FancyBboxPatch((3.0, 0.4), 0.7, 1.4, 
                                          boxstyle="round,pad=0.08", 
                                          fc=LAV, ec=DEEP["lav"], lw=2)
    ax.add_patch(gly_rect_bot)
    ax.text(3.35, 1.1, "glycerol", ha="center", va="center", 
            rotation=90, fontsize=14, fontweight="bold", color=INK)

    # 3 Separated Fatty acids
    y_tails_bot = [1.6, 1.1, 0.6]
    for y in y_tails_bot:
        zx, zy = make_zigzag(4.5, y, 7.3, n_zigs=7, amp=0.14)
        ax.plot(zx, zy, color=DEEP["orange"], lw=2.5)

    # Label for separated fatty acids
    ax.text(7.6, 1.1, "fatty acids", ha="left", va="center", 
            fontsize=14, color=INK)

    save(fig, out)
