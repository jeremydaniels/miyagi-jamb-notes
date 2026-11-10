from style import *
import numpy as np

def draw(out):
    fig = canvas(12, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(1958, 2005)
    ax.set_ylim(-3.5, 4.0)
    ax.axis("off")

    # Title
    ax.text(
        1981, 3.3,
        "Nigeria's Post-Independence Constitutions",
        fontsize=18,
        fontweight="bold",
        color=INK,
        ha="center",
        va="center"
    )

    # Main timeline axis
    y_axis = 0.0
    ax.annotate(
        "",
        xy=(2003, y_axis),
        xytext=(1959, y_axis),
        arrowprops=dict(arrowstyle="->", color=INK, lw=2.5, mutation_scale=20)
    )

    events = [
        {
            "year": 1963,
            "title": "1963 Constitution",
            "rep": "First Republic",
            "detail": "Parliamentary System",
            "side": 1,  # Above
            "color": DEEP["green"],
            "fill": GREEN
        },
        {
            "year": 1979,
            "title": "1979 Constitution",
            "rep": "Second Republic",
            "detail": "Presidential System",
            "side": -1,  # Below
            "color": DEEP["blue"],
            "fill": BLUE
        },
        {
            "year": 1989,
            "title": "1989 Constitution",
            "rep": "Third Republic (Aborted)",
            "detail": "Two-party System",
            "side": 1,  # Above
            "color": DEEP["green"],
            "fill": GREEN
        },
        {
            "year": 1999,
            "title": "1999 Constitution",
            "rep": "Fourth Republic",
            "detail": "Presidential System",
            "side": -1,  # Below
            "color": DEEP["blue"],
            "fill": BLUE
        }
    ]

    for ev in events:
        x = ev["year"]
        side = ev["side"]
        color = ev["color"]
        fill_col = ev["fill"]

        # Marker circle on the line
        ax.plot(x, y_axis, marker="o", markersize=10, color=color, zorder=5)

        # Stems connecting timeline to labels
        y_label = y_axis + side * 1.5
        ax.plot([x, x], [y_axis, y_label], color=color, lw=2, linestyle="--", zorder=3)

        # Text box contents
        box_text = f"\\textbf{{{ev['year']}}}\n{ev['rep']}\n{ev['detail']}"
        # Alternative without raw latex for robustness:
        lines = [f"{ev['year']}", ev['rep'], ev['detail']]
        full_text = "\n".join(lines)

        va_align = "bottom" if side == 1 else "top"
        y_text = y_axis + side * 1.65

        ax.text(
            x,
            y_text,
            full_text,
            fontsize=14,
            ha="center",
            va=va_align,
            color=INK,
            linespacing=1.3,
            bbox=dict(
                boxstyle="round,pad=0.6",
                facecolor="white",
                edgecolor=color,
                lw=2
            )
        )

    save(fig, out)
