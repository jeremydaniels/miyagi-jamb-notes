from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(7, 6.8, "IUCN Red List Categories", ha="center", va="center", fontsize=16, weight="bold", color=INK)

    # Main 7 categories
    # LC, NT, VU, EN, CR, EW, EX
    main_cats = [
        {"code": "LC", "name": "Least Concern", "color": "#60C659", "tc": "white"},
        {"code": "NT", "name": "Near Threatened", "color": "#CCE266", "tc": INK},
        {"code": "VU", "name": "Vulnerable", "color": "#F9E858", "tc": INK},
        {"code": "EN", "name": "Endangered", "color": "#FC7F3F", "tc": "white"},
        {"code": "CR", "name": "Critically Endangered", "color": "#D81E05", "tc": "white"},
        {"code": "EW", "name": "Extinct in the Wild", "color": "#542344", "tc": "white"},
        {"code": "EX", "name": "Extinct", "color": "#000000", "tc": "white"}
    ]

    box_w = 1.15
    box_h = 1.15
    gap = 0.22
    start_x = 0.8
    box_y = 3.6

    x_centers = []

    for i, cat in enumerate(main_cats):
        bx = start_x + i * (box_w + gap)
        by = box_y
        cx = bx + box_w / 2
        cy = by + box_h / 2
        x_centers.append(cx)

        # Draw box
        rect = patches.FancyBboxPatch((bx, by), box_w, box_h,
                                     boxstyle="round,pad=0.04,rounding_size=0.15",
                                     fc=cat["color"], ec=INK, lw=1.2)
        ax.add_patch(rect)

        # Code inside box
        ax.text(cx, cy, cat["code"], ha="center", va="center", fontsize=14, weight="bold", color=cat["tc"])

        # Label above box (slanted or 2 lines)
        words = cat["name"].split()
        if len(words) == 1:
            lbl = words[0]
        elif len(words) == 2:
            lbl = f"{words[0]}\n{words[1]}"
        else: # Critically Endangered / Extinct in the Wild
            lbl = f"{words[0]}\n{' '.join(words[1:])}"

        ax.text(cx, by + box_h + 0.25, lbl, ha="center", va="bottom", fontsize=11, weight="bold", color=INK, multialignment="center")

    # Threatened bracket over VU (index 2), EN (index 3), CR (index 4)
    # Positions of these boxes:
    vu_x = x_centers[2] - box_w / 2 - 0.05
    cr_x = x_centers[4] + box_w / 2 + 0.05
    mid_threat = (vu_x + cr_x) / 2
    bracket_y = box_y + box_h + 1.25

    # Draw bracket line
    bw = 0.15
    ax.plot([vu_x, vu_x, mid_threat, mid_threat], [bracket_y - 0.1, bracket_y, bracket_y, bracket_y + bw], color=INK, lw=1.8)
    ax.plot([cr_x, cr_x, mid_threat, mid_threat], [bracket_y - 0.1, bracket_y, bracket_y, bracket_y + bw], color=INK, lw=1.8)
    ax.text(mid_threat, bracket_y + bw + 0.12, "Threatened", ha="center", va="bottom", fontsize=13, weight="bold", color=INK)

    # Separate grey boxes for Data Deficient (DD) and Not Evaluated (NE)
    side_cats = [
        {"code": "DD", "name": "Data Deficient", "color": "#D0D3D4"},
        {"code": "NE", "name": "Not Evaluated", "color": "#FFFFFF"}
    ]
    side_start_x = start_x + 7 * (box_w + gap) + 0.5

    # Divider line
    div_x = side_start_x - 0.35
    ax.plot([div_x, div_x], [box_y - 0.5, box_y + box_h + 1.2], color=GREY, lw=1.5, linestyle="--")

    for i, cat in enumerate(side_cats):
        bx = side_start_x + i * (box_w + gap)
        by = box_y
        cx = bx + box_w / 2
        cy = by + box_h / 2

        rect = patches.FancyBboxPatch((bx, by), box_w, box_h,
                                     boxstyle="round,pad=0.04,rounding_size=0.15",
                                     fc=cat["color"], ec=INK, lw=1.2)
        ax.add_patch(rect)
        ax.text(cx, cy, cat["code"], ha="center", va="center", fontsize=14, weight="bold", color=INK)

        words = cat["name"].split()
        lbl = f"{words[0]}\n{words[1]}"
        ax.text(cx, by + box_h + 0.25, lbl, ha="center", va="bottom", fontsize=11, weight="bold", color=INK, multialignment="center")

    # Arrow under categories indicating extinction risk
    arr_y = box_y - 0.4
    ax.annotate("", xy=(x_centers[6] + box_w/2, arr_y), xytext=(x_centers[0] - box_w/2, arr_y),
                arrowprops=dict(arrowstyle="->", lw=2, color=INK))
    ax.text((x_centers[0] + x_centers[6]) / 2, arr_y - 0.25, "Increasing risk of extinction",
            ha="center", va="top", fontsize=11, color=INK, style="italic")

    # Helper to draw simple stylized animal silhouettes
    # Gorilla icon under Critically Endangered (x_centers[4])
    def draw_gorilla(x, y, scale=0.45):
        # Body
        torso = patches.Ellipse((x + 0.1*scale, y + 0.1*scale), 1.6*scale, 1.2*scale, angle=25, fc=INK, ec="none")
        # Shoulder / back crest
        crest = patches.Ellipse((x - 0.3*scale, y + 0.5*scale), 1.0*scale, 0.9*scale, angle=40, fc=INK, ec="none")
        # Head
        head = patches.Circle((x - 0.8*scale, y + 0.65*scale), 0.42*scale, fc=INK, ec="none")
        # Brow/jaw
        jaw = patches.Circle((x - 0.98*scale, y + 0.52*scale), 0.32*scale, fc=INK, ec="none")
        # Forearm / knuckle walk
        arm1 = patches.Polygon([[x - 0.5*scale, y + 0.3*scale], [x - 0.8*scale, y - 0.6*scale], [x - 0.6*scale, y - 0.6*scale], [x - 0.2*scale, y + 0.1*scale]], fc=INK, closed=True)
        # Hind leg
        leg1 = patches.Polygon([[x + 0.4*scale, y], [x + 0.7*scale, y - 0.6*scale], [x + 0.9*scale, y - 0.6*scale], [x + 0.7*scale, y + 0.3*scale]], fc=INK, closed=True)
        for p in [torso, crest, head, jaw, arm1, leg1]:
            ax.add_patch(p)

    # Drill icon under Endangered (x_centers[3])
    def draw_drill(x, y, scale=0.42):
        # Body
        body = patches.Ellipse((x, y + 0.1*scale), 1.5*scale, 0.9*scale, angle=10, fc=INK, ec="none")
        # Head
        head = patches.Circle((x - 0.75*scale, y + 0.45*scale), 0.35*scale, fc=INK, ec="none")
        # Prominent muzzle
        snout = patches.Polygon([[x - 0.7*scale, y + 0.55*scale], [x - 1.15*scale, y + 0.3*scale], [x - 0.8*scale, y + 0.2*scale]], fc=INK, closed=True)
        # Foreleg
        arm = patches.Polygon([[x - 0.4*scale, y + 0.1*scale], [x - 0.6*scale, y - 0.6*scale], [x - 0.45*scale, y - 0.6*scale], [x - 0.2*scale, y]], fc=INK, closed=True)
        # Hindleg
        leg = patches.Polygon([[x + 0.3*scale, y + 0.1*scale], [x + 0.5*scale, y - 0.6*scale], [x + 0.65*scale, y - 0.6*scale], [x + 0.55*scale, y + 0.2*scale]], fc=INK, closed=True)
        # Short stumpy tail
        tail = patches.Polygon([[x + 0.65*scale, y + 0.3*scale], [x + 0.95*scale, y + 0.6*scale], [x + 0.8*scale, y + 0.2*scale]], fc=INK, closed=True)
        for p in [body, head, snout, arm, leg, tail]:
            ax.add_patch(p)

    # Draw animals and their connecting indicators
    # Endangered: Drill
    en_cx = x_centers[3]
    ax.plot([en_cx, en_cx], [arr_y - 0.45, 1.85], color=GREY, lw=1.2, linestyle=":")
    draw_drill(en_cx, 1.35, scale=0.5)
    ax.text(en_cx, 0.65, "Drill", ha="center", va="top", fontsize=12, weight="bold", color=INK)

    # Critically Endangered: Cross River gorilla
    cr_cx = x_centers[4]
    ax.plot([cr_cx, cr_cx], [arr_y - 0.45, 1.85], color=GREY, lw=1.2, linestyle=":")
    draw_gorilla(cr_cx, 1.35, scale=0.55)
    ax.text(cr_cx, 0.65, "Cross River gorilla", ha="center", va="top", fontsize=12, weight="bold", color=INK)

    save(fig, out)
