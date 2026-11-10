from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 6)
    
    # Subplot 1: Triangle of Forces
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax1.set_xlim(-0.2, 5.2)
    ax1.set_ylim(-0.5, 4.5)
    ax1.set_title("Triangle of Forces", fontsize=18, color=INK, pad=15, weight="bold")
    
    # Vertices of the triangle
    t_verts = [np.array([0.5, 0.8]), np.array([4.2, 0.8]), np.array([2.0, 3.8])]
    t_colors = [DEEP["blue"], DEEP["orange"], DEEP["green"]]
    t_labels = [r"$\mathbf{F}_1$", r"$\mathbf{F}_2$", r"$\mathbf{F}_3$"]
    t_offsets = [np.array([0.0, -0.4]), np.array([0.35, 0.2]), np.array([-0.45, 0.1])]
    
    for i in range(3):
        p1 = t_verts[i]
        p2 = t_verts[(i + 1) % 3]
        vec = p2 - p1
        mid = (p1 + p2) / 2.0
        
        ax1.annotate(
            "",
            xy=p2,
            xytext=p1,
            arrowprops=dict(
                arrowstyle="-|>",
                color=t_colors[i],
                lw=3.0,
                mutation_scale=22
            )
        )
        
        lbl_pos = mid + t_offsets[i]
        ax1.text(
            lbl_pos[0],
            lbl_pos[1],
            t_labels[i],
            color=t_colors[i],
            fontsize=16,
            ha="center",
            va="center",
            weight="bold",
            bbox=dict(fc="white", ec="none", pad=2)
        )

    # Subplot 2: Polygon of Forces
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_xlim(-0.5, 5.5)
    ax2.set_ylim(-0.5, 4.5)
    ax2.set_title("Polygon of Forces", fontsize=18, color=INK, pad=15, weight="bold")
    
    # Vertices of an irregular closed pentagon
    p_verts = [
        np.array([0.8, 0.8]),
        np.array([3.8, 0.6]),
        np.array([4.8, 2.5]),
        np.array([2.8, 4.0]),
        np.array([1.0, 3.0])
    ]
    p_colors = [DEEP["blue"], DEEP["orange"], DEEP["green"], DEEP["lav"], DEEP["pink"]]
    p_labels = [r"$\mathbf{F}_1$", r"$\mathbf{F}_2$", r"$\mathbf{F}_3$", r"$\mathbf{F}_4$", r"$\mathbf{F}_5$"]
    p_offsets = [
        np.array([0.0, -0.4]),
        np.array([0.45, 0.0]),
        np.array([0.35, 0.35]),
        np.array([-0.25, 0.35]),
        np.array([-0.45, -0.1])
    ]
    
    for i in range(5):
        p1 = p_verts[i]
        p2 = p_verts[(i + 1) % 5]
        vec = p2 - p1
        mid = (p1 + p2) / 2.0
        
        ax2.annotate(
            "",
            xy=p2,
            xytext=p1,
            arrowprops=dict(
                arrowstyle="-|>",
                color=p_colors[i],
                lw=3.0,
                mutation_scale=22
            )
        )
        
        lbl_pos = mid + p_offsets[i]
        ax2.text(
            lbl_pos[0],
            lbl_pos[1],
            p_labels[i],
            color=p_colors[i],
            fontsize=16,
            ha="center",
            va="center",
            weight="bold",
            bbox=dict(fc="white", ec="none", pad=2)
        )

    plt.subplots_adjust(left=0.05, right=0.95, top=0.88, bottom=0.08, wspace=0.15)
    save(fig, out)
