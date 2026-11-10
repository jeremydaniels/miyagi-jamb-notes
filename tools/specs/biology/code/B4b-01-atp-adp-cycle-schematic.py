from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(15, 10)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.axis('off')

    def regular_polygon(center, radius, n_sides, rotation=0):
        angles = np.linspace(0, 2 * np.pi, n_sides, endpoint=False) + rotation
        x = center[0] + radius * np.cos(angles)
        y = center[1] + radius * np.sin(angles)
        return np.column_stack((x, y))

    def draw_nucleoside(base_pos):
        bx, by = base_pos
        # Ribose (Pentagon)
        ribose_center = (bx + 1.1, by)
        ribose_poly = regular_polygon(ribose_center, 0.45, 5, rotation=np.pi/10)
        ribose_patch = patches.Polygon(ribose_poly, closed=True, fc=CREAM, ec=DEEP["orange"], lw=2, zorder=3)
        ax.add_patch(ribose_patch)

        # Adenine (Hexagon pair)
        # Using radius 0.4, rotation pi/6, center distance 0.4 * sqrt(3) ≈ 0.693 to share vertical edge
        hex1_center = (bx - 0.346, by + 0.1)
        hex2_center = (bx + 0.346, by + 0.1)
        hex1 = regular_polygon(hex1_center, 0.4, 6, rotation=np.pi/6)
        hex2 = regular_polygon(hex2_center, 0.4, 6, rotation=np.pi/6)
        
        p1 = patches.Polygon(hex1, closed=True, fc=LAV, ec=DEEP["lav"], lw=2, zorder=3)
        p2 = patches.Polygon(hex2, closed=True, fc=LAV, ec=DEEP["lav"], lw=2, zorder=3)
        ax.add_patch(p1)
        ax.add_patch(p2)

        # Connector ribose to adenine
        ax.plot([bx + 0.65, bx + 0.8], [by + 0.1, by], color=INK, lw=2, zorder=2)
        return ribose_center

    # ----------------- LEFT: ATP Molecule -----------------
    atp_rx, atp_ry = draw_nucleoside((1.5, 5.0))
    p_atp = [atp_rx + 0.8, atp_rx + 1.6, atp_rx + 2.4]
    ax.plot([atp_rx + 0.45, p_atp[0]], [atp_ry, atp_ry], color=INK, lw=2, zorder=2)
    for i, px in enumerate(p_atp):
        if i > 0:
            ax.plot([p_atp[i-1] + 0.32, px - 0.32], [atp_ry, atp_ry], color=INK, lw=2, zorder=2)
        c = patches.Circle((px, atp_ry), 0.32, fc=PINK, ec=DEEP["pink"], lw=2, zorder=3)
        ax.add_patch(c)
        ax.text(px, atp_ry, "P", ha='center', va='center', fontsize=13, weight='bold', color=INK, zorder=4)

    # Title for ATP
    ax.text(3.1, 4.0, "ATP (adenosine triphosphate)", ha='center', va='center', fontsize=14, weight='bold', color=INK)

    # ----------------- RIGHT: ADP + separate Phosphate Molecule -----------------
    adp_rx, adp_ry = draw_nucleoside((9.2, 5.0))
    p_adp = [adp_rx + 0.8, adp_rx + 1.6]
    ax.plot([adp_rx + 0.45, p_adp[0]], [adp_ry, adp_ry], color=INK, lw=2, zorder=2)
    ax.plot([p_adp[0] + 0.32, p_adp[1] - 0.32], [adp_ry, adp_ry], color=INK, lw=2, zorder=2)
    for px in p_adp:
        c = patches.Circle((px, adp_ry), 0.32, fc=PINK, ec=DEEP["pink"], lw=2, zorder=3)
        ax.add_patch(c)
        ax.text(px, adp_ry, "P", ha='center', va='center', fontsize=13, weight='bold', color=INK, zorder=4)

    # Separate single inorganic phosphate circle
    pi_x, pi_y = 13.5, 5.0
    ax.text(12.35, 5.0, "+", ha='center', va='center', fontsize=22, weight='bold', color=INK)
    c_pi = patches.Circle((pi_x, pi_y), 0.32, fc=PINK, ec=DEEP["pink"], lw=2, zorder=3)
    ax.add_patch(c_pi)
    ax.text(pi_x, pi_y, "P", ha='center', va='center', fontsize=13, weight='bold', color=INK, zorder=4)

    # Title for ADP
    ax.text(11.9, 4.0, "ADP (adenosine diphosphate)", ha='center', va='center', fontsize=14, weight='bold', color=INK)

    # ----------------- STRUCTURAL LABELS (Left / Top-Left) -----------------
    ax.annotate("adenine", xy=(1.5, 5.5), xytext=(1.5, 6.2),
                ha='center', va='bottom', fontsize=12, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2', lw=0.8))
    ax.annotate("ribose", xy=(2.6, 5.45), xytext=(2.6, 6.2),
                ha='center', va='bottom', fontsize=12, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2', lw=0.8))
    ax.annotate("phosphate", xy=(3.8, 5.35), xytext=(3.8, 6.2),
                ha='center', va='bottom', fontsize=12, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2', lw=0.8))

    # ----------------- CYCLE ARROWS -----------------
    top_arrow = patches.FancyArrowPatch((11.0, 6.8), (4.6, 6.8),
                                       connectionstyle="arc3,rad=0.35",
                                       arrowstyle="Simple,tail_width=4,head_width=12,head_length=12",
                                       fc=DEEP["blue"], ec=DEEP["blue"], zorder=2)
    ax.add_patch(top_arrow)

    bot_arrow = patches.FancyArrowPatch((4.6, 3.2), (11.0, 3.2),
                                       connectionstyle="arc3,rad=0.35",
                                       arrowstyle="Simple,tail_width=4,head_width=12,head_length=12",
                                       fc=DEEP["orange"], ec=DEEP["orange"], zorder=2)
    ax.add_patch(bot_arrow)

    # ----------------- TOP CYCLE LABELS & MITOCHONDRION -----------------
    ax.text(7.8, 8.2, "phosphate added", ha='center', va='center', fontsize=13, weight='bold',
            color=DEEP["blue"], bbox=dict(fc='white', ec='none', pad=4), zorder=5)

    ax.text(7.8, 9.4, "energy from respiration", ha='center', va='center', fontsize=14, weight='bold', color=INK)

    mito_center = (4.7, 8.8)
    mito_bg = patches.Ellipse(mito_center, 1.4, 0.7, angle=-10, fc=CREAM, ec=DEEP["orange"], lw=2, zorder=3)
    ax.add_patch(mito_bg)
    crx = np.linspace(mito_center[0] - 0.45, mito_center[0] + 0.45, 6)
    cry = mito_center[1] + 0.14 * np.sin(np.linspace(0, 3*np.pi, 6))
    ax.plot(crx, cry, color=DEEP["orange"], lw=2, zorder=4)

    ax.annotate("", xy=(6.5, 8.0), xytext=(5.6, 8.6),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.5, connectionstyle="arc3,rad=-0.1"))

    # ----------------- BOTTOM CYCLE LABELS & CELL WORK -----------------
    ax.text(7.8, 2.5, "phosphate removed", ha='center', va='center', fontsize=13, weight='bold',
            color=DEEP["orange"], bbox=dict(fc='white', ec='none', pad=3), zorder=5)

    ax.annotate("", xy=(7.8, 1.1), xytext=(7.8, 1.7),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5))

    ax.text(7.8, 0.9, "energy for cell work", ha='center', va='center', fontsize=13, weight='bold', color=INK)
    ax.text(7.8, 0.45, "energy for muscle contraction, active transport, growth",
            ha='center', va='center', fontsize=11.5, color=INK)

    m_x, m_y = 2.4, 1.0
    for dy in [-0.2, 0.0, 0.2]:
        ax.plot([m_x - 0.5, m_x + 0.5], [m_y + dy, m_y + dy], color=DEEP["pink"], lw=3)
        for dx in np.linspace(-0.35, 0.35, 4):
            ax.plot([m_x + dx, m_x + dx], [m_y + dy - 0.08, m_y + dy + 0.08], color=DEEP["pink"], lw=1.5)

    dc_x, dc_y = 12.3, 1.0
    c1 = patches.Circle((dc_x - 0.22, dc_y), 0.3, fc=LAV, ec=DEEP["lav"], lw=1.5)
    c2 = patches.Circle((dc_x + 0.22, dc_y), 0.3, fc=LAV, ec=DEEP["lav"], lw=1.5)
    ax.add_patch(c1)
    ax.add_patch(c2)

    pr_x = np.linspace(13.3, 14.7, 5)
    pr_y = 1.0 + 0.15 * np.sin(np.linspace(0, 1.5*np.pi, 5))
    ax.plot(pr_x, pr_y, color=GREY, lw=2, zorder=2)
    for px, py in zip(pr_x, pr_y):
        ax.add_patch(patches.Circle((px, py), 0.12, fc=GREEN, ec=DEEP["green"], lw=1.5, zorder=3))

    save(fig, out)
