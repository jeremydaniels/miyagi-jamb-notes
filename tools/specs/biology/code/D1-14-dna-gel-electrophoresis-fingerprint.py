from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Gel background rectangle
    gel_left = 2.6
    gel_right = 7.8
    gel_bottom = 0.9
    gel_top = 6.4
    gel_width = gel_right - gel_left
    gel_height = gel_top - gel_bottom

    gel = patches.Rectangle(
        (gel_left, gel_bottom), gel_width, gel_height,
        facecolor="#ECEFF1", edgecolor=GREY, linewidth=1.5, zorder=1
    )
    ax.add_patch(gel)

    # Lane positions (x-coordinates)
    lane_xs = [3.2, 4.2, 5.2, 6.2, 7.2]
    lane_titles = ["Crime scene", "Suspect 1", "Suspect 2", "Suspect 3", "Victim"]

    # Wells at the top of each lane
    well_width = 0.52
    well_height = 0.18
    well_y = 6.05

    for x in lane_xs:
        well = patches.Rectangle(
            (x - well_width / 2, well_y), well_width, well_height,
            facecolor="#CFD8DC", edgecolor=INK, linewidth=1.2, zorder=2
        )
        ax.add_patch(well)

    # Band patterns (y positions, within gel area)
    # Crime scene (Lane 1) and Suspect 2 (Lane 3) must match exactly
    pattern_match = [5.4, 4.8, 4.1, 3.3, 2.7, 1.9, 1.3]
    pattern_s1 =    [5.6, 5.0, 4.3, 3.6, 2.9, 2.3, 1.5]
    pattern_s3 =    [5.2, 4.5, 3.9, 3.1, 2.5, 1.8, 1.1]
    pattern_vic =   [5.5, 4.7, 4.2, 3.5, 2.8, 2.1, 1.4]

    patterns = [pattern_match, pattern_s1, pattern_match, pattern_s3, pattern_vic]

    band_w = 0.48
    band_h = 0.07

    for lx, pat in zip(lane_xs, patterns):
        for by in pat:
            band = patches.Rectangle(
                (lx - band_w / 2, by - band_h / 2), band_w, band_h,
                facecolor=INK, edgecolor="none", zorder=3
            )
            ax.add_patch(band)

    # Lane column labels above the gel
    for x, title in zip(lane_xs, lane_titles):
        ax.text(
            x, gel_top + 0.35, title,
            ha="center", va="bottom", fontsize=11.5, weight="bold", color=INK,
            rotation=25
        )

    # Electrodes (+ and -) and Direction of DNA movement
    # Negative electrode (top)
    top_elec_y = well_y + well_height / 2
    ax.text(gel_right + 0.35, top_elec_y, "–", fontsize=18, weight="bold", ha="center", va="center", color=INK)
    ax.text(gel_right + 0.7, top_elec_y, "negative electrode", fontsize=11, ha="left", va="center", color=INK)

    # Positive electrode (bottom)
    bot_elec_y = gel_bottom + 0.2
    ax.text(gel_right + 0.35, bot_elec_y, "+", fontsize=18, weight="bold", ha="center", va="center", color=INK)
    ax.text(gel_right + 0.7, bot_elec_y, "positive electrode", fontsize=11, ha="left", va="center", color=INK)

    # Arrow indicating direction of DNA movement (middle right)
    arrow_x = gel_right + 0.35
    arrow_top = top_elec_y - 0.4
    arrow_bottom = bot_elec_y + 0.4
    ax.annotate(
        "", xy=(arrow_x, arrow_bottom), xytext=(arrow_x, arrow_top),
        arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.5, mutation_scale=18)
    )
    ax.text(
        arrow_x + 0.3, (arrow_top + arrow_bottom) / 2, "direction of DNA movement",
        fontsize=11.5, color=DEEP["blue"], weight="bold", rotation=-90,
        ha="left", va="center"
    )

    # Size label moved further right / vertically separated so it doesn't overlap electrode labels
    ax.annotate(
        "small fragments\ntravel further",
        xy=(gel_right, 1.3), xytext=(gel_right + 2.5, 2.2),
        fontsize=11.5, color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
        ha="center", va="center",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35")
    )

    # Left annotations: "wells" and "bands (DNA fragments)"
    ax.annotate(
        "wells",
        xy=(lane_xs[0] - well_width / 2, top_elec_y),
        xytext=(0.8, top_elec_y),
        fontsize=12, color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
        ha="left", va="center",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3")
    )

    ax.annotate(
        "bands (DNA fragments)",
        xy=(lane_xs[0] - band_w / 2, 4.8),
        xytext=(0.4, 4.8),
        fontsize=11.5, color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
        ha="left", va="center",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3")
    )

    # Matching pattern indicator linking Lane 1 and Lane 3
    brace_y = 0.42
    ax.plot([lane_xs[0], lane_xs[0], lane_xs[2], lane_xs[2]],
            [gel_bottom - 0.08, brace_y, brace_y, gel_bottom - 0.08],
            color=DEEP["pink"], lw=1.8, linestyle="--")
    ax.text(
        (lane_xs[0] + lane_xs[2]) / 2, brace_y - 0.05, "matching pattern",
        ha="center", va="top", fontsize=11.5, weight="bold", color=DEEP["pink"],
        bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.25", lw=1.2)
    )

    save(fig, out)
