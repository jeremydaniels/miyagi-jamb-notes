from style import *
import matplotlib.patches as patches

def draw(out):
    # Canvas size: roughly landscape
    fig = canvas(12, 8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Window bounds
    wx, wy, ww, wh = 0.5, 0.5, 8.5, 7.0

    # Main browser window background & outer border
    win_rect = patches.FancyBboxPatch((wx, wy), ww, wh, boxstyle="round,pad=0.0,rounding_size=0.15",
                                      edgecolor=INK, facecolor='white', lw=2)
    ax.add_patch(win_rect)

    # 1. Title Bar
    tb_h = 0.65
    tb_y = wy + wh - tb_h
    tbar = patches.Rectangle((wx, tb_y), ww, tb_h, edgecolor=INK, facecolor=BLUE, lw=1.5)
    ax.add_patch(tbar)
    ax.text(wx + 0.35, tb_y + tb_h / 2, "Example Web Page - Classic Browser", va='center', ha='left',
            fontsize=15, fontweight='bold', color=INK)

    # Window control buttons (min, max, close)
    for i, col in enumerate([GREEN, ORANGE, PINK]):
        circ = patches.Circle((wx + ww - 1.1 + i * 0.35, tb_y + tb_h / 2), 0.12,
                              facecolor=col, edgecolor=INK, lw=1.2)
        ax.add_patch(circ)

    # 2. Menu Bar
    mb_h = 0.55
    mb_y = tb_y - mb_h
    mbar = patches.Rectangle((wx, mb_y), ww, mb_h, edgecolor=INK, facecolor=CREAM, lw=1.5)
    ax.add_patch(mbar)
    menus = ["File", "Edit", "View", "History", "Bookmarks", "Tools", "Help"]
    cur_x = wx + 0.4
    for m in menus:
        ax.text(cur_x, mb_y + mb_h / 2, m, va='center', ha='left', fontsize=14, color=INK)
        cur_x += 1.15

    # 3. Tool Bar
    tb2_h = 0.8
    tb2_y = mb_y - tb2_h
    toolbar = patches.Rectangle((wx, tb2_y), ww, tb2_h, edgecolor=INK, facecolor=GREY, lw=1.5)
    ax.add_patch(toolbar)

    # Tool buttons: Back, Forward, Refresh, Home
    tool_btns = [
        ("◀", "Back"),
        ("▶", "Forward"),
        ("⟳", "Refresh"),
        ("⌂", "Home")
    ]
    bx = wx + 0.35
    for icon, lbl in tool_btns:
        btn_box = patches.FancyBboxPatch((bx, tb2_y + 0.1), 1.25, 0.6,
                                         boxstyle="round,pad=0.03,rounding_size=0.08",
                                         facecolor='white', edgecolor=INK, lw=1.3)
        ax.add_patch(btn_box)
        ax.text(bx + 0.28, tb2_y + 0.4, icon, va='center', ha='center', fontsize=15, color=INK)
        ax.text(bx + 0.72, tb2_y + 0.4, lbl, va='center', ha='center', fontsize=14, color=INK)
        bx += 1.45

    # 4. Address Bar & Search Bar Row
    addr_h = 0.75
    addr_y = tb2_y - addr_h
    addr_row = patches.Rectangle((wx, addr_y), ww, addr_h, edgecolor=INK, facecolor=CREAM, lw=1.5)
    ax.add_patch(addr_row)

    # Address Bar
    ab_x, ab_w = wx + 0.35, 4.8
    addr_box = patches.FancyBboxPatch((ab_x, addr_y + 0.12), ab_w, 0.5,
                                      boxstyle="round,pad=0.02,rounding_size=0.06",
                                      facecolor='white', edgecolor=INK, lw=1.3)
    ax.add_patch(addr_box)
    ax.text(ab_x + 0.2, addr_y + 0.37, "http://www.example.com", va='center', ha='left',
            fontsize=14, color=INK, family='monospace')

    # Search Bar
    sb_x, sb_w = ab_x + ab_w + 0.3, 2.3
    srch_box = patches.FancyBboxPatch((sb_x, addr_y + 0.12), sb_w, 0.5,
                                      boxstyle="round,pad=0.02,rounding_size=0.06",
                                      facecolor='white', edgecolor=INK, lw=1.3)
    ax.add_patch(srch_box)
    ax.text(sb_x + 0.2, addr_y + 0.37, "🔍 Search...", va='center', ha='left',
            fontsize=14, color=DEEP['orange'])

    # 5. Webpage Area
    web_y = wy
    web_h = addr_y - wy
    web_area = patches.Rectangle((wx, web_y), ww, web_h, edgecolor=INK, facecolor='white', lw=1.5)
    ax.add_patch(web_area)

    # Webpage content
    ax.text(wx + 0.6, web_y + web_h - 0.7, "Welcome to Example Domain",
            fontsize=17, fontweight='bold', color=INK)
    ax.text(wx + 0.6, web_y + web_h - 1.4,
            "This domain is established to be used for illustrative examples in documents.\n"
            "You may use this domain in literature without prior coordination.",
            fontsize=14, color=INK, linespacing=1.6)

    # Hyperlink inside webpage
    hl_text = "More information..."
    hl_x = wx + 0.6
    hl_y = web_y + web_h - 2.5
    ax.text(hl_x, hl_y, hl_text, fontsize=15, color=DEEP['blue'])
    ax.plot([hl_x, hl_x + 2.5], [hl_y - 0.08, hl_y - 0.08], color=DEEP['blue'], lw=2.0)

    # Labels and pointers arranged clearly on the right without overlapping
    callouts = [
        ("Title Bar",    (wx + ww, tb_y + tb_h / 2),       (9.5, tb_y + tb_h / 2)),
        ("Menu Bar",     (wx + ww, mb_y + mb_h / 2),       (9.5, mb_y + mb_h / 2)),
        ("Tool Bar",     (wx + ww, tb2_y + tb2_h / 2),     (9.5, tb2_y + tb2_h / 2)),
        ("Address Bar",  (wx + ww, addr_y + addr_h / 2),   (9.5, addr_y + addr_h / 2 + 0.2)),
        ("Search Bar",   (sb_x + sb_w / 2, addr_y),        (9.5, addr_y - 0.6)),
        ("Hyperlink",    (hl_x + 2.5, hl_y - 0.05),        (9.5, hl_y - 0.05))
    ]

    for text, pt_from, pt_to in callouts:
        ax.annotate(text, xy=pt_from, xytext=pt_to,
                    fontsize=15, fontweight='bold', color=INK,
                    va='center', ha='left',
                    bbox=dict(boxstyle="round,pad=0.3", fc=CREAM, ec=INK, lw=1.3),
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.6))

    save(fig, out)
