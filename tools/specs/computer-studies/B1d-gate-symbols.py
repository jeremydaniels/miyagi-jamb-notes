"""Hand-written code drawing for B1d-01 (three gate symbols in separate panels). Run: python tools/specs/computer-studies/B1d-gate-symbols.py OUT.png"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "codedraw"))
from style import *
from matplotlib.patches import FancyBboxPatch

fig = canvas(13, 3.6)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 13); ax.set_ylim(0, 3.6); ax.set_aspect("equal"); ax.axis("off")
panels = [("AND gate", "AND", 2, 2), ("OR gate", "OR", 2, 2), ("NOT gate", "NOT", 1, 1)]
for i, (title, kind, nin, _) in enumerate(panels):
    x0 = 0.25 + i * 4.3
    ax.add_patch(FancyBboxPatch((x0, 0.25), 3.9, 3.1, boxstyle="round,pad=0.02,rounding_size=0.15", fc="white", ec=GREY, lw=2))
    cx = x0 + 1.95
    r = gate(ax, kind, cx, 1.65, w=1.5, h=1.0)
    ax.text(cx, 2.95, title, ha="center", va="center", fontsize=18, color=INK, fontweight="bold")
    names = ["A", "B"] if nin == 2 else ["A"]
    for (px, py), nm in zip(r["in"], names):
        ax.text(px - 0.12, py, nm, ha="right", va="center", fontsize=16, color=INK)
    ox, oy = r["out"]
    ax.text(ox + 0.12, oy, "Q", ha="left", va="center", fontsize=16, color=INK)
save(fig, sys.argv[1])
