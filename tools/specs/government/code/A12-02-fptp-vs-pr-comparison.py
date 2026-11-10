from style import *
import numpy as np
import matplotlib.patches as patches
import matplotlib.path as mpath

def draw(out):
    fig = canvas(15, 8.5)
    
    # Left: FPTP, Right: PR
    ax_left = fig.add_axes([0.05, 0.08, 0.42, 0.78])
    ax_right = fig.add_axes([0.53, 0.08, 0.44, 0.78])
    
    # ------------------ LEFT: FPTP ------------------
    ax_left.set_title("First-Past-The-Post: Winner takes all", fontsize=16, color=INK, pad=18, weight="bold")
    ax_left.set_xlim(-0.5, 3.8)
    ax_left.set_ylim(0, 115)
    ax_left.set_ylabel("Vote share (%)", fontsize=14, color=INK)
    ax_left.set_xticks([0.6, 1.6, 2.6])
    ax_left.set_xticklabels(["Party A\n40%", "Party B\n35%", "Party C\n25%"], fontsize=14, color=INK)
    ax_left.spines['top'].set_visible(False)
    ax_left.spines['right'].set_visible(False)
    ax_left.spines['left'].set_color(GREY)
    ax_left.spines['bottom'].set_color(GREY)
    ax_left.tick_params(colors=INK, labelsize=14)
    ax_left.set_yticks([0, 20, 40, 60, 80, 100])
    ax_left.grid(axis='y', linestyle='--', alpha=0.4, color=GREY)
    
    parties = [0.6, 1.6, 2.6]
    votes = [40, 35, 25]
    colors = [BLUE, PINK, GREEN]
    edge_colors = [DEEP["blue"], DEEP["pink"], DEEP["green"]]
    
    for x, v, c, ec in zip(parties, votes, colors, edge_colors):
        rect = patches.FancyBboxPatch((x - 0.35, 0), 0.7, v,
                                      boxstyle="round,pad=0.02,rounding_size=0.1",
                                      facecolor=c, edgecolor=ec, lw=2)
        ax_left.add_patch(rect)
    
    # Winner indicator above Party A
    ax_left.annotate("WINNER\n(Plurality)", xy=(0.6, 42), xytext=(0.6, 56),
                     fontsize=14, weight="bold", color=DEEP["blue"], ha="center",
                     arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2))
    
    # District seat box with Trophy
    seat_box = patches.FancyBboxPatch((1.6, 52), 1.9, 54,
                                      boxstyle="round,pad=0.05,rounding_size=0.2",
                                      facecolor=CREAM, edgecolor=ORANGE, lw=2.5)
    ax_left.add_patch(seat_box)
    
    ax_left.text(2.55, 100, "District Result:\nSingle Seat", fontsize=14, weight="bold",
                 color=INK, ha="center", va="top")
    
    # Trophy icon drawn at (2.55, 74)
    tx, ty = 2.55, 71
    # Cup
    cup = patches.Polygon([[tx-0.3, ty+8], [tx+0.3, ty+8], [tx+0.25, ty], [tx-0.25, ty]],
                          facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2)
    ax_left.add_patch(cup)
    # Handles
    h_left = patches.Arc((tx-0.3, ty+4.5), 0.35, 0.6, angle=0, theta1=90, theta2=270,
                         color=DEEP["orange"], lw=2.5)
    h_right = patches.Arc((tx+0.3, ty+4.5), 0.35, 0.6, angle=0, theta1=270, theta2=90,
                          color=DEEP["orange"], lw=2.5)
    ax_left.add_patch(h_left)
    ax_left.add_patch(h_right)
    # Stem & Base
    stem = patches.Rectangle((tx-0.08, ty-4), 0.16, 4, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.5)
    base = patches.Rectangle((tx-0.35, ty-7), 0.7, 3, facecolor=DEEP["orange"], edgecolor=INK, lw=1.5)
    ax_left.add_patch(stem)
    ax_left.add_patch(base)
    
    ax_left.text(2.55, 56, "100% of seats to Party A", fontsize=14, weight="bold",
                 color=DEEP["blue"], ha="center")
    
    # ------------------ RIGHT: PR ------------------
    ax_right.set_title("Proportional Representation: Seats match vote percentage",
                       fontsize=16, color=INK, pad=18, weight="bold")
    ax_right.axis('off')
    
    # Sub-axes for Pie Chart (votes) inside ax_right space
    # Positions relative to figure:
    pie_ax = fig.add_axes([0.52, 0.28, 0.22, 0.45])
    pie_ax.axis('off')
    
    pie_labels = ["Party A\n40%", "Party B\n35%", "Party C\n25%"]
    wedges, texts = pie_ax.pie([40, 35, 25], labels=pie_labels, startangle=90,
                               colors=[BLUE, PINK, GREEN],
                               wedgeprops=dict(edgecolor='white', linewidth=2.5),
                               textprops=dict(fontsize=14, color=INK, weight="bold"))
    pie_ax.set_title("Votes Share", fontsize=15, color=INK, weight="bold", y=-0.12)
    
    # Sub-axes for Parliament Chamber (seats)
    parl_ax = fig.add_axes([0.75, 0.22, 0.23, 0.55])
    parl_ax.axis('off')
    parl_ax.set_aspect('equal')
    
    # Generate semi-circular parliamentary seating arrangement (100 seats)
    n_seats = 100
    radii = [1.0, 1.25, 1.5, 1.75, 2.0]
    seats_per_ring = [12, 16, 20, 24, 28]  # Sum = 100
    
    seat_coords = []
    for r, n in zip(radii, seats_per_ring):
        angles = np.linspace(np.pi, 0, n + 2)[1:-1]  # Exclude extreme horizontal ends
        for theta in angles:
            seat_coords.append((r * np.cos(theta), r * np.sin(theta), theta))
            
    # Sort seats from left (pi) to right (0) by angle descending
    seat_coords.sort(key=lambda item: -item[2])
    
    # 40 Party A (Blue), 35 Party B (Red/Pink), 25 Party C (Green)
    seat_colors = [BLUE]*40 + [PINK]*35 + [GREEN]*25
    seat_edge_colors = [DEEP["blue"]]*40 + [DEEP["pink"]]*35 + [DEEP["green"]]*25
    
    for (x, y, _), c, ec in zip(seat_coords, seat_colors, seat_edge_colors):
        dot = patches.Circle((x, y), 0.08, facecolor=c, edgecolor=ec, lw=1.2)
        parl_ax.add_patch(dot)
        
    parl_ax.set_xlim(-2.3, 2.3)
    parl_ax.set_ylim(-0.4, 2.3)
    parl_ax.text(0, -0.25, "Parliament Seats (100)\n40 Blue / 35 Red / 25 Green",
                 fontsize=14, weight="bold", color=INK, ha="center")
    
    # Explanatory caption box at bottom of right side
    ax_right.text(0.5, 0.04, "Seats in Parliament directly reflect total votes received",
                  fontsize=14, ha="center", va="center", color=INK,
                  bbox=dict(boxstyle="round,pad=0.5", fc=CREAM, ec=GREY, lw=1.5))
    
    save(fig, out)
