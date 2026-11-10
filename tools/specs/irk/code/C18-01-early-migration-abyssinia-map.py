from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7)
    
    # Left subplot: Map (Arabian Peninsula & Horn of Africa)
    # Right subplot: Inset illustration of Ja'far bin Abi Talib before King an-Najashi
    ax_map = fig.add_axes([0.05, 0.08, 0.44, 0.84])
    ax_ill = fig.add_axes([0.53, 0.08, 0.42, 0.84])
    
    # ------------------ MAP SETUP ------------------
    ax_map.set_xlim(30, 52)
    ax_map.set_ylim(6, 28)
    ax_map.set_aspect('equal')
    ax_map.axis('off')
    
    # Background sea
    ax_map.set_facecolor('#EBF4F6')
    fig.patch.set_facecolor('white')
    
    # Simplified coastline polygons
    # Arabian Peninsula
    arabia_coords = [
        (33, 28), (36, 28), (40, 29), (48, 29), (50, 26), 
        (52, 24), (52, 22), (50, 18), (45, 14), (43.5, 12.5), 
        (43, 13.5), (41.5, 16.5), (39.8, 21.4), (38, 24), 
        (35, 27.5), (34, 27), (33, 28)
    ]
    arabia_poly = patches.Polygon(arabia_coords, closed=True, facecolor=CREAM, edgecolor=GREY, lw=1.5)
    ax_map.add_patch(arabia_poly)
    
    # Africa (Horn of Africa & Egypt/Sudan/Eritrea/Ethiopia/Somalia)
    africa_coords = [
        (30, 28), (32.5, 28), (32.5, 25), (34.5, 23), (37.5, 19),
        (39, 16), (41.5, 14), (43, 12), (43.5, 11.5), (46, 12),
        (51, 11.5), (49, 8), (45, 6), (40, 6), (36, 6), 
        (30, 6), (30, 28)
    ]
    africa_poly = patches.Polygon(africa_coords, closed=True, facecolor='#F3EFE6', edgecolor=GREY, lw=1.5)
    ax_map.add_patch(africa_poly)
    
    # Abyssinia territory highlight (approx Ethiopia/Eritrea)
    abyssinia_coords = [
        (36, 17), (40, 16), (42.5, 13.5), (42, 10.5), 
        (38, 8.5), (34.5, 11), (35, 14)
    ]
    abyssinia_patch = patches.Polygon(abyssinia_coords, closed=True, facecolor=GREEN, alpha=0.35,
                                      edgecolor=DEEP['green'], lw=2, linestyle='--')
    ax_map.add_patch(abyssinia_patch)
    
    # Red Sea label (placed north-west in northern Red Sea to avoid migration path)
    ax_map.text(35.2, 24.5, "Red Sea", fontsize=15, color=DEEP['blue'], fontstyle='italic', rotation=-40,
                bbox=dict(fc='white', ec='none', alpha=0.8, pad=1.5), zorder=6)
    
    # Makkah position & marker
    makkah_coords = (39.82, 21.42)
    ax_map.plot(makkah_coords[0], makkah_coords[1], 'o', color=DEEP['pink'], markersize=8, zorder=7)
    ax_map.text(makkah_coords[0] + 0.8, makkah_coords[1] + 0.5, "Makkah", fontsize=15, fontweight='bold', color=INK,
                bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25', lw=0.8), zorder=8)
    
    # Abyssinia target point & label
    # Target location in Abyssinian highlands
    aksum_coords = (38.8, 14.2)
    ax_map.plot(aksum_coords[0], aksum_coords[1], 's', color=DEEP['green'], markersize=8, zorder=7)
    # Label placed cleanly below the marker and territory so there is no overlap
    ax_map.text(37.5, 11.2, "Abyssinia", fontsize=16, fontweight='bold', color=INK, ha='center',
                bbox=dict(fc='white', ec=DEEP['green'], boxstyle='round,pad=0.3', lw=1.2), zorder=8)
    
    # Dotted Migration arrow (Makkah -> Abyssinia)
    ax_map.annotate("", xy=aksum_coords, xytext=makkah_coords,
                    arrowprops=dict(arrowstyle="->,head_length=0.7,head_width=0.5",
                                    color=DEEP['pink'], lw=2.5, linestyle=":",
                                    connectionstyle="arc3,rad=-0.12"),
                    zorder=5)
    
    # Migration text label along route (placed to the right of the path, clear of Red Sea label)
    ax_map.text(41.4, 18.0, "Migration to Abyssinia\n(615 CE)", fontsize=14, color=DEEP['pink'],
                ha='left', va='center', fontweight='bold',
                bbox=dict(fc='white', ec=DEEP['pink'], boxstyle='round,pad=0.3', lw=1), zorder=8)
    
    # Map title / caption
    ax_map.text(30.5, 6.8, "Sketch map: zones are approximate", fontsize=14, color=GREY, fontstyle='italic')
    ax_map.set_title("The First Hijrah (Abyssinia)", fontsize=17, fontweight='bold', color=INK, pad=12)

    # ------------------ INSET ILLUSTRATION ------------------
    ax_ill.set_xlim(0, 10)
    ax_ill.set_ylim(0, 10)
    ax_ill.axis('off')
    
    # Background panel
    rect_bg = patches.FancyBboxPatch((0.2, 0.2), 9.6, 9.6, boxstyle="round,pad=0.2",
                                     fc='#FAFAFA', ec=GREY, lw=1.5)
    ax_ill.add_patch(rect_bg)
    
    # Floor / Dais
    ax_ill.fill_between([0.5, 9.5], 0.5, 2.2, color='#EFEBE9')
    ax_ill.plot([0.5, 9.5], [2.2, 2.2], color=GREY, lw=1.5)
    
    # King's Throne (Right side)
    throne_base = patches.Rectangle((7.0, 2.0), 2.2, 1.4, fc=ORANGE, ec=INK, lw=1.5)
    throne_back = patches.Rectangle((8.6, 3.2), 0.6, 4.0, fc=ORANGE, ec=INK, lw=1.5)
    ax_ill.add_patch(throne_base)
    ax_ill.add_patch(throne_back)
    
    # King an-Najashi (seated)
    # Robe
    king_body = patches.Polygon([(7.3, 2.8), (8.7, 2.8), (8.4, 5.2), (7.6, 5.2)], fc=LAV, ec=INK, lw=1.5)
    ax_ill.add_patch(king_body)
    # Head (African King: dark complexion)
    king_head = patches.Circle((8.0, 5.8), 0.55, fc='#5D4037', ec=INK, lw=1.5)
    ax_ill.add_patch(king_head)
    # Crown
    crown = patches.Polygon([(7.45, 6.25), (8.55, 6.25), (8.55, 6.8), (8.25, 6.5), (8.0, 6.9), (7.75, 6.5), (7.45, 6.8)],
                            fc='#FBC02D', ec=INK, lw=1.5)
    ax_ill.add_patch(crown)
    # Attentive arms
    ax_ill.plot([7.6, 7.1], [4.6, 4.3], color=INK, lw=2.5, solid_capstyle='round')
    
    # King Label
    ax_ill.text(8.0, 7.5, "King an-Najashi", fontsize=15, fontweight='bold', color=INK, ha='center',
                bbox=dict(fc='white', ec=DEEP['lav'], boxstyle='round,pad=0.25', lw=1.2))
    
    # Muslim Delegates / Arabs (Left side)
    def draw_delegate(x, y, robe_color):
        body = patches.Polygon([(x - 0.45, y), (x + 0.45, y), (x + 0.3, y + 2.8), (x - 0.3, y + 2.8)],
                               fc=robe_color, ec=INK, lw=1.5)
        head = patches.Circle((x, y + 3.2), 0.4, fc='#D7CCC8', ec=INK, lw=1.5)
        ax_ill.add_patch(body)
        ax_ill.add_patch(head)
        ax_ill.plot([x - 0.4, x + 0.4], [y + 3.4, y + 3.4], color=INK, lw=1.5)
        
    draw_delegate(1.6, 2.2, BLUE)
    draw_delegate(2.6, 2.2, '#ECEFF1')
    
    # Foreground speaker: Ja'far bin Abi Talib
    jafar_x, jafar_y = 4.2, 2.2
    # Robe (Green)
    jafar_body = patches.Polygon([(jafar_x - 0.55, jafar_y), (jafar_x + 0.55, jafar_y), 
                                  (jafar_x + 0.35, jafar_y + 3.1), (jafar_x - 0.35, jafar_y + 3.1)],
                                 fc=GREEN, ec=INK, lw=1.6)
    ax_ill.add_patch(jafar_body)
    # Head
    jafar_head = patches.Circle((jafar_x, jafar_y + 3.55), 0.45, fc='#D7CCC8', ec=INK, lw=1.5)
    ax_ill.add_patch(jafar_head)
    # Beard
    beard = patches.Polygon([(jafar_x - 0.3, jafar_y + 3.45), (jafar_x + 0.3, jafar_y + 3.45), (jafar_x, jafar_y + 2.95)],
                            fc=INK)
    ax_ill.add_patch(beard)
    
    # Reciting / Gesturing arm towards the King
    ax_ill.plot([jafar_x + 0.25, 5.2, 5.8], [jafar_y + 2.7, jafar_y + 3.0, jafar_y + 3.3],
                color=INK, lw=2.5, solid_capstyle='round')
    
    # Ja'far Label
    ax_ill.text(4.2, 6.7, "Ja'far bin Abi Talib", fontsize=15, fontweight='bold', color=INK, ha='center',
                bbox=dict(fc='white', ec=DEEP['green'], boxstyle='round,pad=0.25', lw=1.2))
    
    # Caption indicating Qur'an recitation
    speech_bubble = patches.FancyBboxPatch((3.5, 0.7), 5.5, 1.2, boxstyle="round,pad=0.2",
                                          fc='white', ec=GREY, lw=1.2)
    ax_ill.add_patch(speech_bubble)
    ax_ill.text(6.25, 1.3, "Reciting Surah Maryam\nbefore the royal court",
                fontsize=14, fontstyle='italic', color=INK, ha='center', va='center')
    
    ax_ill.set_title("Audience before the Negus", fontsize=17, fontweight='bold', color=INK, pad=12)

    save(fig, out)
