"""Ten sample code-drawn images for the pilot (one from each of ten subjects).
Run:  python tools/codedraw/samples.py [outdir]
Each function name matches the placeholder it answers (see PILOT-GALLERY.md)."""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from style import *
from matplotlib.patches import Rectangle, FancyBboxPatch, Polygon, Circle, PathPatch
from matplotlib.path import Path as MPath

HERE = os.path.dirname(os.path.abspath(__file__))


def axes_clean(ax, xl, yl, xmax, ymax):
    ax.set_xlim(0, xmax); ax.set_ylim(0, ymax)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    for s in ("left", "bottom"): ax.spines[s].set_linewidth(2); ax.spines[s].set_color(INK)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel(xl, fontsize=15, color=INK, loc="right"); ax.set_ylabel(yl, fontsize=15, color=INK, loc="top", rotation=0, labelpad=14)
    ax.plot(1, 0, ">k", transform=ax.transAxes, clip_on=False, ms=8); ax.plot(0, 1, "^k", transform=ax.transAxes, clip_on=False, ms=8)


def math_proportion(out):
    fig = canvas(11, 5)
    a, b = fig.subplots(1, 2)
    x = np.linspace(0, 5, 50); axes_clean(a, "x", "y", 5.4, 10.8); a.plot(x, 2 * x, color=DEEP["blue"], lw=3.5)
    a.text(0.25, 0.9, "Direct Proportion\n(y = kx)", transform=a.transAxes, fontsize=15, fontweight="semibold", color=INK, va="top")
    a.text(-0.05, -0.02, "O", transform=a.transAxes, fontsize=13, ha="right", va="top", color=INK)
    x = np.linspace(0.55, 6, 100); axes_clean(b, "x", "y", 6.4, 11); b.plot(x, 6 / x, color=DEEP["pink"], lw=3.5)
    b.text(0.45, 0.9, "Inverse Proportion\n(xy = k)", transform=b.transAxes, fontsize=15, fontweight="semibold", color=INK, va="top")
    b.text(-0.05, -0.02, "O", transform=b.transAxes, fontsize=13, ha="right", va="top", color=INK)
    fig.subplots_adjust(wspace=0.25); save(fig, out)


def _wire(ax, pts):
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=INK, lw=2.5, solid_capstyle="round")


def _resistor(ax, x0, x1, y, label, vertical=False, c=CREAM):
    if not vertical:
        w = (x1 - x0) * 0.5; cx = (x0 + x1) / 2
        _wire(ax, [(x0, y), (cx - w / 2, y)]); _wire(ax, [(cx + w / 2, y), (x1, y)])
        ax.add_patch(Rectangle((cx - w / 2, y - 0.22), w, 0.44, fc=c, ec=INK, lw=2.5, zorder=3))
        ax.text(cx, y + 0.5, label, ha="center", fontsize=15, color=INK)


def _cell(ax, x, y0, y1):
    ym = (y0 + y1) / 2
    _wire(ax, [(x, y0), (x, ym - 0.15)]); _wire(ax, [(x, ym + 0.15), (x, y1)])
    ax.plot([x - 0.35, x + 0.35], [ym + 0.15, ym + 0.15], color=INK, lw=3)       # long plate (+)
    ax.plot([x - 0.18, x + 0.18], [ym - 0.15, ym - 0.15], color=INK, lw=6)       # short plate (-)
    ax.text(x - 0.55, ym + 0.25, "+", fontsize=14, ha="center"); ax.text(x - 0.55, ym - 0.45, "–", fontsize=14, ha="center")


def physics_circuits(out):
    fig = canvas(12, 5.2); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 24); ax.set_ylim(0, 10.4); ax.axis("off")
    # series: rectangle loop
    top, bot, L, R = 7, 2.4, 1.2, 10.8
    _cell(ax, L, bot, top)
    _wire(ax, [(L, top), (2.6, top)])
    for k, (a0, a1) in enumerate([(2.6, 5.2), (5.2, 7.8), (7.8, 10.4)]):
        _resistor(ax, a0, a1, top, f"R{k+1}")
    _wire(ax, [(10.4, top), (R, top), (R, bot), (L, bot)])
    ax.text(6, 0.7, "Series", ha="center", fontsize=16, fontweight="semibold", color=INK)
    # parallel
    L2, R2 = 14, 22.6; ys = [8.2, 5.2, 2.2]; xa, xb = 16.2, 21
    _cell(ax, L2, 2.2, 8.2)
    _wire(ax, [(L2, 8.2), (xa, 8.2)]); _wire(ax, [(L2, 2.2), (xa, 2.2)])
    _wire(ax, [(xa, 2.2), (xa, 8.2)]); _wire(ax, [(xb + 0.6, 2.2), (xb + 0.6, 8.2)])
    for k, y in enumerate(ys):
        _resistor(ax, xa, xb + 0.6, y, f"R{k+1}")
    for y in (2.2, 8.2): ax.add_patch(Circle((xa, y), 0.14, fc=INK)); ax.add_patch(Circle((xb + 0.6, y), 0.14, fc=INK))
    ax.text(18.3, 0.7, "Parallel", ha="center", fontsize=16, fontweight="semibold", color=INK)
    save(fig, out)


def chem_pentane(out):
    fig = canvas(12, 5); ax = fig.add_axes([0, 0, 1, 1]); ax.axis("off"); ax.set_aspect("equal")
    sp = 1.0
    def molecule(carbons, bonds, ox, oy):
        nb = {c: 0 for c in carbons}; pos = {c: (ox + carbons[c][0] * sp, oy + carbons[c][1] * sp) for c in carbons}
        for a, b in bonds: nb[a] += 1; nb[b] += 1
        for a, b in bonds: ax.plot([pos[a][0], pos[b][0]], [pos[a][1], pos[b][1]], color=INK, lw=2.4, zorder=1)
        dirs = {"u": (0, 1), "d": (0, -1), "l": (-1, 0), "r": (1, 0)}
        for c, (cx, cy) in pos.items():
            used = set()
            for a, b in bonds:
                if c in (a, b):
                    o = b if a == c else a; dx, dy = pos[o][0] - cx, pos[o][1] - cy
                    used.add("r" if dx > 0.5 else "l" if dx < -0.5 else "u" if dy > 0.5 else "d")
            for k, (dx, dy) in dirs.items():
                if k not in used and len([1 for _ in used]) < 4:
                    hx, hy = cx + dx * sp * 0.75, cy + dy * sp * 0.75
                    ax.plot([cx, hx], [cy, hy], color=INK, lw=1.8, zorder=1)
                    ax.text(hx, hy, "H", ha="center", va="center", fontsize=12, color=INK, bbox=dict(fc="white", ec="none", pad=1.2), zorder=3)
                    used.add(k)
            ax.text(cx, cy, "C", ha="center", va="center", fontsize=14, fontweight="semibold", color=DEEP["blue"], bbox=dict(fc="white", ec="none", pad=1.5), zorder=3)
    molecule({i: (i, 0) for i in range(5)}, [(i, i + 1) for i in range(4)], 0.8, 3)
    molecule({0: (0, 0), 1: (1, 0), 2: (2, 0), 3: (3, 0), 4: (1, 1)}, [(0, 1), (1, 2), (2, 3), (1, 4)], 7, 3)
    molecule({0: (0, 0), 1: (1, 0), 2: (-1, 0), 3: (0, 1), 4: (0, -1)}, [(0, 1), (0, 2), (0, 3), (0, 4)], 14, 3)
    for x, t in [(2.8, "Pentane"), (8.5, "2-methylbutane"), (14, "2,2-dimethylpropane")]:
        ax.text(x, 0.0, t, ha="center", fontsize=16, fontweight="semibold", color=INK)
    ax.set_xlim(-1.2, 17.2); ax.set_ylim(-0.6, 5.6)
    save(fig, out)


def econ_demand_shift(out):
    fig = canvas(7.5, 6.2); ax = fig.add_subplot(111); axes_clean(ax, "Quantity", "Price", 10, 10)
    x = np.linspace(1, 9, 50)
    ax.plot(x, 9 - 0.9 * x - 0.0, color=DEEP["blue"], lw=3.5); ax.plot(x + 1.8, 9 - 0.9 * x, color=DEEP["pink"], lw=3.5)
    s = np.linspace(1.2, 9, 50); ax.plot(s, 0.2 + 0.85 * s, color=DEEP["green"], lw=3.5)
    def eq(xx):  # intersection of D: y = 9-0.9(x-shift), S: 0.2+0.85x
        return xx
    # D1: y=9-0.9x ; S: y=0.2+0.85x -> x=8.8/1.75
    q1 = 8.8 / 1.75; p1 = 0.2 + 0.85 * q1
    # D2: y=9-0.9(x-1.8) -> x=(9+1.62-0.2)/1.75
    q2 = (9 + 1.62 - 0.2) / 1.75; p2 = 0.2 + 0.85 * q2
    for (q, p, e) in [(q1, p1, "E1"), (q2, p2, "E2")]:
        ax.plot([q, q], [0, p], ls="--", color=GREY, lw=2); ax.plot([0, q], [p, p], ls="--", color=GREY, lw=2)
        ax.plot(q, p, "o", color=INK, ms=9, zorder=5); ax.text(q + 0.35, p - 0.55, e, fontsize=15, fontweight="semibold", bbox=dict(fc="white", ec="none", pad=1.5), zorder=6)
    for (q, lbl) in [(q1, "Q1"), (q2, "Q2")]: ax.text(q, -0.55, lbl, ha="center", fontsize=14)
    for (p, lbl) in [(p1, "P1"), (p2, "P2")]: ax.text(-0.25, p, lbl, ha="right", va="center", fontsize=14)
    ax.annotate("", xy=(3.75, 7.2), xytext=(2.1, 7.2), arrowprops=dict(arrowstyle="-|>", lw=2.5, color=INK))
    ax.annotate("", xy=(0.55, p2), xytext=(0.55, p1), arrowprops=dict(arrowstyle="-|>", lw=2.5, color=INK))
    ax.annotate("", xy=(q2, 0.55), xytext=(q1, 0.55), arrowprops=dict(arrowstyle="-|>", lw=2.5, color=INK))
    ax.text(0.55, 8.3, "D1", color=DEEP["blue"], fontsize=15, fontweight="semibold"); ax.text(2.35, 8.55, "D2", color=DEEP["pink"], fontsize=15, fontweight="semibold")
    ax.text(8.9, 8.1, "S", color=DEEP["green"], fontsize=15, fontweight="semibold")
    save(fig, out)


def geo_nigeria_hazards(out):
    g = json.load(open(os.path.join(HERE, "..", "data", "ne_50m_nigeria.geojson")))
    polys = [np.array(p[0]) for p in g["coordinates"]]
    main = max(polys, key=len)
    fig = canvas(8.5, 7.5); ax = fig.add_axes([0.02, 0.02, 0.96, 0.96]); ax.set_aspect(1 / np.cos(np.radians(9)))
    ax.axis("off")
    path = MPath(main); patch = PathPatch(path, fc="#f3f3f0", ec=INK, lw=2); ax.add_patch(patch)
    def zone(poly_xy, fc, hatch=None):
        p = Polygon(poly_xy, closed=True, fc=fc, ec="none", hatch=hatch, alpha=0.9, zorder=2); ax.add_patch(p); p.set_clip_path(patch)
    zone([[2, 11.4], [15, 11.4], [15, 14.5], [2, 14.5]], "#f6dc7a")                      # north: desertification
    zone([[2, 3.5], [10.5, 3.5], [10.5, 5.9], [2, 5.9]], "#9fc7ea")                      # coast and delta
    zone([[6.9, 5.9], [8.9, 5.9], [8.9, 7.2], [6.9, 7.2]], "#c49a6c", hatch="////")       # south-east: gully erosion
    ax.add_patch(PathPatch(path, fc="none", ec=INK, lw=2.4, zorder=4))
    lab = dict(fontsize=13, color=INK, ha="center", va="center", bbox=dict(fc="white", ec=INK, lw=1, boxstyle="round,pad=0.35"), zorder=6)
    for (tx, ty, t, px, py) in [(7.0, 14.3, "Prone to desertification\nand drought", 8.5, 12.8),
                                (12.9, 6.9, "Severe gully erosion", 8.6, 6.6),
                                (4.2, 3.9, "Prone to coastal flooding\nand oil pollution", 5.5, 4.9)]:
        ax.annotate("", xy=(px, py), xytext=(tx, ty), arrowprops=dict(arrowstyle="-", lw=1.5, color=INK), zorder=5)
        ax.text(tx, ty, t, **lab)
    ax.text(8.7, 9.2, "NIGERIA", fontsize=18, fontweight="semibold", color="#6b7280", ha="center")
    ax.text(8.7, 2.4, "Sketch map: zones are approximate. Outline: Natural Earth (public domain).", fontsize=9.5, color="#6b7280", ha="center")
    ax.set_xlim(1, 16.5); ax.set_ylim(2, 15.2)
    save(fig, out)


def acc_t_account(out):
    fig = canvas(9.5, 5.6); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
    ax.text(5, 5.55, "Subscriptions Account", ha="center", fontsize=19, fontweight="semibold", color=INK)
    ax.plot([0.5, 9.5], [4.85, 4.85], color=INK, lw=3); ax.plot([5, 5], [4.85, 0.7], color=INK, lw=3)
    ax.text(2.75, 5.05, "Debit (Dr)", ha="center", fontsize=14, color=DEEP["blue"], fontweight="semibold"); ax.text(7.25, 5.05, "Credit (Cr)", ha="center", fontsize=14, color=DEEP["pink"], fontweight="semibold")
    for x0 in (0.5, 5.0): ax.text(x0 + 3.9, 4.55, "₦", ha="center", fontsize=13, color="#6b7280")
    rows_l = [("Opening arrears", "owed from last year", CREAM), ("Closing advance", "paid for next year", CREAM), ("Income & Expenditure", "balancing figure", "#cfe8d2")]
    rows_r = [("Opening advance", "paid last year for this year", CREAM), ("Cash received", "subscriptions paid this year", CREAM)]
    for k, (t, s, c) in enumerate(rows_l):
        y = 3.85 - k * 1.05
        ax.add_patch(FancyBboxPatch((0.6, y - 0.4), 4.3, 0.8, boxstyle="round,pad=0.02,rounding_size=0.1", fc=c, ec=INK if k == 2 else GREY, lw=3 if k == 2 else 1.5))
        ax.text(0.8, y + 0.08, t, fontsize=14, fontweight="semibold" if k == 2 else "medium", color=INK, va="center"); ax.text(0.8, y - 0.22, s, fontsize=10.5, color="#6b7280", va="center")
    for k, (t, s, c) in enumerate(rows_r):
        y = 3.85 - k * 1.05
        ax.add_patch(FancyBboxPatch((5.1, y - 0.4), 4.3, 0.8, boxstyle="round,pad=0.02,rounding_size=0.1", fc=c, ec=GREY, lw=1.5))
        ax.text(5.3, y + 0.08, t, fontsize=14, color=INK, va="center"); ax.text(5.3, y - 0.22, s, fontsize=10.5, color="#6b7280", va="center")
    save(fig, out)


def bio_photosynthesis_graph(out):
    fig = canvas(9, 6.2); ax = fig.add_subplot(111); axes_clean(ax, "Light intensity", "Rate of photosynthesis", 10, 10)
    x = np.linspace(0, 10, 200)
    def curve(top, k): return top * (1 - np.exp(-k * x))
    c1, c2, c3 = curve(3.0, 0.75), curve(5.6, 0.5), curve(8.4, 0.5)
    ax.plot(x, c1, color=DEEP["green"], lw=3.5, label="low CO₂, 25 °C"); ax.plot(x, c2, color=DEEP["blue"], lw=3.5, label="high CO₂, 25 °C"); ax.plot(x, c3, color=DEEP["orange"], lw=3.5, label="high CO₂, 35 °C")
    ax.annotate("light is the\nlimiting factor", xy=(0.75, curve(3.0, 0.75)[15]), xytext=(1.9, 0.55), fontsize=12.5, color=INK, arrowprops=dict(arrowstyle="-", color=INK, lw=1.3), ha="center", bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    ax.annotate("another factor\nis limiting", xy=(7.3, 3.0), xytext=(7.3, 1.25), fontsize=12.5, color=INK, arrowprops=dict(arrowstyle="-", color=INK, lw=1.3), ha="center", bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    ax.legend(loc="upper left", frameon=True, fontsize=12.5, edgecolor=GREY)
    save(fig, out)


def hist_timeline(out):
    fig = canvas(13, 5.6); ax = fig.add_axes([0, 0, 1, 1]); ax.axis("off")
    ax.set_xlim(0, 60); ax.set_ylim(-5.2, 5.2)
    ax.plot([2, 58], [0, 0], color=INK, lw=4, solid_capstyle="round")
    ev = [("1922", "Clifford\nConstitution", "Elective principle", 1, GREEN), ("1946", "Richards\nConstitution", "Regionalism", -1, BLUE),
          ("1951", "Macpherson\nConstitution", "Quasi-federalism", 1, LAV), ("1954", "Lyttelton\nConstitution", "Federalism", -1, PINK),
          ("1957–1958", "Constitutional\nConferences", "Lagos and London", 1, CREAM), ("1960", "Independence", "1 October", -1, "#cfe8d2")]
    xs = np.linspace(7, 53, len(ev)); bw, bh = 9.2, 3.1
    for x, (yr, t_, s, side, c) in zip(xs, ev):
        ax.plot([x, x], [0, 1.0 * side], color=INK, lw=2); ax.plot(x, 0, "o", ms=14, color=c, mec=INK, mew=2.5, zorder=4)
        y0 = 1.0 if side > 0 else -1.0 - bh
        ax.add_patch(FancyBboxPatch((x - bw / 2, y0), bw, bh, boxstyle="round,pad=0.05,rounding_size=0.3", fc=c, ec=INK, lw=1.8, zorder=3))
        yc = y0 + bh / 2
        ax.text(x, yc + 1.0, yr, ha="center", va="center", fontsize=15, fontweight="semibold", color=INK, zorder=5)
        ax.text(x, yc + 0.0, t_, ha="center", va="center", fontsize=11, color=INK, zorder=5, linespacing=1.1)
        ax.text(x, yc - 1.1, s, ha="center", va="center", fontsize=9.8, color="#4b5563", zorder=5)
    ax.text(30, -4.9, "Not to scale: milestones are evenly spaced.", ha="center", fontsize=10, color="#6b7280")
    save(fig, out)


def gov_court_pyramid(out):
    fig = canvas(10.5, 6.6); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 13); ax.set_ylim(0, 8); ax.axis("off")
    tiers = [("Supreme Court", PINK), ("Court of Appeal", LAV), ("Federal High Court / State High Courts /\nSharia & Customary Courts of Appeal", BLUE), ("Magistrate Courts /\nArea & Customary Courts", "#cfe8d2")]
    H = 1.75; cx = 6.2; base = 9.0; top = 1.6
    def half(y): return top / 2 + (base - top) / 2 * (y / (4 * H))
    for k, (t, c) in enumerate(tiers):
        y0 = k * H + 0.15; y1 = (k + 1) * H - 0.05
        yl0, yl1 = 4 * H - y0, 4 * H - y1
        h0, h1 = half(4 * H - yl0) if False else base / 2 - (base - top) / 2 * ((y0 - 0) / (4 * H)), base / 2 - (base - top) / 2 * ((y1 - 0) / (4 * H))
        # tier k=0 is the BASE (widest)
        pass
    for k, (t, c) in enumerate(reversed(tiers)):
        y0 = k * H + 0.1; y1 = (k + 1) * H - 0.05
        w0 = base - (base - top) * (y0 / (4 * H)); w1 = base - (base - top) * (y1 / (4 * H))
        ax.add_patch(Polygon([[cx - w0 / 2, y0 + 0.25], [cx + w0 / 2, y0 + 0.25], [cx + w1 / 2, y1 + 0.25], [cx - w1 / 2, y1 + 0.25]], fc=c, ec=INK, lw=2.2))
        ax.text(cx, (y0 + y1) / 2 + 0.25, t, ha="center", va="center", fontsize=12.5 if k < 2 else 13.5, fontweight="semibold" if k == 3 else "medium", color=INK)
    ax.annotate("", xy=(11.9, 7.5), xytext=(11.9, 0.7), arrowprops=dict(arrowstyle="-|>", lw=3, color=INK))
    ax.text(12.15, 4.1, "Direction of appeals", rotation=90, va="center", ha="center", fontsize=13, color=INK)
    save(fig, out)


def commerce_channels(out):
    fig = canvas(12.5, 6.6); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 25); ax.set_ylim(0, 13.2); ax.axis("off")
    rows = [("Direct Sales", []), ("", ["Retailer"]), ("Traditional Channel", ["Wholesaler", "Retailer"]), ("", ["Agent", "Wholesaler", "Retailer"])]
    labels = ["Direct Sales", "", "Traditional Channel", ""]
    colors = {"Manufacturer": GREEN, "Consumer": BLUE}
    bw, bh = 3.6, 1.7
    for r, (_, mids) in enumerate(rows):
        y = 11.4 - r * 3.45
        chain = ["Manufacturer"] + mids + ["Consumer"]
        ax.text(0.2, y + 1.15, labels[r], fontsize=13.5, fontweight="semibold", color=INK, va="bottom")
        gap = (24 - len(chain) * bw) / max(1, len(chain) - 1) if len(chain) > 1 else 0
        xs = []
        xcur = 0.4
        for k, name in enumerate(chain):
            xs.append(xcur)
            ax.add_patch(FancyBboxPatch((xcur, y - bh / 2), bw, bh, boxstyle="round,pad=0.03,rounding_size=0.25", fc=colors.get(name, CREAM), ec=INK, lw=2))
            ax.text(xcur + bw / 2, y, name, ha="center", va="center", fontsize=13.5, color=INK)
            xcur += bw + (min(gap, 2.6))
        for k in range(len(chain) - 1):
            ax.annotate("", xy=(xs[k + 1] - 0.05, y), xytext=(xs[k] + bw + 0.05, y), arrowprops=dict(arrowstyle="-|>", lw=2.4, color=INK))
    save(fig, out)


ALL = {"mathematics-A2-proportion-graphs": math_proportion, "physics-A31-series-parallel-circuits": physics_circuits,
       "chemistry-A16a-pentane-isomers": chem_pentane, "economics-A7-demand-shift": econ_demand_shift,
       "geography-B11-nigeria-hazards-sketch-map": geo_nigeria_hazards, "accounting-A11-subscriptions-t-account": acc_t_account,
       "biology-B2b-photosynthesis-rate-graph": bio_photosynthesis_graph, "history-C6-constitutional-timeline": hist_timeline,
       "government-A4-court-hierarchy-pyramid": gov_court_pyramid, "commerce-A4a-distribution-channels": commerce_channels}

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", ".image-work", "code")
    os.makedirs(out, exist_ok=True)
    for name, fn in ALL.items():
        fn(os.path.join(out, name + ".png")); print(name)
