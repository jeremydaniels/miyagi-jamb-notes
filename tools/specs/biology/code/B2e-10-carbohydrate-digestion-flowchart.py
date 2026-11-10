from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(15, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Title
    ax.text(7.5, 9.5, "Carbohydrate Digestion Along the Alimentary Canal", 
            ha="center", va="center", fontsize=16, weight="bold", color=INK)

    # -------------------------------------------------------------
    # Left side: Simple Outline Drawing of the Alimentary Canal
    # -------------------------------------------------------------
    y = np.linspace(8.8, 1.2, 800)
    x = np.ones_like(y) * 2.5
    w = np.ones_like(y) * 0.4

    # Stomach section
    stomach_mask = (y <= 7.2) & (y > 5.5)
    ts = (7.2 - y[stomach_mask]) / 1.7
    x[stomach_mask] = 2.5 + 0.6 * np.sin(np.pi * ts)
    w[stomach_mask] = 0.4 + 0.9 * np.sin(np.pi * ts)

    # Duodenum section
    duo_mask = (y <= 5.5) & (y > 4.2)
    td = (5.5 - y[duo_mask]) / 1.3
    x[duo_mask] = 2.5 - 0.4 * np.sin(np.pi * td)
    w[duo_mask] = 0.4

    # Ileum section (coiled)
    ileum_mask = (y <= 4.2) & (y > 1.8)
    ti = (4.2 - y[ileum_mask]) / 2.4
    x[ileum_mask] = 2.5 + 0.4 * np.sin(7 * np.pi * ti)
    w[ileum_mask] = 0.35

    # Rectum/End section
    rectum_mask = y <= 1.8
    tr = (1.8 - y[rectum_mask]) / 0.6
    x[rectum_mask] = 2.5
    w[rectum_mask] = 0.35

    # Define segment boundaries and colors
    segments = [
        (y > 7.2, CREAM, "mouth"),
        (stomach_mask, PINK, "stomach"),
        (duo_mask, LAV, "duodenum"),
        ((y <= 4.2) & (y > 1.2), GREEN, "ileum")
    ]

    # Draw the colored sections
    for mask, color, label in segments:
        y_seg = y[mask]
        x_seg = x[mask]
        w_seg = w[mask]
        ax.fill_betweenx(y_seg, x_seg - w_seg/2, x_seg + w_seg/2, color=color, edgecolor="none")

    # Draw the continuous outer lines of the canal
    x_left = x - w/2
    x_right = x + w/2
    ax.plot(x_left, y, color=INK, lw=2.5)
    ax.plot(x_right, y, color=INK, lw=2.5)

    # Labels for the outline
    label_y = {"mouth": 8.0, "stomach": 6.35, "duodenum": 4.85, "ileum": 3.0}
    for label, cy in label_y.items():
        ax.text(0.5, cy, label, ha="left", va="center", fontsize=13, weight="bold", color=INK)
        ax.plot([1.6, 2.0], [cy, cy], color=GREY, lw=1.5, ls="--")

    # Dashed connection lines from anatomical regions to flow chart blocks
    dash_kw = dict(color=GREY, lw=1.5, ls="--")
    ax.plot([3.0, 4.4], [8.0, 8.0], **dash_kw)
    ax.plot([3.5, 4.4], [6.35, 6.35], **dash_kw)
    ax.plot([2.9, 4.4], [4.85, 4.85], **dash_kw)
    ax.plot([3.0, 4.4], [3.0, 3.0], **dash_kw)

    # -------------------------------------------------------------
    # Right side: Flow Chart of Digestion Processes
    # -------------------------------------------------------------

    # 1. Mouth Block
    mouth_flow = patches.FancyBboxPatch((4.4, 7.35), 7.2, 1.3, boxstyle="round,pad=0.12",
                                        fc="white", ec=DEEP["orange"], lw=1.8)
    ax.add_patch(mouth_flow)
    ax.text(4.6, 8.3, "mouth", fontsize=12.5, weight="bold", color=DEEP["orange"])
    
    ax.text(5.2, 7.75, "starch", fontsize=13, weight="bold", color=INK, va="center")
    ax.annotate("", xy=(8.2, 7.75), xytext=(6.2, 7.75), arrowprops=dict(arrowstyle="->", lw=2, color=INK))
    ax.text(7.2, 8.1, "salivary amylase", fontsize=11.5, style="italic", ha="center", color=DEEP["blue"])
    ax.text(8.5, 7.75, "maltose", fontsize=13, weight="bold", color=INK, va="center")

    ax.annotate("", xy=(8.0, 6.8), xytext=(8.0, 7.3), arrowprops=dict(arrowstyle="->", lw=2, color=GREY))

    # 2. Stomach Block
    stomach_flow = patches.FancyBboxPatch((4.4, 5.75), 7.2, 1.0, boxstyle="round,pad=0.12",
                                          fc="white", ec=DEEP["pink"], lw=1.8)
    ax.add_patch(stomach_flow)
    ax.text(4.6, 6.4, "stomach", fontsize=12.5, weight="bold", color=DEEP["pink"])
    ax.text(8.0, 6.1, "no carbohydrate digestion\n(acid stops amylase)", 
            ha="center", va="center", fontsize=12, color=INK)

    ax.annotate("", xy=(8.0, 5.2), xytext=(8.0, 5.7), arrowprops=dict(arrowstyle="->", lw=2, color=GREY))

    # 3. Duodenum Block
    duod_flow = patches.FancyBboxPatch((4.4, 4.2), 7.2, 1.0, boxstyle="round,pad=0.12",
                                       fc="white", ec=DEEP["lav"], lw=1.8)
    ax.add_patch(duod_flow)
    ax.text(4.6, 4.85, "duodenum", fontsize=12.5, weight="bold", color=DEEP["lav"])
    
    ax.text(5.2, 4.5, "starch", fontsize=13, weight="bold", color=INK, va="center")
    ax.annotate("", xy=(8.2, 4.5), xytext=(6.2, 4.5), arrowprops=dict(arrowstyle="->", lw=2, color=INK))
    ax.text(7.2, 4.85, "pancreatic amylase", fontsize=11.5, style="italic", ha="center", color=DEEP["blue"])
    ax.text(8.5, 4.5, "maltose", fontsize=13, weight="bold", color=INK, va="center")

    ax.annotate("", xy=(8.0, 3.65), xytext=(8.0, 4.15), arrowprops=dict(arrowstyle="->", lw=2, color=GREY))

    # 4. Ileum Block
    ileum_flow = patches.FancyBboxPatch((4.4, 1.2), 7.2, 2.4, boxstyle="round,pad=0.12",
                                        fc="white", ec=DEEP["green"], lw=1.8)
    ax.add_patch(ileum_flow)
    ax.text(4.6, 3.3, "ileum", fontsize=12.5, weight="bold", color=DEEP["green"])

    # Three enzyme reactions in Ileum
    y1 = 2.9
    ax.text(4.9, y1, "maltose", fontsize=12, weight="bold", color=INK, va="center")
    ax.annotate("", xy=(7.1, y1), xytext=(5.9, y1), arrowprops=dict(arrowstyle="->", lw=1.8, color=INK))
    ax.text(6.5, y1 + 0.2, "maltase", fontsize=11, style="italic", ha="center", color=DEEP["blue"])
    ax.text(7.3, y1, "glucose", fontsize=12, weight="bold", color=INK, va="center")

    y2 = 2.2
    ax.text(4.9, y2, "sucrose", fontsize=12, weight="bold", color=INK, va="center")
    ax.annotate("", xy=(7.1, y2), xytext=(5.9, y2), arrowprops=dict(arrowstyle="->", lw=1.8, color=INK))
    ax.text(6.5, y2 + 0.2, "sucrase", fontsize=11, style="italic", ha="center", color=DEEP["blue"])
    ax.text(7.3, y2, "glucose and fructose", fontsize=12, weight="bold", color=INK, va="center")

    y3 = 1.5
    ax.text(4.9, y3, "lactose", fontsize=12, weight="bold", color=INK, va="center")
    ax.annotate("", xy=(7.1, y3), xytext=(5.9, y3), arrowprops=dict(arrowstyle="->", lw=1.8, color=INK))
    ax.text(6.5, y3 + 0.2, "lactase", fontsize=11, style="italic", ha="center", color=DEEP["blue"])
    ax.text(7.3, y3, "glucose and galactose", fontsize=12, weight="bold", color=INK, va="center")

    # -------------------------------------------------------------
    # Absorption: Arrow from Ileum to Blood
    # -------------------------------------------------------------
    # Blood vessel drawing shifted right to prevent text overlap
    blood_box = patches.FancyBboxPatch((13.7, 1.2), 0.8, 2.4, boxstyle="round,pad=0.1",
                                       fc=PINK, ec=DEEP["pink"], lw=2)
    ax.add_patch(blood_box)
    ax.text(14.1, 2.4, "Blood", ha="center", va="center", fontsize=13, weight="bold", color=INK, rotation=-90)

    # Arrow to blood labelled "glucose absorbed"
    ax.annotate("", xy=(13.6, 2.4), xytext=(11.75, 2.4),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["pink"]))
    ax.text(12.675, 2.55, "glucose\nabsorbed", ha="center", va="bottom", fontsize=11.5, weight="bold", color=DEEP["pink"])

    save(fig, out)
