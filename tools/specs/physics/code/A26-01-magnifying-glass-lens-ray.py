from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    f = 4.0
    lens_height = 5.2

    x_min, x_max = -9.2, 7.0
    ax.plot([x_min, x_max], [0, 0], color=INK, lw=1.5, zorder=1)

    lens_thick = 0.55
    t = np.linspace(-lens_height, lens_height, 200)
    x_lens_r = lens_thick * (1 - (t / lens_height)**2)
    x_lens_l = -x_lens_r
    ax.fill_betweenx(t, x_lens_l, x_lens_r, color=BLUE, alpha=0.18, zorder=2)
    ax.plot(x_lens_l, t, color=DEEP["blue"], lw=2, zorder=3)
    ax.plot(x_lens_r, t, color=DEEP["blue"], lw=2, zorder=3)
    ax.plot([0, 0], [-lens_height, lens_height], color=DEEP["blue"], lw=1.2, ls=":", zorder=3)

    ax.plot([-f, f], [0, 0], "o", color=INK, markersize=5, zorder=4)
    ax.text(-f, -0.45, "Focal point F", ha="center", va="top", fontsize=15, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))
    ax.text(f, -0.45, "F", ha="center", va="top", fontsize=15, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    u = -2.0
    h = 1.6
    v = (u * f) / (u + f)
    h_img = (h / u) * v

    ax.annotate("", xy=(u, h), xytext=(u, 0),
                arrowprops=dict(arrowstyle="-|>", color=DEEP["green"], lw=3.0,
                                mutation_scale=22), zorder=6)
    ax.text(u, -0.45, "Object", ha="center", va="top", fontsize=15, color=DEEP["green"], weight="bold",
            bbox=dict(fc="white", ec="none", pad=2))

    ax.plot([v, v], [0, h_img], color=DEEP["pink"], lw=3.5, ls="--", zorder=6)
    head_len = 0.35
    head_w = 0.22
    ax.fill([v, v - head_w, v + head_w], [h_img, h_img - head_len, h_img - head_len],
            color=DEEP["pink"], zorder=7)

    ax.annotate("Virtual, erect, magnified image", xy=(v + 0.1, h_img), xytext=(-1.5, 4.2),
                arrowprops=dict(arrowstyle="-", color=GREY, lw=1.2),
                ha="center", va="bottom", fontsize=15, color=DEEP["pink"], weight="bold",
                bbox=dict(fc="white", ec="none", pad=2), zorder=8)

    ax.plot([u, 0], [h, h], color=DEEP["orange"], lw=2.2, zorder=5)
    x_fwd1 = np.linspace(0, 6.2, 100)
    y_fwd1 = h * (1.0 - x_fwd1 / f)
    ax.plot(x_fwd1, y_fwd1, color=DEEP["orange"], lw=2.2, zorder=5)
    x_back1 = np.linspace(v - 1.5, 0, 100)
    y_back1 = h * (1.0 - x_back1 / f)
    ax.plot(x_back1, y_back1, color=DEEP["orange"], lw=1.8, ls="--", zorder=4)

    x_fwd2 = np.linspace(0, 6.2, 100)
    y_fwd2 = (h / u) * x_fwd2
    ax.plot([u, 0], [h, 0], color=DEEP["blue"], lw=2.2, zorder=5)
    ax.plot(x_fwd2, y_fwd2, color=DEEP["blue"], lw=2.2, zorder=5)
    x_back2 = np.linspace(v - 1.5, 0, 100)
    y_back2 = (h / u) * x_back2
    ax.plot(x_back2, y_back2, color=DEEP["blue"], lw=1.8, ls="--", zorder=4)

    def add_arrow(p1, p2, color):
        mx = (p1[0] + p2[0]) / 2.0
        my = (p1[1] + p2[1]) / 2.0
        dx = (p2[0] - p1[0]) * 0.001
        dy = (p2[1] - p1[1]) * 0.001
        ax.annotate("", xy=(mx + dx, my + dy), xytext=(mx - dx, my - dy),
                    arrowprops=dict(arrowstyle="->", color=color, lw=2.0, mutation_scale=15),
                    zorder=7)

    add_arrow((u, h), (0, h), DEEP["orange"])
    add_arrow((0, h), (3.0, h * (1.0 - 3.0 / f)), DEEP["orange"])
    add_arrow((u, h), (0, 0), DEEP["blue"])
    add_arrow((0, 0), (3.0, (h / u) * 3.0), DEEP["blue"])

    ax.text(0.15, -0.45, "O", ha="left", va="top", fontsize=15, color=INK)

    ax.set_xlim(-9.2, 6.8)
    ax.set_ylim(-4.2, 5.0)

    save(fig, out)
