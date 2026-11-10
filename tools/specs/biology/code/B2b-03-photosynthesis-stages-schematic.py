from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(16, 10.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10.5)
    ax.axis("off")

    # Chloroplast Outer and Inner Envelope (Large Oval)
    outer_envelope = patches.Ellipse((8, 5.2), 14.8, 8.8, edgecolor=DEEP["green"], facecolor="#f4f9f4", lw=3.5, zorder=1)
    inner_envelope = patches.Ellipse((8, 5.2), 14.3, 8.3, edgecolor=DEEP["green"], facecolor="#ffffff", lw=1.8, linestyle="--", zorder=2)
    ax.add_patch(outer_envelope)
    ax.add_patch(inner_envelope)

    # Title & Region Dividers / Labels
    ax.text(8, 10.0, "Photosynthesis: Light Reactions & Calvin Cycle", fontsize=18, fontweight="bold", ha="center", va="center", color=INK)
    
    # Left & Right Zone Titles
    ax.text(4.2, 8.6, "Light reactions (grana / thylakoids)", fontsize=15, fontweight="bold", ha="center", va="center", color=DEEP["green"], bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"), zorder=10)
    ax.text(11.8, 8.6, "Dark reactions (stroma) / Calvin cycle", fontsize=15, fontweight="bold", ha="center", va="center", color=DEEP["orange"], bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"), zorder=10)
    
    # Stroma background label
    ax.text(13.2, 2.0, "stroma", fontsize=15, fontstyle="italic", color=DEEP["green"], ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", fc="#eef7ee", ec=DEEP["green"], lw=1.2), zorder=10)

    # --- LEFT SIDE: Light Reactions & Granum ---
    # Draw Granum (Stack of Thylakoids)
    stack_x = 4.2
    disc_y_list = [4.3, 4.8, 5.3, 5.8]
    for y in disc_y_list:
        disc = patches.FancyBboxPatch((stack_x - 1.2, y - 0.2), 2.4, 0.4, boxstyle="round,pad=0.08", edgecolor=DEEP["green"], facecolor=GREEN, lw=1.8, zorder=3)
        ax.add_patch(disc)
    
    # Granum & Chlorophyll Labels
    ax.text(stack_x, 3.8, "granum", fontsize=15, fontweight="bold", ha="center", va="center", color=DEEP["green"], bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=1), zorder=10)
    ax.text(stack_x, 5.05, "chlorophyll", fontsize=14, ha="center", va="center", color=INK, zorder=10, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # Sunlight Arrow striking thylakoids
    ax.annotate("sunlight", xy=(3.2, 5.7), xytext=(1.2, 7.8),
                arrowprops=dict(facecolor=DEEP["orange"], edgecolor=DEEP["orange"], width=3, headwidth=10, shrink=0.05),
                fontsize=15, fontweight="bold", color=DEEP["orange"], ha="center", va="center", zorder=10, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # Water entering
    ax.annotate("water (H₂O)", xy=(stack_x - 0.7, 4.3), xytext=(1.3, 3.0),
                arrowprops=dict(facecolor=DEEP["blue"], edgecolor=DEEP["blue"], width=2.5, headwidth=9, shrink=0.05),
                fontsize=15, fontweight="bold", color=DEEP["blue"], ha="center", va="center", zorder=10, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # Photolysis inside / next to granum
    ax.text(2.6, 4.6, "photolysis", fontsize=14, fontstyle="italic", ha="center", va="center", color=INK, bbox=dict(boxstyle="round,pad=0.2", fc=CREAM, ec=GREY, lw=1), zorder=10)

    # Oxygen leaving
    ax.annotate("oxygen (O₂)", xy=(1.5, 1.4), xytext=(stack_x - 0.5, 4.0),
                arrowprops=dict(facecolor=DEEP["blue"], edgecolor=DEEP["blue"], width=2.5, headwidth=9, shrink=0.05),
                fontsize=15, fontweight="bold", color=DEEP["blue"], ha="center", va="center", zorder=10, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # --- CROSSING ARROWS (Between Grana and Stroma) ---
    # Top forwarding arrows: ATP and reduced NADP
    # ATP forward
    ax.annotate("", xy=(9.8, 6.7), xytext=(5.5, 6.7),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=3, mutation_scale=20), zorder=10)
    ax.text(7.65, 7.05, "ATP", fontsize=14, fontweight="bold", ha="center", va="center", color=DEEP["pink"], bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"), zorder=10)

    # Reduced NADP forward
    ax.annotate("", xy=(9.8, 5.9), xytext=(5.5, 5.9),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=3, mutation_scale=20), zorder=10)
    ax.text(7.65, 6.25, "reduced NADP", fontsize=14, fontweight="bold", ha="center", va="center", color=DEEP["blue"], bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"), zorder=10)

    # Bottom returning arrows: ADP + phosphate and NADP
    # NADP return
    ax.annotate("", xy=(5.5, 4.8), xytext=(9.8, 4.8),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.5, linestyle="--", mutation_scale=20), zorder=10)
    ax.text(7.65, 5.15, "NADP", fontsize=14, ha="center", va="center", color=DEEP["blue"], bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"), zorder=10)

    # ADP + phosphate return
    ax.annotate("", xy=(5.5, 4.0), xytext=(9.8, 4.0),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5, linestyle="--", mutation_scale=20), zorder=10)
    ax.text(7.65, 4.35, "ADP + phosphate", fontsize=14, ha="center", va="center", color=DEEP["pink"], bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"), zorder=10)

    # --- RIGHT SIDE: Calvin Cycle (Dark Reactions) ---
    cx, cy, r = 11.8, 5.2, 1.8
    # Center label for Calvin cycle
    ax.text(cx, cy, "Calvin\ncycle", fontsize=16, fontweight="bold", ha="center", va="center", color=DEEP["orange"], bbox=dict(boxstyle="circle,pad=0.3", fc="#fff6ee", ec=DEEP["orange"], lw=1.5), zorder=10)

    # Pathway nodes on the circle:
    # 1. RuBP at top-left (~140 deg)
    rubp_x, rubp_y = cx + r * np.cos(np.radians(135)), cy + r * np.sin(np.radians(135))
    ax.text(rubp_x, rubp_y, "RuBP (5C)", fontsize=14, fontweight="bold", ha="center", va="center", color=INK, bbox=dict(boxstyle="round,pad=0.25", fc=CREAM, ec=GREY), zorder=10)

    # 2. PGA at top-right (~45 deg)
    pga_x, pga_y = cx + r * np.cos(np.radians(40)), cy + r * np.sin(np.radians(40))
    ax.text(pga_x, pga_y, "2 × PGA (3C)", fontsize=14, fontweight="bold", ha="center", va="center", color=INK, bbox=dict(boxstyle="round,pad=0.25", fc=CREAM, ec=GREY), zorder=10)

    # 3. Triose phosphate at bottom (~270 deg)
    tp_x, tp_y = cx, cy - r
    ax.text(tp_x, tp_y, "triose phosphate (3C)", fontsize=14, fontweight="bold", ha="center", va="center", color=INK, bbox=dict(boxstyle="round,pad=0.25", fc=CREAM, ec=GREY), zorder=10)

    # CO2 entering at top
    ax.annotate("CO₂", xy=(cx, cy + r - 0.2), xytext=(cx, 9.3),
                arrowprops=dict(facecolor=DEEP["green"], edgecolor=DEEP["green"], width=2.5, headwidth=9, shrink=0.08),
                fontsize=15, fontweight="bold", color=DEEP["green"], ha="center", va="center", zorder=11, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # Cycle arrows
    ax.annotate("", xy=(pga_x, pga_y + 0.3), xytext=(rubp_x + 0.6, rubp_y + 0.6),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=3, connectionstyle="arc3,rad=-0.4", mutation_scale=20), zorder=9)
    
    ax.annotate("", xy=(tp_x + 0.8, tp_y + 0.4), xytext=(pga_x + 0.4, pga_y - 0.3),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=3, connectionstyle="arc3,rad=-0.4", mutation_scale=20), zorder=9)

    ax.annotate("", xy=(rubp_x - 0.4, rubp_y - 0.4), xytext=(tp_x - 0.8, tp_y + 0.4),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=3, connectionstyle="arc3,rad=-0.4", mutation_scale=20), zorder=9)

    # Regeneration uses ATP annotation on Arc 3
    ax.text(cx - 1.6, cy - 0.5, "uses ATP", fontsize=14, fontstyle="italic", ha="center", va="center", color=DEEP["pink"], bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"), zorder=10)

    # Product leaving cycle from triose phosphate -> glucose -> starch
    ax.annotate("", xy=(cx + 2.5, tp_y), xytext=(tp_x + 1.5, tp_y),
                arrowprops=dict(facecolor=INK, edgecolor=INK, width=2.5, headwidth=9), zorder=10)
    ax.text(cx + 2.6, tp_y, "glucose", fontsize=14, fontweight="bold", ha="left", va="center", color=INK, bbox=dict(boxstyle="round,pad=0.2", fc=CREAM, ec=GREY), zorder=10)

    ax.annotate("", xy=(cx + 2.8, tp_y - 1.3), xytext=(cx + 2.8, tp_y - 0.4),
                arrowprops=dict(facecolor=INK, edgecolor=INK, width=2.5, headwidth=9), zorder=10)
    ax.text(cx + 2.8, tp_y - 1.6, "starch", fontsize=14, fontweight="bold", ha="center", va="center", color=INK, bbox=dict(boxstyle="round,pad=0.2", fc=CREAM, ec=GREY), zorder=10)

    save(fig, out)
