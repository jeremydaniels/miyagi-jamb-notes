from style import *
import numpy as np

def draw(out):
    fig = canvas(14, 12)
    
    axes = [
        fig.add_subplot(2, 2, 1),
        fig.add_subplot(2, 2, 2),
        fig.add_subplot(2, 2, 3),
        fig.add_subplot(2, 2, 4)
    ]
    
    titles = [
        "Strong Acid vs Strong Base",
        "Weak Acid vs Strong Base",
        "Strong Acid vs Weak Base",
        "Weak Acid vs Weak Base"
    ]
    
    v = np.linspace(0, 50, 400)
    
    def sigmoid(x, x0, k):
        return 1.0 / (1.0 + np.exp(-k * (x - x0)))

    # 1. Strong Acid vs Strong Base
    base1 = np.where(v < 25, 1.2 * (v / 25.0)**3, 1.2)
    tail1 = np.where(v >= 25, 2.8 * (1 - np.exp(-(v - 25.0) / 10.0)), 0)
    ph1 = 1.0 + base1 + 8.0 * sigmoid(v, 25.0, 1.8) + tail1
    ph1 = np.clip(ph1, 1.0, 13.0)
    
    # 2. Weak Acid vs Strong Base
    tail2 = np.where(v >= 25, 2.0 * (1 - np.exp(-(v - 25.0) / 12.0)), 0)
    ph2 = 3.0 + 1.2 * (1 - np.exp(-v / 3.0)) + 1.5 * (v / 25.0) + 4.5 * sigmoid(v, 25.0, 1.2) + tail2
    ph2 = np.clip(ph2, 3.0, 12.5)

    # 3. Strong Acid vs Weak Base
    base3 = np.where(v < 25, 1.0 * (v / 25.0)**3, 1.0)
    tail3 = np.where(v >= 25, 3.0 * (1 - np.exp(-(v - 25.0) / 10.0)), 0)
    ph3 = 1.0 + base3 + 4.2 * sigmoid(v, 25.0, 1.2) + tail3
    ph3 = np.clip(ph3, 1.0, 9.2)

    # 4. Weak Acid vs Weak Base
    ph4 = 3.0 + 0.8 * (1 - np.exp(-v / 4.0)) + 4.8 * sigmoid(v, 25.0, 0.15)
    ph4 = np.clip(ph4, 3.0, 9.5)

    curves = [ph1, ph2, ph3, ph4]
    eq_pts = [
        (25.0, 7.0, "Equivalence point\n(pH = 7)"),
        (25.0, 8.8, "Equivalence point\n(pH > 7)"),
        (25.0, 5.2, "Equivalence point\n(pH < 7)"),
        (25.0, 6.2, "Equivalence point\n(gradual inflection)")
    ]

    for i, ax in enumerate(axes):
        ax.set_facecolor("white")
        ax.axhline(7, color=GREY, linestyle="--", linewidth=1.2, zorder=1)
        ax.axvline(25, color=GREY, linestyle=":", linewidth=1.2, zorder=1)
        
        ax.plot(v, curves[i], color=DEEP["blue"], lw=3.5, zorder=3)
        
        eq_v, eq_ph, eq_lbl = eq_pts[i]
        ax.plot(eq_v, eq_ph, "o", color=DEEP["pink"], markersize=8, zorder=4)
        
        xytext = (eq_v - 8, eq_ph + 2.2) if i == 2 else (eq_v - 16, eq_ph + 1.8)
        if i == 1:
            xytext = (eq_v - 16, eq_ph + 1.8)
        elif i == 0:
            xytext = (eq_v - 16, eq_ph + 1.8)
        elif i == 3:
            xytext = (eq_v - 16, eq_ph + 2.0)

        ax.annotate(
            eq_lbl,
            xy=(eq_v, eq_ph),
            xytext=xytext,
            fontsize=14,
            color=INK,
            weight="bold",
            arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.8),
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", alpha=0.9),
            zorder=5
        )
        
        ax.set_xlim(0, 52)
        ax.set_ylim(0, 14.5)
        ax.set_yticks([0, 2, 4, 6, 7, 8, 10, 12, 14])
        ax.set_xticks([0, 10, 20, 25, 30, 40, 50])
        ax.set_xticklabels(["0", "10", "20", "$V_{eq}$", "30", "40", "50"], fontsize=14)
        ax.tick_params(axis="both", labelsize=14, colors=INK)
        
        ax.set_title(titles[i], fontsize=16, weight="bold", color=INK, pad=12)
        ax.set_xlabel("Volume of base added", fontsize=15, color=INK, labelpad=6)
        ax.set_ylabel("pH", fontsize=15, color=INK, labelpad=6)
        
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(INK)
        ax.spines["bottom"].set_color(INK)
        ax.spines["left"].set_linewidth(1.5)
        ax.spines["bottom"].set_linewidth(1.5)

    plt.tight_layout(pad=3.5)
    save(fig, out)
