from style import *
import numpy as np
import matplotlib.patches as patches

def draw_soldier(ax, cx, cy, scale=0.4):
    # Helmet / head
    helmet = patches.Arc((cx, cy + 0.12 * scale), 0.6 * scale, 0.5 * scale, angle=0, theta1=0, theta2=180, color=DEEP["blue"], lw=2.5)
    ax.add_patch(helmet)
    ax.plot([cx - 0.35 * scale, cx + 0.35 * scale], [cy + 0.12 * scale, cy + 0.12 * scale], color=DEEP["blue"], lw=2.5)
    # Face outline
    ax.plot([cx - 0.22 * scale, cx - 0.22 * scale, cx + 0.22 * scale, cx + 0.22 * scale], 
            [cy + 0.12 * scale, cy - 0.05 * scale, cy - 0.05 * scale, cy + 0.12 * scale], color=DEEP["blue"], lw=2)
    # Shoulders / body
    body = patches.Polygon([[cx - 0.45 * scale, cy - 0.4 * scale], 
                            [cx - 0.3 * scale, cy - 0.12 * scale], 
                            [cx + 0.3 * scale, cy - 0.12 * scale], 
                            [cx + 0.45 * scale, cy - 0.4 * scale]], 
                           closed=True, edgecolor=DEEP["blue"], facecolor=BLUE, lw=2)
    ax.add_patch(body)

def draw_coin(ax, cx, cy, scale=0.4):
    outer = patches.Circle((cx, cy), 0.35 * scale, edgecolor=DEEP["blue"], facecolor=CREAM, lw=2.5)
    inner = patches.Circle((cx, cy), 0.28 * scale, edgecolor=DEEP["blue"], facecolor="none", lw=1.5, ls="--")
    ax.add_patch(outer)
    ax.add_patch(inner)
    ax.text(cx, cy, "₦", color=DEEP["blue"], fontsize=18, weight="bold", ha="center", va="center")

def draw_grad_cap(ax, cx, cy, scale=0.4):
    # Diamond top
    diamond = patches.Polygon([[cx, cy + 0.25 * scale], 
                              [cx + 0.45 * scale, cy + 0.05 * scale], 
                              [cx, cy - 0.15 * scale], 
                              [cx - 0.45 * scale, cy + 0.05 * scale]], 
                             closed=True, edgecolor=DEEP["orange"], facecolor=ORANGE, lw=2)
    ax.add_patch(diamond)
    # Skull cap under
    skull = patches.Polygon([[cx - 0.22 * scale, cy - 0.06 * scale],
                             [cx - 0.22 * scale, cy - 0.3 * scale],
                             [cx + 0.22 * scale, cy - 0.3 * scale],
                             [cx + 0.22 * scale, cy - 0.06 * scale]],
                            closed=True, edgecolor=DEEP["orange"], facecolor=CREAM, lw=2)
    ax.add_patch(skull)
    # Tassel
    ax.plot([cx, cx + 0.38 * scale, cx + 0.38 * scale], 
            [cy + 0.05 * scale, cy - 0.05 * scale, cy - 0.25 * scale], 
            color=DEEP["orange"], lw=2)

def draw_factory(ax, cx, cy, scale=0.4):
    # Main building with saw-tooth roof
    poly = patches.Polygon([
        [cx - 0.4 * scale, cy - 0.35 * scale],
        [cx - 0.4 * scale, cy + 0.1 * scale],
        [cx - 0.15 * scale, cy - 0.05 * scale],
        [cx - 0.15 * scale, cy + 0.1 * scale],
        [cx + 0.15 * scale, cy - 0.05 * scale],
        [cx + 0.15 * scale, cy + 0.2 * scale],
        [cx + 0.4 * scale, cy + 0.2 * scale],
        [cx + 0.4 * scale, cy - 0.35 * scale]
    ], closed=True, edgecolor=DEEP["orange"], facecolor=ORANGE, lw=2)
    ax.add_patch(poly)
    # Chimney smoke / line
    ax.plot([cx + 0.25 * scale, cx + 0.25 * scale], [cy + 0.2 * scale, cy + 0.35 * scale], color=DEEP["orange"], lw=2.5)
    ax.plot([cx + 0.32 * scale, cx + 0.32 * scale], [cy + 0.2 * scale, cy + 0.3 * scale], color=DEEP["orange"], lw=2)

def draw_chief_crown(ax, cx, cy, scale=0.4):
    # Cap / Crown of chief with bead patterns
    crown = patches.Polygon([
        [cx - 0.35 * scale, cy - 0.25 * scale],
        [cx - 0.38 * scale, cy + 0.15 * scale],
        [cx - 0.15 * scale, cy + 0.05 * scale],
        [cx, cy + 0.3 * scale],
        [cx + 0.15 * scale, cy + 0.05 * scale],
        [cx + 0.38 * scale, cy + 0.15 * scale],
        [cx + 0.35 * scale, cy - 0.25 * scale]
    ], closed=True, edgecolor=DEEP["green"], facecolor=GREEN, lw=2)
    ax.add_patch(crown)
    # Feather/plume
    ax.plot([cx, cx + 0.1 * scale, cx + 0.25 * scale], 
            [cy + 0.3 * scale, cy + 0.45 * scale, cy + 0.48 * scale], 
            color=DEEP["green"], lw=2.5)

def draw_market(ax, cx, cy, scale=0.4):
    # Stall canopy / roof
    canopy = patches.Polygon([
        [cx - 0.45 * scale, cy + 0.1 * scale],
        [cx - 0.35 * scale, cy + 0.3 * scale],
        [cx + 0.35 * scale, cy + 0.3 * scale],
        [cx + 0.45 * scale, cy + 0.1 * scale]
    ], closed=True, edgecolor=DEEP["green"], facecolor=GREEN, lw=2)
    ax.add_patch(canopy)
    # Stall posts & table
    ax.plot([cx - 0.35 * scale, cx - 0.35 * scale], [cy + 0.1 * scale, cy - 0.35 * scale], color=DEEP["green"], lw=2)
    ax.plot([cx + 0.35 * scale, cx + 0.35 * scale], [cy + 0.1 * scale, cy - 0.35 * scale], color=DEEP["green"], lw=2)
    ax.plot([cx - 0.4 * scale, cx + 0.4 * scale], [cy - 0.1 * scale, cy - 0.1 * scale], color=DEEP["green"], lw=2.5)
    # Baskets/goods on table
    b1 = patches.Circle((cx - 0.15 * scale, cy - 0.02 * scale), 0.08 * scale, color=CREAM, ec=DEEP["green"], lw=1.5)
    b2 = patches.Circle((cx + 0.15 * scale, cy - 0.02 * scale), 0.08 * scale, color=CREAM, ec=DEEP["green"], lw=1.5)
    ax.add_patch(b1)
    ax.add_patch(b2)

def draw(out):
    # Increased width to 14 to give more space for text labels
    fig = canvas(14, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(7.0, 7.0, "Division of Legislative Powers under the 1954 Constitution", 
            fontsize=18, weight="bold", ha="center", va="center", color=INK)

    cols = [
        {
            "x": 0.6, "w": 4.0,
            "title": "Exclusive List",
            "sub": "(Federal Only)",
            "header_bg": BLUE, "line_col": DEEP["blue"],
            "items": [
                {"label": "Defence", "draw": draw_soldier},
                {"label": "Currency", "draw": draw_coin}
            ]
        },
        {
            "x": 5.0, "w": 4.0,
            "title": "Concurrent List",
            "sub": "(Federal & Regional)",
            "header_bg": ORANGE, "line_col": DEEP["orange"],
            "items": [
                {"label": "Higher Education", "draw": draw_grad_cap},
                {"label": "Industry", "draw": draw_factory}
            ]
        },
        {
            "x": 9.4, "w": 4.0,
            "title": "Residual List",
            "sub": "(Regional Only)",
            "header_bg": GREEN, "line_col": DEEP["green"],
            "items": [
                {"label": "Chieftaincy", "draw": draw_chief_crown},
                {"label": "Local trade", "draw": draw_market}
            ]
        }
    ]

    card_y = 0.6
    card_h = 5.8
    header_h = 1.3

    for col in cols:
        x, w = col["x"], col["w"]
        # Outer Card
        outer_card = patches.FancyBboxPatch((x, card_y), w, card_h,
                                            boxstyle="round,pad=0.0,rounding_size=0.15",
                                            facecolor="white", edgecolor=GREY, lw=1.5)
        ax.add_patch(outer_card)

        # Header Box
        header_box = patches.FancyBboxPatch((x, card_y + card_h - header_h), w, header_h,
                                            boxstyle="round,pad=0.0,rounding_size=0.15",
                                            facecolor=col["header_bg"], edgecolor=col["line_col"], lw=1.5)
        ax.add_patch(header_box)
        
        # Header text
        ax.text(x + w / 2.0, card_y + card_h - 0.45, col["title"],
                fontsize=16, weight="bold", ha="center", va="center", color=INK)
        ax.text(x + w / 2.0, card_y + card_h - 0.85, col["sub"],
                fontsize=14, weight="normal", ha="center", va="center", color=INK)

        # Draw items (2 per column)
        item_centers_y = [card_y + card_h - 2.4, card_y + card_h - 4.2]
        for i, it in enumerate(col["items"]):
            cy = item_centers_y[i]
            # Sub-card background
            sub_box = patches.FancyBboxPatch((x + 0.25, cy - 0.6), w - 0.5, 1.35,
                                             boxstyle="round,pad=0.0,rounding_size=0.1",
                                             facecolor=CREAM, edgecolor=GREY, lw=1.0)
            ax.add_patch(sub_box)
            # Icon
            it["draw"](ax, x + 0.95, cy + 0.08, scale=1.1)
            # Label
            ax.text(x + 1.65, cy + 0.08, it["label"], fontsize=15, weight="bold",
                    ha="left", va="center", color=INK)

    save(fig, out)
