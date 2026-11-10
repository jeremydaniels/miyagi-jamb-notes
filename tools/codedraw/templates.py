"""Fixed layout templates for code-drawn images. Gemini fills in a JSON spec; these draw it.

    from templates import render
    render(spec_dict, "out.png")

Every template measures its text, sizes boxes to fit, and never uses a font below MIN_PT, so text never
overlaps and is always readable on a phone. Templates (spec["template"]):

  flowchart  {"nodes":[{"id","text","shape":"box|round|diamond|oval|plain","color"}], "edges":[{"from","to","label"}],
              "direction":"TB|LR", "title"}                      flows, trees, organisation charts, classifications
  cycle      {"items":["text",...], "center":"text", "edge_labels":["text",...], "title", "colors":[...]}
  hub        {"center":"text", "spokes":["text",...], "title"}                  concept maps, "users of ..." diagrams
  graph      {"x_label","y_label","xmax","ymax","series":[{"label","points":[[x,y],...],"smooth":true,"color","style":"solid|dashed",
              "label_at":"end|start|mid"}], "guides":[{"x","y","x_text","y_text"}], "points":[{"x","y","text","dx","dy"}],
              "shades":[{"polygon":[[x,y],...],"text","color"}], "notes":[{"x","y","text"}], "xticks":[[x,"text"]], "yticks":[[y,"text"]], "title"}
  chart      {"kind":"bar|hbar|pie|stacked","categories":[...],"series":[{"label","values":[...]}], "y_label","x_label","title","values_shown":true}
  table      {"columns":["..."], "rows":[["..."]], "title", "first_col_bold":true, "col_colors":[...], "caption"}
  timeline   {"events":[{"when","title","text"}], "title"}
  taccount   {"accounts":[{"title","left_head":"Dr","right_head":"Cr","left":[[date,particulars,amount],...],"right":[...]}], "title"}
"""
import math, textwrap
import numpy as np
from matplotlib.patches import FancyBboxPatch, Polygon, Ellipse, FancyArrowPatch, Rectangle
from style import plt, INK, GREEN, BLUE, PINK, LAV, CREAM, ORANGE, GREY, DEEP

MIN_PT = 14            # smallest text in any template
TITLE_PT = 19
PALETTE = {"green": GREEN, "blue": BLUE, "pink": PINK, "lav": LAV, "cream": CREAM, "orange": ORANGE, "grey": GREY, "white": "#ffffff"}
CYCLE = [BLUE, GREEN, CREAM, PINK, LAV, ORANGE, GREY]
EDGE = "#4a5160"


def col(c, default=CREAM):
    return PALETTE.get(c, c) if c else default


def W(s, n):
    return "\n".join(textwrap.fill(p, n) for p in str(s).split("\n"))


def new_fig(w_in, h_in):
    fig = plt.figure(figsize=(w_in, h_in), dpi=150)
    fig.patch.set_facecolor("white")
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, w_in); ax.set_ylim(0, h_in); ax.axis("off")
    return fig, ax


def measure(fig, s, pt, weight="medium", spacing=1.25):
    t = fig.text(0, 0, s, fontsize=pt, fontweight=weight, linespacing=spacing)
    bb = t.get_window_extent(fig.canvas.get_renderer()); t.remove()
    return bb.width / fig.dpi, bb.height / fig.dpi


def txt_size(s, pt=MIN_PT, weight="medium"):
    fig = plt.figure(figsize=(4, 4), dpi=150)
    r = measure(fig, s, pt, weight); plt.close(fig); return r


def finish(fig, out):
    fig.savefig(out, facecolor="white", dpi=150)
    plt.close(fig)


def declutter(fig, texts, ax=None, iters=60):
    """Nudge overlapping Text artists apart (vertically first) until their boxes do not intersect."""
    r = fig.canvas.get_renderer()
    for _ in range(iters):
        moved = False
        bbs = [t.get_window_extent(r).expanded(1.04, 1.12) for t in texts]
        for i in range(len(texts)):
            for j in range(i + 1, len(texts)):
                a, b = bbs[i], bbs[j]
                if a.overlaps(b):
                    dy = (min(a.y1, b.y1) - max(a.y0, b.y0)) / 2 + 2
                    up, dn = (texts[i], texts[j]) if a.y0 + a.y1 > b.y0 + b.y1 else (texts[j], texts[i])
                    for t, s in ((up, 1), (dn, -1)):
                        x, y = t.get_position()
                        inv = (ax or t.axes).transData.inverted()
                        p0 = inv.transform((0, 0)); p1 = inv.transform((0, dy))
                        t.set_position((x, y + s * (p1[1] - p0[1])))
                    moved = True
        if not moved:
            break


# ---------------------------------------------------------------- flowchart / tree
def _layers(nodes, edges):
    ids = [n["id"] for n in nodes]
    out = {i: [] for i in ids}
    for e in edges:
        if e["from"] in out and e["to"] in out:
            out[e["from"]].append(e["to"])
    state, back = {}, set()
    def dfs(u):
        state[u] = 1
        for v in out[u]:
            if state.get(v) == 1: back.add((u, v))
            elif v not in state: dfs(v)
        state[u] = 2
    indeg = {i: 0 for i in ids}
    for e in edges:
        if e["to"] in indeg and e["from"] in indeg: indeg[e["to"]] += 1
    for i in ids:
        if indeg[i] == 0 and i not in state: dfs(i)
    for i in ids:
        if i not in state: dfs(i)
    layer = {i: 0 for i in ids}
    for _ in range(len(ids) + 1):
        ch = False
        for e in edges:
            a, b = e["from"], e["to"]
            if a in layer and b in layer and (a, b) not in back and layer[b] < layer[a] + 1:
                layer[b] = layer[a] + 1; ch = True
        if not ch: break
    return layer, back


def flowchart(spec, out):
    nodes, edges = spec["nodes"], [e for e in spec.get("edges", [])]
    direction = spec.get("direction", "TB").upper()
    layer, back = _layers(nodes, edges)
    ids = [n["id"] for n in nodes]; byid = {n["id"]: n for n in nodes}
    nl = max(layer.values()) + 1
    groups = [[i for i in ids if layer[i] == k] for k in range(nl)]
    pos = {}
    for k, g in enumerate(groups):                   # order within a layer by the mean position of the parents
        if k == 0:
            order = g
        else:
            def key(i):
                ps = [pos[e["from"]] for e in edges if e["to"] == i and e["from"] in pos]
                return sum(ps) / len(ps) if ps else 0
            order = sorted(g, key=key)
        for j, i in enumerate(order): pos[i] = j - (len(order) - 1) / 2
        groups[k] = order
    wrap_n = 20 if direction == "TB" else 18
    probe = plt.figure(figsize=(4, 4), dpi=150)
    size = {}
    for n in nodes:
        t = W(n["text"], wrap_n); w, h = measure(probe, t, MIN_PT)
        shape = n.get("shape", "box")
        pad_w, pad_h = (0.55, 0.38) if shape in ("diamond",) else (0.4, 0.3)
        if shape == "diamond": w, h = w * 1.5, h * 1.6
        size[n["id"]] = (w + pad_w, h + pad_h, t)
    plt.close(probe)
    mw = max(s[0] for s in size.values()); mh = max(s[1] for s in size.values())
    widest = max(len(g) for g in groups)
    gap_w, gap_h = 0.5, 0.75
    if direction == "TB":
        cell_w, cell_h = mw + gap_w, mh + gap_h
        fw = max(widest * cell_w, 5.5) + 0.8; fh = nl * cell_h + 0.8 + (0.7 if spec.get("title") else 0)
        P = lambda i: (fw / 2 + pos[i] * cell_w, fh - 0.4 - (0.7 if spec.get("title") else 0) - layer[i] * cell_h - mh / 2)
    else:
        cell_w, cell_h = mw + 1.0, mh + 0.5
        fw = nl * cell_w + 0.8; fh = max(widest * cell_h, 3) + 0.8 + (0.7 if spec.get("title") else 0)
        P = lambda i: (0.4 + layer[i] * cell_w + mw / 2, (fh - (0.7 if spec.get("title") else 0)) / 2 - pos[i] * cell_h)
    fig, ax = new_fig(fw, fh)
    if spec.get("title"):
        ax.text(fw / 2, fh - 0.4, spec["title"], ha="center", va="center", fontsize=TITLE_PT, fontweight="semibold", color=INK)
    boxes = {}
    for k, n in enumerate(nodes):
        x, y = P(n["id"]); w, h, t = size[n["id"]]
        w = mw if n.get("shape", "box") != "diamond" else max(w, mw); h = max(h, mh) if n.get("shape", "box") != "diamond" else h
        shape = n.get("shape", "box"); c = col(n.get("color"), [CREAM, BLUE, GREEN, LAV, PINK][k % 5] if not n.get("color") and False else CREAM)
        if not n.get("color"): c = [BLUE, GREEN, CREAM, PINK, LAV][layer[n["id"]] % 5] if direction == "TB" else CREAM
        if shape == "diamond":
            ax.add_patch(Polygon([[x, y + h / 2], [x + w / 2, y], [x, y - h / 2], [x - w / 2, y]], fc=c, ec=EDGE, lw=1.6, zorder=3))
        elif shape == "oval":
            ax.add_patch(Ellipse((x, y), w, h, fc=c, ec=EDGE, lw=1.6, zorder=3))
        elif shape == "plain":
            pass
        else:
            ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={0.18 if shape=='round' else 0.07}", fc=c, ec=EDGE, lw=1.6, zorder=3))
        ax.text(x, y, t, ha="center", va="center", fontsize=MIN_PT, color=INK, zorder=4, linespacing=1.25)
        boxes[n["id"]] = (x, y, w, h)
    labels = []
    for e in edges:
        a, b = e["from"], e["to"]
        if a not in boxes or b not in boxes: continue
        (x1, y1, w1, h1), (x2, y2, w2, h2) = boxes[a], boxes[b]
        is_back = (a, b) in back; skip = abs(layer[b] - layer[a]) > 1 or layer[a] == layer[b]
        rad = 0.0
        if direction == "TB":
            if is_back:
                p, q, rad = (x1 + w1 / 2, y1), (x2 + w2 / 2, y2), -0.5
            elif layer[b] > layer[a]:
                p, q = (x1, y1 - h1 / 2), (x2, y2 + h2 / 2)
                if skip: p, q, rad = (x1 + w1 / 2, y1), (x2 + w2 / 2, y2), 0.0; q = (x2 + w2 / 2, y2); p = (x1 + w1 / 2, y1); rad = -0.25
            else:
                p, q = ((x1 + w1 / 2, y1), (x2 - w2 / 2, y2)) if x2 > x1 else ((x1 - w1 / 2, y1), (x2 + w2 / 2, y2))
        else:
            if is_back:
                p, q, rad = (x1, y1 + h1 / 2), (x2, y2 + h2 / 2), 0.5
            elif layer[b] > layer[a]:
                p, q = (x1 + w1 / 2, y1), (x2 - w2 / 2, y2)
                if skip: rad = 0.25
            else:
                p, q = ((x1, y1 - h1 / 2), (x2, y2 + h2 / 2)) if y2 < y1 else ((x1, y1 + h1 / 2), (x2, y2 - h2 / 2))
        ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=22, lw=2.0, color=EDGE, connectionstyle=f"arc3,rad={rad}", zorder=2, shrinkA=1, shrinkB=1))
        if e.get("label"):
            mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
            labels.append(ax.text(mx + 0.5 * rad * (q[1] - p[1]), my - 0.5 * rad * (q[0] - p[0]), W(e["label"], 16), ha="center", va="center", fontsize=MIN_PT - 1, color=INK,
                                  bbox=dict(fc="white", ec="none", pad=1.5), zorder=5))
    declutter(fig, labels, ax)
    finish(fig, out)


# ---------------------------------------------------------------- cycle and hub
def _node(ax, x, y, w, h, text, c, pt=MIN_PT):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.15", fc=c, ec=EDGE, lw=1.6, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=pt, color=INK, zorder=4, linespacing=1.25)


def cycle(spec, out):
    items = [W(t, 16) for t in spec["items"]]; n = len(items)
    probe = plt.figure(figsize=(4, 4), dpi=150)
    sz = [measure(probe, t, MIN_PT) for t in items]; plt.close(probe)
    bw = max(s[0] for s in sz) + 0.4; bh = max(s[1] for s in sz) + 0.3
    R = max(2.0, (n * (bw + 0.35)) / (2 * math.pi) * 1.15, (bh + 0.4) * n / (2 * math.pi) * 1.6)
    rx, ry = R * 1.1 + bw / 2 * 0.2, R
    fw, fh = 2 * rx + bw + 1.2, 2 * ry + bh + 1.2 + (0.7 if spec.get("title") else 0)
    fig, ax = new_fig(fw, fh)
    cx, cy = fw / 2, (fh - (0.7 if spec.get("title") else 0)) / 2
    if spec.get("title"):
        ax.text(fw / 2, fh - 0.4, spec["title"], ha="center", va="center", fontsize=TITLE_PT, fontweight="semibold", color=INK)
    pts = [(cx + rx * math.sin(2 * math.pi * k / n), cy + ry * math.cos(2 * math.pi * k / n)) for k in range(n)]
    cols = spec.get("colors") or CYCLE
    for k in range(n):
        a, b = pts[k], pts[(k + 1) % n]
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=24, lw=2.4, color=DEEP["blue"], connectionstyle="arc3,rad=-0.18", zorder=2,
                                     patchA=Rectangle((a[0] - bw / 2 - .05, a[1] - bh / 2 - .05), bw + .1, bh + .1), patchB=Rectangle((b[0] - bw / 2 - .08, b[1] - bh / 2 - .08), bw + .16, bh + .16)))
    for k in range(n):
        _node(ax, *pts[k], bw, bh, items[k], col(cols[k % len(cols)], CYCLE[k % len(CYCLE)]))
    labs = []
    for k, t in enumerate(spec.get("edge_labels") or []):
        if not t: continue
        a, b = pts[k % n], pts[(k + 1) % n]
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        vx, vy = mx - cx, my - cy; d = math.hypot(vx, vy) or 1
        labs.append(ax.text(mx + vx / d * 0.55, my + vy / d * 0.35, W(t, 14), ha="center", va="center", fontsize=MIN_PT - 1, color=INK, bbox=dict(fc="white", ec="none", pad=1.5), zorder=5))
    if spec.get("center"):
        ax.text(cx, cy, W(spec["center"], 16), ha="center", va="center", fontsize=MIN_PT + 2, fontweight="semibold", color=INK)
    declutter(fig, labs, ax)
    finish(fig, out)


def hub(spec, out):
    sp = [W(t, 18) for t in spec["spokes"]]; n = len(sp)
    probe = plt.figure(figsize=(4, 4), dpi=150)
    sz = [measure(probe, t, MIN_PT) for t in sp]; cs = measure(probe, W(spec["center"], 14), MIN_PT + 2, "semibold"); plt.close(probe)
    bw = max(s[0] for s in sz) + 0.4; bh = max(s[1] for s in sz) + 0.3
    R = max(2.4, n * (max(bw, bh) + 0.3) / (2 * math.pi) * 1.1)
    rx, ry = R * 1.15, R
    fw, fh = 2 * rx + bw + 1.0, 2 * ry + bh + 1.0 + (0.7 if spec.get("title") else 0)
    fig, ax = new_fig(fw, fh); cx, cy = fw / 2, (fh - (0.7 if spec.get("title") else 0)) / 2
    if spec.get("title"):
        ax.text(fw / 2, fh - 0.4, spec["title"], ha="center", va="center", fontsize=TITLE_PT, fontweight="semibold", color=INK)
    pts = [(cx + rx * math.sin(2 * math.pi * k / n), cy + ry * math.cos(2 * math.pi * k / n)) for k in range(n)]
    cw, ch = cs[0] + 0.7, cs[1] + 0.6
    for k, p in enumerate(pts):
        ax.add_patch(FancyArrowPatch((cx, cy), p, arrowstyle="-|>", mutation_scale=22, lw=2.2, color=EDGE, zorder=2,
                                     patchA=Ellipse((cx, cy), cw + .1, ch + .1), patchB=Rectangle((p[0] - bw / 2 - .06, p[1] - bh / 2 - .06), bw + .12, bh + .12)))
    ax.add_patch(Ellipse((cx, cy), cw, ch, fc=GREEN, ec=EDGE, lw=1.8, zorder=3))
    ax.text(cx, cy, W(spec["center"], 14), ha="center", va="center", fontsize=MIN_PT + 2, fontweight="semibold", color=INK, zorder=4)
    for k, p in enumerate(pts):
        _node(ax, *p, bw, bh, sp[k], CYCLE[k % len(CYCLE)])
    finish(fig, out)


# ---------------------------------------------------------------- graph
def _spline(pts, n=160):
    p = np.array(pts, float)
    if len(p) < 3: return p[:, 0], p[:, 1]
    t = np.r_[0, np.cumsum(np.hypot(*np.diff(p, axis=0).T))]
    tt = np.linspace(0, t[-1], n)
    x = np.interp(tt, t, p[:, 0]); y = np.interp(tt, t, p[:, 1])
    # Catmull-Rom through the points (parametrised by chord length)
    out = []
    P = np.vstack([2 * p[0] - p[1], p, 2 * p[-1] - p[-2]])
    for i in range(len(p) - 1):
        p0, p1, p2, p3 = P[i], P[i + 1], P[i + 2], P[i + 3]
        for s in np.linspace(0, 1, max(8, n // len(p)), endpoint=False):
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * s + (2 * p0 - 5 * p1 + 4 * p2 - p3) * s ** 2 + (-p0 + 3 * p1 - 3 * p2 + p3) * s ** 3))
    out.append(p[-1]); o = np.array(out)
    return o[:, 0], o[:, 1]


def graph(spec, out):
    fig = plt.figure(figsize=(9.5, 7.2), dpi=150); fig.patch.set_facecolor("white")
    ax = fig.add_axes([0.1, 0.12, 0.84, 0.76])
    xmax, ymax = spec.get("xmax", 10), spec.get("ymax", 10)
    ax.set_xlim(0, xmax); ax.set_ylim(0, ymax)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    for s in ("left", "bottom"): ax.spines[s].set_linewidth(2.4); ax.spines[s].set_color(INK)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel(spec.get("x_label", ""), fontsize=MIN_PT + 2, color=INK, loc="right")
    ax.set_ylabel(spec.get("y_label", ""), fontsize=MIN_PT + 2, color=INK, loc="top", rotation=0, labelpad=10)
    ax.plot(1, 0, ">k", transform=ax.transAxes, clip_on=False, ms=9); ax.plot(0, 1, "^k", transform=ax.transAxes, clip_on=False, ms=9)
    if spec.get("title"): fig.suptitle(spec["title"], fontsize=TITLE_PT, fontweight="semibold", color=INK, y=0.97)
    texts = []
    for sh in spec.get("shades", []):
        ax.add_patch(Polygon(sh["polygon"], closed=True, fc=col(sh.get("color"), "#c8e6c9"), ec="none", alpha=0.7, zorder=1))
        if sh.get("text"):
            c = np.mean(np.array(sh["polygon"], float), axis=0)
            texts.append(ax.text(c[0], c[1], W(sh["text"], 14), ha="center", va="center", fontsize=MIN_PT, color=INK, zorder=6))
    palette = [DEEP["blue"], DEEP["pink"], DEEP["green"], DEEP["orange"], DEEP["lav"]]
    for k, s in enumerate(spec.get("series", [])):
        pts = s["points"]; c = col(s.get("color"), palette[k % 5]) if s.get("color") else palette[k % 5]
        x, y = _spline(pts) if s.get("smooth", True) and len(pts) > 2 else (np.array([p[0] for p in pts]), np.array([p[1] for p in pts]))
        ax.plot(x, y, color=c, lw=3.4, ls="--" if s.get("style") == "dashed" else "-", zorder=3, solid_capstyle="round")
        if s.get("label"):
            at = s.get("label_at", "end"); i = {"end": -1, "start": 0, "mid": len(x) // 2}[at]
            ha = {"end": "left", "start": "right", "mid": "center"}[at]
            dx = {"end": 0.012, "start": -0.012, "mid": 0}[at] * xmax
            texts.append(ax.text(x[i] + dx, y[i], W(s["label"], 16), color=c, fontsize=MIN_PT + 1, fontweight="semibold", ha=ha, va="center", zorder=6,
                                 bbox=dict(fc="white", ec="none", pad=1.2, alpha=0.9)))
    for gd in spec.get("guides", []):
        gx, gy = gd.get("x"), gd.get("y")
        if gx is not None and gy is not None:
            ax.plot([gx, gx], [0, gy], color="#7a8190", ls=(0, (5, 4)), lw=2, zorder=2); ax.plot([0, gx], [gy, gy], color="#7a8190", ls=(0, (5, 4)), lw=2, zorder=2)
            ax.plot([gx], [gy], "o", color=INK, ms=9, zorder=5)
        elif gx is not None:
            ax.plot([gx, gx], [0, ymax * 0.97], color="#7a8190", ls=(0, (5, 4)), lw=2, zorder=2)
        elif gy is not None:
            ax.plot([0, xmax * 0.97], [gy, gy], color="#7a8190", ls=(0, (5, 4)), lw=2, zorder=2)
        if gd.get("x_text") and gx is not None:
            ax.text(gx, -0.012 * ymax, W(gd["x_text"], 12), ha="center", va="top", fontsize=MIN_PT, color=INK, clip_on=False)
        if gd.get("y_text") and gy is not None:
            ax.text(-0.012 * xmax, gy, W(gd["y_text"], 12), ha="right", va="center", fontsize=MIN_PT, color=INK, clip_on=False)
    for t_, lst in (("x", spec.get("xticks", [])), ("y", spec.get("yticks", []))):
        for v, s_ in lst:
            if t_ == "x": ax.text(v, -0.012 * ymax, s_, ha="center", va="top", fontsize=MIN_PT, color=INK, clip_on=False)
            else: ax.text(-0.012 * xmax, v, s_, ha="right", va="center", fontsize=MIN_PT, color=INK, clip_on=False)
    for p in spec.get("points", []):
        ax.plot([p["x"]], [p["y"]], "o", color=INK, ms=9, zorder=5)
        if p.get("text"):
            texts.append(ax.text(p["x"] + p.get("dx", 0.02 * xmax), p["y"] + p.get("dy", 0.03 * ymax), W(p["text"], 16), fontsize=MIN_PT, color=INK, ha="left", va="bottom", zorder=6,
                                 bbox=dict(fc="white", ec="none", pad=1.2, alpha=0.9)))
    for nt in spec.get("notes", []):
        texts.append(ax.text(nt["x"], nt["y"], W(nt["text"], 18), fontsize=MIN_PT, color=INK, ha="center", va="center", zorder=6, bbox=dict(fc="white", ec="none", pad=1.2, alpha=0.9)))
    declutter(fig, texts, ax)
    finish(fig, out)


# ---------------------------------------------------------------- chart (bar / pie / stacked)
def chart(spec, out):
    kind = spec.get("kind", "bar"); cats = spec.get("categories", []); series = spec.get("series", [])
    fig = plt.figure(figsize=(9.5, 7), dpi=150); fig.patch.set_facecolor("white")
    colors = [BLUE, PINK, GREEN, ORANGE, LAV, CREAM]
    if spec.get("title"): fig.suptitle(spec["title"], fontsize=TITLE_PT, fontweight="semibold", color=INK, y=0.97)
    if kind == "pie":
        ax = fig.add_axes([0.05, 0.08, 0.9, 0.78]); vals = series[0]["values"]
        w, _ = ax.pie(vals, colors=colors[:len(vals)], startangle=90, counterclock=False, wedgeprops=dict(ec="white", lw=3))
        for wedge, c, v in zip(w, cats, vals):
            ang = math.radians((wedge.theta1 + wedge.theta2) / 2)
            ax.text(1.18 * math.cos(ang), 1.18 * math.sin(ang), W(f"{c}\n{v:g}{spec.get('unit', '%')}" if spec.get("values_shown", True) else c, 14), ha="center", va="center", fontsize=MIN_PT + 1, color=INK)
        ax.set_xlim(-1.7, 1.7); ax.set_ylim(-1.5, 1.5)
        finish(fig, out); return
    ax = fig.add_axes([0.13, 0.16, 0.82, 0.70])
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    for s in ("left", "bottom"): ax.spines[s].set_linewidth(2); ax.spines[s].set_color(INK)
    ax.tick_params(labelsize=MIN_PT, colors=INK, length=4)
    n, ns = len(cats), max(1, len(series)); idx = np.arange(n)
    if kind in ("bar", "stacked"):
        wd = 0.7 / (1 if kind == "stacked" else ns); bottom = np.zeros(n)
        for k, s in enumerate(series):
            v = np.array(s["values"], float)
            xs = idx if kind == "stacked" else idx - 0.35 + wd * (k + 0.5)
            bars = ax.bar(xs, v, wd, bottom=bottom if kind == "stacked" else 0, color=colors[k % 6], ec=EDGE, lw=1.3, label=s.get("label"))
            if spec.get("values_shown", True):
                for b, vv, bt in zip(bars, v, bottom):
                    ax.text(b.get_x() + b.get_width() / 2, (bt + vv / 2) if kind == "stacked" else vv, f"{vv:g}", ha="center", va="center" if kind == "stacked" else "bottom", fontsize=MIN_PT, color=INK)
            if kind == "stacked": bottom += v
        ax.set_xticks(idx); ax.set_xticklabels([W(c, 10) for c in cats])
    else:
        hs = 0.7 / ns
        for k, s in enumerate(series):
            v = np.array(s["values"], float); ys = idx - 0.35 + hs * (k + 0.5)
            bars = ax.barh(ys, v, hs, color=colors[k % 6], ec=EDGE, lw=1.3, label=s.get("label"))
            if spec.get("values_shown", True):
                for b, vv in zip(bars, v): ax.text(vv, b.get_y() + b.get_height() / 2, f" {vv:g}", ha="left", va="center", fontsize=MIN_PT, color=INK)
        ax.set_yticks(idx); ax.set_yticklabels([W(c, 14) for c in cats]); ax.invert_yaxis()
    ax.set_xlabel(spec.get("x_label", ""), fontsize=MIN_PT + 1, color=INK); ax.set_ylabel(spec.get("y_label", ""), fontsize=MIN_PT + 1, color=INK)
    if ns > 1: ax.legend(fontsize=MIN_PT, frameon=False, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=ns)
    finish(fig, out)


# ---------------------------------------------------------------- table
def table(spec, out):
    cols_, rows = spec["columns"], spec["rows"]; nc = len(cols_)
    probe = plt.figure(figsize=(4, 4), dpi=150)
    wrapn = max(14, int(46 / nc * 1.25)) if nc > 1 else 40
    def cell(s, bold=False):
        t = W(s, wrapn); return t, measure(probe, t, MIN_PT, "semibold" if bold else "medium")
    heads = [cell(c, True) for c in cols_]
    body = [[cell(str(c), spec.get("first_col_bold", True) and j == 0) for j, c in enumerate(r)] for r in rows]
    cw = [max([heads[j][1][0]] + [r[j][1][0] for r in body if j < len(r)]) + 0.35 for j in range(nc)]
    plt.close(probe)
    rh = [max(h[1][1] for h in heads) + 0.32] + [max(c[1][1] for c in r) + 0.3 for r in body]
    fw = sum(cw) + 0.6; title_h = 0.75 if spec.get("title") else 0.1; cap_h = 0.8 if spec.get("caption") else 0.1
    fh = sum(rh) + title_h + cap_h + 0.4
    fig, ax = new_fig(fw, fh)
    if spec.get("title"): ax.text(fw / 2, fh - 0.4, spec["title"], ha="center", va="center", fontsize=TITLE_PT, fontweight="semibold", color=INK)
    y = fh - title_h - 0.2; hc = spec.get("col_colors") or [BLUE] * nc
    for i in range(len(rh)):
        x = 0.3; y -= rh[i]
        for j in range(nc):
            if i == 0: fc, t, bold = col(hc[j % len(hc)], BLUE), heads[j][0], "semibold"
            else:
                r = body[i - 1]; t = r[j][0] if j < len(r) else ""; fc = "#f4f1e8" if i % 2 else "#ffffff"
                if j == 0 and spec.get("first_col_bold", True): fc = "#e8eef6"
                bold = "semibold" if (j == 0 and spec.get("first_col_bold", True)) else "medium"
            ax.add_patch(Rectangle((x, y), cw[j], rh[i], fc=fc, ec="#9aa1ad", lw=1.3))
            ax.text(x + cw[j] / 2, y + rh[i] / 2, t, ha="center", va="center", fontsize=MIN_PT, fontweight=bold, color=INK, linespacing=1.25)
            x += cw[j]
    if spec.get("caption"): ax.text(fw / 2, 0.45, W(spec["caption"], int(fw * 7)), ha="center", va="center", fontsize=MIN_PT, color=INK, style="italic")
    finish(fig, out)


# ---------------------------------------------------------------- timeline (vertical, phone friendly)
def timeline(spec, out):
    ev = spec["events"]
    probe = plt.figure(figsize=(4, 4), dpi=150)
    items = []
    for e in ev:
        when = W(e.get("when", ""), 12); body = (e.get("title", "") + ("\n" if e.get("title") and e.get("text") else "") + e.get("text", ""))
        tw = W(e.get("title", ""), 38); xw = W(e.get("text", ""), 46)
        wh = measure(probe, when, MIN_PT + 1, "semibold"); th = measure(probe, tw, MIN_PT + 1, "semibold") if tw else (0, 0); xh = measure(probe, xw, MIN_PT) if xw else (0, 0)
        items.append((when, tw, xw, wh, th, xh))
    plt.close(probe)
    fw = 9.5; left = 2.2
    hs = [max(i[3][1], i[4][1] + i[5][1] + (0.08 if i[1] and i[2] else 0)) + 0.4 for i in items]
    th_ = 0.8 if spec.get("title") else 0.2
    fh = sum(hs) + th_ + 0.4
    fig, ax = new_fig(fw, fh)
    if spec.get("title"): ax.text(fw / 2, fh - 0.4, spec["title"], ha="center", va="center", fontsize=TITLE_PT, fontweight="semibold", color=INK)
    ax.plot([left, left], [0.25, fh - th_ - 0.15], color=EDGE, lw=3, zorder=1)
    y = fh - th_
    for k, (it, h) in enumerate(zip(items, hs)):
        cy = y - h / 2
        ax.text(left - 0.35, cy, it[0], ha="right", va="center", fontsize=MIN_PT + 1, fontweight="semibold", color=DEEP["blue"])
        ax.plot([left], [cy], "o", ms=14, mfc=CYCLE[k % 7], mec=EDGE, mew=2, zorder=3)
        top = cy + (it[4][1] + it[5][1] + (0.08 if it[1] and it[2] else 0)) / 2
        if it[1]:
            ax.text(left + 0.4, top, it[1], ha="left", va="top", fontsize=MIN_PT + 1, fontweight="semibold", color=INK); top -= it[4][1] + 0.08
        if it[2]:
            ax.text(left + 0.4, top, it[2], ha="left", va="top", fontsize=MIN_PT, color=INK)
        y -= h
    finish(fig, out)


# ---------------------------------------------------------------- T-accounts
def taccount(spec, out):
    accs = spec["accounts"]; n = len(accs); ncol = 1 if n == 1 else 2
    probe = plt.figure(figsize=(4, 4), dpi=150)
    def rows_of(a): return max(len(a.get("left", [])), len(a.get("right", [])), 1)
    rh = measure(probe, "Xg", MIN_PT)[1] + 0.2
    def colw(a, side):
        rs = a.get(side, [])
        wd = [0, 0, 0]
        for r in rs:
            for j in range(3):
                wd[j] = max(wd[j], measure(probe, str(r[j]) if j < len(r) else "", MIN_PT)[0])
        return [max(wd[0], 0.6) + 0.15, max(wd[1], 1.0) + 0.2, max(wd[2], 0.8) + 0.2]
    cells = []
    for a in accs:
        lw_, rw_ = colw(a, "left"), colw(a, "right"); cells.append((lw_, rw_, sum(lw_), sum(rw_)))
    plt.close(probe)
    cell_w = max(c[2] + c[3] for c in cells) + 0.4
    nrows = math.ceil(n / ncol)
    heights = [max(rows_of(accs[k]) for k in range(r * ncol, min(n, r * ncol + ncol))) * rh + 1.3 for r in range(nrows)]
    th_ = 0.8 if spec.get("title") else 0.2
    fw = ncol * (cell_w + 0.4) + 0.4; fh = sum(heights) + th_ + 0.3
    fig, ax = new_fig(fw, fh)
    if spec.get("title"): ax.text(fw / 2, fh - 0.4, spec["title"], ha="center", va="center", fontsize=TITLE_PT, fontweight="semibold", color=INK)
    y0 = fh - th_
    for r in range(nrows):
        for c in range(ncol):
            k = r * ncol + c
            if k >= n: break
            a = accs[k]; lw_, rw_, sl, sr = cells[k]; x0 = 0.4 + c * (cell_w + 0.4); w_ = cell_w
            half = w_ / 2
            ax.text(x0 + w_ / 2, y0 - 0.3, a.get("title", ""), ha="center", va="center", fontsize=MIN_PT + 2, fontweight="semibold", color=INK)
            ly = y0 - 0.65
            ax.plot([x0, x0 + w_], [ly, ly], color=INK, lw=3); ax.plot([x0 + half, x0 + half], [ly, ly - rows_of(a) * rh - 0.45], color=INK, lw=3)
            ax.text(x0 + 0.08, ly + 0.17, a.get("left_head", "Dr"), fontsize=MIN_PT, fontweight="semibold", color=DEEP["blue"], va="center")
            ax.text(x0 + w_ - 0.08, ly + 0.17, a.get("right_head", "Cr"), fontsize=MIN_PT, fontweight="semibold", color=DEEP["pink"], va="center", ha="right")
            for side, base, widths in (("left", x0, lw_), ("right", x0 + half, rw_)):
                scale = (half - 0.1) / sum(widths)
                for i, row in enumerate(a.get(side, [])):
                    yy = ly - 0.25 - i * rh - rh / 2 + 0.1; xx = base + 0.06
                    for j in range(3):
                        t = str(row[j]) if j < len(row) else ""
                        cw_ = widths[j] * min(1.0, scale) if scale < 1 else widths[j]
                        if j == 2: ax.text(xx + cw_ - 0.05, yy, t, ha="right", va="center", fontsize=MIN_PT, color=INK)
                        else: ax.text(xx, yy, t, ha="left", va="center", fontsize=MIN_PT, color=INK)
                        xx += cw_
        y0 -= heights[r]
    finish(fig, out)


TEMPLATES = {"flowchart": flowchart, "cycle": cycle, "hub": hub, "graph": graph, "chart": chart, "table": table, "timeline": timeline, "taccount": taccount}


def render(spec, out):
    TEMPLATES[spec["template"]](spec, out)
