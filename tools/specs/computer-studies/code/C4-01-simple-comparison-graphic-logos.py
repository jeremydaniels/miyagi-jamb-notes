from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 10)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_aspect('equal')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Main Diagram Title
    ax.text(6, 9.5, "Comparison of Graphics & Design Software", 
            ha='center', va='center', fontsize=18, weight='bold', color=INK)

    # 4 Software Panels: 2x2 grid
    # Centers / Bounding boxes
    # Top-Left: Paint (simple drawing)
    # Top-Right: CorelDraw (vector logo design with nodes)
    # Bottom-Left: Photoshop (editing a photograph)
    # Bottom-Right: AutoCAD (blueprint of a house)

    panels = [
        {"title": "MS Paint (Simple Drawing)", "type": "Raster / Bitmap", "x": 0.8, "y": 5.1, "w": 4.9, "h": 3.8},
        {"title": "CorelDraw (Vector Illustration)", "type": "Vector Graphics", "x": 6.3, "y": 5.1, "w": 4.9, "h": 3.8},
        {"title": "Photoshop (Photo Editing)", "type": "Image Manipulation", "x": 0.8, "y": 0.7, "w": 4.9, "h": 3.8},
        {"title": "AutoCAD (CAD Drafting)", "type": "Precision / Blueprint", "x": 6.3, "y": 0.7, "w": 4.9, "h": 3.8}
    ]

    # Draw panel frames
    for p in panels:
        # Outer card box
        rect = patches.FancyBboxPatch((p["x"], p["y"]), p["w"], p["h"],
                                      boxstyle="round,pad=0.1,rounding_size=0.15",
                                      facecolor=CREAM, edgecolor=GREY, lw=1.5)
        ax.add_patch(rect)
        # Title bar background
        title_bar = patches.FancyBboxPatch((p["x"], p["y"] + p["h"] - 0.75), p["w"], 0.75,
                                          boxstyle="round,pad=0.05,rounding_size=0.1",
                                          facecolor=LAV, edgecolor=GREY, lw=1.2)
        ax.add_patch(title_bar)
        
        # Panel Title & Category
        ax.text(p["x"] + 0.25, p["y"] + p["h"] - 0.38, p["title"],
                ha='left', va='center', fontsize=14, weight='bold', color=INK)
        ax.text(p["x"] + p["w"] - 0.25, p["y"] + p["h"] - 0.38, p["type"],
                ha='right', va='center', fontsize=14, color=DEEP["blue"], style='italic')

        # Screen area (canvas inside app)
        screen = patches.Rectangle((p["x"] + 0.25, p["y"] + 0.25), p["w"] - 0.5, p["h"] - 1.15,
                                   facecolor="white", edgecolor=GREY, lw=1)
        ax.add_patch(screen)

    # -------------------------------------------------------------
    # 1. MS Paint: Simple Drawing (House, Sun, Brush/Palette UI)
    # -------------------------------------------------------------
    px, py = 1.05, 5.35
    # Toolbar strip on top of canvas
    tool_bar = patches.Rectangle((px, py + 2.2), 4.4, 0.45, facecolor=CREAM, edgecolor=GREY, lw=0.8)
    ax.add_patch(tool_bar)
    # Tools icons (brush, bucket, pencil, palette dots)
    ax.text(px + 0.2, py + 2.42, "✏️  🖌️  🪣", fontsize=14, va='center')
    colors = [DEEP["pink"], DEEP["blue"], DEEP["green"], DEEP["orange"], INK]
    for i, col in enumerate(colors):
        ax.plot(px + 1.8 + i*0.25, py + 2.42, marker='s', markersize=7, color=col)

    # Simple child-like house
    # House body
    h_box = patches.Rectangle((px + 1.2, py + 0.3), 1.8, 1.1, facecolor=PINK, edgecolor=INK, lw=2)
    ax.add_patch(h_box)
    # House roof
    roof = patches.Polygon([[px + 1.0, py + 1.4], [px + 2.1, py + 2.05], [px + 3.2, py + 1.4]],
                           closed=True, facecolor=ORANGE, edgecolor=INK, lw=2)
    ax.add_patch(roof)
    # Door and Window
    door = patches.Rectangle((px + 1.8, py + 0.3), 0.5, 0.7, facecolor=CREAM, edgecolor=INK, lw=1.5)
    ax.add_patch(door)
    win = patches.Rectangle((px + 1.4, py + 0.8), 0.35, 0.35, facecolor="white", edgecolor=INK, lw=1.5)
    ax.add_patch(win)
    # Sun
    sun = patches.Circle((px + 3.7, py + 1.7), 0.3, facecolor=ORANGE, edgecolor=INK, lw=1.5)
    ax.add_patch(sun)
    # Sun rays
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        r1, r2 = 0.35, 0.5
        ax.plot([px + 3.7 + r1*np.cos(angle), px + 3.7 + r2*np.cos(angle)],
                [py + 1.7 + r1*np.sin(angle), py + 1.7 + r2*np.sin(angle)], color=INK, lw=1.5)
    
    # Simple caption
    ax.text(px + 2.2, py + 0.15, "Raster pixels & freehand shapes", ha='center', fontsize=14, color=INK)

    # -------------------------------------------------------------
    # 2. CorelDraw: Vector Logo Design with Bézier Handles & Nodes
    # -------------------------------------------------------------
    cx, cy = 6.55, 5.35
    # Smooth Bézier curve / Vector leaf-like or shield logo
    t = np.linspace(0, 1, 100)
    # Control points for curved vector shape
    P0 = np.array([cx + 1.0, cy + 0.8])
    P1 = np.array([cx + 1.0, cy + 2.2])
    P2 = np.array([cx + 3.4, cy + 2.2])
    P3 = np.array([cx + 3.4, cy + 0.8])
    curve = (1-t)**3 * P0[:,None] + 3*(1-t)**2*t * P1[:,None] + 3*(1-t)*t**2 * P2[:,None] + t**3 * P3[:,None]
    
    # Fill inner area with soft GREEN
    inner_curve = np.hstack([curve, np.array([[cx + 3.4, cx + 1.0], [cy + 0.8, cy + 0.8]])])
    ax.fill(inner_curve[0], inner_curve[1], color=GREEN, alpha=0.5)
    ax.plot(curve[0], curve[1], color=DEEP["green"], lw=3.0)

    # Node points (anchor points) - standard vector editor look
    nodes = [P0, P3, np.array([cx + 2.2, cy + 1.85])]
    for n in nodes:
        ax.plot(n[0], n[1], marker='s', markersize=8, color=DEEP["blue"], markeredgecolor=INK, markeredgewidth=1.2)

    # Tangent control handles
    handle_left = np.array([cx + 1.6, cy + 2.05])
    handle_right = np.array([cx + 2.8, cy + 2.05])
    mid_node = nodes[2]
    ax.plot([handle_left[0], handle_right[0]], [handle_left[1], handle_right[1]], '--', color=DEEP["orange"], lw=1.5)
    ax.plot(handle_left[0], handle_left[1], marker='o', markersize=6, color=DEEP["orange"])
    ax.plot(handle_right[0], handle_right[1], marker='o', markersize=6, color=DEEP["orange"])

    # Node label callout
    ax.annotate("Anchor nodes & handles", xy=(mid_node[0], mid_node[1]), xytext=(mid_node[0] - 0.2, cy + 2.4),
                fontsize=14, color=INK, ha='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    ax.text(cx + 2.2, cy + 0.35, "Scalable vector paths & anchors", ha='center', fontsize=14, color=INK)

    # -------------------------------------------------------------
    # 3. Photoshop: Photo Editing (Layers, Filters, Adjustment)
    # -------------------------------------------------------------
    sx, sy = 1.05, 0.95
    # Photograph canvas: Landscape with mountains and sun
    # Left side: "Before" / original, Right side: "After" / edited (enhanced contrast)
    photo_box = patches.Rectangle((sx + 0.2, sy + 0.4), 2.5, 2.0, facecolor=BLUE, edgecolor=INK, lw=1.5)
    ax.add_patch(photo_box)

    # Mountain shapes
    m1 = patches.Polygon([[sx + 0.2, sy + 0.4], [sx + 1.1, sy + 1.6], [sx + 2.0, sy + 0.4]],
                         closed=True, facecolor=GREY, edgecolor=INK, lw=1.2)
    m2 = patches.Polygon([[sx + 1.2, sy + 0.4], [sx + 2.1, sy + 1.8], [sx + 2.7, sy + 0.4]],
                         closed=True, facecolor=DEEP["green"], edgecolor=INK, lw=1.2)
    ax.add_patch(m1)
    ax.add_patch(m2)
    
    # Layer adjustment overlay box (floating UI palette)
    layer_panel = patches.Rectangle((sx + 2.9, sy + 0.4), 1.35, 2.0, facecolor=CREAM, edgecolor=GREY, lw=1)
    ax.add_patch(layer_panel)
    ax.text(sx + 3.57, sy + 2.2, "Layers", ha='center', fontsize=14, weight='bold', color=INK)
    
    # Mock layer strips
    layer_y = [sy + 1.65, sy + 1.25, sy + 0.85]
    layer_names = ["Adjustment", "Layer 1", "Background"]
    layer_colors = [ORANGE, LAV, "white"]
    for ly, l_name, lc in zip(layer_y, layer_names, layer_colors):
        l_rect = patches.Rectangle((sx + 3.0, ly - 0.15), 1.15, 0.3, facecolor=lc, edgecolor=GREY, lw=0.8)
        ax.add_patch(l_rect)
        ax.text(sx + 3.08, ly, l_name, fontsize=14, va='center', color=INK)

    # Selection marquee around part of image
    marquee = patches.Rectangle((sx + 0.7, sy + 0.8), 1.3, 0.9,
                                linestyle='--', edgecolor=DEEP["pink"], facecolor='none', lw=2)
    ax.add_patch(marquee)
    ax.text(sx + 1.35, sy + 0.15, "Photo retouching & layer stack", ha='center', fontsize=14, color=INK)

    # -------------------------------------------------------------
    # 4. AutoCAD: House Blueprint (Architectural Drafting)
    # -------------------------------------------------------------
    bx, by = 6.55, 0.95
    # Blueprint styling: Floor plan with dimension arrows
    # Outer walls
    ax.plot([bx + 0.6, bx + 3.8, bx + 3.8, bx + 0.6, bx + 0.6],
            [by + 0.5, by + 0.5, by + 2.2, by + 2.2, by + 0.5],
            color=DEEP["blue"], lw=3)
    
    # Interior room division walls
    ax.plot([bx + 2.2, bx + 2.2], [by + 0.5, by + 2.2], color=DEEP["blue"], lw=2)
    ax.plot([bx + 0.6, bx + 2.2], [by + 1.3, by + 1.3], color=DEEP["blue"], lw=2)

    # Room Labels
    ax.text(bx + 1.4, by + 1.75, "ROOM 1", ha='center', va='center', fontsize=14, weight='bold', color=INK)
    ax.text(bx + 1.4, by + 0.9, "KITCHEN", ha='center', va='center', fontsize=14, weight='bold', color=INK)
    ax.text(bx + 3.0, by + 1.35, "LIVING\nROOM", ha='center', va='center', fontsize=14, weight='bold', color=INK)

    # Door swing arcs (drafting standard)
    arc1 = patches.Arc((bx + 2.2, by + 0.9), 0.6, 0.6, angle=0, theta1=90, theta2=180, color=DEEP["blue"], lw=1.5)
    ax.add_patch(arc1)
    ax.plot([bx + 2.2, bx + 2.2], [by + 0.9, by + 1.2], color=DEEP["blue"], lw=1.5)

    # Dimension line on top
    dim_y = by + 2.45
    ax.annotate("", xy=(bx + 0.6, dim_y), xytext=(bx + 3.8, dim_y),
                arrowprops=dict(arrowstyle="<->", color=DEEP["pink"], lw=1.5))
    ax.plot([bx + 0.6, bx + 0.6], [by + 2.25, dim_y + 0.1], color=GREY, lw=1)
    ax.plot([bx + 3.8, bx + 3.8], [by + 2.25, dim_y + 0.1], color=GREY, lw=1)
    ax.text(bx + 2.2, dim_y, "10.50 m", ha='center', va='center', fontsize=14,
            bbox=dict(fc="white", ec='none', pad=1), color=DEEP["pink"], weight='bold')

    ax.text(bx + 2.2, by + 0.15, "Precise CAD architectural blueprint", ha='center', fontsize=14, color=INK)

    save(fig, out)
