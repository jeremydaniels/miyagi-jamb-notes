from style import *
import matplotlib.pyplot as plt
import numpy as np

def draw(out):
    # Canvas setup
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(6.0, 6.8, "Linkage Effects in the Oil Sector", 
            fontsize=18, fontweight="bold", ha="center", va="center", color=INK)

    # Box properties
    # Center box: Crude Oil Extraction
    center_bbox = dict(boxstyle="round,pad=0.8", facecolor=CREAM, edgecolor=DEEP["orange"], lw=2.5)
    ax.text(6.0, 4.4, "Crude Oil\nExtraction", 
            fontsize=16, fontweight="bold", ha="center", va="center", color=INK, bbox=center_bbox)

    # Backward Linkages box (left)
    backward_text = "Backward Linkages:\nProduction of drilling pipes,\nengineering services, boats"
    backward_bbox = dict(boxstyle="round,pad=0.7", facecolor=BLUE, edgecolor=DEEP["blue"], lw=2)
    ax.text(2.1, 4.4, backward_text, 
            fontsize=14, ha="center", va="center", color=INK, bbox=backward_bbox)

    # Forward Linkages box (right)
    forward_text = "Forward Linkages:\nRefineries,\nPetrochemicals, Plastics"
    forward_bbox = dict(boxstyle="round,pad=0.7", facecolor=GREEN, edgecolor=DEEP["green"], lw=2)
    ax.text(9.9, 4.4, forward_text, 
            fontsize=14, ha="center", va="center", color=INK, bbox=forward_bbox)

    # Consumption Linkages box (bottom)
    consumption_text = "Consumption Linkages:\nWorkers buy food, housing, and clothes"
    consumption_bbox = dict(boxstyle="round,pad=0.7", facecolor=LAV, edgecolor=DEEP["lav"], lw=2)
    ax.text(6.0, 1.4, consumption_text, 
            fontsize=14, ha="center", va="center", color=INK, bbox=consumption_bbox)

    # Arrows
    arrow_props = dict(arrowstyle="-|>", mutation_scale=22, lw=2.5, color=INK)

    # Center to Backward (pointing backward/left)
    ax.annotate("", xy=(3.8, 4.4), xytext=(4.75, 4.4), arrowprops=arrow_props)

    # Center to Forward (pointing forward/right)
    ax.annotate("", xy=(8.2, 4.4), xytext=(7.25, 4.4), arrowprops=arrow_props)

    # Center to Consumption (pointing downward)
    ax.annotate("", xy=(6.0, 2.2), xytext=(6.0, 3.65), arrowprops=arrow_props)

    save(fig, out)
