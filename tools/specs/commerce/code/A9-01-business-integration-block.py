from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Title
    ax.text(7, 9.5, "Types of Business Combinations", ha="center", va="center", 
            fontsize=18, weight="bold", color=INK)

    # Box styling helper
    def draw_box(x, y, w, h, text, bg_col, edge_col=INK, highlight=False):
        lw = 2.5 if highlight else 1.5
        rect = patches.FancyBboxPatch(
            (x - w / 2, y - h / 2), w, h,
            boxstyle="round,pad=0.1,rounding_size=0.15",
            facecolor=bg_col, edgecolor=edge_col, linewidth=lw
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha="center", va="center", fontsize=15, 
                weight="bold" if highlight else "normal", color=INK)

    # Supply Chain Boxes
    bw, bh = 3.6, 0.9
    cx = 5.6
    y_ranch = 8.2
    y_tannery = 6.2
    y_shoe = 4.2
    y_retail = 2.2

    draw_box(cx, y_ranch, bw, bh, "Cattle Ranch", CREAM)
    draw_box(cx, y_tannery, bw, bh, "Leather Tannery", CREAM)
    draw_box(cx, y_shoe, bw, bh, "Shoe Factory", BLUE, edge_col=DEEP["blue"], highlight=True)
    draw_box(cx, y_retail, bw, bh, "Shoe Retail Shop", CREAM)

    # Rival Shoe Factory
    rx = 1.6
    draw_box(rx, y_shoe, 2.8, bh, "Rival Shoe Factory", LAV, edge_col=DEEP["lav"])

    # Conglomerate
    cdx = 11.5
    draw_box(cdx, y_shoe, 3.2, bh, "Soft Drink Factory", ORANGE, edge_col=DEEP["orange"])

    # Horizontal Integration
    ax.annotate(
        "", xy=(rx + 1.4, y_shoe), xytext=(cx - bw / 2, y_shoe),
        arrowprops=dict(arrowstyle="<->", lw=2.5, color=DEEP["blue"], mutation_scale=18)
    )
    ax.text(
        (rx + 1.4 + cx - bw / 2) / 2, y_shoe + 0.3,
        "Horizontal Integration", ha="center", va="bottom",
        fontsize=14, color=DEEP["blue"], weight="bold",
        bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none")
    )

    # Conglomerate Integration (dashed line, originating from shoe factory)
    ax.annotate(
        "", xy=(cdx - 1.6, y_shoe), xytext=(cx + bw / 2, y_shoe),
        arrowprops=dict(arrowstyle="<->", lw=2.2, ls="--", color=DEEP["orange"], mutation_scale=18)
    )
    ax.text(
        (cx + bw / 2 + cdx - 1.6) / 2, y_shoe + 0.3,
        "Conglomerate Integration", ha="center", va="bottom",
        fontsize=14, color=DEEP["orange"], weight="bold",
        bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none")
    )

    # Backward Vertical Integration
    v_arrow_x = cx + bw / 2 + 0.35
    ax.annotate(
        "", xy=(v_arrow_x, y_tannery), xytext=(v_arrow_x, y_shoe + bh / 2 - 0.1),
        arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["green"], mutation_scale=18)
    )
    ax.text(
        v_arrow_x + 0.15, (y_tannery + y_shoe) / 2,
        "Backward Vertical Integration", ha="left", va="center",
        fontsize=14, color=DEEP["green"], weight="bold",
        bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none")
    )

    # Forward Vertical Integration
    ax.annotate(
        "", xy=(v_arrow_x, y_retail), xytext=(v_arrow_x, y_shoe - bh / 2 + 0.1),
        arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["green"], mutation_scale=18)
    )
    ax.text(
        v_arrow_x + 0.15, (y_shoe + y_retail) / 2,
        "Forward Vertical Integration", ha="left", va="center",
        fontsize=14, color=DEEP["green"], weight="bold",
        bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none")
    )
    
    # Supply chain downward flow arrows (grey / subtle)
    chain_arrows = [
        (y_ranch - bh / 2, y_tannery + bh / 2),
        (y_tannery - bh / 2, y_shoe + bh / 2),
        (y_shoe - bh / 2, y_retail + bh / 2)
    ]
    for y1, y2 in chain_arrows:
        ax.annotate(
            "", xy=(cx, y2), xytext=(cx, y1),
            arrowprops=dict(arrowstyle="->", lw=1.8, color=GREY, mutation_scale=15)
        )

    save(fig, out)
