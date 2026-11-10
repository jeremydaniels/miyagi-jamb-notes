from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def draw_stick_figure(ax, x, y, height=1.0, color=INK):
    head_r = height * 0.12
    head_y = y + height - head_r
    circle = plt.Circle((x, head_y), head_r, color=color, fill=False, lw=2)
    ax.add_patch(circle)
    
    neck_y = head_y - head_r
    crotch_y = y + height * 0.4
    ax.plot([x, x], [neck_y, crotch_y], color=color, lw=2)
    
    ax.plot([x, x - height * 0.15], [crotch_y, y], color=color, lw=2)
    ax.plot([x, x + height * 0.15], [crotch_y, y], color=color, lw=2)
    
    shoulder_y = neck_y - height * 0.1
    ax.plot([x - height * 0.15, x, x + height * 0.15], 
            [shoulder_y - height * 0.15, shoulder_y, shoulder_y - height * 0.15], 
            color=color, lw=2)

def draw_plane(ax, x, y, scale=0.4):
    body_x = [x - 1.2 * scale, x + 1.2 * scale]
    body_y = [y, y + 0.2 * scale]
    ax.plot(body_x, body_y, color=DEEP["blue"], lw=3)
    ax.plot([x - 0.2 * scale, x + 0.3 * scale, x - 0.1 * scale],
            [y + 0.1 * scale, y + 0.8 * scale, y + 0.1 * scale], color=DEEP["blue"], lw=2.5)
    ax.plot([x - 1.2 * scale, x - 1.0 * scale],
            [y, y + 0.5 * scale], color=DEEP["blue"], lw=2.5)

def draw_boat(ax, x, y, scale=0.4):
    hull_x = [x - 1.0 * scale, x - 0.7 * scale, x + 0.7 * scale, x + 1.0 * scale]
    hull_y = [y + 0.4 * scale, y, y, y + 0.4 * scale]
    ax.plot(hull_x, hull_y, color=DEEP["orange"], lw=2.5)
    ax.plot([x, x], [y + 0.4 * scale, y + 1.2 * scale], color=INK, lw=2)
    ax.plot([x, x + 0.6 * scale, x], [y + 1.1 * scale, y + 0.6 * scale, y + 0.6 * scale], 
            color=DEEP["orange"], lw=2)

def draw(out):
    fig = canvas(14, 7.5)
    
    # Subplot 1: Angle of Elevation
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_xlim(-0.5, 9.5)
    ax1.set_ylim(-0.8, 7.5)
    ax1.set_aspect('equal')
    ax1.axis('off')
    
    # Ground
    ax1.plot([-0.5, 9.5], [0, 0], color=GREY, lw=2.5)
    
    # Observer
    obs_x, obs_ground_y = 1.0, 0.0
    person_h = 1.8
    draw_stick_figure(ax1, obs_x, obs_ground_y, height=person_h)
    eye_x, eye_y = obs_x, obs_ground_y + person_h * 0.88
    
    # Target: Aeroplane
    plane_x, plane_y = 8.0, 5.5
    draw_plane(ax1, plane_x, plane_y, scale=0.6)
    
    # Horizontal line of sight
    ax1.plot([eye_x, 8.5], [eye_y, eye_y], color=INK, ls='--', lw=2)
    ax1.text(eye_x + 3.2, eye_y - 0.4, "Horizontal line of sight", fontsize=14, ha='center', color=INK,
             bbox=dict(fc='white', ec='none', pad=2))
    
    # Line of sight to plane
    ax1.plot([eye_x, plane_x], [eye_y, plane_y], color=DEEP["blue"], lw=2.5)
    
    # Angle arc
    angle_rad = np.arctan2(plane_y - eye_y, plane_x - eye_x)
    angle_deg = np.degrees(angle_rad)
    arc1 = Arc((eye_x, eye_y), 3.0, 3.0, angle=0, theta1=0, theta2=angle_deg, 
               color=DEEP["pink"], lw=2.5)
    ax1.add_patch(arc1)
    
    # Angle label
    lbl_rad = angle_rad / 2.0
    lbl_r = 2.4
    lx = eye_x + lbl_r * np.cos(lbl_rad)
    ly = eye_y + lbl_r * np.sin(lbl_rad)
    ax1.text(lx + 0.2, ly + 0.15, "Angle of\nelevation", fontsize=15, 
             color=DEEP["pink"], fontweight='bold', va='center')
    
    ax1.text(eye_x, eye_y + 0.5, "Observer", fontsize=14, ha='center', color=INK)
    ax1.text(plane_x, plane_y + 0.7, "Aeroplane", fontsize=14, ha='center', color=INK)
    ax1.set_title("Angle of Elevation", fontsize=18, pad=20, fontweight='bold', color=INK)

    # Subplot 2: Angle of Depression
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_xlim(-0.5, 9.5)
    ax2.set_ylim(-0.8, 7.5)
    ax2.set_aspect('equal')
    ax2.axis('off')
    
    # Cliff & Water
    cliff_x = 2.2
    cliff_top = 4.8
    # Cliff face
    ax2.plot([-0.5, cliff_x, cliff_x], [cliff_top, cliff_top, 0], color=GREY, lw=2.5)
    ax2.fill_between([-0.5, cliff_x], [cliff_top, cliff_top], [0, 0], color=CREAM, alpha=0.6)
    
    # Water surface
    ax2.plot([cliff_x, 9.5], [0, 0], color=DEEP["blue"], lw=2)
    
    # Observer on cliff
    c_obs_x = 1.4
    c_obs_y = cliff_top
    draw_stick_figure(ax2, c_obs_x, c_obs_y, height=person_h)
    c_eye_x, c_eye_y = c_obs_x, c_obs_y + person_h * 0.88
    
    # Boat
    boat_x, boat_y = 7.5, 0.0
    draw_boat(ax2, boat_x, boat_y, scale=0.6)
    boat_target_x, boat_target_y = boat_x, boat_y + 0.3
    
    # Small water ripples well below the text/ground line (y = -0.55)
    for wx in [6.8, 7.8, 8.6]:
        ax2.plot([wx, wx + 0.4], [-0.55, -0.55], color=DEEP["blue"], lw=1.5)
    
    # Horizontal line from observer's eye
    ax2.plot([c_eye_x, 8.5], [c_eye_y, c_eye_y], color=INK, ls='--', lw=2)
    ax2.text(c_eye_x + 3.2, c_eye_y + 0.35, "Horizontal line of sight", fontsize=14, ha='center', color=INK,
             bbox=dict(fc='white', ec='none', pad=2))
    
    # Line of sight to boat
    ax2.plot([c_eye_x, boat_target_x], [c_eye_y, boat_target_y], color=DEEP["orange"], lw=2.5)
    
    # Secondary horizontal line at boat level
    ax2.plot([boat_target_x - 4.5, boat_target_x + 1.2], [boat_target_y, boat_target_y], 
             color=INK, ls='--', lw=2)
    ax2.text(boat_target_x - 2.5, boat_target_y - 0.42, "Horizontal line at boat level", 
             fontsize=14, ha='center', color=INK,
             bbox=dict(fc='white', ec='none', pad=2))
    
    # Angle calculation
    dx = boat_target_x - c_eye_x
    dy = c_eye_y - boat_target_y
    dep_rad = np.arctan2(dy, dx)
    dep_deg = np.degrees(dep_rad)
    
    # Depression arc at top
    arc2 = Arc((c_eye_x, c_eye_y), 3.0, 3.0, angle=0, theta1=-dep_deg, theta2=0, 
               color=DEEP["pink"], lw=2.5)
    ax2.add_patch(arc2)
    
    lx2 = c_eye_x + 2.3 * np.cos(-dep_rad / 2.0)
    ly2 = c_eye_y + 2.3 * np.sin(-dep_rad / 2.0)
    ax2.text(lx2 + 0.2, ly2 - 0.15, "Angle of\ndepression", fontsize=15, 
             color=DEEP["pink"], fontweight='bold', va='center')
    
    # Alternate angle arc at boat
    arc3 = Arc((boat_target_x, boat_target_y), 3.0, 3.0, angle=0, theta1=180 - dep_deg, theta2=180, 
               color=DEEP["pink"], lw=2.5)
    ax2.add_patch(arc3)
    
    lx3 = boat_target_x - 2.3 * np.cos(dep_rad / 2.0)
    ly3 = boat_target_y + 2.3 * np.sin(dep_rad / 2.0)
    ax2.text(lx3 - 0.2, ly3 - 0.1, "Alternate\nangle", fontsize=14, 
             color=DEEP["pink"], ha='right', va='center',
             bbox=dict(fc='white', ec='none', pad=2))
    
    ax2.text(c_obs_x, c_eye_y + 0.5, "Observer", fontsize=14, ha='center', color=INK)
    ax2.text(boat_x, boat_y + 0.9, "Boat", fontsize=14, ha='center', color=INK)
    ax2.set_title("Angle of Depression", fontsize=18, pad=20, fontweight='bold', color=INK)
    
    save(fig, out)
