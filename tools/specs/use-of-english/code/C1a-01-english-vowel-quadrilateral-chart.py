from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 8.2)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.8, 9.0)
    ax.axis("off")

    y_close = 7.0
    y_cm = 5.0
    y_om = 3.0
    y_open = 1.0
    y_levels = [y_close, y_cm, y_om, y_open]

    def front_x(y):
        return 2.2 + (7.0 - y) / 6.0 * 1.6

    def back_x(y):
        return 8.8 - (7.0 - y) / 6.0 * 2.0

    def central_x(y):
        return (front_x(y) + back_x(y)) / 2.0

    grid_lw = 2.0
    grid_color = GREY

    for y in y_levels:
        ax.plot([front_x(y), back_x(y)], [y, y], color=grid_color, lw=grid_lw, zorder=1)

    for frac in [0.0, 0.5, 1.0]:
        xs = [front_x(y) + frac * (back_x(y) - front_x(y)) for y in [7.0, 1.0]]
        ax.plot(xs, [7.0, 1.0], color=grid_color, lw=grid_lw, ls="--" if frac == 0.5 else "-", zorder=1)

    ax.text(front_x(7.0), 7.6, "Front", fontsize=16, ha="center", va="bottom", color=INK, weight="bold")
    ax.text(central_x(7.0), 7.6, "Central", fontsize=16, ha="center", va="bottom", color=INK, weight="bold")
    ax.text(back_x(7.0), 7.6, "Back", fontsize=16, ha="center", va="bottom", color=INK, weight="bold")

    height_labels = [
        (y_close, "Close"),
        (y_cm, "Close-mid"),
        (y_om, "Open-mid"),
        (y_open, "Open")
    ]
    for y, label in height_labels:
        ax.text(front_x(y) - 0.4, y, label, fontsize=15, ha="right", va="center", color=INK, weight="bold")

    ax.text(0.6, 8.45, "Front of mouth on the left", fontsize=14, fontstyle="italic", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    ax.text(5.5, 8.5, "English Vowel Quadrilateral (RP Monophthongs)", fontsize=17, ha="center", va="bottom", color=INK, weight="bold")

    vowels = [
        {"sym": "/iː/", "word": "see", "pos": (front_x(7.0), 7.0), "long": True, "offset": (0.2, 0.15), "ha": "left"},
        {"sym": "/ɪ/", "word": "sit", "pos": (front_x(6.0) + 0.6, 6.0), "long": False, "offset": (0.2, 0.15), "ha": "left"},
        {"sym": "/e/", "word": "bed", "pos": (front_x(4.0), 4.0), "long": False, "offset": (0.2, 0.15), "ha": "left"},
        {"sym": "/æ/", "word": "cat", "pos": (front_x(1.5), 1.5), "long": False, "offset": (0.2, 0.15), "ha": "left"},
        
        {"sym": "/ɜː/", "word": "bird", "pos": (central_x(4.5), 4.5), "long": True, "offset": (0.2, 0.15), "ha": "left"},
        {"sym": "/ə/", "word": "about", "pos": (central_x(3.8), 3.8), "long": False, "offset": (0.2, -0.2), "ha": "left"},
        {"sym": "/ʌ/", "word": "cup", "pos": (central_x(1.8), 1.8), "long": False, "offset": (-0.2, 0.25), "ha": "right"},
        
        {"sym": "/uː/", "word": "food", "pos": (back_x(7.0), 7.0), "long": True, "offset": (-0.2, -0.35), "ha": "right"},
        {"sym": "/ʊ/", "word": "book", "pos": (back_x(6.0) - 0.6, 6.0), "long": False, "offset": (-0.2, 0.15), "ha": "right"},
        {"sym": "/ɔː/", "word": "law", "pos": (back_x(4.0), 4.0), "long": True, "offset": (-0.2, 0.15), "ha": "right"},
        {"sym": "/ɒ/", "word": "hot", "pos": (back_x(1.5), 1.5), "long": False, "offset": (0.2, 0.2), "ha": "left"},
        {"sym": "/ɑː/", "word": "car", "pos": (back_x(1.0), 1.0), "long": True, "offset": (-0.2, 0.25), "ha": "right"},
    ]

    for v in vowels:
        px, py = v["pos"]
        col = DEEP["blue"] if v["long"] else DEEP["orange"]
        ax.plot(px, py, "o", markersize=10, color=col, zorder=5)

        ox, oy = v["offset"]
        label_text = f"{v['sym']} \"{v['word']}\""
        
        ax.text(px + ox, py + oy, label_text, fontsize=14, ha=v["ha"], va="center",
                color=INK, weight="medium",
                bbox=dict(fc="white", ec="none", pad=1.5, alpha=0.9), zorder=6)

    leg_y = -0.3
    ax.plot(3.0, leg_y, "o", markersize=9, color=DEEP["blue"])
    ax.text(3.25, leg_y, "Long vowel", fontsize=15, va="center", color=INK)

    ax.plot(6.0, leg_y, "o", markersize=9, color=DEEP["orange"])
    ax.text(6.25, leg_y, "Short vowel", fontsize=15, va="center", color=INK)

    save(fig, out)
