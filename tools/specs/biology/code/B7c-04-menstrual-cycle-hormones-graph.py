from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse

def draw(out):
    fig = canvas(12, 10.5)
    
    # 4 subplots sharing x axis
    gs = fig.add_gridspec(4, 1, height_ratios=[2, 1.8, 2, 2.3], hspace=0.18,
                           left=0.12, right=0.92, top=0.94, bottom=0.10)
    
    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1], sharex=ax0)
    ax2 = fig.add_subplot(gs[2], sharex=ax0)
    ax3 = fig.add_subplot(gs[3], sharex=ax0)
    
    days = np.linspace(1, 28, 500)
    
    # Helper to style axes cleanly
    for ax in [ax0, ax1, ax2, ax3]:
        ax.set_facecolor("white")
        ax.set_xlim(1, 28)
        # Vertical dotted guideline for day 14 (ovulation)
        ax.axvline(14, color=GREY, linestyle="--", lw=1.2, zorder=1)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(left=False, labelleft=False)
        if ax != ax3:
            ax.spines['bottom'].set_visible(False)
            ax.tick_params(bottom=False, labelbottom=False)

    # -------------------------------------------------------------
    # BAND 0: Pituitary Hormones (FSH, LH)
    # -------------------------------------------------------------
    fsh = 2.5 + 2.5 * np.exp(-((days - 3) / 2.5)**2) + 2.2 * np.exp(-((days - 14) / 1.2)**2) + 0.5 * np.exp(-((days - 20) / 4)**2)
    lh = 1.2 + 8.5 * np.exp(-((days - 13.8) / 0.8)**2) + 0.3 * np.sin(days / 2.0)
    
    ax0.plot(days, fsh, color=DEEP["blue"], lw=3, label="FSH")
    ax0.plot(days, lh, color=DEEP["orange"], lw=3, label="LH")
    ax0.set_ylim(0, 11)
    
    ax0.text(1.2, 8.8, "Pituitary hormones", fontsize=13, fontweight="bold", color=INK)
    ax0.text(4, 5.8, "FSH", color=DEEP["blue"], fontsize=12, fontweight="bold")
    ax0.text(11.8, 8.2, "LH", color=DEEP["orange"], fontsize=12, fontweight="bold")
    
    # LH surge label
    ax0.annotate("LH surge", xy=(13.8, 9.7), xytext=(16, 9.5),
                 fontsize=11.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec="none", pad=1))

    # -------------------------------------------------------------
    # BAND 1: Ovary Events (Follicle developing, Ovulation, Corpus luteum)
    # -------------------------------------------------------------
    ax1.set_ylim(-1, 1)
    ax1.text(1.2, 0.7, "Ovary events", fontsize=13, fontweight="bold", color=INK)
    
    # 1. Small follicle (Day 3.5)
    ax1.add_patch(Circle((3.5, 0), 0.3, fc=CREAM, ec=DEEP["orange"], lw=1.5))
    ax1.add_patch(Circle((3.5, 0), 0.08, fc=DEEP["pink"], ec="none"))
    
    # 2. Growing follicle (Day 8.5)
    ax1.add_patch(Circle((8.5, 0), 0.5, fc=CREAM, ec=DEEP["orange"], lw=1.5))
    ax1.add_patch(Circle((8.5, 0), 0.3, fc="white", ec=DEEP["blue"], lw=1))
    ax1.add_patch(Circle((8.6, 0.05), 0.1, fc=DEEP["pink"], ec="none"))
    
    # 3. Mature follicle bursting & releasing egg at Day 14
    ax1.add_patch(Circle((13.4, 0), 0.65, fc=CREAM, ec=DEEP["orange"], lw=1.5))
    ax1.add_patch(Circle((13.3, 0), 0.42, fc="white", ec=DEEP["blue"], lw=1))
    ax1.plot([13.8, 14.2], [0.35, 0.5], color=DEEP["orange"], lw=1.5)
    ax1.plot([13.9, 14.3], [-0.2, -0.35], color=DEEP["orange"], lw=1.5)
    ax1.add_patch(Circle((14.6, 0.1), 0.14, fc=DEEP["pink"], ec=DEEP["orange"], lw=1.5))
    
    # 4. Corpus luteum developing (Day 19)
    ax1.add_patch(Ellipse((19, 0), 1.2, 1.0, fc=CREAM, ec=DEEP["orange"], lw=2.5, linestyle="-"))
    ax1.add_patch(Circle((19, 0), 0.25, fc="white", ec=DEEP["orange"], lw=1))
    
    # 5. Corpus luteum shrinking (Day 25)
    ax1.add_patch(Ellipse((25, 0), 0.7, 0.5, fc=GREY, ec=INK, lw=1.5, linestyle=":"))
    
    # Labels for ovary events
    ax1.text(6.0, -0.75, "follicle developing", fontsize=11, ha="center", color=INK,
             bbox=dict(fc="white", ec="none", pad=1))
    ax1.text(14.0, -0.75, "ovulation", fontsize=11.5, ha="center", fontweight="bold", color=INK,
             bbox=dict(fc="white", ec="none", pad=1))
    ax1.text(21.5, -0.75, "corpus luteum", fontsize=11, ha="center", color=INK,
             bbox=dict(fc="white", ec="none", pad=1))

    # -------------------------------------------------------------
    # BAND 2: Ovarian Hormones (Oestrogen, Progesterone)
    # -------------------------------------------------------------
    oestrogen = 1.5 + 7.5 * np.exp(-((days - 12.5) / 2.2)**2) + 3.0 * np.exp(-((days - 21) / 3.5)**2)
    prog = 0.8 + 7.8 / (1.0 + np.exp(-1.2 * (days - 15.5))) * (1.0 / (1.0 + np.exp(0.9 * (days - 25.0))))
    
    ax2.plot(days, oestrogen, color=DEEP["pink"], lw=3, label="oestrogen")
    ax2.plot(days, prog, color=DEEP["lav"], lw=3, label="progesterone")
    ax2.set_ylim(0, 11)
    
    ax2.text(1.2, 8.8, "Ovarian hormones", fontsize=13, fontweight="bold", color=INK)
    ax2.text(10.5, 7.8, "oestrogen", color=DEEP["pink"], fontsize=12, fontweight="bold",
             bbox=dict(fc="white", ec="none", pad=1))
    ax2.text(20.0, 7.8, "progesterone", color=DEEP["lav"], fontsize=12, fontweight="bold",
             bbox=dict(fc="white", ec="none", pad=1))

    # -------------------------------------------------------------
    # BAND 3: Uterine Lining Thickness
    # -------------------------------------------------------------
    endometrium = np.piecewise(days, [
        days <= 4.5,
        (days > 4.5) & (days <= 14),
        days > 14
    ], [
        lambda d: 3.5 - 2.5 * (d - 1) / 3.5,
        lambda d: 1.0 + 5.0 * ((d - 4.5) / 9.5)**1.2,
        lambda d: 6.0 + 2.0 * np.sin((d - 14) / 14 * np.pi) - 0.5 * np.maximum(0, d - 26)
    ])
    
    ax3.fill_between(days, 0, endometrium, color=PINK, alpha=0.6, ec=DEEP["pink"], lw=2)
    vessel_x = np.linspace(15, 27, 20)
    for vx in vessel_x:
        vy = np.linspace(0.2, endometrium[int((vx-1)/27*499)] * 0.85, 25)
        vw = 0.15 * np.sin(vy * 3 + vx)
        ax3.plot(vx + vw, vy, color="#D45372", lw=0.8, alpha=0.7)

    ax3.set_ylim(0, 10.5)
    ax3.text(1.2, 9.2, "Thickness of uterus lining", fontsize=13, fontweight="bold", color=INK)
    
    # Separate phase annotations in Band 3
    ax3.text(3.0, 5.0, "menstruation", fontsize=11, ha="center", color=INK,
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    ax3.text(8.0, 2.2, "repair phase", fontsize=11, ha="center", color=INK,
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    ax3.text(11.5, 6.2, "endometrium\nthickening", fontsize=10.5, ha="center", color=INK,
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    ax3.text(21.5, 4.2, "endometrium\nmaintained", fontsize=11, ha="center", color=INK,
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Distinct "day 14" indicator placed safely inside ax3 above the x-axis
    ax3.annotate("day 14", xy=(14, 0.4), xytext=(14, 1.8),
                 fontsize=11.5, fontweight="bold", ha="center", color=DEEP["orange"],
                 bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.2", lw=1.2),
                 arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=1.5))

    # X axis styling on the bottom subplot
    ax3.spines['bottom'].set_color(INK)
    ax3.spines['bottom'].set_linewidth(1.5)
    ax3.set_xticks(range(1, 29, 2))
    ax3.tick_params(bottom=True, labelbottom=True, labelsize=11, color=INK)
    ax3.set_xlabel("days 1 to 28", fontsize=13, fontweight="bold", color=INK, labelpad=10)

    save(fig, out)
