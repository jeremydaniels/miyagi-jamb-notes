from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(10, 11)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.88])
    ax.set_xlim(-5.2, 5.2)
    ax.set_ylim(-0.8, 10.2)
    ax.axis("off")

    # Lead block / Radioactive source at the bottom
    block_w = 2.0
    block_h = 1.3
    lead_color = GREY
    ax.fill_between([-block_w/2, block_w/2], [0.1, 0.1], [block_h, block_h], color=lead_color, ec=INK, lw=2)
    
    # Collimator cavity
    cavity_w = 0.35
    cavity_h = 0.9
    ax.fill_between([-cavity_w/2, cavity_w/2], [block_h - cavity_h, block_h - cavity_h], [block_h + 0.05, block_h + 0.05], color="white", ec=INK, lw=1.5)
    
    # Source dot inside cavity
    ax.plot(0, block_h - cavity_h + 0.25, marker='o', markersize=9, color=DEEP["orange"])
    ax.text(0, -0.15, "Radioactive source", ha="center", va="top", fontsize=15, fontweight="bold", color=INK)
    ax.text(block_w/2 + 0.35, block_h/2 + 0.05, "Lead block", ha="left", va="center", fontsize=14, color=INK)

    # Plates geometry
    plate_left_x = -2.7
    plate_right_x = 2.7
    plate_y_bot = 2.4
    plate_y_top = 6.8
    plate_thickness = 0.45

    # Positive plate (Left)
    ax.fill_between([plate_left_x - plate_thickness, plate_left_x], [plate_y_bot, plate_y_bot], [plate_y_top, plate_y_top], color=PINK, ec=INK, lw=2)
    # Negative plate (Right)
    ax.fill_between([plate_right_x, plate_right_x + plate_thickness], [plate_y_bot, plate_y_bot], [plate_y_top, plate_y_top], color=BLUE, ec=INK, lw=2)

    # Charge signs on plates
    for y_sign in np.linspace(plate_y_bot + 0.5, plate_y_top - 0.5, 6):
        ax.text(plate_left_x - plate_thickness/2, y_sign, "+", ha="center", va="center", fontsize=18, fontweight="bold", color=INK)
        ax.text(plate_right_x + plate_thickness/2, y_sign, "−", ha="center", va="center", fontsize=20, fontweight="bold", color=INK)

    ax.text(plate_left_x - plate_thickness/2, plate_y_top + 0.3, "Positive\nplate (+)", ha="center", va="bottom", fontsize=14, fontweight="bold", color=INK)
    ax.text(plate_right_x + plate_thickness/2, plate_y_top + 0.3, "Negative\nplate (−)", ha="center", va="bottom", fontsize=14, fontweight="bold", color=INK)

    # Beams origin
    y_start = block_h + 0.05
    y_enter = plate_y_bot

    # Common straight path up to electric field entry
    ax.plot([0, 0], [y_start, y_enter], color=INK, lw=2, ls="--")

    # 1. Gamma ray (gamma): unaffected, wavy line straight up
    y_gamma = np.linspace(y_enter, 9.1, 400)
    wave_amp = 0.08
    wave_freq = 24
    x_gamma = wave_amp * np.sin(wave_freq * (y_gamma - y_enter))
    ax.plot(x_gamma, y_gamma, color=DEEP["green"], lw=2.5)
    ax.annotate("", xy=(0, 9.5), xytext=(0, 9.0),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.5, mutation_scale=18))
    ax.text(0, 9.65, r"$\gamma$ ray (neutral)", ha="center", va="bottom", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # 2. Alpha particle (alpha): heavy, bends slightly towards negative plate (right)
    # Curves gently within field, passes out above the plates, stays comfortably clear of the right plate
    k_alpha = 0.048
    y_alpha_field = np.linspace(y_enter, plate_y_top, 120)
    x_alpha_field = k_alpha * (y_alpha_field - y_enter)**2
    # Straight exit trajectory
    slope_alpha = 2 * k_alpha * (plate_y_top - y_enter)
    x_alpha_exit_start = x_alpha_field[-1]
    y_alpha_exit = np.linspace(plate_y_top, 9.0, 60)
    x_alpha_exit = x_alpha_exit_start + slope_alpha * (y_alpha_exit - plate_y_top)

    x_alpha = np.concatenate([x_alpha_field, x_alpha_exit])
    y_alpha = np.concatenate([y_alpha_field, y_alpha_exit])
    ax.plot(x_alpha, y_alpha, color=DEEP["blue"], lw=2.5)

    # Arrow for alpha
    ax.annotate("", xy=(x_alpha[-1] + slope_alpha * 0.45, y_alpha[-1] + 0.45),
                xytext=(x_alpha[-1], y_alpha[-1]),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.5, mutation_scale=18))
    ax.text(x_alpha[-1] + slope_alpha * 0.5 + 0.1, y_alpha[-1] + 0.55,
            r"$\alpha$ particle (+2)", ha="left", va="bottom", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # 3. Beta particle (beta): light, bends sharply towards positive plate (left)
    # Remains between the plates and exits at the top left without intersecting the left plate (plate_left_x = -2.7)
    k_beta = -0.115
    y_beta_field = np.linspace(y_enter, plate_y_top, 120)
    x_beta_field = k_beta * (y_beta_field - y_enter)**2  # at plate_y_top: ~ -2.23 > -2.7
    slope_beta = 2 * k_beta * (plate_y_top - y_enter)
    x_beta_exit_start = x_beta_field[-1]
    y_beta_exit = np.linspace(plate_y_top, 8.7, 60)
    x_beta_exit = x_beta_exit_start + slope_beta * (y_beta_exit - plate_y_top)

    x_beta = np.concatenate([x_beta_field, x_beta_exit])
    y_beta = np.concatenate([y_beta_field, y_beta_exit])
    ax.plot(x_beta, y_beta, color=DEEP["pink"], lw=2.5)

    # Arrow for beta
    ax.annotate("", xy=(x_beta[-1] + slope_beta * 0.45, y_beta[-1] + 0.45),
                xytext=(x_beta[-1], y_beta[-1]),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5, mutation_scale=18))
    ax.text(x_beta[-1] + slope_beta * 0.5 - 0.1, y_beta[-1] + 0.55,
            r"$\beta$ particle (−1)", ha="right", va="bottom", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # Deflection explanation annotations (positioned completely outside the plates)
    ax.annotate("Deflects slightly\ntowards (−) plate\n(heavy, positive)",
                xy=(1.5, 5.0), xytext=(3.5, 4.4),
                fontsize=14, color=INK, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"))

    ax.annotate("Deflects sharply\ntowards (+) plate\n(light, negative)",
                xy=(-1.5, 4.8), xytext=(-3.5, 4.4),
                fontsize=14, color=INK, ha="right", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"))

    # Electric field label between the plates
    ax.text(0, 2.0, "Electric Field", ha="center", va="center", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.4"))

    # Title
    ax.text(0, 10.1, "Deflection of Radiations in an Electric Field",
            fontsize=17, fontweight="bold", color=INK, ha="center", va="top")

    save(fig, out)
