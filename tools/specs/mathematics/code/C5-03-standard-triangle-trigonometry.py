from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(7, 6)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_aspect("equal")
    ax.axis("off")

    # Define vertices for an arbitrary acute-angled triangle
    # Angles: A (bottom-left), B (bottom-right), C (top)
    A = np.array([1.5, 1.5])
    B = np.array([7.5, 1.5])
    C = np.array([5.0, 6.0])

    # Check acuteness:
    # AB = (6, 0), AC = (3.5, 4.5), BC = (-2.5, 4.5)
    # Dot products:
    # A: AB . AC = 6*3.5 = 21 > 0
    # B: BA . BC = (-6)*(-2.5) = 15 > 0
    # C: CA . CB = (-3.5)*(-2.5) + (-4.5)*(-4.5) = 8.75 + 20.25 = 29 > 0
    # All dot products > 0, so all angles are acute!

    # Draw triangle fill and edges
    tri = plt.Polygon([A, B, C], closed=True, facecolor=CREAM, edgecolor=DEEP["blue"], lw=2.5, zorder=2)
    ax.add_patch(tri)

    # Plot vertex dots
    pts = np.array([A, B, C])
    ax.scatter(pts[:, 0], pts[:, 1], color=DEEP["blue"], s=40, zorder=4)

    # Label vertices: A, B, C
    # Vertex offsets
    ax.text(A[0] - 0.35, A[1] - 0.35, "A", fontsize=18, color=INK, ha="right", va="top", weight="bold")
    ax.text(B[0] + 0.35, B[1] - 0.35, "B", fontsize=18, color=INK, ha="left", va="top", weight="bold")
    ax.text(C[0], C[1] + 0.35, "C", fontsize=18, color=INK, ha="center", va="bottom", weight="bold")

    # Midpoints of opposite sides:
    # Side opposite A is BC -> label 'a'
    # Side opposite B is AC -> label 'b'
    # Side opposite C is AB -> label 'c'
    mid_a = (B + C) / 2.0
    mid_b = (A + C) / 2.0
    mid_c = (A + B) / 2.0

    # Normal vectors for labeling outside the triangle
    # Side a (BC): direction BC = C - B = (-2.5, 4.5). Outward normal = (4.5, 2.5)
    norm_a = np.array([4.5, 2.5])
    norm_a = norm_a / np.linalg.norm(norm_a)
    pos_a = mid_a + norm_a * 0.45

    # Side b (AC): direction AC = (3.5, 4.5). Outward normal = (-4.5, 3.5)
    norm_b = np.array([-4.5, 3.5])
    norm_b = norm_b / np.linalg.norm(norm_b)
    pos_b = mid_b + norm_b * 0.45

    # Side c (AB): direction AB = (6, 0). Outward normal = (0, -1)
    norm_c = np.array([0, -1])
    pos_c = mid_c + norm_c * 0.45

    # Label sides with lowercase letters
    ax.text(pos_a[0], pos_a[1], "a", fontsize=16, color=INK, style="italic", ha="center", va="center",
            bbox=dict(fc="white", ec="none", pad=2))
    ax.text(pos_b[0], pos_b[1], "b", fontsize=16, color=INK, style="italic", ha="center", va="center",
            bbox=dict(fc="white", ec="none", pad=2))
    ax.text(pos_c[0], pos_c[1], "c", fontsize=16, color=INK, style="italic", ha="center", va="center",
            bbox=dict(fc="white", ec="none", pad=2))

    ax.set_xlim(0.5, 8.5)
    ax.set_ylim(0.5, 7.0)

    save(fig, out)
