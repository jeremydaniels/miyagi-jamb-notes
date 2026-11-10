from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 12)
    ax = fig.add_subplot(111)
    ax.set_xlim(-6.5, 6.5)
    ax.set_ylim(-6.5, 6.5)
    ax.set_aspect("equal")
    ax.axis("off")

    categories = [
        {"ar": "Al-Fuqara", "en": "The Poor", "icon": "empty_pockets"},
        {"ar": "Al-Masakin", "en": "The Needy", "icon": "needy_bowl"},
        {"ar": "Al-Amilina", "en": "Zakah Administrators", "icon": "admin_scroll"},
        {"ar": "Mu'allafat al-Qulub", "en": "Reconciliation of Hearts", "icon": "heart"},
        {"ar": "Fir-Riqab", "en": "Freeing Captives", "icon": "broken_chain"},
        {"ar": "Al-Gharimin", "en": "Those in Debt", "icon": "debt_scale"},
        {"ar": "Fi Sabilillah", "en": "In the Cause of Allah", "icon": "path_sun"},
        {"ar": "Ibn as-Sabil", "en": "The Stranded Traveller", "icon": "traveller"}
    ]

    colors = [GREEN, BLUE, PINK, LAV, ORANGE, CREAM, GREEN, BLUE]
    edge_colors = [
        DEEP["green"], DEEP["blue"], DEEP["pink"], DEEP["lav"],
        DEEP["orange"], DEEP["orange"], DEEP["green"], DEEP["blue"]
    ]

    r_in = 2.1
    r_out = 5.6
    n = 8
    angle_step = 360 / n

    for i, cat in enumerate(categories):
        theta1 = i * angle_step
        theta2 = (i + 1) * angle_step
        wedge = patches.Wedge(
            (0, 0), r_out, theta1, theta2, width=r_out - r_in,
            facecolor=colors[i % len(colors)], edgecolor="white", linewidth=3
        )
        ax.add_patch(wedge)

        mid_angle = (theta1 + theta2) / 2
        rad = np.radians(mid_angle)

        # Icon positions
        r_icon = 4.35
        xi, yi = r_icon * np.cos(rad), r_icon * np.sin(rad)
        ec = edge_colors[i % len(edge_colors)]

        # Draw thematic icon per category
        if cat["icon"] == "empty_pockets":
            ax.plot([xi - 0.2, xi + 0.2], [yi - 0.1, yi - 0.1], color=ec, lw=2.5)
            ax.plot([xi - 0.2, xi - 0.15, xi + 0.15, xi + 0.2], [yi - 0.1, yi - 0.35, yi - 0.35, yi - 0.1], color=ec, lw=2.5)
            ax.plot([xi - 0.28, xi - 0.15], [yi - 0.1, yi + 0.12], color=ec, lw=2.2)
            ax.plot([xi + 0.28, xi + 0.15], [yi - 0.1, yi + 0.12], color=ec, lw=2.2)
            ax.plot(xi, yi + 0.28, "o", color=ec, markersize=8)

        elif cat["icon"] == "needy_bowl":
            bowl = patches.Arc((xi, yi - 0.05), 0.55, 0.45, theta1=180, theta2=360, color=ec, lw=3)
            ax.add_patch(bowl)
            ax.plot([xi - 0.275, xi + 0.275], [yi - 0.05, yi - 0.05], color=ec, lw=3)
            ax.plot(xi, yi + 0.2, "o", color=ec, markersize=5)
            ax.plot(xi - 0.12, yi + 0.12, "o", color=ec, markersize=4)
            ax.plot(xi + 0.12, yi + 0.12, "o", color=ec, markersize=4)

        elif cat["icon"] == "admin_scroll":
            rect = patches.FancyBboxPatch((xi - 0.22, yi - 0.28), 0.44, 0.56,
                                          boxstyle="round,pad=0.04", fc="white", ec=ec, lw=2.5)
            ax.add_patch(rect)
            ax.plot([xi - 0.13, xi + 0.13], [yi + 0.14, yi + 0.14], color=ec, lw=2.2)
            ax.plot([xi - 0.13, xi + 0.13], [yi + 0.0, yi + 0.0], color=ec, lw=2.2)
            ax.plot([xi - 0.13, xi + 0.05], [yi - 0.14, yi - 0.14], color=ec, lw=2.2)

        elif cat["icon"] == "heart":
            t = np.linspace(0, 2 * np.pi, 100)
            hx = 0.023 * 16 * np.sin(t) ** 3
            hy = 0.023 * (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t))
            ax.fill(xi + hx, yi + hy + 0.05, color=ec)

        elif cat["icon"] == "broken_chain":
            l1 = patches.Ellipse((xi - 0.16, yi), 0.32, 0.2, angle=25, fill=False, edgecolor=ec, lw=2.8)
            l2 = patches.Ellipse((xi + 0.16, yi), 0.32, 0.2, angle=-25, fill=False, edgecolor=ec, lw=2.8)
            ax.add_patch(l1)
            ax.add_patch(l2)
            ax.plot([xi - 0.06, xi - 0.01], [yi + 0.14, yi + 0.24], color=ec, lw=2)
            ax.plot([xi + 0.06, xi + 0.01], [yi - 0.14, yi - 0.24], color=ec, lw=2)

        elif cat["icon"] == "debt_scale":
            ax.plot([xi, xi], [yi - 0.26, yi + 0.24], color=ec, lw=2.5)
            ax.plot([xi - 0.28, xi + 0.28], [yi + 0.18, yi + 0.1], color=ec, lw=2.5)
            ax.plot([xi - 0.28, xi - 0.34], [yi + 0.18, yi - 0.04], color=ec, lw=1.8)
            ax.plot([xi - 0.28, xi - 0.22], [yi + 0.18, yi - 0.04], color=ec, lw=1.8)
            ax.plot([xi + 0.28, xi + 0.22], [yi + 0.1, yi - 0.12], color=ec, lw=1.8)
            ax.plot([xi + 0.28, xi + 0.34], [yi + 0.1, yi - 0.12], color=ec, lw=1.8)
            p1 = patches.Arc((xi - 0.28, yi - 0.04), 0.18, 0.14, theta1=180, theta2=360, color=ec, lw=2)
            p2 = patches.Arc((xi + 0.28, yi - 0.12), 0.18, 0.14, theta1=180, theta2=360, color=ec, lw=2)
            ax.add_patch(p1)
            ax.add_patch(p2)

        elif cat["icon"] == "path_sun":
            ax.plot([xi - 0.22, xi], [yi - 0.24, yi + 0.14], color=ec, lw=2.5)
            ax.plot([xi + 0.22, xi], [yi - 0.24, yi + 0.14], color=ec, lw=2.5)
            ax.plot(xi, yi + 0.2, "o", color=ec, markersize=9)
            for a in range(0, 360, 45):
                ra = np.radians(a)
                ax.plot([xi + 0.16 * np.cos(ra), xi + 0.23 * np.cos(ra)],
                        [yi + 0.2 + 0.16 * np.sin(ra), yi + 0.2 + 0.23 * np.sin(ra)], color=ec, lw=1.8)

        elif cat["icon"] == "traveller":
            # Walking stick + travel bag
            ax.plot([xi + 0.18, xi + 0.12], [yi + 0.28, yi - 0.28], color=ec, lw=2.5)
            bag = patches.FancyBboxPatch((xi - 0.26, yi - 0.22), 0.36, 0.36,
                                         boxstyle="round,pad=0.03", fc=ec, ec=ec)
            ax.add_patch(bag)
            ax.plot([xi - 0.16, xi - 0.16, xi + 0.02, xi + 0.02],
                    [yi + 0.14, yi + 0.24, yi + 0.24, yi + 0.14], color=ec, lw=2)

        # Labels positioned nicely inside slice
        r_text = 3.0
        xt, yt = r_text * np.cos(rad), r_text * np.sin(rad)
        label_text = f"{cat['ar']}\n({cat['en']})"
        ax.text(xt, yt, label_text, ha="center", va="center",
                fontsize=14, color=INK, fontweight="bold",
                bbox=dict(fc="white", ec="none", pad=2, alpha=0.9))

    # Outer dividing boundaries
    for i in range(n):
        angle = np.radians(i * angle_step)
        ax.plot([r_in * np.cos(angle), r_out * np.cos(angle)],
                [r_in * np.sin(angle), r_out * np.sin(angle)],
                color="white", lw=3.5)

    # Outer border circle
    outer_circle = patches.Circle((0, 0), r_out, fill=False, edgecolor=GREY, lw=2)
    ax.add_patch(outer_circle)

    # Center circle
    center_patch = patches.Circle((0, 0), r_in, facecolor="white", edgecolor=GREY, lw=3)
    ax.add_patch(center_patch)

    inner_ring = patches.Circle((0, 0), r_in - 0.18, fill=False, edgecolor=DEEP["blue"], lw=1.5, ls="--")
    ax.add_patch(inner_ring)

    # Center text
    ax.text(0, 0.35, "Q. 9:60", ha="center", va="center",
            fontsize=17, fontweight="bold", color=DEEP["blue"])
    ax.text(0, -0.25, "Zakah\nBeneficiaries", ha="center", va="center",
            fontsize=16, fontweight="bold", color=INK)

    save(fig, out)
