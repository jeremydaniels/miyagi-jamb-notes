from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.axis("off")

    # Quadrant wedges (Wedge angles: 0-360)
    # Top-Right (Price): 0 to 90
    # Top-Left (Product): 90 to 180
    # Bottom-Left (Place): 180 to 270
    # Bottom-Right (Promotion): 270 to 360
    r_outer = 4.3
    r_inner = 1.6

    wedge_product = patches.Wedge((0, 0), r_outer, 90, 180, width=r_outer-r_inner,
                                  facecolor=BLUE, edgecolor="white", lw=4)
    wedge_price = patches.Wedge((0, 0), r_outer, 0, 90, width=r_outer-r_inner,
                                facecolor=GREEN, edgecolor="white", lw=4)
    wedge_place = patches.Wedge((0, 0), r_outer, 180, 270, width=r_outer-r_inner,
                                facecolor=ORANGE, edgecolor="white", lw=4)
    wedge_promo = patches.Wedge((0, 0), r_outer, 270, 360, width=r_outer-r_inner,
                                facecolor=PINK, edgecolor="white", lw=4)

    for w in [wedge_product, wedge_price, wedge_place, wedge_promo]:
        ax.add_patch(w)

    # Centre circle for Target Market
    centre_circle = patches.Circle((0, 0), r_inner, facecolor="white", edgecolor=INK, lw=2.5)
    ax.add_patch(centre_circle)
    ax.text(0, 0, "Target\nMarket", ha="center", va="center", fontsize=17, weight="bold", color=INK)

    # --- TOP LEFT: Product (Box & Star) ---
    ax.text(-2.6, 3.4, "Product", ha="center", va="center", fontsize=18, weight="bold", color=DEEP["blue"])
    
    # Physical Box Icon
    box_x, box_y = -3.2, 1.8
    # Isometric box / simple flat box
    ax.add_patch(patches.Rectangle((box_x - 0.45, box_y - 0.45), 0.9, 0.9, facecolor="white", edgecolor=DEEP["blue"], lw=2))
    # Box flaps/lines
    ax.plot([box_x - 0.45, box_x + 0.45], [box_y, box_y], color=DEEP["blue"], lw=1.5)
    ax.plot([box_x, box_x], [box_y, box_y + 0.45], color=DEEP["blue"], lw=1.5)

    # Star Icon
    star_x, star_y = -1.8, 2.3
    angles = np.linspace(0, 2 * np.pi, 11)[:-1] - np.pi / 2
    r_star = np.array([0.45, 0.2] * 5)
    sx = star_x + r_star * np.cos(angles)
    sy = star_y - r_star * np.sin(angles)
    star_poly = patches.Polygon(np.column_stack([sx, sy]), facecolor="white", edgecolor=DEEP["blue"], lw=2)
    ax.add_patch(star_poly)

    # --- TOP RIGHT: Price (Price tag & Naira sign ₦) ---
    ax.text(2.6, 3.4, "Price", ha="center", va="center", fontsize=18, weight="bold", color=DEEP["green"])
    
    # Price Tag Icon
    pt_x, pt_y = 1.9, 2.1
    tag_coords = np.array([
        [pt_x - 0.4, pt_y - 0.5],
        [pt_x + 0.2, pt_y - 0.5],
        [pt_x + 0.5, pt_y],
        [pt_x + 0.2, pt_y + 0.5],
        [pt_x - 0.4, pt_y + 0.5]
    ])
    tag_poly = patches.Polygon(tag_coords, facecolor="white", edgecolor=DEEP["green"], lw=2)
    ax.add_patch(tag_poly)
    ax.add_patch(patches.Circle((pt_x + 0.2, pt_y), 0.08, facecolor=DEEP["green"]))

    # Naira sign (₦)
    ax.text(3.2, 2.0, "₦", ha="center", va="center", fontsize=28, weight="bold", color=DEEP["green"],
            bbox=dict(boxstyle="circle,pad=0.2", facecolor="white", edgecolor=DEEP["green"], lw=2))

    # --- BOTTOM LEFT: Place (Delivery truck & Map pin) ---
    ax.text(-2.6, -3.5, "Place", ha="center", va="center", fontsize=18, weight="bold", color=DEEP["orange"])

    # Delivery Truck Icon
    tk_x, tk_y = -3.2, -2.1
    # Cargo body
    ax.add_patch(patches.Rectangle((tk_x - 0.55, tk_y - 0.2), 0.7, 0.55, facecolor="white", edgecolor=DEEP["orange"], lw=2))
    # Cabin
    cabin_coords = np.array([
        [tk_x + 0.15, tk_y - 0.2],
        [tk_x + 0.5, tk_y - 0.2],
        [tk_x + 0.5, tk_y + 0.1],
        [tk_x + 0.35, tk_y + 0.3],
        [tk_x + 0.15, tk_y + 0.3]
    ])
    ax.add_patch(patches.Polygon(cabin_coords, facecolor="white", edgecolor=DEEP["orange"], lw=2))
    # Wheels
    ax.add_patch(patches.Circle((tk_x - 0.3, tk_y - 0.25), 0.12, facecolor="white", edgecolor=DEEP["orange"], lw=2))
    ax.add_patch(patches.Circle((tk_x + 0.32, tk_y - 0.25), 0.12, facecolor="white", edgecolor=DEEP["orange"], lw=2))

    # Map Pin Icon
    pin_x, pin_y = -1.8, -2.1
    # Pin head
    ax.add_patch(patches.Circle((pin_x, pin_y + 0.15), 0.32, facecolor="white", edgecolor=DEEP["orange"], lw=2))
    # Pin inner dot
    ax.add_patch(patches.Circle((pin_x, pin_y + 0.15), 0.11, facecolor=DEEP["orange"]))
    # Pin pointer
    pointer = np.array([
        [pin_x - 0.22, pin_y],
        [pin_x + 0.22, pin_y],
        [pin_x, pin_y - 0.4]
    ])
    ax.add_patch(patches.Polygon(pointer, facecolor="white", edgecolor=DEEP["orange"], lw=2))
    # Redraw head circle over base of pointer to look seamless
    ax.add_patch(patches.Circle((pin_x, pin_y + 0.15), 0.3, facecolor="white", edgecolor="none"))
    ax.add_patch(patches.Circle((pin_x, pin_y + 0.15), 0.11, facecolor=DEEP["orange"]))

    # --- BOTTOM RIGHT: Promotion (Megaphone) ---
    ax.text(2.6, -3.5, "Promotion", ha="center", va="center", fontsize=18, weight="bold", color=DEEP["pink"])

    # Megaphone Icon
    mg_x, mg_y = 2.4, -2.1
    # Cone
    cone_pts = np.array([
        [mg_x - 0.4, mg_y - 0.15],
        [mg_x + 0.35, mg_y + 0.45],
        [mg_x + 0.35, mg_y - 0.45],
        [mg_x - 0.4, mg_y + 0.15]
    ])
    ax.add_patch(patches.Polygon(cone_pts, facecolor="white", edgecolor=DEEP["pink"], lw=2))
    # Front rim / ellipse
    ax.add_patch(patches.Ellipse((mg_x + 0.35, mg_y), 0.18, 0.9, facecolor="white", edgecolor=DEEP["pink"], lw=2))
    # Back handle / mouthpiece
    ax.add_patch(patches.Rectangle((mg_x - 0.55, mg_y - 0.12), 0.15, 0.24, facecolor="white", edgecolor=DEEP["pink"], lw=2))
    # Handle grip
    handle_pts = np.array([
        [mg_x - 0.25, mg_y - 0.1],
        [mg_x - 0.15, mg_y - 0.1],
        [mg_x - 0.2, mg_y - 0.42],
        [mg_x - 0.3, mg_y - 0.42]
    ])
    ax.add_patch(patches.Polygon(handle_pts, facecolor="white", edgecolor=DEEP["pink"], lw=2))
    # Sound waves
    ax.plot([mg_x + 0.6, mg_x + 0.72], [mg_y + 0.25, mg_y + 0.35], color=DEEP["pink"], lw=2)
    ax.plot([mg_x + 0.65, mg_x + 0.8], [mg_y, mg_y], color=DEEP["pink"], lw=2)
    ax.plot([mg_x + 0.6, mg_x + 0.72], [mg_y - 0.25, mg_y - 0.35], color=DEEP["pink"], lw=2)

    save(fig, out)
