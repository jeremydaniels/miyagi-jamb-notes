from style import *
import numpy as np
import matplotlib.patches as patches
import matplotlib.path as mpath

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Background landscape ground
    # Left ground (industrial area)
    ground_left = patches.Rectangle((0, 0), 45, 18, fc='#EAEAEA', ec=GREY, lw=1.5)
    ax.add_patch(ground_left)

    # Right ground (countryside / lake slope)
    ground_x = [45, 45, 62, 75, 88, 100, 100]
    ground_y = [0, 18, 18, 10, 10, 14, 0]
    ax.add_patch(patches.Polygon(list(zip(ground_x, ground_y)), fc=CREAM, ec=GREY, lw=1.5))

    # Lake on right
    lake_x = [62, 75, 88, 88, 62]
    lake_y = [18, 10, 10, 0, 0]
    ax.add_patch(patches.Polygon([[62, 18], [75, 10], [88, 10], [88, 0], [62, 0]], fc='#D4E6F1', ec='none'))
    ax.plot([62, 75, 88], [18, 10, 10], color=DEEP['blue'], lw=1.5)

    # --- LEFT SIDE: EMISSION SOURCES ---
    # 1. Factory
    # Building
    ax.add_patch(patches.Rectangle((4, 18), 12, 14, fc='#BDC3C7', ec=INK, lw=1.5))
    # Factory roof ridges
    ax.add_patch(patches.Polygon([[4, 32], [7, 36], [10, 32], [13, 36], [16, 32]], fc='#95A5A6', ec=INK, lw=1.5))
    # Factory windows
    for wx in [6, 9, 12]:
        for wy in [20, 25]:
            ax.add_patch(patches.Rectangle((wx, wy), 1.8, 2.5, fc='#FFFFFF', ec=INK, lw=1))
    # Tall Chimney
    chimney_pts = [[11, 32], [11.5, 46], [14.5, 46], [15, 32]]
    ax.add_patch(patches.Polygon(chimney_pts, fc='#7F8C8D', ec=INK, lw=1.5))
    ax.add_patch(patches.Ellipse((13, 46), 3, 0.8, fc='#34495E', ec=INK, lw=1))

    # 2. Gas flare
    ax.plot([21, 21], [18, 38], color=INK, lw=2.5) # stack
    ax.plot([19, 23], [18, 18], color=INK, lw=2.5) # base
    # Flare tip & flame
    ax.add_patch(patches.Polygon([[20, 38], [22, 38], [22.5, 40], [19.5, 40]], fc=GREY, ec=INK, lw=1))
    flame_pts = [[21, 40], [19.5, 43], [20.5, 46], [21, 48], [22.5, 45], [21.8, 42]]
    ax.add_patch(patches.Polygon(flame_pts, fc=ORANGE, ec=DEEP['orange'], lw=1.5))

    # 3. Car
    # Body
    car_body = patches.Polygon([[27, 21], [30, 24], [35, 24], [38, 21], [40, 21], [40, 19], [26, 19], [26, 21]], 
                               fc=PINK, ec=INK, lw=1.5)
    ax.add_patch(car_body)
    # Car wheels
    ax.add_patch(patches.Circle((29, 19), 1.8, fc='#333333', ec=INK, lw=1.5))
    ax.add_patch(patches.Circle((37, 19), 1.8, fc='#333333', ec=INK, lw=1.5))
    # Exhaust pipe
    ax.plot([26, 24.5], [19.5, 19.5], color=INK, lw=1.5)

    # --- EMISSIONS & RISING GASES ---
    # Grey rising arrows
    # From Chimney
    ax.annotate("", xy=(22, 58), xytext=(13, 47),
                arrowprops=dict(arrowstyle="->", color='#7F8C8D', lw=2.5, mutation_scale=15))
    # From Flare
    ax.annotate("", xy=(26, 58), xytext=(21.5, 48),
                arrowprops=dict(arrowstyle="->", color='#7F8C8D', lw=2.5, mutation_scale=15))
    # From Car
    ax.annotate("", xy=(30, 58), xytext=(24, 20),
                arrowprops=dict(arrowstyle="->", color='#7F8C8D', lw=2.5,
                                connectionstyle="arc3,rad=-0.2", mutation_scale=15))

    # Labels for pollutants
    ax.text(8, 60, "Sulphur (IV) oxide (SO2)", fontsize=11.5, color=INK, fontweight='semibold',
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3'))
    ax.text(25, 52, "Oxides of nitrogen (NOx)", fontsize=11.5, color=INK, fontweight='semibold',
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3'))

    # Curved transport arrows towards cloud
    ax.annotate("", xy=(46, 75), xytext=(27, 65),
                arrowprops=dict(arrowstyle="->", color=DEEP['orange'], lw=3,
                                connectionstyle="arc3,rad=0.15", mutation_scale=18))

    # --- CLOUDS ---
    def draw_cloud(center_x, center_y, scale):
        circles = [
            (center_x, center_y, 6.5 * scale),
            (center_x - 5 * scale, center_y - 1.5 * scale, 5 * scale),
            (center_x + 5 * scale, center_y - 1.5 * scale, 5.5 * scale),
            (center_x - 9 * scale, center_y - 3.5 * scale, 4 * scale),
            (center_x + 9 * scale, center_y - 3.5 * scale, 4.2 * scale),
            (center_x, center_y - 3.5 * scale, 6 * scale),
        ]
        for cx, cy, r in circles:
            ax.add_patch(patches.Circle((cx, cy), r, fc='#D6DBDF', ec='none', zorder=2))
        for cx, cy, r in circles:
            ax.add_patch(patches.Circle((cx, cy), r, fc='none', ec='#7F8C8D', lw=1.2, zorder=3))

    draw_cloud(58, 80, 1.1)

    # Cloud interior: small droplets & reaction label
    for dx, dy in [(52, 78), (54, 82), (57, 79), (61, 81), (63, 77)]:
        ax.add_patch(patches.Circle((dx, dy), 0.7, fc=DEEP['blue'], ec='none', zorder=4))

    ax.text(58, 87, "React with water in clouds", fontsize=12, color=INK, fontweight='bold', ha='center',
            bbox=dict(fc='white', ec=DEEP['orange'], boxstyle='round,pad=0.3', lw=1.5), zorder=5)

    ax.text(58, 72, "Sulphuric and nitric acids", fontsize=11.5, color=INK, ha='center', fontweight='semibold',
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25', lw=1), zorder=5)

    # --- ACID RAIN FALLING ---
    # Rain streaks on the right
    np.random.seed(42)
    for rx in np.linspace(62, 85, 12):
        for ry in np.linspace(50, 66, 4):
            offset = np.random.uniform(-1, 1)
            ax.plot([rx + offset, rx + offset - 2], [ry, ry - 3.5], color=DEEP['blue'], lw=1.8, zorder=2)

    ax.text(78, 58, "Acid rain", fontsize=14, color=DEEP['blue'], fontweight='bold', ha='center',
            bbox=dict(fc='white', ec=DEEP['blue'], boxstyle='round,pad=0.35', lw=1.5), zorder=5)

    # --- RIGHT SIDE: DAMAGE & IMPACTS ---

    # 1. Damaged Trees
    def draw_damaged_tree(x, y):
        # Trunk
        ax.plot([x, x], [y, y + 10], color='#5D4037', lw=3)
        # Bare / broken branches
        ax.plot([x, x - 3], [y + 6, y + 9], color='#5D4037', lw=2)
        ax.plot([x, x + 3.5], [y + 7, y + 10], color='#5D4037', lw=2)
        ax.plot([x, x - 2], [y + 8, y + 11], color='#5D4037', lw=1.8)
        ax.plot([x, x + 2], [y + 9, y + 12], color='#5D4037', lw=1.8)
        # Sparse yellowed leaves
        yellow_leaf = '#D4AC0D'
        ax.add_patch(patches.Ellipse((x - 3.2, y + 9.2), 1.2, 0.7, angle=30, fc=yellow_leaf, ec=INK, lw=0.5))
        ax.add_patch(patches.Ellipse((x + 3.7, y + 10.2), 1.2, 0.7, angle=-20, fc=yellow_leaf, ec=INK, lw=0.5))
        ax.add_patch(patches.Ellipse((x - 1, y + 11.5), 1.2, 0.7, angle=45, fc=yellow_leaf, ec=INK, lw=0.5))
        ax.add_patch(patches.Ellipse((x + 1.5, y + 8), 1.0, 0.6, angle=-10, fc=yellow_leaf, ec=INK, lw=0.5))

    draw_damaged_tree(50, 18)
    draw_damaged_tree(56, 18)
    ax.text(53, 33, "Damaged trees", fontsize=11.5, color=INK, ha='center', fontweight='semibold',
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25'))

    # 2. Acidic Lake with Dead Fish
    # Water surface styling
    ax.plot([65, 73], [8, 8], color=BLUE, lw=1.5)
    ax.plot([76, 85], [6, 6], color=BLUE, lw=1.5)

    def draw_dead_fish(fx, fy):
        # Belly up fish
        ax.add_patch(patches.Ellipse((fx, fy), 2.6, 1.2, fc='#FFFFFF', ec=INK, lw=1))
        ax.add_patch(patches.Polygon([[fx + 1.2, fy], [fx + 2.2, fy + 0.6], [fx + 2.2, fy - 0.6]], fc='#FFFFFF', ec=INK, lw=1))
        # Eye (cross for dead)
        ax.plot([fx - 0.9, fx - 0.5], [fy - 0.2, fy + 0.2], color=INK, lw=1)
        ax.plot([fx - 0.9, fx - 0.5], [fy + 0.2, fy - 0.2], color=INK, lw=1)

    draw_dead_fish(68, 6)
    draw_dead_fish(78, 4)
    draw_dead_fish(83, 7.5)

    ax.text(76, 1, "Dead fish in acidic lake", fontsize=11.5, color=INK, ha='center', fontweight='semibold',
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25'))

    # 3. House with Corroded Roof
    # House walls
    ax.add_patch(patches.Rectangle((88, 14), 7, 7, fc='#EAEDED', ec=INK, lw=1.5))
    # Corrugated rusted roof
    ax.add_patch(patches.Polygon([[87, 21], [91.5, 26], [96, 21]], fc='#B9770E', ec=INK, lw=1.5)) # Rust brown
    # Rust patches / corrugation lines
    ax.plot([89, 91.5], [21.5, 24.5], color='#784212', lw=1.5)
    ax.plot([91, 92.5], [21.2, 23], color='#784212', lw=1.5)
    ax.plot([93, 91.8], [21.5, 23.2], color='#641E16', lw=1.5)
    ax.plot([94.5, 92], [21.2, 24.5], color='#784212', lw=1.5)
    # Door and window
    ax.add_patch(patches.Rectangle((90.5, 14), 2, 4, fc='#BDC3C7', ec=INK, lw=1))

    ax.text(88, 28, "Corroded roof", fontsize=11.5, color=INK, ha='center', fontweight='semibold',
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25'))

    # 4. Eroded Stone Statue
    # Pedestal
    ax.add_patch(patches.Rectangle((96.5, 14), 2.8, 3, fc='#BDC3C7', ec=INK, lw=1.3))
    # Statue body & head (eroded, bumpy)
    statue_pts = [
        [97.2, 17], [96.8, 19], [97.0, 20.5], [97.2, 21.5],
        [97.0, 22.2], [97.4, 23.2], [98.2, 23.0], [98.6, 22.1],
        [98.3, 21.2], [98.7, 19.5], [98.5, 17]
    ]
    ax.add_patch(patches.Polygon(statue_pts, fc='#A6ACAF', ec=INK, lw=1.3))
    # Pit marks / erosion
    ax.plot([97.5, 97.7], [22, 22], color='#566573', lw=1.5)
    ax.plot([97.3, 97.6], [19, 19.2], color='#566573', lw=1.5)
    ax.plot([98.1, 98.3], [18, 18], color='#566573', lw=1.5)

    ax.text(97.5, 25, "Eroded stone", fontsize=11.5, color=INK, ha='center', fontweight='semibold',
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25'))

    # Overall diagram title
    ax.text(50, 95, "Formation and Effects of Acid Rain", fontsize=16, color=INK, fontweight='bold', ha='center')

    save(fig, out)
