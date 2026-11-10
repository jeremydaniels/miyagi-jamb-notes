from style import *
import matplotlib.patches as patches

def draw(out):
    # Balanced 10x8 landscape canvas
    fig = canvas(10, 8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Main application window: left-aligned with space on the right for annotations
    # Coordinates: x in [0.5, 7.3], y in [0.6, 7.4]
    wx0, wy0, ww, wh = 0.5, 0.6, 6.8, 6.8

    # Outer window frame
    window = patches.FancyBboxPatch((wx0, wy0), ww, wh,
                                    boxstyle="round,pad=0,rounding_size=0.15",
                                    fc="#F3F5F8", ec=INK, lw=1.8)
    ax.add_patch(window)

    # 1. Title Bar (top: y in [6.85, 7.4])
    title_bar = patches.Rectangle((wx0, 6.85), ww, 0.55, fc="#2B579A", ec=INK, lw=1.5)
    ax.add_patch(title_bar)
    ax.text(wx0 + ww / 2 - 0.3, 7.12, "Document1 - Microsoft Word", ha="center", va="center",
            color="white", fontsize=14, weight="bold")
    ax.text(wx0 + ww - 0.45, 7.12, "—  □  ✕", ha="center", va="center", color="white", fontsize=11)

    # 2. Ribbon Tabs (y in [6.3, 6.85])
    tabs_bg = patches.Rectangle((wx0, 6.3), ww, 0.55, fc="#E8EDF4", ec=GREY, lw=1)
    ax.add_patch(tabs_bg)

    # Active "Home" tab highlighted
    active_tab = patches.Rectangle((1.55, 6.3), 0.95, 0.55, fc="white", ec="none")
    ax.add_patch(active_tab)
    ax.plot([1.55, 1.55], [6.3, 6.85], color=GREY, lw=1)
    ax.plot([2.5, 2.5], [6.3, 6.85], color=GREY, lw=1)

    ax.text(1.0, 6.57, "File", ha="center", va="center", color=INK, fontsize=14)
    ax.text(2.02, 6.57, "Home", ha="center", va="center", color=DEEP["blue"], fontsize=14, weight="bold")
    ax.text(3.05, 6.57, "Insert", ha="center", va="center", color=INK, fontsize=14)
    ax.text(4.25, 6.57, "Page Layout", ha="center", va="center", color="#666666", fontsize=14)

    # 3. Ribbon Groups (y in [5.1, 6.3])
    ribbon_body = patches.Rectangle((wx0, 5.1), ww, 1.2, fc="white", ec=GREY, lw=1)
    ax.add_patch(ribbon_body)

    # Font Group
    font_group = patches.Rectangle((0.65, 5.18), 2.9, 1.04, fc="#FAFBFC", ec="#CCD3DC", lw=1, ls="--")
    ax.add_patch(font_group)
    ax.text(2.1, 5.33, "Font", ha="center", va="center", color=INK, fontsize=14, weight="bold")

    # Font tools
    ax.add_patch(patches.Rectangle((0.8, 5.82), 1.5, 0.3, fc="white", ec=GREY, lw=0.8))
    ax.text(0.9, 5.97, "Calibri", ha="left", va="center", fontsize=14, color=INK)
    ax.add_patch(patches.Rectangle((2.4, 5.82), 0.6, 0.3, fc="white", ec=GREY, lw=0.8))
    ax.text(2.55, 5.97, "11", ha="left", va="center", fontsize=14, color=INK)

    for i, b_txt in enumerate(["B", "I", "U"]):
        bx = 0.85 + i * 0.55
        ax.add_patch(patches.Rectangle((bx, 5.5), 0.42, 0.26, fc="#EDF1F5", ec=GREY, lw=0.8))
        ax.text(bx + 0.21, 5.63, b_txt, ha="center", va="center", fontsize=14, weight="bold", color=INK)

    # Paragraph Group
    para_group = patches.Rectangle((3.75, 5.18), 3.3, 1.04, fc="#FAFBFC", ec="#CCD3DC", lw=1, ls="--")
    ax.add_patch(para_group)
    ax.text(5.4, 5.33, "Paragraph", ha="center", va="center", color=INK, fontsize=14, weight="bold")

    # Paragraph tools (alignment icons)
    for i in range(4):
        px = 4.0 + i * 0.72
        ax.add_patch(patches.Rectangle((px, 5.72), 0.55, 0.4, fc="#EDF1F5", ec=GREY, lw=0.8))
        for line_idx, line_y in enumerate([6.02, 5.92, 5.82]):
            w_line = 0.38 if (i != 1 or line_idx != 1) else 0.24
            offset = 0.08 + (0.07 if i == 1 and line_idx == 1 else 0)
            ax.plot([px + offset, px + offset + w_line], [line_y, line_y], color=INK, lw=1.5)

    # 4. Workspace (Document Area, y in [1.15, 5.1])
    workspace_bg = patches.Rectangle((wx0, 1.15), ww, 3.95, fc="#E8EBEF", ec=GREY, lw=1)
    ax.add_patch(workspace_bg)

    # White page in center of workspace
    page_x, page_y, page_w, page_h = 1.3, 1.35, 5.2, 3.55
    page = patches.Rectangle((page_x, page_y), page_w, page_h, fc="white", ec="#BCC3CD", lw=1.5)
    ax.add_patch(page)

    # Document text inside workspace (kept short so arrow lines do not cross it)
    ax.text(1.6, 4.4, "Welcome to Microsoft Word.", fontsize=14, color="#444444")
    ax.text(1.6, 4.0, "Create and edit documents.", fontsize=14, color="#444444")
    ax.text(1.6, 3.6, "Format text with styles.", fontsize=14, color="#444444")

    # Blinking vertical cursor placed immediately after the short text
    cursor_x, cursor_y = 3.85, 3.6
    ax.plot([cursor_x, cursor_x], [cursor_y - 0.15, cursor_y + 0.18], color="black", lw=3.0)

    # 5. Status Bar (bottom: y in [0.6, 1.15])
    status_bar = patches.Rectangle((wx0, 0.6), ww, 0.55, fc="#2B579A", ec=INK, lw=1.5)
    ax.add_patch(status_bar)

    ax.text(0.8, 0.88, "Page 1 of 1", ha="left", va="center", color="white", fontsize=14, weight="bold")
    ax.text(2.2, 0.88, "12 words", ha="left", va="center", color="#D0DDEF", fontsize=14)

    # Zoom slider
    ax.text(4.9, 0.88, "−", ha="center", va="center", color="white", fontsize=16, weight="bold")
    ax.plot([5.1, 6.3], [0.88, 0.88], color="white", lw=2.2)
    # Slider thumb
    ax.plot([5.7, 5.7], [0.75, 1.01], color="white", lw=3.8)
    ax.text(6.5, 0.88, "+", ha="center", va="center", color="white", fontsize=15, weight="bold")
    ax.text(7.05, 0.88, "100%", ha="center", va="center", color="white", fontsize=14)

    # ------------------ LABELS & ANNOTATIONS (COMPACT, CLOSE TO TARGETS) ------------------
    # Label: Title Bar
    ax.annotate("Title Bar",
                xy=(wx0 + ww, 7.12), xytext=(7.8, 7.12),
                fontsize=14, weight="bold", color=INK, va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.6),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Label: Ribbon Tabs
    ax.annotate("Tabs\n(File, Home, Insert)",
                xy=(wx0 + ww, 6.57), xytext=(7.8, 6.45),
                fontsize=14, weight="bold", color=INK, va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.6),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Label: Ribbon Groups
    ax.annotate("Groups\n(Font, Paragraph)",
                xy=(wx0 + ww, 5.65), xytext=(7.8, 5.45),
                fontsize=14, weight="bold", color=INK, va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.6),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Label: Workspace
    ax.annotate("Workspace\n(Document area)",
                xy=(page_x + page_w, 2.7), xytext=(7.8, 2.7),
                fontsize=14, weight="bold", color=INK, va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.6),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Label: Cursor (arrow line completely misses the shortened document text)
    ax.annotate("Blinking Cursor",
                xy=(cursor_x + 0.05, cursor_y), xytext=(7.8, 3.6),
                fontsize=14, weight="bold", color=INK, va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.6),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Label: Status Bar
    ax.annotate("Status Bar\n(Page 1 of 1, Zoom slider)",
                xy=(wx0 + ww, 0.88), xytext=(7.8, 1.1),
                fontsize=14, weight="bold", color=INK, va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.6),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    save(fig, out)
