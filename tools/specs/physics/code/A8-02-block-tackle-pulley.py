from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    # Canvas with plenty of width so annotations don't overlap the pulley assembly
    fig = canvas(9.0, 10.0)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 13)
    ax.set_aspect('equal')
    ax.axis('off')

    # Palette and styling constants
    rope_color = DEEP["orange"]
    rw = 3.0

    # Ceiling / Support at top
    ceiling_y = 12.0
    ax.plot([3.5, 9.0], [ceiling_y, ceiling_y], color=INK, lw=3.5)
    for hx in np.linspace(3.7, 8.8, 14):
        ax.plot([hx, hx + 0.3], [ceiling_y, ceiling_y + 0.3], color=GREY, lw=1.5)

    # Pulley block centers
    U_cx, U_cy = 6.0, 9.8    # Upper block center
    L_cx, L_cy = 6.0, 5.6    # Lower block center

    # Pulley radii (concentric sheaves)
    R_out = 1.2
    R_in = 0.6

    # 4 vertical supporting rope segment x-coordinates
    x1 = U_cx - R_out    # 4.8 (outer left)
    x2 = U_cx - R_in     # 5.4 (inner left)
    x3 = U_cx + R_in     # 6.6 (inner right)
    x4 = U_cx + R_out    # 7.2 (outer right)

    # Ceiling attachment bracket
    ax.plot([U_cx, U_cx], [ceiling_y, U_cy + R_out + 0.1], color=INK, lw=3)

    # Upper and Lower block frames (drawn behind pulleys)
    up_frame = patches.FancyBboxPatch((U_cx - 0.5, U_cy - 1.4), 1.0, 2.8,
                                     boxstyle="round,pad=0.15",
                                     facecolor=CREAM, edgecolor=INK, lw=2, zorder=2)
    ax.add_patch(up_frame)

    low_frame = patches.FancyBboxPatch((L_cx - 0.5, L_cy - 1.4), 1.0, 2.8,
                                      boxstyle="round,pad=0.15",
                                      facecolor=CREAM, edgecolor=INK, lw=2, zorder=2)
    ax.add_patch(low_frame)

    # Upper Pulleys (fixed)
    ax.add_patch(patches.Circle((U_cx, U_cy), R_out, facecolor=BLUE, edgecolor=INK, lw=2, zorder=3))
    ax.add_patch(patches.Circle((U_cx, U_cy), R_in, facecolor=LAV, edgecolor=INK, lw=2, zorder=4))
    ax.plot(U_cx, U_cy, marker='o', color=INK, markersize=5, zorder=6)

    # Lower Pulleys (movable)
    ax.add_patch(patches.Circle((L_cx, L_cy), R_out, facecolor=BLUE, edgecolor=INK, lw=2, zorder=3))
    ax.add_patch(patches.Circle((L_cx, L_cy), R_in, facecolor=LAV, edgecolor=INK, lw=2, zorder=4))
    ax.plot(L_cx, L_cy, marker='o', color=INK, markersize=5, zorder=6)

    # --- Continuous Rope Threading ---
    anchor_y = U_cy - 1.4
    
    # Anchor bracket extending from central frame to inner right rope (x3)
    ax.plot([U_cx, x3], [anchor_y, anchor_y], color=INK, lw=3, zorder=6)
    ax.plot([x3], [anchor_y], marker='o', color=INK, markersize=6, zorder=7)

    # Segment 1: Anchor down to lower inner right (x3)
    ax.plot([x3, x3], [anchor_y, L_cy], color=rope_color, lw=rw, zorder=5)

    # Arc 1: Under lower inner pulley (from x3 to x2)
    t1 = np.linspace(0, -np.pi, 50)
    ax.plot(L_cx + R_in * np.cos(t1), L_cy + R_in * np.sin(t1), color=rope_color, lw=rw, zorder=5)

    # Segment 2: Lower inner left (x2) up to upper inner left (x2)
    ax.plot([x2, x2], [L_cy, U_cy], color=rope_color, lw=rw, zorder=5)

    # Arc 2: Over upper inner-to-outer transition (from x2 to x4)
    t2 = np.linspace(np.pi, 0, 50)
    ax.plot(6.3 + 0.9 * np.cos(t2), U_cy + 0.9 * np.sin(t2), color=rope_color, lw=rw, zorder=5)

    # Segment 3: Upper outer right (x4) down to lower outer right (x4)
    ax.plot([x4, x4], [U_cy, L_cy], color=rope_color, lw=rw, zorder=5)

    # Arc 3: Under lower outer pulley (from x4 to x1)
    t3 = np.linspace(0, -np.pi, 50)
    ax.plot(L_cx + R_out * np.cos(t3), L_cy + R_out * np.sin(t3), color=rope_color, lw=rw, zorder=5)

    # Segment 4: Lower outer left (x1) up to upper outer left (x1)
    ax.plot([x1, x1], [L_cy, U_cy], color=rope_color, lw=rw, zorder=5)

    # Arc 4: Over upper outer to effort line (from x1 to x_E)
    x_E = 7.8
    t4 = np.linspace(np.pi, 0, 50)
    ax.plot(6.3 + 1.5 * np.cos(t4), U_cy + 1.5 * np.sin(t4), color=rope_color, lw=rw, zorder=5)

    # Effort Line: Straight down from x_E
    ax.plot([x_E, x_E], [U_cy, 3.4], color=rope_color, lw=rw, zorder=5)

    # Effort Arrow
    ax.annotate("", xy=(x_E, 1.8), xytext=(x_E, 3.4),
                arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.7",
                                color=DEEP["orange"], lw=3.5))
    ax.text(x_E + 0.35, 2.5, "Effort (E)", fontsize=16, fontweight='bold',
            color=INK, va='center')

    # Numbered badges on the 4 vertical rope segments
    strands = [x1, x2, x3, x4]
    for idx, sx in enumerate(strands, 1):
        ax.text(sx, 7.6, f"{idx}", fontsize=14, color=DEEP["blue"], ha="center", va="center",
                fontweight='bold',
                bbox=dict(boxstyle="circle,pad=0.2", fc="white", ec=DEEP["blue"], lw=1.3),
                zorder=8)

    # Hook and Load
    hook_top_y = L_cy - 1.4
    ax.plot([L_cx, L_cx], [hook_top_y, hook_top_y - 0.6], color=INK, lw=3)
    hook_arc = np.linspace(-np.pi / 2, np.pi, 30)
    ax.plot(L_cx - 0.15 + 0.2 * np.cos(hook_arc),
            hook_top_y - 0.8 + 0.2 * np.sin(hook_arc),
            color=INK, lw=3)

    # Heavy Crate (Load)
    crate_w, crate_h = 2.8, 2.0
    crate_x = L_cx - crate_w / 2.0
    crate_y = 0.8

    # Slings from hook to crate
    ax.plot([L_cx, crate_x + 0.4], [hook_top_y - 0.8, crate_y + crate_h], color=GREY, lw=2)
    ax.plot([L_cx, crate_x + crate_w - 0.4], [hook_top_y - 0.8, crate_y + crate_h], color=GREY, lw=2)

    # Crate body
    crate = patches.Rectangle((crate_x, crate_y), crate_w, crate_h,
                              facecolor=CREAM, edgecolor=INK, lw=2.5, zorder=3)
    ax.add_patch(crate)
    ax.plot([crate_x, crate_x + crate_w], [crate_y, crate_y + crate_h], color=GREY, lw=1.5, zorder=4)
    ax.plot([crate_x, crate_x + crate_w], [crate_y + crate_h, crate_y], color=GREY, lw=1.5, zorder=4)

    # Crate label
    ax.text(L_cx, crate_y + crate_h / 2.0, "Load (L)", fontsize=16, fontweight='bold',
            color=INK, ha='center', va='center', zorder=5,
            bbox=dict(fc="white", ec=INK, boxstyle="round,pad=0.35", lw=1.5))

    # --- Labels & Callouts (positioned safely to avoid overlaps) ---
    # Fixed block label (top-left)
    ax.annotate("Two fixed pulleys\n(Upper block)",
                xy=(U_cx - R_out - 0.1, U_cy + 0.2), xytext=(1.8, 10.6),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=GREY))

    # 4 supporting segments callout (middle-left, cleanly spaced)
    ax.annotate("4 vertical rope segments\nsupporting movable block",
                xy=(x1 - 0.1, 7.6), xytext=(1.8, 7.6),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.5),
                bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=DEEP["blue"], lw=1.3))

    # Movable block label (bottom-left)
    ax.annotate("Two movable pulleys\n(Lower block)",
                xy=(L_cx - R_out - 0.1, L_cy), xytext=(1.8, 4.6),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=GREY))

    save(fig, out)
