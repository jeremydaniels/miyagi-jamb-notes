from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7)
    
    # We will create 3 subplots or custom panels across the figure
    ax = fig.add_axes([0.05, 0.08, 0.90, 0.84])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis("off")
    
    # Common vertical Energy axis on the left
    ax.annotate("", xy=(0.6, 9.2), xytext=(0.6, 0.8),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5))
    ax.text(0.4, 5.0, "Energy ($E$)", rotation=90, va="center", ha="right",
            fontsize=16, color=INK, weight="bold")
    
    # Subsystem positions (x-centers)
    centers = [2.6, 6.2, 9.8]
    band_w = 2.2
    
    # Titles
    titles = ["Conductor", "Semiconductor", "Insulator"]
    subtitles = ["(overlapping bands)", "(small gap ~1 eV)", "(large gap >3 eV)"]
    
    for i, cx in enumerate(centers):
        ax.text(cx, 9.3, titles[i], ha="center", va="bottom",
                fontsize=17, weight="bold", color=INK)
    
    # Helper to draw a band (rectangle with rounded or clean edges and label)
    def draw_band(x, y, w, h, facecolor, edgecolor, text):
        rect = patches.Rectangle((x - w/2, y), w, h, 
                                 facecolor=facecolor, edgecolor=edgecolor, 
                                 linewidth=2, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y + h/2, text, ha="center", va="center",
                fontsize=14, color=INK, weight="bold", zorder=4)

    # -------------------------------------------------------------
    # 1. CONDUCTOR
    # Overlapping valence band and conduction band
    # Valence band: y = 1.5 to 5.0
    # Conduction band: y = 3.8 to 7.3
    # Overlap region: y = 3.8 to 5.0
    c1 = centers[0]
    vb_y, vb_h = 1.5, 3.5
    cb_y, cb_h = 3.8, 3.5
    
    # Draw non-overlapping parts and overlap
    # Bottom valence
    draw_band(c1, vb_y, band_w, vb_h, BLUE, DEEP["blue"], "")
    # Top conduction
    draw_band(c1, cb_y, band_w, cb_h, GREEN, DEEP["green"], "")
    
    # Overlap area highlight
    overlap = patches.Rectangle((c1 - band_w/2, cb_y), band_w, (vb_y + vb_h) - cb_y,
                                facecolor=ORANGE, edgecolor=DEEP["orange"],
                                linewidth=2, linestyle="--", alpha=0.6, zorder=3)
    ax.add_patch(overlap)
    
    # Labels for Conductor
    ax.text(c1, 2.5, "Valence\nBand", ha="center", va="center", fontsize=14, color=INK, weight="bold", zorder=5)
    ax.text(c1, 6.0, "Conduction\nBand", ha="center", va="center", fontsize=14, color=INK, weight="bold", zorder=5)
    
    # Overlap label
    ax.annotate("Overlap\n(no gap)", xy=(c1 + band_w/2, 4.4), xytext=(c1 + band_w/2 + 0.35, 4.4),
                va="center", ha="left", fontsize=14, color=INK, weight="bold",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    # -------------------------------------------------------------
    # 2. SEMICONDUCTOR
    # Valence band: y = 1.5 to 3.8
    # Forbidden gap: y = 3.8 to 5.0 (gap = 1.2)
    # Conduction band: y = 5.0 to 7.3
    c2 = centers[1]
    vb2_y, vb2_h = 1.5, 2.3
    cb2_y, cb2_h = 5.0, 2.3
    
    draw_band(c2, vb2_y, band_w, vb2_h, BLUE, DEEP["blue"], "Valence\nBand")
    draw_band(c2, cb2_y, band_w, cb2_h, GREEN, DEEP["green"], "Conduction\nBand")
    
    # Gap dimension arrow
    gap_x = c2
    ax.annotate("", xy=(gap_x, cb2_y), xytext=(gap_x, vb2_y + vb2_h),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=2))
    ax.text(c2 + 0.15, 4.4, "Forbidden gap\n$E_g \\approx 1\\text{ eV}$", 
            ha="left", va="center", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=0.2))

    # -------------------------------------------------------------
    # 3. INSULATOR
    # Valence band: y = 1.0 to 2.8
    # Forbidden gap: y = 2.8 to 6.0 (gap = 3.2)
    # Conduction band: y = 6.0 to 7.8
    c3 = centers[2]
    vb3_y, vb3_h = 1.0, 1.8
    cb3_y, cb3_h = 6.0, 1.8
    
    draw_band(c3, vb3_y, band_w, vb3_h, BLUE, DEEP["blue"], "Valence\nBand")
    draw_band(c3, cb3_y, band_w, cb3_h, GREEN, DEEP["green"], "Conduction\nBand")
    
    # Gap dimension arrow
    ax.annotate("", xy=(c3, cb3_y), xytext=(c3, vb3_y + vb3_h),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=2))
    ax.text(c3 + 0.15, 4.4, "Large forbidden gap\n$E_g > 3\\text{ eV}$", 
            ha="left", va="center", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=0.2))

    save(fig, out)
