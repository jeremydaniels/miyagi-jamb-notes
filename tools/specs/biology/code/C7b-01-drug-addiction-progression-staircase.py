from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    # Canvas size: wide and adequately high
    fig = canvas(12, 7.5)
    ax = fig.add_axes([0.05, 0.06, 0.9, 0.88])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Title
    ax.text(6.0, 8.1, "Progression from First Use to Addiction", 
            fontsize=17, fontweight='bold', ha='center', va='center', color=INK)

    # 5 steps parameters
    step_w = 1.7
    step_xs = [0.6, 2.45, 4.3, 6.15, 8.0]
    # Steeper riser heights to separate steps cleanly
    step_heights = [1.2, 2.1, 3.0, 3.9, 4.8]
    step_colors = [GREEN, BLUE, CREAM, ORANGE, PINK]
    edge_colors = [DEEP["green"], DEEP["blue"], GREY, DEEP["orange"], DEEP["pink"]]

    # Labels and descriptions per description:
    # 1: "Experimental use", young person being offered a substance by a friend
    # 2: "Occasional use", party scene
    # 3: "Regular use", person alone using a substance
    # 4: "Tolerance" / "Tolerance: needs more", person taking a larger amount
    # 5: "Dependence and addiction", person looking distressed and shaking
    stage_titles = [
        "Experimental use",
        "Occasional use",
        "Regular use",
        "Tolerance",
        "Dependence and addiction"
    ]
    
    stage_subtitles = [
        "Offered by a friend",
        "Social / party scene",
        "Using alone regularly",
        "Tolerance: needs more",
        "Distress & shaking"
    ]

    # Draw staircase blocks
    for i in range(5):
        x = step_xs[i]
        h = step_heights[i]
        c = step_colors[i]
        ec = edge_colors[i]
        
        # Solid filled block from baseline (y=0.7) to step height
        rect = patches.Rectangle((x, 0.7), step_w, h - 0.7, 
                                 facecolor=c, edgecolor=ec, linewidth=2.0, zorder=2)
        ax.add_patch(rect)
        
        # Step number inside the block
        ax.text(x + step_w/2, 0.7 + (h - 0.7)/2, f"Step {i+1}", 
                fontsize=12, fontweight='bold', ha='center', va='center', color=INK, zorder=3)

    # Helper function for stick figures
    def draw_stick_figure(cx, cy, scale=0.75, distressed=False, offering=False, receiving=False, holding=False):
        # cy is base/feet level
        head_r = 0.12 * scale
        head_cy = cy + 0.85 * scale
        head = patches.Circle((cx, head_cy), head_r, facecolor=INK, edgecolor=INK, zorder=4)
        ax.add_patch(head)
        
        torso_top = head_cy - head_r
        torso_bot = cy + 0.35 * scale
        ax.plot([cx, cx], [torso_top, torso_bot], color=INK, lw=2.2, zorder=4)
        
        # Legs
        ax.plot([cx, cx - 0.12 * scale], [torso_bot, cy], color=INK, lw=2.0, zorder=4)
        ax.plot([cx, cx + 0.12 * scale], [torso_bot, cy], color=INK, lw=2.0, zorder=4)
        
        arm_y = torso_top - 0.1 * scale
        if distressed:
            # Hands clutching head, trembling posture
            ax.plot([cx, cx - 0.16 * scale, cx - 0.1 * scale], 
                    [arm_y, arm_y + 0.18 * scale, head_cy], color=INK, lw=2.0, zorder=4)
            ax.plot([cx, cx + 0.16 * scale, cx + 0.1 * scale], 
                    [arm_y, arm_y + 0.18 * scale, head_cy], color=INK, lw=2.0, zorder=4)
        elif offering:
            # Reaching out with hand holding item
            ax.plot([cx, cx + 0.22 * scale], [arm_y, arm_y + 0.05 * scale], color=INK, lw=2.0, zorder=4)
            ax.plot([cx, cx - 0.12 * scale], [arm_y, arm_y - 0.12 * scale], color=INK, lw=2.0, zorder=4)
            # Item
            ax.scatter([cx + 0.24 * scale], [arm_y + 0.05 * scale], s=25, color=DEEP["green"], zorder=5)
        elif receiving:
            # Hand extended forward to receive
            ax.plot([cx, cx - 0.2 * scale], [arm_y, arm_y + 0.02 * scale], color=INK, lw=2.0, zorder=4)
            ax.plot([cx, cx + 0.12 * scale], [arm_y, arm_y - 0.12 * scale], color=INK, lw=2.0, zorder=4)
        elif holding:
            # Hand holding container/glass/substance
            ax.plot([cx, cx + 0.18 * scale], [arm_y, arm_y - 0.02 * scale], color=INK, lw=2.0, zorder=4)
            ax.plot([cx, cx - 0.12 * scale], [arm_y, arm_y - 0.15 * scale], color=INK, lw=2.0, zorder=4)
            # larger container / dose
            rect_dose = patches.Rectangle((cx + 0.16 * scale, arm_y - 0.08 * scale), 0.1 * scale, 0.18 * scale, 
                                          facecolor=DEEP["orange"], edgecolor=INK, lw=1.2, zorder=5)
            ax.add_patch(rect_dose)
        else:
            # Relaxed arms
            ax.plot([cx - 0.12 * scale, cx, cx + 0.12 * scale], 
                    [arm_y - 0.15 * scale, arm_y, arm_y - 0.15 * scale], color=INK, lw=2.0, zorder=4)

    # Illustrations placed directly standing on each step tread:
    # Tread y = step_heights[i] + 0.05
    # Step 1: Young person offered substance by friend
    s1_base = step_heights[0] + 0.05
    draw_stick_figure(step_xs[0] + 0.55, s1_base, scale=0.75, offering=True)
    draw_stick_figure(step_xs[0] + 1.15, s1_base, scale=0.75, receiving=True)

    # Step 2: Party scene (two figures, musical note, festive)
    s2_base = step_heights[1] + 0.05
    draw_stick_figure(step_xs[1] + 0.6, s2_base, scale=0.75)
    draw_stick_figure(step_xs[1] + 1.15, s2_base, scale=0.75)
    ax.text(step_xs[1] + 0.88, s2_base + 0.82, "♫", fontsize=15, color=DEEP["blue"], ha='center', va='bottom')

    # Step 3: Person alone using a substance
    s3_base = step_heights[2] + 0.05
    draw_stick_figure(step_xs[2] + 0.85, s3_base, scale=0.75)
    # Cup / item on table beside them
    ax.plot([step_xs[2] + 1.25, step_xs[2] + 1.55], [s3_base + 0.35, s3_base + 0.35], color=INK, lw=1.5)
    ax.plot([step_xs[2] + 1.4, step_xs[2] + 1.4], [s3_base, s3_base + 0.35], color=INK, lw=1.5)
    ax.scatter([step_xs[2] + 1.4], [s3_base + 0.42], s=20, color=INK, zorder=4)

    # Step 4: Person taking a larger amount ("Tolerance: needs more")
    s4_base = step_heights[3] + 0.05
    draw_stick_figure(step_xs[3] + 0.75, s4_base, scale=0.75, holding=True)
    # Arrow indicating larger / increased amount
    ax.annotate("+ dose", xy=(step_xs[3] + 1.35, s4_base + 0.6), xytext=(step_xs[3] + 1.35, s4_base + 0.2),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.0),
                fontsize=11, fontweight='bold', color=DEEP["orange"], ha='center', va='bottom')

    # Step 5: Distressed and shaking
    s5_base = step_heights[4] + 0.05
    draw_stick_figure(step_xs[4] + 0.85, s5_base, scale=0.75, distressed=True)
    # Shiver / vibration waves
    for y_vib in [s5_base + 0.3, s5_base + 0.55, s5_base + 0.75]:
        ax.plot([step_xs[4] + 0.45, step_xs[4] + 0.48, step_xs[4] + 0.45], 
                [y_vib - 0.06, y_vib, y_vib + 0.06], color=DEEP["pink"], lw=1.6)
        ax.plot([step_xs[4] + 1.25, step_xs[4] + 1.22, step_xs[4] + 1.25], 
                [y_vib - 0.06, y_vib, y_vib + 0.06], color=DEEP["pink"], lw=1.6)

    # Text labels: Place firmly ABOVE the figures on each step so they never overlap
    # Figures stand up to h + 0.85. Labels placed at h + 1.05 and h + 1.45.
    for i in range(5):
        h = step_heights[i]
        cx = step_xs[i] + step_w / 2
        ec = edge_colors[i]
        
        # Sub-explanation text
        ax.text(cx, h + 1.05, stage_subtitles[i], 
                fontsize=10.5, ha='center', va='bottom', color=INK, style='italic', zorder=5)

        # Primary title box
        ax.text(cx, h + 1.45, stage_titles[i], 
                fontsize=11.5, fontweight='bold', ha='center', va='bottom', color=INK,
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=ec, lw=1.5), zorder=6)

    # Bottom Progression Arrow spanning steps 1 to 5
    ax.annotate("", xy=(9.7, 0.4), xytext=(0.6, 0.4),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.2))
    ax.text(5.15, 0.15, "Progression of dependency and loss of control", 
            fontsize=12, ha='center', va='center', color=INK, fontweight='semibold')

    # Side panel: Withdrawal symptoms when stopped
    panel_x = 10.05
    panel_y = 1.4
    panel_w = 1.65
    panel_h = 4.8
    
    panel_rect = patches.FancyBboxPatch((panel_x, panel_y), panel_w, panel_h,
                                        boxstyle="round,pad=0.15",
                                        facecolor=CREAM, edgecolor=GREY, lw=1.5, zorder=2)
    ax.add_patch(panel_rect)

    # Heading inside panel
    ax.text(panel_x + panel_w/2, panel_y + panel_h - 0.35, "Withdrawal\nsymptoms", 
            fontsize=12, fontweight='bold', ha='center', va='top', color=INK, zorder=4)

    # Down arrow labelled "Withdrawal symptoms when stopped"
    arrow_top_y = panel_y + panel_h - 1.2
    arrow_bot_y = panel_y + 1.2
    ax.annotate("", xy=(panel_x + panel_w/2, arrow_bot_y), xytext=(panel_x + panel_w/2, arrow_top_y),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=3.5, mutation_scale=18), zorder=4)

    # Arrow text
    ax.text(panel_x + panel_w/2, (arrow_top_y + arrow_bot_y)/2, "when\nstopped", 
            fontsize=11, fontweight='bold', ha='center', va='center', color=DEEP["pink"],
            bbox=dict(boxstyle="square,pad=0.2", fc="white", ec=GREY, lw=0.8), zorder=5)

    # Panel note at bottom
    ax.text(panel_x + panel_w/2, panel_y + 0.45, "Severe physical &\npsychological\ndistress", 
            fontsize=10, ha='center', va='center', color=INK, zorder=4)

    # Dashed connection arrow from Step 5 to the Withdrawal panel
    ax.annotate("", xy=(panel_x, 4.6), xytext=(step_xs[4] + step_w, 4.8),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.8, linestyle="--"), zorder=5)

    save(fig, out)
