from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Overall Title / Main Header
    ax.text(6, 6.3, "Timeline of the Quranic Revelation", ha='center', va='center',
            fontsize=18, fontweight='bold', color=INK)
    ax.text(6, 5.75, "Total: 23 Years of Piecemeal Revelation", ha='center', va='center',
            fontsize=15, color=DEEP['orange'], fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', fc=CREAM, ec=DEEP['orange'], lw=1.5))

    # Left Icon: Crescent Moon
    # Crescent drawn at x=0.9, y=4.4
    moon_center_x, moon_center_y = 0.9, 4.45
    r = 0.4
    theta = np.linspace(-np.pi/2, np.pi/2, 50)
    # Outer arc
    outer_x = moon_center_x + r * np.cos(theta)
    outer_y = moon_center_y + r * np.sin(theta)
    # Inner arc (shifted slightly right and smaller radius)
    inner_x = (moon_center_x + 0.15) + (r * 0.85) * np.cos(theta[::-1])
    inner_y = moon_center_y + (r * 0.85) * np.sin(theta[::-1])
    poly_x = np.concatenate([outer_x, inner_x])
    poly_y = np.concatenate([outer_y, inner_y])
    ax.fill(poly_x, poly_y, color=DEEP['orange'], zorder=5)

    # Timeline layout
    # Start: x=1.6, Hijrah: x=7.2 (13 yrs), End: x=11.0 (10 yrs) -> total 9.4 units
    # Ratio: 13 / 23 = 56.5% -> 1.6 + 9.4 * (13/23) = 6.91
    x_start = 1.8
    x_split = 7.1
    x_end = 11.2
    y_bar = 3.6
    bar_h = 0.55

    # Makkan section bar (warm sand / cream / orange tones)
    sand_color = '#E8C59A'
    rect_makka = patches.FancyBboxPatch((x_start, y_bar - bar_h/2), x_split - x_start, bar_h,
                                        boxstyle="round,pad=0.04,rounding_size=0.15",
                                        facecolor=sand_color, edgecolor=DEEP['orange'], lw=2, zorder=3)
    ax.add_patch(rect_makka)

    # Madinan section bar (green)
    rect_madina = patches.FancyBboxPatch((x_split, y_bar - bar_h/2), x_end - x_split, bar_h,
                                         boxstyle="round,pad=0.04,rounding_size=0.15",
                                         facecolor=GREEN, edgecolor=DEEP['green'], lw=2, zorder=3)
    ax.add_patch(rect_madina)

    # Bar Labels
    ax.text((x_start + x_split)/2, y_bar, "Makkan Period (13 Years)",
            ha='center', va='center', fontsize=14, fontweight='bold', color=INK, zorder=4)
    ax.text((x_split + x_end)/2, y_bar, "Madinan Period (10 Years)",
            ha='center', va='center', fontsize=14, fontweight='bold', color=INK, zorder=4)

    # Key Milestone Endpoints (Labels with pointer stems)
    # 610 CE at x_start
    ax.plot([x_start, x_start], [y_bar + bar_h/2, 4.45], color=DEEP['orange'], lw=2, zorder=2)
    ax.plot(x_start, y_bar + bar_h/2, marker='o', markersize=7, color=DEEP['orange'], zorder=4)
    ax.text(x_start + 0.1, 4.8, "610 CE: First Revelation in Makkah (Age 40)",
            ha='left', va='center', fontsize=14, fontweight='bold', color=INK,
            bbox=dict(boxstyle='square,pad=0.3', fc='white', ec='none'))

    # 622 CE Hijrah marker
    ax.plot([x_split, x_split], [y_bar - bar_h/2 - 0.25, y_bar + bar_h/2 + 0.25],
            color=INK, lw=2, linestyle='--', zorder=4)
    ax.text(x_split, y_bar + bar_h/2 + 0.5, "622 CE: Hijrah\n(Migration to Madinah)",
            ha='center', va='bottom', fontsize=14, color=INK, fontweight='semibold',
            bbox=dict(boxstyle='round,pad=0.3', fc='white', ec=GREY, lw=1))

    # 632 CE at x_end
    ax.plot([x_end, x_end], [y_bar + bar_h/2, 4.45], color=DEEP['green'], lw=2, zorder=2)
    ax.plot(x_end, y_bar + bar_h/2, marker='o', markersize=7, color=DEEP['green'], zorder=4)
    ax.text(x_end, 4.8, "632 CE: Final Revelation in Madinah (Age 63)",
            ha='right', va='center', fontsize=14, fontweight='bold', color=INK,
            bbox=dict(boxstyle='square,pad=0.3', fc='white', ec='none'))

    # Helper function to draw a scroll icon unrolling gradually
    def draw_scroll(cx, cy, unroll_stage=1):
        """
        Draws a stylized scroll unrolling across stages 1 to 4.
        cx, cy: center coordinates
        unroll_stage: 1 (rolled), 2 (slightly open), 3 (half open), 4 (fully unrolled)
        """
        w = 0.35 + 0.2 * unroll_stage
        h = 0.38
        # parchment sheet
        sheet = patches.Rectangle((cx - w/2, cy - h/2), w, h,
                                  fc='#FFFDF0', ec=DEEP['orange'] if cx < x_split else DEEP['green'],
                                  lw=1.5, zorder=4)
        ax.add_patch(sheet)
        # horizontal text lines on parchment
        num_lines = unroll_stage + 1
        for i in range(num_lines):
            line_x = cx - w/2 + 0.08 + i * (w - 0.16) / max(1, num_lines - 1)
            ax.plot([line_x, line_x], [cy - h/2 + 0.08, cy + h/2 - 0.08],
                    color=GREY, lw=1.2, zorder=5)
        # left roll cylinder
        roll_l = patches.Ellipse((cx - w/2, cy), 0.1, h + 0.06,
                                 fc=CREAM, ec=DEEP['orange'] if cx < x_split else DEEP['green'], lw=1.5, zorder=6)
        ax.add_patch(roll_l)
        # right roll cylinder
        roll_r = patches.Ellipse((cx + w/2, cy), 0.1, h + 0.06,
                                 fc=CREAM, ec=DEEP['orange'] if cx < x_split else DEEP['green'], lw=1.5, zorder=6)
        ax.add_patch(roll_r)

    # Draw scrolls along the timeline representing gradual piecemeal unrolling
    scroll_positions = [
        (3.0, 2.5, 1),
        (5.2, 2.5, 2),
        (8.3, 2.5, 3),
        (10.2, 2.5, 4),
    ]
    for (sx, sy, stage) in scroll_positions:
        draw_scroll(sx, sy, stage)

    # Caption for the scroll icons
    ax.text(6.0, 2.35, "Gradual (piecemeal) revelation of verses over 23 years",
            ha='center', va='top', fontsize=14, fontstyle='italic', color=GREY)

    # Phase Description Boxes at the Bottom
    # Makkan Phase Focus
    makkan_box = patches.FancyBboxPatch((1.8, 0.6), 4.8, 1.25,
                                        boxstyle="round,pad=0.1,rounding_size=0.15",
                                        facecolor=CREAM, edgecolor=DEEP['orange'], lw=1.5)
    ax.add_patch(makkan_box)
    ax.text(4.2, 1.45, "Makkan phase: Focus on Faith",
            ha='center', va='center', fontsize=15, fontweight='bold', color=INK)
    ax.text(4.2, 0.95, "Tawhid (monotheism), morality, the Hereafter",
            ha='center', va='center', fontsize=14, color=INK)

    # Madinan Phase Focus
    madinan_box = patches.FancyBboxPatch((7.0, 0.6), 4.2, 1.25,
                                         boxstyle="round,pad=0.1,rounding_size=0.15",
                                         facecolor='#E8F5E9', edgecolor=DEEP['green'], lw=1.5)
    ax.add_patch(madinan_box)
    ax.text(9.1, 1.45, "Madinan phase: Focus on Laws",
            ha='center', va='center', fontsize=15, fontweight='bold', color=INK)
    ax.text(9.1, 0.95, "Legislation, community, statehood, rituals",
            ha='center', va='center', fontsize=14, color=INK)

    save(fig, out)
