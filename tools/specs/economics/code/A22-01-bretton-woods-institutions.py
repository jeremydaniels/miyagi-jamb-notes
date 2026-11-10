from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Title
    ax.text(6.0, 8.0, "The Bretton Woods Institutions (1944)", 
            fontsize=18, fontweight='bold', color=INK, ha='center', va='center')

    # Central Balance Scales Structure
    # Base
    base_pts = np.array([[5.0, 0.8], [7.0, 0.8], [6.6, 1.2], [5.4, 1.2]])
    ax.add_patch(patches.Polygon(base_pts, closed=True, facecolor=GREY, edgecolor=INK, lw=2))
    
    # Central Column / Pillar
    ax.add_patch(patches.Rectangle((5.85, 1.2), 0.3, 4.8, facecolor=CREAM, edgecolor=INK, lw=2))
    
    # Fulcrum (top pivot)
    ax.add_patch(patches.Circle((6.0, 6.0), 0.25, facecolor=GREY, edgecolor=INK, lw=2, zorder=5))
    
    # Beam (horizontal)
    ax.plot([2.5, 9.5], [6.0, 6.0], color=INK, lw=4, solid_capstyle='round')

    # Left & Right Chains / Hangers
    left_x = 2.5
    right_x = 9.5
    pan_y = 4.2
    
    # Left chains
    ax.plot([left_x, left_x - 1.2], [6.0, pan_y + 0.1], color=INK, lw=1.5)
    ax.plot([left_x, left_x + 1.2], [6.0, pan_y + 0.1], color=INK, lw=1.5)
    # Left Pan
    left_pan = patches.Arc((left_x, pan_y), 2.5, 0.6, angle=0, theta1=180, theta2=360, color=INK, lw=2.5)
    ax.add_patch(left_pan)
    ax.plot([left_x - 1.25, left_x + 1.25], [pan_y, pan_y], color=INK, lw=2)

    # Right chains
    ax.plot([right_x, right_x - 1.2], [6.0, pan_y + 0.1], color=INK, lw=1.5)
    ax.plot([right_x, right_x + 1.2], [6.0, pan_y + 0.1], color=INK, lw=1.5)
    # Right Pan
    right_pan = patches.Arc((right_x, pan_y), 2.5, 0.6, angle=0, theta1=180, theta2=360, color=INK, lw=2.5)
    ax.add_patch(right_pan)
    ax.plot([right_x - 1.25, right_x + 1.25], [pan_y, pan_y], color=INK, lw=2)

    # --- LEFT SIDE: IMF ---
    # Classical Building Pediment & Columns
    # Building base on pan
    ax.add_patch(patches.Rectangle((left_x - 1.0, pan_y + 0.05), 2.0, 0.2, facecolor=BLUE, edgecolor=DEEP['blue'], lw=1.5))
    # Columns
    for col_x in np.linspace(left_x - 0.8, left_x + 0.8, 4):
        ax.add_patch(patches.Rectangle((col_x - 0.1, pan_y + 0.25), 0.2, 0.65, facecolor=BLUE, edgecolor=DEEP['blue'], lw=1.2))
    # Entablature
    ax.add_patch(patches.Rectangle((left_x - 0.95, pan_y + 0.9), 1.9, 0.2, facecolor=BLUE, edgecolor=DEEP['blue'], lw=1.5))
    # Triangular pediment
    ped_left = np.array([[left_x - 1.0, pan_y + 1.1], [left_x + 1.0, pan_y + 1.1], [left_x, pan_y + 1.6]])
    ax.add_patch(patches.Polygon(ped_left, closed=True, facecolor=BLUE, edgecolor=DEEP['blue'], lw=1.5))
    
    # Institution Name
    ax.text(left_x, pan_y + 0.6, "IMF", fontsize=15, fontweight='bold', color=DEEP['blue'], ha='center', va='center',
            bbox=dict(fc='white', ec=DEEP['blue'], boxstyle='round,pad=0.2', lw=1.2))

    # Currency icons floating / placed around IMF
    curr_bg_props = dict(boxstyle='circle,pad=0.25', facecolor=CREAM, edgecolor=DEEP['blue'], lw=1.5)
    ax.text(left_x - 1.5, pan_y + 1.4, "$", fontsize=16, fontweight='bold', color=DEEP['blue'], ha='center', va='center', bbox=curr_bg_props)
    ax.text(left_x, pan_y + 1.95, "€", fontsize=16, fontweight='bold', color=DEEP['blue'], ha='center', va='center', bbox=curr_bg_props)
    ax.text(left_x + 1.5, pan_y + 1.4, "¥", fontsize=16, fontweight='bold', color=DEEP['blue'], ha='center', va='center', bbox=curr_bg_props)

    # Left descriptive text
    left_desc = "• Short-term stability\n• Exchange rate stabilization\n• Balance of payments support"
    ax.text(left_x, 2.3, left_desc, fontsize=14, color=INK, ha='center', va='center',
            bbox=dict(fc='white', ec=DEEP['blue'], boxstyle='round,pad=0.5', lw=1.5))


    # --- RIGHT SIDE: WORLD BANK ---
    # Classical Building Pediment & Columns
    # Building base on pan
    ax.add_patch(patches.Rectangle((right_x - 1.0, pan_y + 0.05), 2.0, 0.2, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5))
    # Columns
    for col_x in np.linspace(right_x - 0.8, right_x + 0.8, 4):
        ax.add_patch(patches.Rectangle((col_x - 0.1, pan_y + 0.25), 0.2, 0.65, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.2))
    # Entablature
    ax.add_patch(patches.Rectangle((right_x - 0.95, pan_y + 0.9), 1.9, 0.2, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5))
    # Triangular pediment
    ped_right = np.array([[right_x - 1.0, pan_y + 1.1], [right_x + 1.0, pan_y + 1.1], [right_x, pan_y + 1.6]])
    ax.add_patch(patches.Polygon(ped_right, closed=True, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5))
    
    # Institution Name
    ax.text(right_x, pan_y + 0.6, "World Bank (IBRD)", fontsize=14, fontweight='bold', color=DEEP['green'], ha='center', va='center',
            bbox=dict(fc='white', ec=DEEP['green'], boxstyle='round,pad=0.2', lw=1.2))

    # Icons around World Bank: Road, Hospital, School
    icon_bg_props = dict(boxstyle='round,pad=0.3', facecolor=CREAM, edgecolor=DEEP['green'], lw=1.5)
    ax.text(right_x - 1.6, pan_y + 1.4, "Road 🛣", fontsize=14, fontweight='bold', color=DEEP['green'], ha='center', va='center', bbox=icon_bg_props)
    ax.text(right_x, pan_y + 1.95, "Hospital 🏥", fontsize=14, fontweight='bold', color=DEEP['green'], ha='center', va='center', bbox=icon_bg_props)
    ax.text(right_x + 1.6, pan_y + 1.4, "School 🏫", fontsize=14, fontweight='bold', color=DEEP['green'], ha='center', va='center', bbox=icon_bg_props)

    # Right descriptive text
    right_desc = "• Long-term development\n• Poverty reduction & growth\n• Infrastructure & reconstruction"
    ax.text(right_x, 2.3, right_desc, fontsize=14, color=INK, ha='center', va='center',
            bbox=dict(fc='white', ec=DEEP['green'], boxstyle='round,pad=0.5', lw=1.5))

    # Bottom summary tag
    ax.text(6.0, 0.4, "Complementary mandates established to promote international economic cooperation",
            fontsize=14, style='italic', color=INK, ha='center', va='center')

    save(fig, out)
