from style import *
import numpy as np
import matplotlib.pyplot as plt

def is_inside_seven(x, y):
    # Top horizontal bar of '7'
    # Centered around (0,0), radius of plate is ~1.0
    # Let 7 span x from -0.4 to 0.45, y from -0.55 to 0.55
    # Top bar: x in [-0.35, 0.42], y in [0.32, 0.52]
    in_top_bar = (-0.35 <= x <= 0.42) and (0.32 <= y <= 0.52)
    
    # Slanted stem: from (0.35, 0.42) down to (-0.18, -0.52)
    # Line equation: x - x0 = (x1 - x0)/(y1 - y0) * (y - y0)
    # y ranges from -0.52 to 0.42
    # center x at y: x_c = 0.35 + (0.35 - (-0.18))/(0.42 - (-0.52)) * (y - 0.42)
    # x_c = 0.35 + (0.53 / 0.94) * (y - 0.42) = 0.35 + 0.5638 * (y - 0.42)
    in_stem = False
    if -0.52 <= y <= 0.42:
        xc = 0.35 + 0.5638 * (y - 0.42)
        if abs(x - xc) <= 0.12:
            in_stem = True
            
    # Small downward serif on the left of top bar
    in_serif = (-0.35 <= x <= -0.22) and (0.22 <= y <= 0.40)
    
    return in_top_bar or in_stem or in_serif

def draw(out):
    fig = canvas(12, 6.8)
    
    # Create two subplots side by side
    ax1 = fig.add_axes([0.06, 0.12, 0.42, 0.74])
    ax2 = fig.add_axes([0.52, 0.12, 0.42, 0.74])
    
    for ax in (ax1, ax2):
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_xlim(-1.25, 1.25)
        ax.set_ylim(-1.25, 1.25)
        
    # Generate pseudorandom dots inside circle of radius 1.0 using dart throwing
    np.random.seed(42)
    dots = []  # list of (x, y, r, is_7)
    
    # We want ~550 dots
    attempts = 0
    max_attempts = 15000
    r_plate = 1.0
    
    while attempts < max_attempts and len(dots) < 520:
        attempts += 1
        # Random position in circle
        theta = np.random.uniform(0, 2 * np.pi)
        rad = np.sqrt(np.random.uniform(0, 1)) * (r_plate - 0.04)
        x = rad * np.cos(theta)
        y = rad * np.sin(theta)
        
        # Determine dot radius
        r = np.random.uniform(0.026, 0.062)
        
        # Check collision with existing dots
        collision = False
        for (ex, ey, er, _) in dots:
            dist = np.hypot(x - ex, y - ey)
            if dist < (r + er + 0.008):
                collision = True
                break
        if not collision:
            in_7 = is_inside_seven(x, y)
            dots.append((x, y, r, in_7))
            
    # Colour palettes
    # Normal vision:
    # 7 is soft orange-reds:
    orange_shades = [
        '#E76F51', '#F4A261', '#E65C40', '#EE8255', '#D95338', '#F28E2B'
    ]
    # Background is soft greens:
    green_shades = [
        '#7FB069', '#8EBA77', '#A3C985', '#6A9955', '#588157', '#8BB174', '#95C179'
    ]
    
    # Red-green colour blind vision:
    # Both orange-red and green collapse to similar muddy olive-brown / mustard-khaki tones
    # Subtle variations in olive brown so the plate looks realistic but number is invisible
    cb_olive_shades = [
        '#A19562', '#8F8552', '#998D5A', '#AAA06F', '#B3A877', '#877B4A', '#9B905E', '#A69B67'
    ]
    
    # Draw dots on ax1 (Normal colour vision)
    for i, (x, y, r, in_7) in enumerate(dots):
        if in_7:
            c = orange_shades[i % len(orange_shades)]
        else:
            c = green_shades[i % len(green_shades)]
        circle = plt.Circle((x, y), r, color=c, ec='none')
        ax1.add_patch(circle)
        
    # Draw dots on ax2 (Red-green colour blindness)
    # Notice: we don't distinguish in_7, both get assigned from cb_olive_shades
    for i, (x, y, r, in_7) in enumerate(dots):
        c = cb_olive_shades[(i * 3 + 7) % len(cb_olive_shades)]
        circle = plt.Circle((x, y), r, color=c, ec='none')
        ax2.add_patch(circle)
        
    # Plate background subtle borders
    for ax in (ax1, ax2):
        rim = plt.Circle((0, 0), r_plate + 0.015, color=GREY, fill=False, lw=1.5, ls=':')
        ax.add_patch(rim)

    # Labels and annotations
    # Titles above each plate
    ax1.text(0, 1.15, "Normal colour vision", fontsize=15, ha='center', va='bottom', weight='bold', color=INK)
    ax2.text(0, 1.15, "Red-green colour blindness", fontsize=15, ha='center', va='bottom', weight='bold', color=INK)
    
    # Subtitles / annotations below plates
    ax1.text(0, -1.18, "Number 7 clearly visible", fontsize=13, ha='center', va='top', color=INK)
    ax2.text(0, -1.18, "Number hidden (muddy olive-brown)", fontsize=13, ha='center', va='top', color=INK)
    
    # Add an annotation pointing to the hidden area on the right plate
    ax2.annotate("number hidden", xy=(0.12, 0.05), xytext=(0.48, -0.65),
                 fontsize=12, color=INK, ha='center',
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5, shrinkB=6),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"))
                 
    save(fig, out)
