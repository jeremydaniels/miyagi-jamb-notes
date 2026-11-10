from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 11)
    
    # 2 subplots: Top for Map + Strip of paper, Bottom for Profile graph
    ax_top = fig.add_axes([0.1, 0.56, 0.82, 0.38])
    ax_bot = fig.add_axes([0.1, 0.08, 0.82, 0.38])
    
    # Set limits
    ax_top.set_xlim(-1, 11)
    ax_top.set_ylim(-2.8, 6.2)
    ax_top.axis("off")
    
    # Top: Draw topographical hill contours (concentric ellipses)
    # Hill center at (5.0, 3.2) to move it away from A-B
    center = (5.0, 3.2)
    contours = [
        (100, 4.4, 2.7),
        (200, 3.4, 2.1),
        (300, 2.4, 1.5),
        (400, 1.3, 0.85)
    ]
    
    theta = np.linspace(0, 2 * np.pi, 200)
    for h, rx, ry in contours:
        x_c = center[0] + rx * np.cos(theta)
        y_c = center[1] + ry * np.sin(theta)
        ax_top.plot(x_c, y_c, color=DEEP["orange"], lw=2.0)
        # Contour label (placed at top part of ellipse)
        ax_top.text(center[0], center[1] + ry, f"{h} m", fontsize=14, color=INK,
                    ha="center", va="center", bbox=dict(fc="white", ec="none", pad=1.5))
        
    ax_top.text(center[0], center[1], "Hill Summit\n(450 m)", fontsize=14, color=INK,
                ha="center", va="center", style="italic", bbox=dict(fc="white", ec="none", pad=1.5))
    
    # Line A-B crossing the hill horizontally along y = 1.5
    y_line = 1.5
    xA, xB = 0.5, 9.5
    
    # Tick marks positions along y=1.5 where contours cross
    # Intersections with ellipses centered at (5.0, 3.2): 
    # (x - 5)^2 / rx^2 + (1.5 - 3.2)^2 / ry^2 = 1
    # x = 5 +- rx * sqrt(1 - (1.7/ry)^2) if 1.7 < ry
    ticks = []
    dy = y_line - center[1]
    for h, rx, ry in contours:
        if abs(dy) < ry:
            dx = rx * np.sqrt(1 - (dy / ry)**2)
            ticks.append((5.0 - dx, h))
            ticks.append((5.0 + dx, h))
    ticks.sort(key=lambda t: t[0])
    
    # Topographical map title
    ax_top.text(0.0, 6.0, "Topographical Map & Paper Strip Method", fontsize=17, fontweight="bold", color=INK)
    
    # Draw line A - B
    ax_top.plot([xA, xB], [y_line, y_line], color=INK, lw=2.2, ls="--")
    ax_top.scatter([xA, xB], [y_line, y_line], color=INK, s=45, zorder=5)
    ax_top.text(xA - 0.25, y_line, "A", fontsize=16, fontweight="bold", ha="right", va="center", color=INK)
    ax_top.text(xB + 0.25, y_line, "B", fontsize=16, fontweight="bold", ha="left", va="center", color=INK)
    
    # Straight-edged strip of paper laid just below line A-B (or along A-B)
    paper_top = 1.45
    paper_h = 1.3
    paper_bot = paper_top - paper_h
    paper_rect = plt.Rectangle((xA - 0.2, paper_bot), (xB - xA + 0.4), paper_h,
                               fc=CREAM, ec=GREY, lw=1.8, zorder=3)
    ax_top.add_patch(paper_rect)
    
    ax_top.text((xA + xB) / 2, paper_bot + 0.35, "Straight-edged strip of paper",
                fontsize=14, ha="center", va="center", color=INK, style="italic")
    
    # Draw tick marks on paper strip edge
    ax_top.scatter([xA, xB], [paper_top, paper_top], color=INK, s=30, zorder=4)
    ax_top.text(xA, paper_top - 0.25, "A", fontsize=14, fontweight="bold", ha="center", va="top")
    ax_top.text(xB, paper_top - 0.25, "B", fontsize=14, fontweight="bold", ha="center", va="top")
    
    for x_pos, h in ticks:
        # Tick line on paper
        ax_top.plot([x_pos, x_pos], [paper_top, paper_top - 0.22], color=DEEP["blue"], lw=2.2, zorder=4)
        ax_top.text(x_pos, paper_top - 0.3, f"{h}", fontsize=14, color=DEEP["blue"],
                    ha="center", va="top", rotation=90)
        
    # Bottom: Graph with horizontal axis A-B and vertical axis height in metres
    ax_bot.set_xlim(-1, 11)
    ax_bot.set_ylim(0, 520)
    
    # Stylise bottom plot
    ax_bot.spines["top"].set_visible(False)
    ax_bot.spines["right"].set_visible(False)
    ax_bot.spines["left"].set_color(INK)
    ax_bot.spines["left"].set_linewidth(1.8)
    ax_bot.spines["bottom"].set_color(INK)
    ax_bot.spines["bottom"].set_linewidth(1.8)
    
    ax_bot.set_yticks([0, 100, 200, 300, 400, 500])
    ax_bot.set_yticklabels(["0", "100", "200", "300", "400", "500"], fontsize=14, color=INK)
    ax_bot.set_ylabel("Height (metres)", fontsize=16, color=INK, labelpad=8)
    
    # Set horizontal axis ticks specifically at A, B
    ax_bot.set_xticks([xA, xB])
    ax_bot.set_xticklabels(["A", "B"], fontsize=16, fontweight="bold", color=INK)
    ax_bot.set_xlabel("Cross-profile line A – B", fontsize=16, color=INK, labelpad=10)
    ax_bot.text(0.0, 535, "Cross-Profile Graph", fontsize=17, fontweight="bold", color=INK)
    
    # Subtle horizontal gridlines for heights
    for gh in [100, 200, 300, 400]:
        ax_bot.axhline(gh, color=GREY, lw=1.0, ls=":", zorder=1)
        
    # Project ticks upwards (represented here as guide lines from paper down to graph points)
    for x_pos, h in ticks:
        # Point on graph
        ax_bot.plot([x_pos, x_pos], [0, h], color=DEEP["blue"], lw=1.5, ls="--", alpha=0.6, zorder=2)
        ax_bot.scatter(x_pos, h, color=DEEP["blue"], s=55, zorder=5)
        
    # Smooth hill profile curve joining tick mark points
    x_prof = np.linspace(xA, xB, 300)
    pts_x = [xA] + [t[0] for t in ticks] + [xB]
    pts_y = [20] + [t[1] for t in ticks] + [20]
    
    poly = np.poly1d(np.polyfit(pts_x, pts_y, 6))
    y_curve = np.clip(poly(x_prof), 0, 500)
    
    # Fill area under hill curve
    ax_bot.fill_between(x_prof, y_curve, color=GREEN, alpha=0.35, zorder=3)
    ax_bot.plot(x_prof, y_curve, color=DEEP["green"], lw=3.2, zorder=4, label="Smooth hill profile")
    
    # Annotation on the projection & profile
    ax_bot.annotate("Tick marks projected\nto contour heights",
                    xy=(ticks[1][0], ticks[1][1]), xytext=(1.0, 380),
                    fontsize=14, color=INK,
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                    bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    ax_bot.annotate("Smooth curve\njoins points",
                    xy=(5.0, poly(5.0)), xytext=(6.5, 430),
                    fontsize=14, color=INK,
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                    bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    save(fig, out)
