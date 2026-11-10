from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Main window outline
    win = patches.FancyBboxPatch((0.5, 0.4), 11.0, 7.2, boxstyle="round,pad=0,rounding_size=0.15",
                                fc="white", ec=GREY, lw=2)
    ax.add_patch(win)

    # Title Bar
    title_bar = patches.Rectangle((0.5, 7.1), 11.0, 0.5, fc=CREAM, ec=GREY, lw=1.5)
    ax.add_patch(title_bar)
    ax.text(0.8, 7.35, "Presentation1 - PowerPoint", fontsize=14, color=INK, va="center", fontweight="bold")
    # Window controls (min, max, close)
    for i, col in enumerate([GREEN, ORANGE, PINK]):
        ax.add_patch(patches.Circle((11.0 - i * 0.3, 7.35), 0.1, fc=col, ec=INK, lw=1))

    # Ribbon container
    ribbon = patches.Rectangle((0.5, 5.7), 11.0, 1.4, fc="#F8F9FA", ec=GREY, lw=1.5)
    ax.add_patch(ribbon)

    # Ribbon tabs
    tabs = ["File", "Home", "Insert", "Design", "Transitions", "Animations", "Slide Show", "View"]
    for i, t in enumerate(tabs):
        tab_x = 0.8 + i * 1.15
        is_active = (t == "Animations")
        if is_active:
            tab_bg = patches.Rectangle((tab_x - 0.1, 6.7), 1.05, 0.4, fc="white", ec=GREY, lw=1.2)
            ax.add_patch(tab_bg)
            ax.text(tab_x + 0.42, 6.9, t, fontsize=14, color=DEEP["blue"], weight="bold", ha="center", va="center")
        else:
            ax.text(tab_x + 0.42, 6.9, t, fontsize=14, color=INK, ha="center", va="center")

    # Ribbon items inside Animations tab
    # Animation icons (small stars)
    for j in range(3):
        ax.add_patch(patches.Rectangle((1.0 + j * 0.9, 5.85), 0.75, 0.75, fc=CREAM, ec=GREY, lw=1))
        # Draw a small star
        star_x, star_y = 1.37 + j * 0.9, 6.22
        ax.plot([star_x], [star_y], marker="*", markersize=14, color=DEEP["green"])

    # Animation Painter Button (highlighted)
    painter_box = patches.FancyBboxPatch((4.2, 5.8), 2.2, 0.85, boxstyle="round,pad=0.05",
                                         fc=LAV, ec=DEEP["lav"], lw=2)
    ax.add_patch(painter_box)

    # Star + paintbrush icon inside the button
    ax.plot([4.55], [6.25], marker="*", markersize=16, color=DEEP["orange"])
    # Paintbrush handle and head
    ax.plot([4.75, 4.95], [6.05, 6.35], color=DEEP["orange"], lw=3.5, solid_capstyle='round')
    ax.plot([4.68, 4.75], [5.95, 6.05], color=INK, lw=4, solid_capstyle='round')
    ax.text(5.05, 6.22, "Animation\nPainter", fontsize=14, color=INK, va="center", weight="bold")

    # Cursor hovering over Animation Painter
    cursor_x, cursor_y = 5.6, 5.85
    cursor = patches.Polygon([
        [cursor_x, cursor_y],
        [cursor_x, cursor_y - 0.45],
        [cursor_x + 0.12, cursor_y - 0.35],
        [cursor_x + 0.25, cursor_y - 0.55],
        [cursor_x + 0.35, cursor_y - 0.5],
        [cursor_x + 0.22, cursor_y - 0.3],
        [cursor_x + 0.38, cursor_y - 0.3]
    ], closed=True, fc="white", ec=INK, lw=1.8, zorder=10)
    ax.add_patch(cursor)

    # Left slide pane
    slide_pane = patches.Rectangle((0.5, 0.4), 2.5, 5.3, fc="#FAFAFA", ec=GREY, lw=1.5)
    ax.add_patch(slide_pane)

    # Section Header in Slide Pane
    sec_rect = patches.Rectangle((0.6, 5.25), 2.3, 0.35, fc=CREAM, ec=GREY, lw=1)
    ax.add_patch(sec_rect)
    # Triangle collapse icon
    ax.plot([0.7, 0.8, 0.7], [5.5, 5.42, 5.35], color=INK, lw=1.5)
    ax.text(0.9, 5.42, "Section 1", fontsize=14, color=INK, va="center", weight="bold")

    # Thumbnail 1 (Active)
    thumb1 = patches.Rectangle((0.8, 3.8), 1.9, 1.3, fc="white", ec=DEEP["blue"], lw=2.5)
    ax.add_patch(thumb1)
    ax.text(0.68, 4.9, "1", fontsize=14, color=INK, ha="right", va="center")
    # Mini elements inside thumbnail 1
    ax.add_patch(patches.Rectangle((1.0, 4.5), 1.5, 0.4, fc=CREAM, ec="none"))
    ax.add_patch(patches.Rectangle((1.3, 4.0), 0.9, 0.4, fc=BLUE, ec="none"))

    # Section 2 Header
    sec_rect2 = patches.Rectangle((0.6, 3.3), 2.3, 0.35, fc=CREAM, ec=GREY, lw=1)
    ax.add_patch(sec_rect2)
    ax.plot([0.7, 0.8, 0.7], [3.55, 3.47, 3.4], color=INK, lw=1.5)
    ax.text(0.9, 3.47, "Section 2", fontsize=14, color=INK, va="center", weight="bold")

    # Thumbnail 2
    thumb2 = patches.Rectangle((0.8, 1.85), 1.9, 1.3, fc="white", ec=GREY, lw=1.5)
    ax.add_patch(thumb2)
    ax.text(0.68, 2.95, "2", fontsize=14, color=INK, ha="right", va="center")
    ax.add_patch(patches.Rectangle((1.0, 2.65), 1.5, 0.3, fc=CREAM, ec="none"))
    ax.add_patch(patches.Rectangle((1.1, 2.05), 1.3, 0.45, fc=PINK, ec="none"))

    # Main slide workspace area
    workspace = patches.Rectangle((3.0, 0.4), 8.5, 5.3, fc="#EDEFEF", ec="none")
    ax.add_patch(workspace)

    # Main Slide canvas
    slide_main = patches.Rectangle((3.6, 0.8), 7.3, 4.5, fc="white", ec=GREY, lw=2)
    ax.add_patch(slide_main)

    # Main Slide Title placeholder
    ax.add_patch(patches.Rectangle((4.2, 4.4), 6.1, 0.6, fc=CREAM, ec=GREY, lw=1, ls="--"))
    ax.text(7.25, 4.7, "Quarterly Report", fontsize=16, color=INK, ha="center", va="center", weight="bold")

    # Picture 1 (Reference object)
    pic1 = patches.Rectangle((4.3, 1.8), 2.3, 1.8, fc=BLUE, ec=DEEP["blue"], lw=1.5)
    ax.add_patch(pic1)
    ax.text(5.45, 2.7, "Figure A", fontsize=14, color=DEEP["blue"], ha="center", va="center", weight="bold")

    # Picture 2 (Aligining picture)
    pic2 = patches.Rectangle((7.8, 1.8), 2.3, 1.8, fc=PINK, ec=DEEP["pink"], lw=1.5)
    ax.add_patch(pic2)
    ax.text(8.95, 2.7, "Figure B", fontsize=14, color=DEEP["pink"], ha="center", va="center", weight="bold")

    # Smart Guides (dashed alignment lines)
    # Top alignment line
    ax.plot([4.0, 10.4], [3.6, 3.6], color=DEEP["orange"], lw=2.2, ls="--")
    # Bottom alignment line
    ax.plot([4.0, 10.4], [1.8, 1.8], color=DEEP["orange"], lw=2.2, ls="--")
    # Vertical center guide
    ax.plot([8.95, 8.95], [1.3, 4.1], color=DEEP["orange"], lw=2.2, ls="--")

    # LABELS with callout arrows / text boxes (clean, legible, phone-friendly)

    # 1. Automatic Ribbons Toolbars
    ax.annotate("Automatic Ribbons Toolbars",
                xy=(3.5, 6.7), xytext=(3.5, 7.55),
                fontsize=15, weight="bold", color=INK, ha="center",
                bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.3", lw=1.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2))

    # 2. Sections
    ax.annotate("Sections",
                xy=(1.75, 5.42), xytext=(1.75, 6.15),
                fontsize=15, weight="bold", color=INK, ha="center",
                bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.3", lw=1.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2))

    # 3. Animation Painter
    ax.annotate("Animation Painter",
                xy=(5.7, 5.7), xytext=(7.4, 6.3),
                fontsize=15, weight="bold", color=INK, ha="left",
                bbox=dict(fc="white", ec=DEEP["lav"], boxstyle="round,pad=0.3", lw=1.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["lav"], lw=2))

    # 4. Smart Guides
    ax.annotate("Smart Guides",
                xy=(7.05, 3.6), xytext=(7.05, 4.1),
                fontsize=15, weight="bold", color=INK, ha="center",
                bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.3", lw=1.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2))

    save(fig, out)
