from style import *
import numpy as np
import math

def draw(out):
    fig = canvas(8, 7)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Coordinates and angles
    barrier_angle = 15 # degrees
    theta_i = 45       # angle of incidence
    
    a_b = math.radians(barrier_angle)
    a_n = math.radians(barrier_angle + 90)
    
    # Directions for rays
    a_inc_ray = math.radians(barrier_angle + 90 + theta_i) # Angle from origin to source
    a_ref_ray = math.radians(barrier_angle + 90 - theta_i) # Angle from origin to destination
    
    # Draw barrier
    L_barrier = 5
    bx = [-L_barrier * math.cos(a_b), L_barrier * math.cos(a_b)]
    by = [-L_barrier * math.sin(a_b), L_barrier * math.sin(a_b)]
    ax.plot(bx, by, color=INK, lw=4)
    ax.text(3.5 * math.cos(a_b), 3.5 * math.sin(a_b) - 0.5, "Barrier", fontsize=16, color=INK, ha='center', va='top')
    
    # Draw hatching for barrier (bottom side)
    for d in np.linspace(-L_barrier + 0.5, L_barrier - 0.5, 20):
        hx1 = d * math.cos(a_b)
        hy1 = d * math.sin(a_b)
        hx2 = hx1 + 0.4 * math.cos(a_b - math.pi/2 - 0.5)
        hy2 = hy1 + 0.4 * math.sin(a_b - math.pi/2 - 0.5)
        ax.plot([hx1, hx2], [hy1, hy2], color=INK, lw=1.5)
    
    # Draw normal
    L_normal = 4.5
    nx = [0, L_normal * math.cos(a_n)]
    ny = [0, L_normal * math.sin(a_n)]
    ax.plot(nx, ny, color=INK, lw=2, linestyle='--')
    ax.text(nx[1], ny[1] + 0.2, "Normal", fontsize=16, color=INK, ha='center', va='bottom', bbox=dict(fc='white', ec='none', pad=2))
    
    # Draw incident ray (arrow pointing to origin)
    L_ray = 5.5
    inc_start_x = L_ray * math.cos(a_inc_ray)
    inc_start_y = L_ray * math.sin(a_inc_ray)
    ax.annotate("", xy=(0, 0), xytext=(inc_start_x, inc_start_y),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.5))
    ax.text(inc_start_x - 0.5, inc_start_y + 0.2, "Incident wave", fontsize=16, color=DEEP["blue"], ha='right', va='bottom')
    
    # Draw reflected ray (arrow pointing away from origin)
    ref_end_x = L_ray * math.cos(a_ref_ray)
    ref_end_y = L_ray * math.sin(a_ref_ray)
    ax.annotate("", xy=(ref_end_x, ref_end_y), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5))
    ax.text(ref_end_x + 0.5, ref_end_y + 0.2, "Reflected wave", fontsize=16, color=DEEP["orange"], ha='left', va='bottom')
    
    # Draw wavefronts
    W_len = 3.5 # Length of wavefront lines
    for d in [2, 3.5, 5]:
        # Incident wavefronts
        cx = d * math.cos(a_inc_ray)
        cy = d * math.sin(a_inc_ray)
        # Perpendicular to incident ray
        a_wf_inc = a_inc_ray + math.pi/2
        wx1 = cx + (W_len/2) * math.cos(a_wf_inc)
        wy1 = cy + (W_len/2) * math.sin(a_wf_inc)
        wx2 = cx - (W_len/2) * math.cos(a_wf_inc)
        wy2 = cy - (W_len/2) * math.sin(a_wf_inc)
        ax.plot([wx1, wx2], [wy1, wy2], color=BLUE, lw=2.5)
        
        # Reflected wavefronts
        cx_r = d * math.cos(a_ref_ray)
        cy_r = d * math.sin(a_ref_ray)
        a_wf_ref = a_ref_ray + math.pi/2
        wrx1 = cx_r + (W_len/2) * math.cos(a_wf_ref)
        wry1 = cy_r + (W_len/2) * math.sin(a_wf_ref)
        wrx2 = cx_r - (W_len/2) * math.cos(a_wf_ref)
        wry2 = cy_r - (W_len/2) * math.sin(a_wf_ref)
        ax.plot([wrx1, wrx2], [wry1, wry2], color=ORANGE, lw=2.5)
    
    # Draw arcs for angles
    R = 1.2
    # Incident angle arc
    t_vals_inc = np.linspace(a_n, a_inc_ray, 30)
    ax.plot(R * np.cos(t_vals_inc), R * np.sin(t_vals_inc), color=INK, lw=1.5)
    mid_inc = (a_n + a_inc_ray) / 2
    ax.text((R + 0.4) * math.cos(mid_inc), (R + 0.4) * math.sin(mid_inc), "i", fontsize=16, color=INK, ha='center', va='center')
    
    # Reflected angle arc
    t_vals_ref = np.linspace(a_ref_ray, a_n, 30)
    ax.plot(R * np.cos(t_vals_ref), R * np.sin(t_vals_ref), color=INK, lw=1.5)
    mid_ref = (a_n + a_ref_ray) / 2
    ax.text((R + 0.4) * math.cos(mid_ref), (R + 0.4) * math.sin(mid_ref), "r", fontsize=16, color=INK, ha='center', va='center')
    
    ax.set_xlim(-6, 6)
    ax.set_ylim(-3, 6)
    save(fig, out)
