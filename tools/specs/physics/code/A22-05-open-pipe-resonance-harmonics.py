from style import *
import numpy as np

def draw(out):
    fig = canvas(12, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 15)
    ax.set_ylim(-0.5, 9.5)
    ax.axis("off")

    # Titles / overall labels
    ax.text(7, 9.1, "Standing Waves in an Open Pipe (Both Ends Open)", 
            ha="center", va="center", fontsize=18, weight="bold", color=INK)

    pipe_x0, pipe_x1 = 1.5, 9.5
    pipe_len = pipe_x1 - pipe_x0
    pipe_radius = 0.85
    xs = np.linspace(pipe_x0, pipe_x1, 400)

    # Harmonics data
    cases = [
        (7.2, 1, "Fundamental  (n = 1)", r"$L = \frac{1}{2}\lambda_1 \rightarrow \lambda_1 = 2L$"),
        (4.4, 2, "2nd Harmonic / 1st Overtone  (n = 2)", r"$L = \lambda_2 \rightarrow \lambda_2 = L$"),
        (1.6, 3, "3rd Harmonic / 2nd Overtone  (n = 3)", r"$L = \frac{3}{2}\lambda_3 \rightarrow \lambda_3 = \frac{2}{3}L$")
    ]

    for y_c, n, title_str, formula_str in cases:
        # Draw Pipe (open at ends: solid top and bottom walls)
        ax.plot([pipe_x0, pipe_x1], [y_c + pipe_radius, y_c + pipe_radius], color=INK, lw=3)
        ax.plot([pipe_x0, pipe_x1], [y_c - pipe_radius, y_c - pipe_radius], color=INK, lw=3)
        
        # Soft fill for inside the pipe
        ax.fill_between([pipe_x0, pipe_x1], y_c - pipe_radius, y_c + pipe_radius, color=CREAM, alpha=0.3)

        # Standing wave envelope
        phase = (xs - pipe_x0) / pipe_len * (n * np.pi)
        amp = 0.65 * pipe_radius
        wave_pos = y_c + amp * np.cos(phase)
        wave_neg = y_c - amp * np.cos(phase)

        ax.fill_between(xs, wave_neg, wave_pos, color=BLUE, alpha=0.15)
        ax.plot(xs, wave_pos, color=DEEP["blue"], lw=2.5)
        ax.plot(xs, wave_neg, color=DEEP["blue"], lw=2, linestyle="--")

        # Central axis (equilibrium line)
        ax.plot([pipe_x0, pipe_x1], [y_c, y_c], color=GREY, lw=1, linestyle=":")

        # Node and Antinode positions
        for k in range(n + 1):
            x_a = pipe_x0 + k * pipe_len / n
            y_a = y_c - pipe_radius - 0.4
            ax.text(x_a, y_a, "A", ha="center", va="top", fontsize=14, weight="bold", color=DEEP["orange"],
                    bbox=dict(fc="white", ec="none", pad=0.2))

        for k in range(n):
            x_node = pipe_x0 + (k + 0.5) * pipe_len / n
            y_node = y_c - pipe_radius - 0.4
            ax.plot([x_node, x_node], [y_c - 0.15, y_c + 0.15], color=DEEP["pink"], lw=2)
            ax.text(x_node, y_node, "N", ha="center", va="top", fontsize=14, weight="bold", color=DEEP["pink"],
                    bbox=dict(fc="white", ec="none", pad=0.2))

        # Harmonic titles and formulas on the right
        ax.text(10.2, y_c + 0.35, title_str, ha="left", va="center", fontsize=15, weight="bold", color=INK)
        ax.text(10.2, y_c - 0.35, formula_str, ha="left", va="center", fontsize=15, color=INK)

    # Dimension bar for pipe length L at the top
    y_dim = 8.6
    ax.annotate("", xy=(pipe_x1, y_dim), xytext=(pipe_x0, y_dim),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5))
    ax.text((pipe_x0 + pipe_x1)/2, y_dim + 0.1, "Pipe Length L", 
            ha="center", va="bottom", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=1))
    
    # Guide dashed lines from ends to length arrow
    ax.plot([pipe_x0, pipe_x0], [7.2 + pipe_radius, y_dim], color=GREY, lw=1, linestyle="--")
    ax.plot([pipe_x1, pipe_x1], [7.2 + pipe_radius, y_dim], color=GREY, lw=1, linestyle="--")

    # Legend / Key for A and N
    ax.text(pipe_x0, -0.1, "A = Antinode (displacement maximum)", ha="left", va="center", fontsize=14, color=DEEP["orange"], weight="bold")
    ax.text(pipe_x0 + 5.0, -0.1, "N = Node (displacement zero)", ha="left", va="center", fontsize=14, color=DEEP["pink"], weight="bold")

    save(fig, out)
