from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_aspect('equal')
    ax.axis('off')

    # Browser Window Outer Dimensions
    bx, by, bw, bh = 0.8, 0.8, 6.2, 5.2

    # Browser main frame (window)
    window_rect = patches.FancyBboxPatch((bx, by), bw, bh,
                                         boxstyle="Round,pad=0.02,rounding_size=0.15",
                                         facecolor="white", edgecolor=INK, linewidth=2.0)
    ax.add_patch(window_rect)

    # Title bar / Tab bar background
    title_h = 0.55
    title_rect = patches.FancyBboxPatch((bx, by + bh - title_h), bw, title_h,
                                        boxstyle="Round,pad=0.02,rounding_size=0.15",
                                        facecolor=CREAM, edgecolor=INK, linewidth=1.5)
    ax.add_patch(title_rect)

    # Window control dots (close, minimize, maximize)
    dot_y = by + bh - title_h / 2
    for i, c in enumerate([DEEP["pink"], DEEP["orange"], DEEP["green"]]):
        circle = plt.Circle((bx + 0.3 + i * 0.28, dot_y), 0.08, facecolor=c, edgecolor=INK, linewidth=1.0)
        ax.add_patch(circle)

    # Browser tab
    tab_w, tab_h = 2.2, 0.4
    tab_rect = patches.FancyBboxPatch((bx + 1.2, by + bh - title_h + 0.05), tab_w, tab_h,
                                      boxstyle="Round,pad=0.01,rounding_size=0.08",
                                      facecolor="white", edgecolor=GREY, linewidth=1.2)
    ax.add_patch(tab_rect)
    ax.text(bx + 1.35, by + bh - title_h + 0.22, "JAMB Portal", fontsize=14, color=INK, va="center")

    # Navigation / Address Bar area
    nav_h = 0.65
    nav_y = by + bh - title_h - nav_h
    nav_bg = patches.Rectangle((bx, nav_y), bw, nav_h, facecolor="#F4F4F4", edgecolor=GREY, linewidth=1.0)
    ax.add_patch(nav_bg)

    # Back / Forward / Refresh arrows (simplified)
    ax.text(bx + 0.25, nav_y + 0.32, "◀", fontsize=15, color=GREY, va="center")
    ax.text(bx + 0.60, nav_y + 0.32, "▶", fontsize=15, color=GREY, va="center")
    ax.text(bx + 0.95, nav_y + 0.32, "↻", fontsize=16, color=INK, va="center", weight="bold")

    # Address Bar
    addr_x, addr_y, addr_w, addr_h = bx + 1.3, nav_y + 0.12, bw - 1.5, 0.42
    addr_rect = patches.FancyBboxPatch((addr_x, addr_y), addr_w, addr_h,
                                       boxstyle="Round,pad=0.01,rounding_size=0.08",
                                       facecolor="white", edgecolor=INK, linewidth=1.2)
    ax.add_patch(addr_rect)
    ax.text(addr_x + 0.2, addr_y + addr_h / 2, "https://www.jamb.org.ng", fontsize=14, color=INK, va="center")

    # Content Area divider
    content_top = nav_y
    ax.plot([bx, bx + bw], [content_top, content_top], color=GREY, linewidth=1.5)

    # Webpage Header / Nav inside content
    site_head_y = content_top - 0.55
    # "Home" button
    home_btn = patches.FancyBboxPatch((bx + 0.5, site_head_y), 1.1, 0.38,
                                      boxstyle="Round,pad=0.01,rounding_size=0.06",
                                      facecolor=LAV, edgecolor=DEEP["lav"], linewidth=1.5)
    ax.add_patch(home_btn)
    ax.text(bx + 1.05, site_head_y + 0.19, "Home", fontsize=14, color=INK, weight="bold", ha="center", va="center")

    # Secondary nav texts
    ax.text(bx + 1.9, site_head_y + 0.19, "About", fontsize=14, color=GREY, va="center")
    ax.text(bx + 2.7, site_head_y + 0.19, "Admissions", fontsize=14, color=GREY, va="center")
    ax.text(bx + 4.1, site_head_y + 0.19, "Contact", fontsize=14, color=GREY, va="center")

    # Homepage Content Heading & Paragraphs
    ax.text(bx + 0.5, content_top - 1.05, "Welcome to JAMB e-Facility", fontsize=16, color=INK, weight="bold")
    
    body_text_1 = "The Joint Admissions and Matriculation Board conducts"
    body_text_2 = "entrance examinations for tertiary institutions in Nigeria."
    body_text_3 = "To view your official examination result online,"
    
    ax.text(bx + 0.5, content_top - 1.45, body_text_1, fontsize=14, color=INK)
    ax.text(bx + 0.5, content_top - 1.75, body_text_2, fontsize=14, color=INK)
    ax.text(bx + 0.5, content_top - 2.05, body_text_3, fontsize=14, color=INK)

    # Blue underlined hyperlink
    link_x = bx + 0.5
    link_y = content_top - 2.45
    link_str = "click here to check Result."
    link_text = ax.text(link_x, link_y, link_str, fontsize=14, color=DEEP["blue"], weight="bold")
    # Draw underline
    ax.plot([link_x, link_x + 2.65], [link_y - 0.04, link_y - 0.04], color=DEEP["blue"], linewidth=1.6)

    # Mouse Pointer (Arrow) hovering over hyperlink
    ptr_x, ptr_y = link_x + 1.3, link_y - 0.05
    pointer_pts = np.array([
        [0.0, 0.0],
        [0.0, -0.38],
        [0.1, -0.28],
        [0.24, -0.45],
        [0.32, -0.41],
        [0.18, -0.24],
        [0.32, -0.24]
    ])
    mouse_poly = patches.Polygon(pointer_pts + [ptr_x, ptr_y], closed=True,
                                 facecolor="white", edgecolor=INK, linewidth=1.8, zorder=5)
    ax.add_patch(mouse_poly)

    # Additional text content below link
    ax.text(bx + 0.5, content_top - 3.1, "Ensure your registration slip is ready before logging in.",
            fontsize=14, color=GREY, style="italic")

    # LABELS and ANNOTATION ARROWS pointing to parts
    # 1. Address bar / URL
    ax.annotate("Address bar / URL",
                xy=(addr_x + addr_w * 0.65, addr_y + addr_h / 2),
                xytext=(8.0, 5.7),
                fontsize=15, color=INK, weight="bold",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # 2. Browser window
    ax.annotate("Browser window",
                xy=(bx + bw, by + bh * 0.75),
                xytext=(7.8, 4.4),
                fontsize=15, color=INK, weight="bold",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # 3. Homepage content
    ax.annotate("Homepage content",
                xy=(bx + 4.2, content_top - 1.2),
                xytext=(7.5, 3.1),
                fontsize=15, color=INK, weight="bold",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # 4. Hyperlink
    ax.annotate("Hyperlink",
                xy=(link_x + 1.8, link_y - 0.02),
                xytext=(7.6, 1.8),
                fontsize=15, color=INK, weight="bold",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    save(fig, out)
