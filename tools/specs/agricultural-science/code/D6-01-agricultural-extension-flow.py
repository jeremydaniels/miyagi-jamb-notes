from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Title
    ax.text(5.0, 8.0, "Two-Way Flow of Agricultural Extension", 
            fontsize=18, fontweight='bold', color=INK, ha='center', va='center')

    # Box coordinates
    # Top: Research Institutes (Scientists)
    # Middle: Extension Agent
    # Bottom: Farmers (End Users)
    box_w = 4.8
    box_h = 1.0

    boxes = [
        {"x": 2.6, "y": 6.3, "title": "Research Institutes (Scientists)", "desc": "Develop innovations & solutions", "color": BLUE, "edge": DEEP["blue"]},
        {"x": 2.6, "y": 3.75, "title": "Extension Agents", "desc": "Facilitate communication & training", "color": LAV, "edge": DEEP["lav"]},
        {"x": 2.6, "y": 1.2, "title": "Farmers (End Users)", "desc": "Apply practices in fields & identify problems", "color": GREEN, "edge": DEEP["green"]}
    ]

    for b in boxes:
        rect = patches.FancyBboxPatch(
            (b["x"], b["y"]), box_w, box_h,
            boxstyle="round,pad=0.18,rounding_size=0.25",
            facecolor=b["color"], edgecolor=b["edge"], linewidth=2.5, zorder=2
        )
        ax.add_patch(rect)
        ax.text(b["x"] + box_w/2, b["y"] + 0.62, b["title"],
                fontsize=15, fontweight='bold', color=INK, ha='center', va='center', zorder=3)
        ax.text(b["x"] + box_w/2, b["y"] + 0.28, b["desc"],
                fontsize=13, color=INK, ha='center', va='center', style='italic', zorder=3)

    # Downward Flow (Right side): "New technologies and ideas"
    # Research -> Extension Agent
    ax.annotate(
        "", xy=(7.7, 4.85), xytext=(7.7, 6.25),
        arrowprops=dict(arrowstyle="-|>", mutation_scale=22, color=DEEP["orange"], lw=3.5)
    )
    # Extension Agent -> Farmers
    ax.annotate(
        "", xy=(7.7, 2.3), xytext=(7.7, 3.65),
        arrowprops=dict(arrowstyle="-|>", mutation_scale=22, color=DEEP["orange"], lw=3.5)
    )

    # Label for Downward Flow
    ax.text(8.2, 4.3, "New technologies\nand ideas\n(Dissemination)",
            fontsize=14, fontweight='bold', color=DEEP["orange"], ha='left', va='center',
            bbox=dict(boxstyle="round,pad=0.4", fc=CREAM, ec=DEEP["orange"], lw=1.5))

    # Upward Flow (Left side): "Farmers' problems and feedback"
    # Farmers -> Extension Agent
    ax.annotate(
        "", xy=(2.3, 3.65), xytext=(2.3, 2.3),
        arrowprops=dict(arrowstyle="-|>", mutation_scale=22, color=DEEP["blue"], lw=3.5)
    )
    # Extension Agent -> Research
    ax.annotate(
        "", xy=(2.3, 6.25), xytext=(2.3, 4.85),
        arrowprops=dict(arrowstyle="-|>", mutation_scale=22, color=DEEP["blue"], lw=3.5)
    )

    # Label for Upward Flow
    ax.text(1.8, 4.3, "Farmers' problems\nand feedback\n(Research Needs)",
            fontsize=14, fontweight='bold', color=DEEP["blue"], ha='right', va='center',
            bbox=dict(boxstyle="round,pad=0.4", fc=CREAM, ec=DEEP["blue"], lw=1.5))

    # Small decorative icons or markers next to labels
    # Mini-indicators
    ax.plot([7.7, 7.7], [3.65, 4.85], color=DEEP["orange"], lw=2, linestyle=":")
    ax.plot([2.3, 2.3], [3.65, 4.85], color=DEEP["blue"], lw=2, linestyle=":")

    save(fig, out)
