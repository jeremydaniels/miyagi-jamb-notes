from style import *
import numpy as np

def draw(out):
    fig = canvas(12, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 12.0)
    ax.set_ylim(-0.6, 7.2)
    ax.axis('off')

    # Data for the three harmonics
    harmonics = [
        {
            'y_center': 5.5,
            'n_quarter': 1,
            'title': r"Fundamental ($n = 1$)",
            'formula': r"$L = \frac{1}{4}\lambda \quad (\lambda = 4L)$",
            'overtone': "Fundamental frequency, $f_1$"
        },
        {
            'y_center': 3.3,
            'n_quarter': 3,
            'title': r"1st Overtone / 3rd Harmonic ($n = 3$)",
            'formula': r"$L = \frac{3}{4}\lambda \quad (\lambda = \frac{4}{3}L)$",
            'overtone': r"Frequency $f_3 = 3f_1$"
        },
        {
            'y_center': 1.1,
            'n_quarter': 5,
            'title': r"2nd Overtone / 5th Harmonic ($n = 5$)",
            'formula': r"$L = \frac{5}{4}\lambda \quad (\lambda = \frac{4}{5}L)$",
            'overtone': r"Frequency $f_5 = 5f_1$"
        }
    ]

    pipe_x_start = 1.2
    pipe_x_end = 6.8
    pipe_h = 0.72  # half-height
    L = pipe_x_end - pipe_x_start

    for h in harmonics:
        yc = h['y_center']
        nq = h['n_quarter']

        # Pipe background fill
        ax.fill_between([pipe_x_start, pipe_x_end], [yc - pipe_h, yc - pipe_h], [yc + pipe_h, yc + pipe_h],
                        color=CREAM, alpha=0.35, zorder=1)

        # Pipe walls (closed at left, open at right)
        # Top wall
        ax.plot([pipe_x_start, pipe_x_end], [yc + pipe_h, yc + pipe_h], color=INK, lw=3, zorder=4)
        # Bottom wall
        ax.plot([pipe_x_start, pipe_x_end], [yc - pipe_h, yc - pipe_h], color=INK, lw=3, zorder=4)
        # Closed end wall (left)
        ax.plot([pipe_x_start, pipe_x_start], [yc - pipe_h, yc + pipe_h], color=INK, lw=4.5, zorder=4)

        # Dashed end cap at open right end
        ax.plot([pipe_x_end, pipe_x_end], [yc - pipe_h, yc + pipe_h], color=GREY, lw=1.5, ls='--', zorder=2)

        # Centerline
        ax.plot([pipe_x_start, pipe_x_end], [yc, yc], color=GREY, lw=1, ls=':', zorder=2)

        # Standing wave curve (displacement)
        x = np.linspace(pipe_x_start, pipe_x_end, 300)
        x_rel = x - pipe_x_start
        wave_amp = 0.55
        wave_curve = wave_amp * np.sin(nq * np.pi * x_rel / (2.0 * L))

        # Two counter-phased envelopes
        ax.plot(x, yc + wave_curve, color=DEEP['blue'], lw=2.5, zorder=3)
        ax.plot(x, yc - wave_curve, color=DEEP['blue'], lw=2.0, ls='--', alpha=0.7, zorder=3)
        ax.fill_between(x, yc - np.abs(wave_curve), yc + np.abs(wave_curve), color=BLUE, alpha=0.15, zorder=2)

        # Nodes and Antinodes markings
        node_xs = [pipe_x_start + (2 * k * L) / nq for k in range((nq // 2) + 1)]
        antinode_xs = [pipe_x_start + ((2 * k + 1) * L) / nq for k in range((nq + 1) // 2)]

        for nx in node_xs:
            ax.plot(nx, yc, marker='o', markersize=6, color=DEEP['pink'], zorder=5)
            ax.text(nx, yc - pipe_h - 0.28, "N", color=DEEP['pink'], fontsize=14, fontweight='bold',
                    ha='center', va='top')

        for ax_pos in antinode_xs:
            ax.text(ax_pos, yc - pipe_h - 0.28, "A", color=DEEP['blue'], fontsize=14, fontweight='bold',
                    ha='center', va='top')

        # Text labels on the right
        ax.text(7.3, yc + 0.45, h['title'], fontsize=16, fontweight='bold', color=INK, va='center')
        ax.text(7.3, yc, h['formula'], fontsize=15, color=INK, va='center')
        ax.text(7.3, yc - 0.42, h['overtone'], fontsize=14, color=GREY, va='center')

    # Overall length indicator on top diagram
    top_yc = harmonics[0]['y_center']
    arrow_y = top_yc + pipe_h + 0.35
    ax.annotate('', xy=(pipe_x_start, arrow_y), xytext=(pipe_x_end, arrow_y),
                arrowprops=dict(arrowstyle='<->', color=INK, lw=1.5))
    ax.text((pipe_x_start + pipe_x_end) / 2, arrow_y + 0.1, r"Length $L$",
            fontsize=15, ha='center', va='bottom', color=INK,
            bbox=dict(fc='white', ec='none', pad=1))

    # Closed and open indicators
    ax.text(pipe_x_start - 0.2, top_yc, "Closed\nend", fontsize=14, ha='right', va='center', color=INK)
    ax.text(pipe_x_end + 0.15, top_yc + pipe_h + 0.05, "Open end", fontsize=14, ha='left', va='bottom', color=INK)

    # Key / Legend at bottom
    ax.text(pipe_x_start, -0.3, r"$\mathbf{N}$ = Node (zero displacement)       $\mathbf{A}$ = Antinode (max displacement)",
            fontsize=14, color=INK, va='center')

    save(fig, out)
