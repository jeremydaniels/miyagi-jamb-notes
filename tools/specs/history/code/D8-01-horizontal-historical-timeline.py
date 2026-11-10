from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(15, 8.5)
    ax = fig.add_subplot(111)
    ax.set_facecolor('white')

    # Configure coordinate space
    # Timeline x-axis spans 1993: Jan 1 = day 1, Dec 31 = day 365
    ax.set_xlim(0, 365)
    ax.set_ylim(-4, 4)
    ax.axis('off')

    # Main timeline horizontal axis
    y_line = 0.0
    ax.annotate(
        "",
        xy=(355, y_line),
        xytext=(15, y_line),
        arrowprops=dict(arrowstyle="->", color=INK, lw=3, mutation_scale=20)
    )

    # Title
    ax.text(
        182, 3.4,
        "Nigeria's 1993 Political Crisis: Key Events",
        ha="center", va="center",
        fontsize=18, fontweight="bold", color=INK
    )

    # Month reference ticks/labels along the line
    months = [
        ("Jan", 1), ("Feb", 32), ("Mar", 60), ("Apr", 91),
        ("May", 121), ("Jun", 152), ("Jul", 182), ("Aug", 213),
        ("Sep", 244), ("Oct", 274), ("Nov", 305), ("Dec", 335)
    ]
    for name, day in months:
        ax.plot([day, day], [y_line - 0.12, y_line + 0.12], color=GREY, lw=1.5)
        ax.text(day, y_line - 0.35, name, ha="center", va="top", fontsize=14, color=GREY)

    # Events data: (day_of_year, side, date_label, event_text, box_color, border_color)
    # Days:
    # June 12 = 163
    # June 23 = 174
    # August 26 = 238
    # November 10 = 314
    # November 17 = 321
    events = [
        {
            "day": 163,
            "x_box": 120,
            "y_box": 2.1,
            "y_stem": 0.4,
            "date": "June 12",
            "desc": "Presidential election held",
            "color": CREAM,
            "border": DEEP["green"]
        },
        {
            "day": 174,
            "x_box": 160,
            "y_box": -2.3,
            "y_stem": -0.6,
            "date": "June 23",
            "desc": "Election annulled\nby the military",
            "color": PINK,
            "border": DEEP["pink"]
        },
        {
            "day": 238,
            "x_box": 230,
            "y_box": 2.1,
            "y_stem": 0.4,
            "date": "August 26",
            "desc": "Babangida steps aside;\nING formed under Shonekan",
            "color": BLUE,
            "border": DEEP["blue"]
        },
        {
            "day": 314,
            "x_box": 285,
            "y_box": -2.3,
            "y_stem": -0.6,
            "date": "November 10",
            "desc": "High Court declares\nING illegal",
            "color": LAV,
            "border": DEEP["lav"]
        },
        {
            "day": 321,
            "x_box": 330,
            "y_box": 2.1,
            "y_stem": 0.4,
            "date": "November 17",
            "desc": "Shonekan resigns;\nAbacha takes over",
            "color": ORANGE,
            "border": DEEP["orange"]
        }
    ]

    for ev in events:
        day = ev["day"]
        x_box = ev["x_box"]
        y_box = ev["y_box"]
        y_stem = ev["y_stem"]

        # Marker on the timeline
        ax.plot(day, y_line, marker="o", markersize=8, color=ev["border"], zorder=5)

        # Connector line from marker to callout box
        ax.plot([day, x_box], [y_stem, y_box + (-0.7 if y_box > 0 else 0.7)],
                color=ev["border"], lw=1.8, linestyle="--", zorder=3)
        ax.plot([day, day], [y_line, y_stem],
                color=ev["border"], lw=2.2, zorder=3)

        # Text box content
        full_text = f"$\\mathbf{{{ev['date']}}}$\n{ev['desc']}"
        ax.text(
            x_box, y_box,
            full_text,
            ha="center", va="center",
            fontsize=14,
            color=INK,
            bbox=dict(
                boxstyle="round,pad=0.6",
                facecolor=ev["color"],
                edgecolor=ev["border"],
                linewidth=2
            ),
            zorder=6
        )

    save(fig, out)
