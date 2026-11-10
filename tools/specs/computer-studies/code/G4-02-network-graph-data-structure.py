from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)

    # Vertices: name -> (x, y)
    nodes = {
        'A': (2.2, 5.2),
        'B': (4.8, 5.8),
        'C': (7.8, 4.8),
        'D': (6.6, 2.5),
        'E': (3.8, 1.8),
        'F': (1.6, 2.8),
        'G': (4.5, 3.8)
    }

    # Edges: pairs of vertex names
    edges = [
        ('A', 'B'),
        ('B', 'C'),
        ('C', 'D'),
        ('D', 'E'),
        ('E', 'F'),
        ('F', 'A'),
        ('A', 'G'),
        ('B', 'G'),
        ('D', 'G'),
        ('E', 'G'),
        ('F', 'G'),
        ('B', 'D')
    ]

    # Draw Edges (straight lines)
    for u, v in edges:
        x1, y1 = nodes[u]
        x2, y2 = nodes[v]
        ax.plot([x1, x2], [y1, y2], color=GREY, lw=2.8, zorder=1)

    # Draw Vertices (circles)
    node_radius = 0.45
    for name, (x, y) in nodes.items():
        circle = plt.Circle((x, y), node_radius, facecolor=BLUE, edgecolor=DEEP['blue'], lw=2.5, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, name, color=INK, fontsize=16, weight='bold', ha='center', va='center', zorder=3)

    # Title
    ax.text(5.0, 6.5, "Graph Data Structure", fontsize=18, weight='bold', ha='center', va='center', color=INK)

    # Annotations pointing to Edge and Vertex
    # Edge annotation pointing to edge between A and B
    mid_ab = ((nodes['A'][0] + nodes['B'][0]) / 2, (nodes['A'][1] + nodes['B'][1]) / 2)
    ax.annotate("Edge\n(connection)",
                xy=mid_ab, xytext=(2.2, 6.3),
                fontsize=14, color=INK, ha='center', va='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
                zorder=4)

    # Vertex annotation pointing to node C
    ax.annotate("Vertex (Node)",
                xy=(nodes['C'][0] + 0.35, nodes['C'][1] + 0.3),
                xytext=(8.5, 6.0),
                fontsize=14, color=INK, ha='center', va='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
                zorder=4)

    save(fig, out)
