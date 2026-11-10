from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Circle

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # Title
    ax.text(50, 96, "Land Use Act of 1978", ha="center", va="center",
            fontsize=18, fontweight="bold", color=INK)

    # 1. Top Section: Map / State Land Box
    state_box = FancyBboxPatch((32, 74), 36, 18, boxstyle="round,pad=1.2",
                               fc=CREAM, ec=DEEP["orange"], lw=2.5)
    ax.add_patch(state_box)
    
    # State map sketch inside the box
    poly_pts = np.array([
        [37, 79], [42, 87], [50, 89], [58, 86], [63, 82], 
        [60, 77], [52, 76], [45, 78]
    ])
    state_poly = Polygon(poly_pts, closed=True, fc=GREEN, ec=DEEP["green"], lw=2, alpha=0.7)
    ax.add_patch(state_poly)
    ax.text(50, 82.5, "All State Land\nVested in Governor", ha="center", va="center",
            fontsize=14, fontweight="bold", color=INK)
    ax.text(50, 71.5, "Map of a Nigerian State", ha="center", va="top",
            fontsize=14, style="italic", color=INK)

    # Arrow 1: From State Land to State Governor
    ax.annotate("", xy=(50, 58), xytext=(50, 68),
                arrowprops=dict(facecolor=DEEP["blue"], edgecolor=DEEP["blue"],
                                width=3, headwidth=10, headlength=10))

    # 2. Middle Section: State Governor
    gov_box = FancyBboxPatch((28, 41), 44, 16.5, boxstyle="round,pad=1.0",
                             fc=LAV, ec=DEEP["lav"], lw=2)
    ax.add_patch(gov_box)

    # Governor Icon / Sketch: head, body, document
    ax.add_patch(Circle((35, 51.5), 2.2, fc=CREAM, ec=INK, lw=1.5))
    ax.add_patch(Polygon([[31.5, 43], [38.5, 43], [37, 48.5], [33, 48.5]],
                         closed=True, fc=BLUE, ec=INK, lw=1.5))
    
    doc_gov = FancyBboxPatch((36.5, 45), 7, 7, boxstyle="square,pad=0.2",
                             fc="white", ec=INK, lw=1.2)
    ax.add_patch(doc_gov)
    ax.text(40, 48.5, "Act\n1978", ha="center", va="center", fontsize=14, color=INK)

    ax.text(56, 52, "State Governor", ha="center", va="center",
            fontsize=16, fontweight="bold", color=INK)
    ax.text(56, 46, "Holds land in trust for the people;\ngrants rights of occupancy",
            ha="center", va="center", fontsize=14, color=INK)

    # Arrow 2: From Governor to Farmer
    ax.annotate("", xy=(30, 26), xytext=(40, 40),
                arrowprops=dict(facecolor=DEEP["green"], edgecolor=DEEP["green"],
                                width=3, headwidth=10, headlength=10))

    # 3. Bottom Left Section: Farmer receiving C of O
    farmer_box = FancyBboxPatch((4, 4), 48, 26, boxstyle="round,pad=1.0",
                                fc=GREEN, ec=DEEP["green"], lw=2, alpha=0.5)
    ax.add_patch(farmer_box)

    # Farmer figure: head with hat, body
    ax.add_patch(Circle((10, 22), 2.0, fc=CREAM, ec=INK, lw=1.5))
    ax.plot([6.5, 13.5], [23.5, 23.5], color=DEEP["orange"], lw=3)
    ax.add_patch(Polygon([[8, 23.5], [12, 23.5], [11, 25.5], [9, 25.5]],
                         closed=True, fc=ORANGE, ec=INK, lw=1))
    ax.add_patch(Polygon([[7, 10], [13, 10], [12, 19.5], [8, 19.5]],
                         closed=True, fc=CREAM, ec=INK, lw=1.5))

    # Certificate of Occupancy document
    c_of_o = FancyBboxPatch((15, 6), 18, 15, boxstyle="square,pad=0.3",
                            fc="white", ec=DEEP["blue"], lw=1.8)
    ax.add_patch(c_of_o)
    ax.text(24, 17, "CERTIFICATE", ha="center", va="center", fontsize=14, fontweight="bold", color=DEEP["blue"])
    ax.text(24, 13.5, "OF OCCUPANCY", ha="center", va="center", fontsize=14, fontweight="bold", color=DEEP["blue"])
    ax.text(24, 10, "(C of O)", ha="center", va="center", fontsize=14, fontweight="bold", color=INK)

    # Label for Farmer
    ax.text(35, 27, "Farmer", ha="left", va="center",
            fontsize=16, fontweight="bold", color=INK)
    ax.text(42, 15, "Receives statutory\nright of occupancy\nvia C of O",
            ha="center", va="center", fontsize=14, color=INK)

    # 4. Bottom Right Section: Signpost with Limits
    # Post
    ax.plot([75, 75], [4, 18], color=DEEP["orange"], lw=6, solid_capstyle="butt")
    # Signboard
    sign_box = FancyBboxPatch((56, 15), 41, 14, boxstyle="round,pad=0.8",
                              fc=CREAM, ec=DEEP["orange"], lw=2.5)
    ax.add_patch(sign_box)
    
    sign_text = "Maximum limit:\n500 ha for crops,\n5000 ha for grazing"
    ax.text(76.5, 22, sign_text, ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK)

    save(fig, out)
