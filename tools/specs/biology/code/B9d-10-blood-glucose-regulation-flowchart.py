from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 12)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # Title
    ax.text(50, 96.5, "Control of Blood Glucose Concentration", 
            ha="center", va="center", fontsize=18, weight="bold", color=INK)

    # Central Bar: Normal Blood Glucose
    bar_width, bar_height = 42, 6
    rect = patches.FancyBboxPatch((50 - bar_width/2, 50 - bar_height/2), bar_width, bar_height,
                                  boxstyle="round,pad=0.5", fc=CREAM, ec=DEEP["green"], lw=2.5, zorder=5)
    ax.add_patch(rect)
    ax.text(50, 50, "Normal blood glucose", ha="center", va="center", fontsize=16, weight="bold", color=INK, zorder=6)

    # Helper function for text boxes
    def draw_box(x, y, w, h, bg_color, border_color, title_text, sub_text=None, title_size=15, sub_size=14, zorder=5):
        box = patches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                                     boxstyle="round,pad=0.6", fc=bg_color, ec=border_color, lw=2, zorder=zorder)
        ax.add_patch(box)
        if sub_text:
            ax.text(x, y + 1.2, title_text, ha="center", va="center", fontsize=title_size, weight="bold", color=INK, zorder=zorder+1)
            ax.text(x, y - 1.5, sub_text, ha="center", va="center", fontsize=sub_size, color=INK, zorder=zorder+1)
        else:
            ax.text(x, y, title_text, ha="center", va="center", fontsize=title_size, weight="bold", color=INK, zorder=zorder+1)

    # ----------------- UPPER LOOP (ORANGE / HIGH GLUCOSE) -----------------
    # Step 1: Rise after meal (Top-Left)
    draw_box(24, 76, 28, 8, ORANGE, DEEP["orange"], "Blood glucose rises", "(after a meal)")
    # Food / Meal Icon (Plate of rice)
    plate = patches.Ellipse((24, 85), 8, 2.5, fc=GREY, ec=INK, lw=1.5, zorder=5)
    mound = patches.Arc((24, 85), 6, 4, angle=0, theta1=0, theta2=180, color=INK, lw=2, zorder=6)
    ax.add_patch(plate)
    ax.add_patch(mound)
    ax.text(24, 86, "• • •", ha="center", va="center", fontsize=14, color=INK, zorder=7)

    # Step 2: Pancreas releases insulin (Top)
    draw_box(50, 89, 28, 8.5, LAV, DEEP["lav"], "Pancreas: beta cells", "release insulin")
    # Insulin dots (purple)
    np.random.seed(42)
    for dx, dy in [(-8, -5.5), (-4, -5.8), (0, -6), (4, -5.8), (8, -5.5)]:
        dot = patches.Circle((50 + dx, 89 + dy), 0.6, fc=DEEP["lav"], ec="none", zorder=7)
        ax.add_patch(dot)

    # Step 3: Liver and muscles store glycogen (Top-Right)
    draw_box(76, 76, 31, 8.5, ORANGE, DEEP["orange"], "Liver and muscles store", "glucose as glycogen")
    ax.text(76, 68, "Cells take up glucose", ha="center", va="center", fontsize=14, 
            style="italic", color=INK, bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", lw=1), zorder=6)

    # Upper Flow Arrows
    arrow_kw_orange = dict(arrowstyle="->,head_length=0.8,head_width=0.5", lw=3, color=DEEP["orange"])
    # 1. From normal up to 'rises'
    ax.annotate("", xy=(24, 71.5), xytext=(35, 53.5), arrowprops=dict(connectionstyle="arc3,rad=-0.15", **arrow_kw_orange))
    # 2. From 'rises' to 'pancreas'
    ax.annotate("", xy=(36, 89), xytext=(24, 80.5), arrowprops=dict(connectionstyle="arc3,rad=-0.2", **arrow_kw_orange))
    # 3. From 'pancreas' to 'storage'
    ax.annotate("", xy=(76, 80.5), xytext=(64, 89), arrowprops=dict(connectionstyle="arc3,rad=-0.2", **arrow_kw_orange))
    # 4. From 'storage' down to normal
    ax.annotate("", xy=(65, 53.5), xytext=(76, 64.5), arrowprops=dict(connectionstyle="arc3,rad=-0.15", **arrow_kw_orange))

    # ----------------- LOWER LOOP (BLUE / LOW GLUCOSE) -----------------
    # Step 1: Fall after exercise/fasting (Bottom-Left)
    draw_box(24, 24, 30, 8, BLUE, DEEP["blue"], "Blood glucose falls", "(exercise or fasting)")
    # Runner icon above/beside
    # Head
    ax.add_patch(patches.Circle((24, 15), 1.0, fc=INK, ec=INK, zorder=5))
    # Body & limbs (stick figure)
    ax.plot([24, 23.5], [14, 11], color=INK, lw=2.2, zorder=5) # torso
    ax.plot([23.5, 25.5, 27], [13.2, 12.5, 13.5], color=INK, lw=2.0, zorder=5) # right arm
    ax.plot([23.5, 21.5, 20.5], [13.2, 12, 11], color=INK, lw=2.0, zorder=5) # left arm
    ax.plot([23.5, 25, 26], [11, 9.5, 7.5], color=INK, lw=2.2, zorder=5) # right leg
    ax.plot([23.5, 21.5, 20.5], [11, 10, 8.5], color=INK, lw=2.2, zorder=5) # left leg

    # Step 2: Pancreas releases glucagon (Bottom)
    draw_box(50, 11, 28, 8.5, GREEN, DEEP["green"], "Pancreas: alpha cells", "release glucagon")
    # Glucagon dots (green)
    for dx, dy in [(-8, 5.5), (-4, 5.8), (0, 6), (4, 5.8), (8, 5.5)]:
        dot = patches.Circle((50 + dx, 11 + dy), 0.6, fc=DEEP["green"], ec="none", zorder=7)
        ax.add_patch(dot)

    # Step 3: Liver changes glycogen to glucose (Bottom-Right)
    draw_box(76, 24, 30, 8.5, BLUE, DEEP["blue"], "Liver changes glycogen", "to glucose")

    # Lower Flow Arrows
    arrow_kw_blue = dict(arrowstyle="->,head_length=0.8,head_width=0.5", lw=3, color=DEEP["blue"])
    # 1. From normal down to 'falls'
    ax.annotate("", xy=(24, 28.5), xytext=(35, 46.5), arrowprops=dict(connectionstyle="arc3,rad=0.15", **arrow_kw_blue))
    # 2. From 'falls' to 'pancreas'
    ax.annotate("", xy=(36, 11), xytext=(24, 19.5), arrowprops=dict(connectionstyle="arc3,rad=0.2", **arrow_kw_blue))
    # 3. From 'pancreas' to 'liver glycogen'
    ax.annotate("", xy=(76, 19.5), xytext=(64, 11), arrowprops=dict(connectionstyle="arc3,rad=0.2", **arrow_kw_blue))
    # 4. From 'liver glycogen' up to normal
    ax.annotate("", xy=(65, 46.5), xytext=(76, 28.5), arrowprops=dict(connectionstyle="arc3,rad=0.15", **arrow_kw_blue))

    save(fig, out)
