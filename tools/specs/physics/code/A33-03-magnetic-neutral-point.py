from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 11)
    
    # We will create two subplots or use one clean axis with (0, 10) x (0, 11) coordinates
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Helper to draw a bar magnet
    def draw_magnet(xc, yc, w, h, left_pole='S', right_pole='N'):
        # xc, yc is center of magnet
        # Left half
        col_left = DEEP['blue'] if left_pole == 'S' else DEEP['pink']
        col_right = DEEP['pink'] if right_pole == 'N' else DEEP['blue']
        
        # Left rectangle
        rect_l = patches.Rectangle((xc - w/2, yc - h/2), w/2, h, 
                                   facecolor=BLUE if left_pole == 'S' else PINK, 
                                   edgecolor=INK, lw=1.5, zorder=4)
        # Right rectangle
        rect_r = patches.Rectangle((xc, yc - h/2), w/2, h, 
                                   facecolor=PINK if right_pole == 'N' else BLUE, 
                                   edgecolor=INK, lw=1.5, zorder=4)
        ax.add_patch(rect_l)
        ax.add_patch(rect_r)
        
        # Pole text
        ax.text(xc - w/4, yc, left_pole, color=INK, fontsize=16, fontweight='bold', ha='center', va='center', zorder=5)
        ax.text(xc + w/4, yc, right_pole, color=INK, fontsize=16, fontweight='bold', ha='center', va='center', zorder=5)

    # -------------------------------------------------------------
    # TOP SCENARIO: N-pole facing S-pole (Attraction)
    # -------------------------------------------------------------
    y_top = 8.2
    ax.text(5, 10.4, "Attraction: Unlike Poles (N facing S)", fontsize=16, fontweight='bold', ha='center', va='center', color=INK)

    # Magnets: left magnet ends at x=3.2 (so center at 1.9, width 2.6, height 1.0)
    # gap between x=3.2 and x=6.8 (center at 5.0)
    # right magnet starts at x=6.8 (center at 8.1, width 2.6, height 1.0)
    mag_w = 2.4
    mag_h = 1.0
    x_left_mag = 2.0
    x_right_mag = 8.0
    
    # Left magnet: S - N (facing right with N)
    draw_magnet(x_left_mag, y_top, mag_w, mag_h, 'S', 'N')
    # Right magnet: S - N (facing left with S)
    draw_magnet(x_right_mag, y_top, mag_w, mag_h, 'S', 'N')
    
    # Field lines connecting N (at x=3.2) to S (at x=6.8)
    x_n = x_left_mag + mag_w/2 # 3.2
    x_s = x_right_mag - mag_w/2 # 6.8
    
    # Lines across the gap
    offsets = [0.0, 0.25, -0.25, 0.45, -0.45, 0.7, -0.7, 1.0, -1.0]
    for dy in offsets:
        # Start at (x_n, y_top + dy * 0.4)
        # End at (x_s, y_top + dy * 0.4)
        # Bulge in middle
        y_start = y_top + dy * 0.4
        y_end = y_top + dy * 0.4
        y_mid = y_top + dy * 1.0
        
        t = np.linspace(0, 1, 100)
        # Quadratic/cubic Bezier curve
        # P0 = (x_n, y_start), P1 = (5.0, y_mid), P2 = (x_s, y_end)
        bx = (1 - t)**2 * x_n + 2 * (1 - t) * t * 5.0 + t**2 * x_s
        by = (1 - t)**2 * y_start + 2 * (1 - t) * t * y_mid + t**2 * y_end
        ax.plot(bx, by, color=DEEP['blue'], lw=1.8, zorder=2)
        
        # Add arrow pointing from N to S (left to right)
        # Arrow near the middle (t=0.55)
        ax.annotate('', xy=(bx[55], by[55]), xytext=(bx[48], by[48]),
                    arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=1.8, mutation_scale=14),
                    zorder=3)
    
    # Outer lines returning around the magnets
    for sgn in [1, -1]:
        # Top/bottom loop lines
        t = np.linspace(0, 1, 100)
        # From left N pole looping back towards S pole of same or other magnet
        lx = (1-t)**2 * (x_n - 0.2) + 2*(1-t)*t * 1.5 + t**2 * (x_left_mag - mag_w/2)
        ly = (1-t)**2 * (y_top + sgn*0.4) + 2*(1-t)*t * (y_top + sgn*1.6) + t**2 * (y_top + sgn*0.3)
        ax.plot(lx, ly, color=DEEP['blue'], lw=1.8, zorder=2)
        ax.annotate('', xy=(lx[45], ly[45]), xytext=(lx[52], ly[52]),
                    arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=1.8, mutation_scale=14),
                    zorder=3)
        
        rx = (1-t)**2 * (x_right_mag + mag_w/2) + 2*(1-t)*t * 8.5 + t**2 * (x_s + 0.2)
        ly_r = (1-t)**2 * (y_top + sgn*0.3) + 2*(1-t)*t * (y_top + sgn*1.6) + t**2 * (y_top + sgn*0.4)
        ax.plot(rx, ly_r, color=DEEP['blue'], lw=1.8, zorder=2)
        ax.annotate('', xy=(rx[52], ly_r[52]), xytext=(rx[45], ly_r[45]),
                    arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=1.8, mutation_scale=14),
                    zorder=3)

    # Dividing line between scenarios
    ax.axhline(5.5, color=GREY, linestyle='--', lw=1.2)

    # -------------------------------------------------------------
    # BOTTOM SCENARIO: N-pole facing N-pole (Repulsion)
    # -------------------------------------------------------------
    y_bot = 2.8
    ax.text(5, 5.0, "Repulsion: Like Poles (N facing N)", fontsize=16, fontweight='bold', ha='center', va='center', color=INK)

    # Left magnet: S - N (facing right with N)
    draw_magnet(x_left_mag, y_bot, mag_w, mag_h, 'S', 'N')
    # Right magnet: N - S (facing left with N)
    draw_magnet(x_right_mag, y_bot, mag_w, mag_h, 'N', 'S')
    
    # Field lines from left N-pole curving upwards and downwards, repelled at x=5
    y_offsets = [0.05, 0.18, 0.32, 0.44]
    
    for dy in y_offsets:
        for sgn in [1, -1]:
            # Left side lines: start at (x_n, y_bot + sgn*dy)
            # Curve away towards x=4.8, y=y_bot + sgn*(dy*3 + 1.2)
            t = np.linspace(0, 1, 100)
            p0 = np.array([x_n, y_bot + sgn * dy])
            p1 = np.array([4.5, y_bot + sgn * dy * 0.8])
            p2 = np.array([4.65, y_bot + sgn * (0.8 + dy * 2.2)])
            
            bx = (1 - t)**2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p2[0]
            by = (1 - t)**2 * p0[1] + 2 * (1 - t) * t * p1[1] + t**2 * p2[1]
            ax.plot(bx, by, color=DEEP['pink'], lw=1.8, zorder=2)
            
            # Arrow pointing outward from N pole
            ax.annotate('', xy=(bx[60], by[60]), xytext=(bx[50], by[50]),
                        arrowprops=dict(arrowstyle="->", color=DEEP['pink'], lw=1.8, mutation_scale=14),
                        zorder=3)
            
            # Right side lines: start at (x_s, y_bot + sgn*dy)
            # Curve away towards x=5.2, y=y_bot + sgn*(dy*3 + 1.2)
            p0_r = np.array([x_s, y_bot + sgn * dy])
            p1_r = np.array([5.5, y_bot + sgn * dy * 0.8])
            p2_r = np.array([5.35, y_bot + sgn * (0.8 + dy * 2.2)])
            
            bx_r = (1 - t)**2 * p0_r[0] + 2 * (1 - t) * t * p1_r[0] + t**2 * p2_r[0]
            by_r = (1 - t)**2 * p0_r[1] + 2 * (1 - t) * t * p1_r[1] + t**2 * p2_r[1]
            ax.plot(bx_r, by_r, color=DEEP['pink'], lw=1.8, zorder=2)
            
            # Arrow pointing outward from N pole
            ax.annotate('', xy=(bx_r[60], by_r[60]), xytext=(bx_r[50], by_r[50]),
                        arrowprops=dict(arrowstyle="->", color=DEEP['pink'], lw=1.8, mutation_scale=14),
                        zorder=3)

    # Neutral point in exact centre (5.0, y_bot)
    ax.scatter([5.0], [y_bot], color=INK, s=90, marker='x', lw=2.5, zorder=6)
    
    # Label for Neutral Point
    ax.annotate("Neutral Point\n(X)", 
                xy=(5.0, y_bot), 
                xytext=(5.0, y_bot - 1.5),
                fontsize=15, 
                fontweight='bold',
                color=INK, 
                ha='center', 
                va='top',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
                zorder=7)

    save(fig, out)
