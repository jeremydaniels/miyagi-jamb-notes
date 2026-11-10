from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9.5, 7)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # Phasor values (lengths)
    vr = 4.4       # Horizontal: V_R & Current I
    vl = 3.8       # Inductive voltage (upward)
    vc = 1.6       # Capacitive voltage (downward)
    v_net = vl - vc  # Net reactive voltage (V_L - V_C = 2.2)

    # Set canvas bounds to fit vectors, labels, and text box comfortably
    ax.set_xlim(-2.6, 6.2)
    ax.set_ylim(-2.4, 4.6)

    # Background reference axes
    ax.axhline(0, color=GREY, lw=1.2, ls="--", alpha=0.6)
    ax.axvline(0, color=GREY, lw=1.2, ls="--", alpha=0.6)

    # 1. Current / Resistor voltage phasor (Horizontal right)
    ax.annotate(
        "", xy=(vr, 0), xytext=(0, 0),
        arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=3.2, mutation_scale=20)
    )
    ax.text(vr + 0.2, 0.0, r"$\mathbf{I},\, \mathbf{V_R}$",
            color=DEEP["blue"], fontsize=16, fontweight="bold", va="center", ha="left")

    # 2. V_L phasor (Vertical up)
    ax.annotate(
        "", xy=(0, vl), xytext=(0, 0),
        arrowprops=dict(arrowstyle="-|>", color=DEEP["green"], lw=2.5, mutation_scale=18)
    )
    ax.text(-0.25, vl, r"$V_L$", color=DEEP["green"], fontsize=16, fontweight="bold", ha="right", va="center")

    # 3. V_C phasor (Vertical down)
    ax.annotate(
        "", xy=(0, -vc), xytext=(0, 0),
        arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=2.5, mutation_scale=18)
    )
    ax.text(-0.25, -vc, r"$V_C$", color=DEEP["pink"], fontsize=16, fontweight="bold", ha="right", va="center")

    # 4. Net reactive voltage (V_L - V_C) on y-axis
    ax.annotate(
        "", xy=(0, v_net), xytext=(0, 0),
        arrowprops=dict(arrowstyle="-|>", color=DEEP["orange"], lw=3.6, mutation_scale=20)
    )
    ax.text(-0.3, v_net * 0.52, r"$V_L - V_C$", color=DEEP["orange"], fontsize=15, fontweight="bold",
            ha="right", va="center", bbox=dict(fc="white", ec="none", pad=1.5))

    # Dashed construction lines for parallelogram
    ax.plot([vr, vr], [0, v_net], color=GREY, lw=1.8, ls=":")
    ax.plot([0, vr], [v_net, v_net], color=GREY, lw=1.8, ls=":")

    # 5. Resultant voltage phasor V
    ax.annotate(
        "", xy=(vr, v_net), xytext=(0, 0),
        arrowprops=dict(arrowstyle="-|>", color=INK, lw=3.5, mutation_scale=22)
    )
    ax.text(vr + 0.15, v_net + 0.15, r"$\mathbf{V}$ (Effective Voltage)",
            color=INK, fontsize=16, fontweight="bold", va="bottom", ha="left")

    # 6. Phase angle theta (θ) arc
    theta_rad = np.arctan2(v_net, vr)
    arc_radius = 1.3
    arc = patches.Arc((0, 0), 2 * arc_radius, 2 * arc_radius, angle=0,
                      theta1=0, theta2=np.degrees(theta_rad), color=INK, lw=1.8)
    ax.add_patch(arc)

    mid_angle = theta_rad / 2
    tx = (arc_radius + 0.32) * np.cos(mid_angle)
    ty = (arc_radius + 0.32) * np.sin(mid_angle)
    ax.text(tx, ty, r"$\theta$", color=INK, fontsize=16, fontweight="bold", ha="center", va="center")

    # Explanatory formula box placed in Quadrant 4 clear of V_C and axis
    info_text = (
        r"$\mathbf{R\text{-}L\text{-}C\ Series\ Circuit}$" + "\n"
        r"$(V_L > V_C\text{: Inductive})$" + "\n"
        r"$V = \sqrt{V_R^2 + (V_L - V_C)^2}$" + "\n"
        r"$\tan\theta = \frac{V_L - V_C}{V_R}$"
    )
    ax.text(1.8, -1.35, info_text, fontsize=14, color=INK, va="center", ha="left",
            bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.55", lw=1.2))

    save(fig, out)
