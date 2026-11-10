from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 14)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # Title & Subtitle
    ax.text(50, 96, "The Four Economic Sectors", fontsize=18, fontweight="bold", ha="center", color=INK)
    ax.text(50, 93, "Circular flow: from raw materials to advanced knowledge", fontsize=15, ha="center", color=INK)

    # Sector configs
    # To form a true non-zigzag cycle (a circle), we route:
    # TL (Primary) -> TR (Secondary) -> BR (Quaternary) -> BL (Tertiary) -> TL (Primary)
    sectors = [
        {"id": "primary", "title": "PRIMARY", "subtitle": "Raw Materials", "cx": 25, "cy": 74, "color": GREEN, "deep": DEEP["green"]},
        {"id": "secondary", "title": "SECONDARY", "subtitle": "Manufacturing", "cx": 75, "cy": 74, "color": ORANGE, "deep": DEEP["orange"]},
        {"id": "tertiary", "title": "TERTIARY", "subtitle": "Services & Retail", "cx": 25, "cy": 26, "color": BLUE, "deep": DEEP["blue"]},
        {"id": "quaternary", "title": "QUATERNARY", "subtitle": "Knowledge & IT", "cx": 75, "cy": 26, "color": LAV, "deep": DEEP["lav"]}
    ]

    w, h = 38, 30
    for sec in sectors:
        x0 = sec["cx"] - w / 2
        y0 = sec["cy"] - h / 2
        card = patches.FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=1.0,rounding_size=2.0",
                                      fc=sec["color"], ec=sec["deep"], lw=2.5, zorder=2)
        ax.add_patch(card)
        
        header_h = 7.0
        header = patches.FancyBboxPatch((x0 + 0.3, y0 + h - header_h), w - 0.6, header_h - 0.3,
                                        boxstyle="round,pad=0.5,rounding_size=1.5",
                                        fc="white", ec=sec["deep"], lw=2, zorder=3)
        ax.add_patch(header)
        ax.text(sec["cx"], y0 + h - 2.8, sec["title"], fontsize=16, fontweight="bold",
                color=sec["deep"], ha="center", va="center", zorder=4)
        ax.text(sec["cx"], y0 + h - 5.5, sec["subtitle"], fontsize=14, fontstyle="italic",
                color=INK, ha="center", va="center", zorder=4)

    # 1. PRIMARY (TL)
    px, py = 25, 74
    # Farmer harvesting crops
    ax.text(15, py - 10, "Farmer\nharvesting crops", fontsize=14, ha="center", color=INK, zorder=5)
    for cx in np.linspace(11, 19, 5):
        ax.plot([cx, cx], [py-6, py-2], color=DEEP["green"], lw=2, zorder=4)
    ax.add_patch(patches.Circle((15, py+3), 1.2, fc=CREAM, ec=INK, lw=1.5, zorder=5)) # Farmer head
    ax.plot([15, 15], [py+1.8, py-3], color=INK, lw=2, zorder=5) # Body
    
    # Oil rig
    ax.text(35, py - 10, "Oil rig\nextraction", fontsize=14, ha="center", color=INK, zorder=5)
    ax.plot([32, 35, 38], [py-6, py+4, py-6], color=INK, lw=2, zorder=4) # Derrick
    ax.plot([33, 37], [py-1, py-1], color=INK, lw=1.5, zorder=4)
    ax.plot([34, 36], [py+1.5, py+1.5], color=INK, lw=1.5, zorder=4)

    # 2. SECONDARY (TR)
    sx, sy = 75, 74
    # Factory with smokestacks
    ax.text(65, sy - 10, "Factory &\nsmokestacks", fontsize=14, ha="center", color=INK, zorder=5)
    ax.add_patch(patches.Rectangle((61, sy-5), 8, 6, fc=CREAM, ec=INK, lw=2, zorder=4))
    ax.plot([63, 63], [sy+1, sy+5], color=INK, lw=3, zorder=4)
    ax.plot([66, 66], [sy+1, sy+4], color=INK, lw=3, zorder=4)
    ax.add_patch(patches.Circle((63, sy+6), 0.8, fc="white", ec=GREY, lw=1, zorder=5))
    
    # Worker welding car
    ax.text(85, sy - 10, "Worker\nwelding a car", fontsize=14, ha="center", color=INK, zorder=5)
    ax.plot([81, 89], [sy-4, sy-4], color=INK, lw=3, zorder=4) # Car body
    ax.add_patch(patches.Circle((83, sy-4), 1, fc=GREY, ec=INK, lw=1.5, zorder=5))
    ax.add_patch(patches.Circle((87, sy-4), 1, fc=GREY, ec=INK, lw=1.5, zorder=5))
    ax.add_patch(patches.Circle((83, sy+2), 1, fc=CREAM, ec=INK, lw=1.5, zorder=5)) # Worker
    ax.plot([83, 83], [sy+1, sy-2], color=INK, lw=2, zorder=5)
    ax.plot([83, 85], [sy, sy-2], color=INK, lw=2, zorder=5) # Welding arm
    ax.scatter([85.5], [sy-2.5], s=80, color=DEEP["orange"], marker="*", zorder=6) # Spark

    # 3. TERTIARY (BL)
    tx, ty = 25, 26
    # Retail shop counter & cashier
    ax.text(15, ty - 10, "Retail shop &\ncashier", fontsize=14, ha="center", color=INK, zorder=5)
    ax.add_patch(patches.Rectangle((12, ty-5), 6, 4, fc=CREAM, ec=INK, lw=2, zorder=4)) # Counter
    ax.add_patch(patches.Circle((15, ty+2), 1.2, fc=CREAM, ec=INK, lw=1.5, zorder=5)) # Cashier
    ax.plot([15, 15], [ty+0.8, ty-1], color=INK, lw=2, zorder=5)
    
    # Delivery truck
    ax.text(35, ty - 10, "Delivery\ntruck", fontsize=14, ha="center", color=INK, zorder=5)
    ax.add_patch(patches.Rectangle((31, ty-3), 6, 5, fc=CREAM, ec=INK, lw=2, zorder=4))
    ax.add_patch(patches.Rectangle((37, ty-3), 2.5, 3, fc=CREAM, ec=INK, lw=2, zorder=4))
    ax.add_patch(patches.Circle((33, ty-3), 1, fc=GREY, ec=INK, lw=1.5, zorder=5))
    ax.add_patch(patches.Circle((38, ty-3), 1, fc=GREY, ec=INK, lw=1.5, zorder=5))

    # 4. QUATERNARY (BR)
    qx, qy = 75, 26
    # Scientist looking through microscope
    ax.text(65, qy - 10, "Scientist &\nmicroscope", fontsize=14, ha="center", color=INK, zorder=5)
    ax.plot([62, 68], [qy-4, qy-4], color=INK, lw=2, zorder=4) # Table
    ax.plot([66, 66], [qy-4, qy-1], color=INK, lw=2, zorder=5) # Microscope
    ax.add_patch(patches.Circle((64, qy+2), 1.2, fc=CREAM, ec=INK, lw=1.5, zorder=5)) # Scientist
    ax.plot([64, 64], [qy+0.8, qy-3], color=INK, lw=2, zorder=5)
    
    # Programmer at multi-monitor computer
    ax.text(85, qy - 10, "Programmer &\nmulti-monitor", fontsize=14, ha="center", color=INK, zorder=5)
    ax.plot([81, 89], [qy-4, qy-4], color=INK, lw=2, zorder=4) # Desk
    ax.add_patch(patches.Rectangle((82, qy-2), 2.5, 2.5, fc=CREAM, ec=INK, lw=1.5, zorder=5)) # Mon 1
    ax.add_patch(patches.Rectangle((85, qy-2), 2.5, 2.5, fc=CREAM, ec=INK, lw=1.5, zorder=5)) # Mon 2
    ax.add_patch(patches.Circle((88, qy+2), 1.2, fc=CREAM, ec=INK, lw=1.5, zorder=5)) # Programmer
    ax.plot([88, 88], [qy+0.8, qy-3], color=INK, lw=2, zorder=5)

    # Circular Flow Arrows (TL -> TR -> BR -> BL -> TL) - Avoids zig-zag
    arrow_props = dict(arrowstyle="->", lw=4, color=INK)
    
    # 1. Primary -> Secondary (Top)
    ax.annotate("", xy=(54, 74), xytext=(46, 74), arrowprops=arrow_props)
    ax.text(50, 77, "Flow of Raw Materials", fontsize=14, ha="center", va="bottom", color=INK, fontweight="bold",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # 2. Secondary -> Quaternary (Right)
    ax.annotate("", xy=(75, 43), xytext=(75, 57), arrowprops=arrow_props)
    ax.text(77, 50, "High-tech equipment\n& research", fontsize=14, ha="left", va="center", color=INK, fontweight="bold",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # 3. Quaternary -> Tertiary (Bottom)
    ax.annotate("", xy=(46, 26), xytext=(54, 26), arrowprops=arrow_props)
    ax.text(50, 23, "Advanced knowledge\n& IT Systems", fontsize=14, ha="center", va="top", color=INK, fontweight="bold",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # 4. Tertiary -> Primary (Left)
    ax.annotate("", xy=(25, 57), xytext=(25, 43), arrowprops=arrow_props)
    ax.text(23, 50, "Services & Funding\nfor extraction", fontsize=14, ha="right", va="center", color=INK, fontweight="bold",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    save(fig, out)
