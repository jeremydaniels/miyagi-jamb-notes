from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(15, 11)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 11)
    ax.axis("off")

    # Title
    ax.text(7.5, 10.5, "Negative Feedback Control of Blood Water Content by ADH",
            fontsize=17, fontweight="bold", ha="center", va="center", color=INK)

    # Box styles
    box_normal = dict(boxstyle="round,pad=0.6", fc=CREAM, ec=DEEP["green"], lw=2.5)
    box_blue = dict(boxstyle="round,pad=0.5", fc="#EDF4FA", ec=DEEP["blue"], lw=1.8)
    box_orange = dict(boxstyle="round,pad=0.5", fc="#FDF2E9", ec=DEEP["orange"], lw=1.8)

    # Top Central: Normal level
    ax.text(7.5, 9.4, "Blood water content normal",
            ha="center", va="center", fontsize=13, fontweight="bold", color=INK, bbox=box_normal)

    # --- LEFT SIDE (Water content rises / Excess water) ---
    ax.text(2.6, 8.1, "Water content rises\n(drinking a lot)",
            ha="center", va="center", fontsize=12, fontweight="bold", color=DEEP["blue"], bbox=box_blue)

    ax.text(2.6, 6.4, "Hypothalamus detects\nhigher water content",
            ha="center", va="center", fontsize=11.5, color=INK, bbox=box_blue)

    ax.text(2.6, 4.7, "Pituitary gland\nreleases less ADH",
            ha="center", va="center", fontsize=11.5, fontweight="bold", color=INK, bbox=box_blue)

    ax.text(2.6, 3.0, "Collecting ducts\nless permeable\n→ Less water reabsorbed",
            ha="center", va="center", fontsize=11.5, color=INK, bbox=box_blue)

    ax.text(2.6, 1.3, "Large volume of\ndilute urine excreted",
            ha="center", va="center", fontsize=12, fontweight="bold", color=DEEP["blue"], bbox=box_blue)

    # --- RIGHT SIDE (Water content falls / Water loss) ---
    ax.text(12.4, 8.1, "Water content falls\n(sweating, little drinking)",
            ha="center", va="center", fontsize=12, fontweight="bold", color=DEEP["orange"], bbox=box_orange)

    ax.text(12.4, 6.4, "Hypothalamus detects\nlower water content",
            ha="center", va="center", fontsize=11.5, color=INK, bbox=box_orange)

    ax.text(12.4, 4.7, "Pituitary gland\nreleases more ADH",
            ha="center", va="center", fontsize=11.5, fontweight="bold", color=INK, bbox=box_orange)

    ax.text(12.4, 3.0, "Collecting ducts\nmore permeable\n→ More water reabsorbed",
            ha="center", va="center", fontsize=11.5, color=INK, bbox=box_orange)

    ax.text(12.4, 1.3, "Small volume of\nconcentrated urine excreted",
            ha="center", va="center", fontsize=12, fontweight="bold", color=DEEP["orange"], bbox=box_orange)

    # --- FLOW ARROWS (LEFT - BLUE) ---
    c_blue = DEEP["blue"]
    arr_b = dict(arrowstyle="-|>,head_length=0.7,head_width=0.4", color=c_blue, lw=2.5)
    arr_b_conn = dict(arrowstyle="-|>,head_length=0.7,head_width=0.4", color=c_blue, lw=2.5, connectionstyle="angle,angleA=0,angleB=90,rad=5")

    # From normal to left stimulus
    ax.annotate("", xy=(2.6, 8.6), xytext=(5.6, 9.4), arrowprops=arr_b_conn)
    # Down the left branch
    ax.annotate("", xy=(2.6, 6.9), xytext=(2.6, 7.5), arrowprops=arr_b)
    ax.annotate("", xy=(2.6, 5.2), xytext=(2.6, 5.8), arrowprops=arr_b)
    ax.annotate("", xy=(2.6, 3.65), xytext=(2.6, 4.15), arrowprops=arr_b)
    ax.annotate("", xy=(2.6, 1.85), xytext=(2.6, 2.35), arrowprops=arr_b)
    # Loop back from left result to normal
    ax.annotate("", xy=(6.0, 9.4), xytext=(1.0, 1.3),
                arrowprops=dict(arrowstyle="-|>,head_length=0.7,head_width=0.4",
                                color=c_blue, lw=2.5,
                                connectionstyle="angle,angleA=90,angleB=180,rad=20"))
    ax.text(0.7, 5.5, "Negative feedback:\nwater content falls\nback to normal",
            ha="center", va="center", fontsize=11, color=c_blue, fontweight="bold",
            bbox=dict(fc="white", ec="none", pad=2))

    # --- FLOW ARROWS (RIGHT - ORANGE) ---
    c_org = DEEP["orange"]
    arr_o = dict(arrowstyle="-|>,head_length=0.7,head_width=0.4", color=c_org, lw=2.5)
    arr_o_conn = dict(arrowstyle="-|>,head_length=0.7,head_width=0.4", color=c_org, lw=2.5, connectionstyle="angle,angleA=180,angleB=90,rad=5")

    # From normal to right stimulus
    ax.annotate("", xy=(12.4, 8.6), xytext=(9.4, 9.4), arrowprops=arr_o_conn)
    # Down the right branch
    ax.annotate("", xy=(12.4, 6.9), xytext=(12.4, 7.5), arrowprops=arr_o)
    ax.annotate("", xy=(12.4, 5.2), xytext=(12.4, 5.8), arrowprops=arr_o)
    ax.annotate("", xy=(12.4, 3.65), xytext=(12.4, 4.15), arrowprops=arr_o)
    ax.annotate("", xy=(12.4, 1.85), xytext=(12.4, 2.35), arrowprops=arr_o)
    # Loop back from right result to normal
    ax.annotate("", xy=(9.0, 9.4), xytext=(14.0, 1.3),
                arrowprops=dict(arrowstyle="-|>,head_length=0.7,head_width=0.4",
                                color=c_org, lw=2.5,
                                connectionstyle="angle,angleA=90,angleB=0,rad=20"))
    ax.text(14.3, 5.5, "Negative feedback:\nwater content rises\nback to normal",
            ha="center", va="center", fontsize=11, color=c_org, fontweight="bold",
            bbox=dict(fc="white", ec="none", pad=2))

    # --- CENTRAL DIAGRAM / ICONS ---
    # Central box for icons
    center_bg = patches.FancyBboxPatch((5.4, 1.3), 4.2, 7.2,
                                       boxstyle="round,pad=0.2",
                                       fc="#FAFAFA", ec=GREY, lw=1.2,
                                       linestyle="--", zorder=0)
    ax.add_patch(center_bg)

    # 1. BRAIN ICON (Hypothalamus & Pituitary)
    bx, by = 7.5, 6.7
    brain = patches.Ellipse((bx, by), 1.9, 1.4, fc=PINK, ec=INK, lw=1.5, zorder=2)
    ax.add_patch(brain)
    stem = patches.Polygon([[bx-0.2, by-0.5], [bx+0.1, by-0.5], [bx-0.05, by-1.0], [bx-0.3, by-0.9]],
                           fc="#E5B2B2", ec=INK, lw=1.3, zorder=1)
    ax.add_patch(stem)
    # Hypothalamus
    hypo = patches.Circle((bx - 0.1, by - 0.2), 0.14, fc=DEEP["orange"], ec=INK, lw=1.2, zorder=3)
    ax.add_patch(hypo)
    # Pituitary gland
    pit = patches.Circle((bx - 0.18, by - 0.52), 0.16, fc=DEEP["pink"], ec=INK, lw=1.2, zorder=3)
    ax.add_patch(pit)

    ax.text(bx, by + 0.88, "Brain & Endocrine System", ha="center", fontsize=11.5, fontweight="bold", color=INK)
    ax.annotate("hypothalamus", xy=(bx - 0.1, by - 0.2), xytext=(bx - 1.85, by + 0.25),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2), fontsize=11, color=INK,
                bbox=dict(fc="white", ec="none", pad=1))
    ax.annotate("pituitary gland\n(releases ADH)", xy=(bx - 0.18, by - 0.52), xytext=(bx + 0.7, by - 0.65),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2), fontsize=11, color=INK,
                bbox=dict(fc="white", ec="none", pad=1))

    # 2. KIDNEY & COLLECTING DUCT ICON
    kx, ky = 7.5, 4.0
    theta = np.linspace(0, 2*np.pi, 100)
    r = 0.65 * (1 + 0.25 * np.cos(theta + np.pi/2))
    kx_pts = kx + r * np.cos(theta) * 0.95
    ky_pts = ky + r * np.sin(theta) * 1.3
    kidney = patches.Polygon(np.column_stack([kx_pts, ky_pts]), fc="#D98880", ec=INK, lw=1.5, zorder=2)
    ax.add_patch(kidney)

    # Indentation (hilum)
    hilum = patches.Ellipse((kx - 0.35, ky), 0.28, 0.55, fc="#FAFAFA", ec="none", zorder=3)
    ax.add_patch(hilum)
    hilum_edge = patches.Arc((kx - 0.25, ky), 0.25, 0.55, angle=0, theta1=85, theta2=275,
                             color=INK, lw=1.3, zorder=4)
    ax.add_patch(hilum_edge)

    # Collecting duct line inside/extending
    cd_x = [kx + 0.15, kx + 0.15, kx - 0.2]
    cd_y = [ky + 0.5, ky - 0.1, ky - 0.5]
    ax.plot(cd_x, cd_y, color=DEEP["blue"], lw=2.5, zorder=5, linestyle="-")

    ax.text(kx, ky + 1.05, "Kidney", ha="center", fontsize=11.5, fontweight="bold", color=INK)
    ax.annotate("collecting duct", xy=(kx + 0.15, ky + 0.1), xytext=(kx - 2.1, ky - 0.1),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2), fontsize=11, color=INK,
                bbox=dict(fc="white", ec="none", pad=1))

    # 3. URINE BEAKERS
    # Left Beaker: Dilute urine
    b1_x, b1_y = 6.4, 2.0
    ax.plot([b1_x - 0.35, b1_x - 0.35, b1_x + 0.35, b1_x + 0.35],
            [b1_y + 0.9, b1_y, b1_y, b1_y + 0.9], color=INK, lw=1.5, zorder=3)
    urine_dilute = patches.Rectangle((b1_x - 0.32, b1_y + 0.02), 0.64, 0.7, fc="#FFF9C4", ec="none", zorder=2)
    ax.add_patch(urine_dilute)
    ax.plot([b1_x - 0.32, b1_x + 0.32], [b1_y + 0.72, b1_y + 0.72], color="#F9E79F", lw=1.5, zorder=3)
    ax.text(b1_x, b1_y - 0.35, "dilute urine\n(large, pale)", ha="center", fontsize=11, color=INK)

    # Right Beaker: Concentrated urine
    b2_x, b2_y = 8.6, 2.0
    ax.plot([b2_x - 0.35, b2_x - 0.35, b2_x + 0.35, b2_x + 0.35],
            [b2_y + 0.9, b2_y, b2_y, b2_y + 0.9], color=INK, lw=1.5, zorder=3)
    urine_conc = patches.Rectangle((b2_x - 0.32, b2_y + 0.02), 0.64, 0.25, fc="#F39C12", ec="none", zorder=2)
    ax.add_patch(urine_conc)
    ax.plot([b2_x - 0.32, b2_x + 0.32], [b2_y + 0.27, b2_y + 0.27], color="#B9770E", lw=1.5, zorder=3)
    ax.text(b2_x, b2_y - 0.35, "concentrated urine\n(small, dark)", ha="center", fontsize=11, color=INK)

    # Key / legend at bottom
    ax.text(7.5, 0.35, "Blue arrows: too much water response   |   Orange arrows: too little water response",
            ha="center", va="center", fontsize=11.5, color=INK, fontstyle="italic")

    save(fig, out)
