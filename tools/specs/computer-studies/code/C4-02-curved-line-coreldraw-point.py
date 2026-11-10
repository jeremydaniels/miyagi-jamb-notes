from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 6)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(4.5, 5.3, "Bézier Curve Components (CorelDRAW)", 
            fontsize=17, weight='bold', color=INK, ha='center')

    # Bézier curve definition
    # Cubic Bézier passing through start, node, and end
    # Segment 1: P0 to Node (P3)
    p0 = np.array([1.2, 2.0])
    c0 = np.array([2.0, 3.8])
    c1 = np.array([3.2, 3.8])
    node = np.array([4.2, 3.0])

    # Segment 2: Node (P3) to P6
    # Smooth node: incoming handle vector equals opposite of outgoing handle vector
    handle_len = 1.6
    handle_angle = np.deg2rad(40) # tangent angle at node
    h_out = node + handle_len * np.array([np.cos(handle_angle), np.sin(handle_angle)])
    h_in = node - handle_len * np.array([np.cos(handle_angle), np.sin(handle_angle)])
    
    p3 = np.array([8.0, 2.2])
    c2 = node + 0.8 * np.array([np.cos(handle_angle), np.sin(handle_angle)])
    c3 = np.array([6.5, 4.0])

    # Generate curve points
    t = np.linspace(0, 1, 100)[:, None]
    curve1 = (1-t)**3 * p0 + 3*(1-t)**2*t * c0 + 3*(1-t)*t**2 * (node - 0.7*np.array([np.cos(handle_angle), np.sin(handle_angle)])) + t**3 * node
    curve2 = (1-t)**3 * node + 3*(1-t)**2*t * c2 + 3*(1-t)*t**2 * c3 + t**3 * p3

    # Draw the main curved line
    ax.plot(curve1[:, 0], curve1[:, 1], color=DEEP["blue"], lw=4, solid_capstyle='round')
    ax.plot(curve2[:, 0], curve2[:, 1], color=DEEP["blue"], lw=4, solid_capstyle='round')

    # Draw start and end endpoints (small squares, typical of vector graphics)
    sq_size = 0.16
    for pt in [p0, p3]:
        rect = plt.Rectangle((pt[0]-sq_size/2, pt[1]-sq_size/2), sq_size, sq_size,
                             facecolor="white", edgecolor=INK, lw=1.5, zorder=4)
        ax.add_patch(rect)

    # Control handle: dotted line extending from the node with an arrow at the end
    ax.annotate("", xy=(h_out[0], h_out[1]), xytext=(node[0], node[1]),
                arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6",
                                color=DEEP["pink"], lw=2.2, linestyle=":", shrinkA=3, shrinkB=0),
                zorder=5)

    # Opposite handle (subtle dotted line with square handle tip, standard CorelDraw style)
    ax.plot([node[0], h_in[0]], [node[1], h_in[1]], color=GREY, lw=1.8, linestyle=":", zorder=3)
    rect_h_in = plt.Rectangle((h_in[0]-sq_size/2, h_in[1]-sq_size/2), sq_size, sq_size,
                              facecolor="white", edgecolor=GREY, lw=1.5, zorder=4)
    ax.add_patch(rect_h_in)

    # The Node: small square on the curved line
    node_size = 0.22
    node_rect = plt.Rectangle((node[0]-node_size/2, node[1]-node_size/2), node_size, node_size,
                              facecolor=DEEP["blue"], edgecolor=INK, lw=1.8, zorder=6)
    ax.add_patch(node_rect)

    # Labels and Annotations
    # 1. Point to the small square and label it "Node"
    ax.annotate("Node", xy=(node[0], node[1] - node_size/2), xytext=(3.0, 1.2),
                fontsize=15, color=INK, weight='bold',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8, shrinkB=4),
                ha="center", va="center",
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"))

    # 2. Point to the dotted line extending from the node with arrow and label it "Control Handle"
    handle_mid = (node + h_out) / 2
    ax.annotate("Control Handle", xy=(handle_mid[0], handle_mid[1]), xytext=(7.0, 4.7),
                fontsize=15, color=INK, weight='bold',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8, shrinkB=4),
                ha="center", va="center",
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"))

    # Label the curved line for clarity
    ax.text(1.8, 1.6, "Curved line", fontsize=14, color=GREY, style='italic', ha='center')

    save(fig, out)
