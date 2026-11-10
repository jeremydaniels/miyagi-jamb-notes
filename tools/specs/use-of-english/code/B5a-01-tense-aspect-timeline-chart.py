from style import *
import numpy as np

def draw(out):
    fig = canvas(12, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(-0.8, 5.2)
    ax.axis('off')

    # Title
    ax.text(5.5, 4.8, "Tense and aspect at a glance", fontsize=18, fontweight='bold', ha='center', va='center', color=INK)

    # Reference points in X
    x_past = 3.6
    x_now = 6.6
    x_future = 9.6

    # Draw vertical reference line for "NOW" (cut before bottom label)
    ax.axvline(x=x_now, ymin=0.18, ymax=0.88, color=DEEP['pink'], linestyle='--', linewidth=2, zorder=1)
    ax.text(x_now, 4.35, "NOW", fontsize=14, fontweight='bold', ha='center', va='center', color=DEEP['pink'],
            bbox=dict(fc='white', ec=DEEP['pink'], boxstyle='round,pad=0.2', lw=1.5))

    # Time Axis at bottom
    y_axis = 0.2
    ax.annotate('', xy=(11.0, y_axis), xytext=(0.5, y_axis),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5, mutation_scale=20))
    ax.text(x_past, y_axis - 0.45, "PAST", fontsize=15, fontweight='bold', ha='center', va='center', color=INK)
    ax.text(x_now, y_axis - 0.45, "NOW", fontsize=15, fontweight='bold', ha='center', va='center', color=DEEP['pink'])
    ax.text(x_future, y_axis - 0.45, "FUTURE", fontsize=15, fontweight='bold', ha='center', va='center', color=INK)

    # Rows configuration
    rows = [
        {
            "name": "Simple",
            "y": 3.7,
            "color": DEEP['blue'],
            "bg": BLUE,
            "examples": ["cooked", "cook", "will cook"],
            "type": "simple"
        },
        {
            "name": "Progressive",
            "y": 2.7,
            "color": DEEP['orange'],
            "bg": ORANGE,
            "examples": ["was cooking", "am cooking", "will be cooking"],
            "type": "progressive"
        },
        {
            "name": "Perfect",
            "y": 1.7,
            "color": DEEP['green'],
            "bg": GREEN,
            "examples": ["had cooked", "have cooked", "will have cooked"],
            "type": "perfect"
        },
        {
            "name": "Perfect progressive",
            "y": 0.7,
            "color": DEEP['lav'],
            "bg": LAV,
            "examples": ["had been cooking", "have been cooking", "will have been cooking"],
            "type": "perf_prog"
        }
    ]

    def draw_wave(cx, cy, width=0.8, color='black'):
        xs = np.linspace(cx - width/2, cx + width/2, 60)
        ys = cy + 0.06 * np.sin((xs - (cx - width/2)) * (4 * np.pi / width))
        ax.plot(xs, ys, color=color, lw=3, solid_capstyle='round')

    for r in rows:
        y = r['y']
        c = r['color']

        # Row label on the left (now enough space because x_past is shifted to 3.6)
        ax.text(0.1, y, r['name'], fontsize=14, fontweight='bold', ha='left', va='center', color=INK,
                bbox=dict(fc=r['bg'], ec='none', boxstyle='round,pad=0.3'))

        # Subtle row guide line
        ax.plot([2.5, 11.0], [y, y], color=GREY, lw=0.8, ls=':', zorder=0)

        # Draw icons and text at Past, Now, Future
        for (cx, ex) in zip([x_past, x_now, x_future], r['examples']):
            # Draw representation
            if r['type'] == 'simple':
                # Single dot
                ax.plot(cx, y + 0.15, marker='o', markersize=9, color=c)
            elif r['type'] == 'progressive':
                # Wavy bar
                draw_wave(cx, y + 0.15, width=0.85, color=c)
            elif r['type'] == 'perfect':
                # Arrow ending at reference point
                ax.annotate('', xy=(cx, y + 0.15), xytext=(cx - 0.8, y + 0.15),
                            arrowprops=dict(arrowstyle="->", color=c, lw=2.5, mutation_scale=14))
                ax.plot(cx, y + 0.15, marker='|', markersize=10, color=c, markeredgewidth=2.5)
            elif r['type'] == 'perf_prog':
                # Wavy bar ending in an arrow at reference point
                xs = np.linspace(cx - 0.85, cx - 0.08, 45)
                ys = (y + 0.15) + 0.06 * np.sin((xs - (cx - 0.85)) * (4 * np.pi / 0.85))
                ax.plot(xs, ys, color=c, lw=2.5)
                ax.annotate('', xy=(cx, y + 0.15), xytext=(cx - 0.15, y + 0.15),
                            arrowprops=dict(arrowstyle="->", color=c, lw=2.5, mutation_scale=14))
                ax.plot(cx, y + 0.15, marker='|', markersize=10, color=c, markeredgewidth=2.5)

            # Example label below the diagram icon
            ax.text(cx, y - 0.22, ex, fontsize=14, fontstyle='italic', ha='center', va='center', color=INK,
                    bbox=dict(fc='white', ec='none', pad=0.1))

    save(fig, out)
