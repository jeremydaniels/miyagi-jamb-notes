from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(15, 6.8)
    
    # 3 subplots for the three phases of the cardiac cycle
    axes = [fig.add_subplot(1, 3, i+1) for i in range(3)]
    
    titles = [
        "1. diastole",
        "2. atrial systole",
        "3. ventricular systole"
    ]
    
    c_red = PINK
    c_deep_red = DEEP["pink"]
    c_blue = BLUE
    c_deep_blue = DEEP["blue"]

    for i, ax in enumerate(axes):
        ax.set_xlim(-5.2, 5.2)
        ax.set_ylim(-5.5, 5.5)
        ax.set_aspect("equal")
        ax.axis("off")
        
        # Subplot Title
        ax.text(0, 5.0, titles[i], ha="center", va="center", fontsize=15, weight="bold", color=INK)
        
        # Chambers geometry depending on phase
        # Atria size
        a_r = 1.6 if i != 1 else 1.2
        a_y = 1.8 if i != 1 else 1.65
        
        # Ventricles size
        v_w = 2.0 if i != 2 else 1.6
        v_bot = -3.8 if i != 2 else -3.3
        
        # Great vessels exiting
        ao = patches.Rectangle((-1.1, 1.1), 0.7, 2.5, facecolor=c_red, edgecolor=c_deep_red, lw=1.5, zorder=1)
        pa = patches.Rectangle((0.4, 1.1), 0.7, 2.5, facecolor=c_blue, edgecolor=c_deep_blue, lw=1.5, zorder=1)
        ax.add_patch(ao)
        ax.add_patch(pa)
        
        # Left Chamber (Diagram Left -> RED)
        la = patches.FancyBboxPatch((-3.2, a_y - 0.7), 2.2, a_r * 1.1, 
                                    boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor=c_red, edgecolor=c_deep_red, lw=1.5, zorder=2)
        ax.add_patch(la)
        
        # Right Chamber (Diagram Right -> BLUE)
        ra = patches.FancyBboxPatch((1.0, a_y - 0.7), 2.2, a_r * 1.1, 
                                    boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor=c_blue, edgecolor=c_deep_blue, lw=1.5, zorder=2)
        ax.add_patch(ra)
        
        # Ventricles
        # Diagram left ventricle (Red)
        lv_poly = np.array([
            [-2.6, 0.4],
            [-0.2, 0.4],
            [-0.2, v_bot],
            [-v_w - 0.4, -1.8]
        ])
        # Diagram right ventricle (Blue)
        rv_poly = np.array([
            [0.2, 0.4],
            [2.6, 0.4],
            [v_w + 0.4, -1.8],
            [0.2, v_bot]
        ])
        
        ax.add_patch(patches.Polygon(lv_poly, closed=True, facecolor=c_red, edgecolor=c_deep_red, lw=1.5, zorder=2))
        ax.add_patch(patches.Polygon(rv_poly, closed=True, facecolor=c_blue, edgecolor=c_deep_blue, lw=1.5, zorder=2))
        
        # Central Septum
        ax.plot([0, 0], [v_bot, 2.5], color=GREY, lw=4, solid_capstyle='round', zorder=3)
        
        # Outer muscular walls
        ax.plot([-3.5, -3.5, -0.1], [1.2, -1.8, v_bot - 0.2], color=GREY, lw=4, zorder=3)
        ax.plot([3.5, 3.5, 0.1], [1.2, -1.8, v_bot - 0.2], color=GREY, lw=3, zorder=3)
        
        if i == 0:
            # DIASTOLE: whole heart relaxed, blood flowing into atria and into ventricles
            # AV valves open (flaps pointing downwards into ventricles)
            ax.plot([-1.8, -1.6], [0.4, -0.3], color=INK, lw=2.5, zorder=4)
            ax.plot([-0.8, -1.0], [0.4, -0.3], color=INK, lw=2.5, zorder=4)
            ax.plot([0.8, 1.0], [0.4, -0.3], color=INK, lw=2.5, zorder=4)
            ax.plot([1.8, 1.6], [0.4, -0.3], color=INK, lw=2.5, zorder=4)
            
            # Flow arrows: into atria and continuing into ventricles
            # Left side (red)
            ax.annotate("", xy=(-1.3, -1.5), xytext=(-2.1, 3.3),
                        arrowprops=dict(arrowstyle="->", color=c_deep_red, lw=2.8), zorder=5)
            # Right side (blue)
            ax.annotate("", xy=(1.3, -1.5), xytext=(2.1, 3.3),
                        arrowprops=dict(arrowstyle="->", color=c_deep_blue, lw=2.8), zorder=5)
            
            # Semilunar valves closed
            ax.plot([-1.1, -0.4], [1.1, 1.1], color=INK, lw=3, zorder=4)
            ax.plot([0.4, 1.1], [1.1, 1.1], color=INK, lw=3, zorder=4)
            
            # Required labels
            ax.text(0, 2.2, "semilunar valves closed", ha="center", fontsize=11,
                    bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=6)
            ax.text(0, -4.6, "atrioventricular valves open", ha="center", fontsize=11, 
                    bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=6)

        elif i == 1:
            # ATRIAL SYSTOLE: atria contracting (smaller), pushing blood into ventricles
            # AV valves wide open
            ax.plot([-1.9, -1.7], [0.4, -0.4], color=INK, lw=2.5, zorder=4)
            ax.plot([-0.7, -0.9], [0.4, -0.4], color=INK, lw=2.5, zorder=4)
            ax.plot([0.7, 0.9], [0.4, -0.4], color=INK, lw=2.5, zorder=4)
            ax.plot([1.9, 1.7], [0.4, -0.4], color=INK, lw=2.5, zorder=4)
            
            # Semilunar valves closed
            ax.plot([-1.1, -0.4], [1.1, 1.1], color=INK, lw=3, zorder=4)
            ax.plot([0.4, 1.1], [1.1, 1.1], color=INK, lw=3, zorder=4)
            
            # Squeeze arrows on atria walls
            ax.annotate("", xy=(-1.0, 1.9), xytext=(-0.4, 1.9),
                        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
            ax.annotate("", xy=(-3.2, 1.9), xytext=(-3.8, 1.9),
                        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
            ax.annotate("", xy=(3.2, 1.9), xytext=(3.8, 1.9),
                        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
            ax.annotate("", xy=(1.0, 1.9), xytext=(0.4, 1.9),
                        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
            
            # Arrows pushing blood from atria into ventricles
            ax.annotate("", xy=(-1.3, -1.5), xytext=(-1.4, 1.4),
                        arrowprops=dict(arrowstyle="->", color=c_deep_red, lw=3), zorder=5)
            ax.annotate("", xy=(1.3, -1.5), xytext=(1.4, 1.4),
                        arrowprops=dict(arrowstyle="->", color=c_deep_blue, lw=3), zorder=5)
            
            ax.text(0, -4.6, "atrioventricular valves open", ha="center", fontsize=11,
                    bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=6)

        elif i == 2:
            # VENTRICULAR SYSTOLE: ventricles contracting, AV valves closed, semilunar valves open
            # Blood leaving through aorta (from left, red) and pulmonary artery (from right, blue)
            
            # AV valves closed (horizontal seal)
            ax.plot([-2.0, -0.6], [0.4, 0.4], color=INK, lw=3, zorder=4)
            ax.plot([0.6, 2.0], [0.4, 0.4], color=INK, lw=3, zorder=4)
            
            # Open semilunar valves (drawn within the vessel base)
            ax.plot([-1.1, -1.0], [1.1, 1.6], color=INK, lw=2, zorder=4)
            ax.plot([-0.4, -0.5], [1.1, 1.6], color=INK, lw=2, zorder=4)
            ax.plot([0.4, 0.5], [1.1, 1.6], color=INK, lw=2, zorder=4)
            ax.plot([1.1, 1.0], [1.1, 1.6], color=INK, lw=2, zorder=4)
            
            # Flow arrows up through vessels
            ax.annotate("", xy=(-0.75, 3.8), xytext=(-0.75, 0.8),
                        arrowprops=dict(arrowstyle="->", color=c_deep_red, lw=3), zorder=5)
            ax.annotate("", xy=(0.75, 3.8), xytext=(0.75, 0.8),
                        arrowprops=dict(arrowstyle="->", color=c_deep_blue, lw=3), zorder=5)
            
            # Inward squeeze markers on ventricles
            ax.annotate("", xy=(-1.9, -1.5), xytext=(-2.7, -1.5),
                        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
            ax.annotate("", xy=(1.9, -1.5), xytext=(2.7, -1.5),
                        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
            
            # Well-spaced destination labels at top
            ax.text(-2.5, 4.15, "blood to body", ha="center", va="center", fontsize=11.5,
                    weight="bold", color=c_deep_red,
                    bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=6)
            ax.text(2.5, 4.15, "blood to lungs", ha="center", va="center", fontsize=11.5,
                    weight="bold", color=c_deep_blue,
                    bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=6)
            
            # Valve status labels
            ax.text(0, 1.8, "semilunar valves open", ha="center", va="center", fontsize=11,
                    bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=6)
            ax.text(0, -4.6, "atrioventricular valves closed (lub)", ha="center", va="center", fontsize=11,
                    bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=6)

    save(fig, out)
