from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(13, 7.2)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7.2)
    ax.axis('off')

    # Overall title
    ax.text(6.5, 6.75, "User Interfaces: CLI vs GUI", fontsize=18, fontweight='bold', ha='center', va='center', color=INK)

    # Subtitles
    ax.text(3.3, 6.2, "Command Line Interface (CLI)", fontsize=16, fontweight='bold', ha='center', va='center', color=INK)
    ax.text(9.7, 6.2, "Graphical User Interface (GUI)", fontsize=16, fontweight='bold', ha='center', va='center', color=INK)

    # Dividing line in center
    ax.plot([6.5, 6.5], [0.9, 6.3], color=GREY, linestyle="--", linewidth=1.5)

    # --- LEFT SIDE: CLI ---
    # Width 5.4, placed from x=0.6 to 6.0
    cli_x, cli_y, cli_w, cli_h = 0.6, 1.3, 5.4, 4.5
    screen_left = patches.FancyBboxPatch((cli_x, cli_y), cli_w, cli_h,
                                         boxstyle="round,pad=0.05,rounding_size=0.15",
                                         linewidth=2.5, edgecolor=INK, facecolor="#181818")
    ax.add_patch(screen_left)

    # CLI Title bar
    cli_tb_h = 0.4
    cli_title_bar = patches.Rectangle((cli_x, cli_y + cli_h - cli_tb_h), cli_w, cli_tb_h,
                                      facecolor="#2e2e2e", edgecolor=INK, linewidth=1.5)
    ax.add_patch(cli_title_bar)
    ax.text(cli_x + 0.2, cli_y + cli_h - cli_tb_h / 2, "Command Prompt",
            fontsize=14, color="white", va='center', fontfamily='monospace', fontweight='bold')

    # Window controls (min/max/close dots)
    ctrl_y = cli_y + cli_h - cli_tb_h / 2
    ax.plot([cli_x + cli_w - 0.7], [ctrl_y], marker='_', markersize=6, color="#cccccc", mew=1.5)
    ax.plot([cli_x + cli_w - 0.45], [ctrl_y], marker='s', fillstyle='none', markersize=6, color="#cccccc", mew=1.5)
    ax.plot([cli_x + cli_w - 0.2], [ctrl_y], marker='x', markersize=6, color="#ff6b6b", mew=1.5)

    # Terminal text (short concise lines that easily fit within cli_w = 5.4 without overflowing)
    cli_lines = [
        (r"C:\> dir", "#ffffff"),
        (r" Directory of C:\ ", "#aaaaaa"),
        (r" <DIR>    Documents", "#cccccc"),
        (r" <DIR>    Pictures", "#cccccc"),
        (r" 14,208   report.txt", "#cccccc"),
        (r"C:\> run_calc.exe", "#ffffff"),
        (r"Starting application...", "#88ff88"),
        (r"C:\> _", "#ffffff")
    ]

    y_pos = 5.0
    for line, col in cli_lines:
        ax.text(cli_x + 0.25, y_pos, line, fontsize=14, color=col, va='center', fontfamily='monospace')
        y_pos -= 0.45

    # CLI Caption
    ax.text(3.3, 0.7, "Text-based input: commands typed via keyboard", fontsize=14, ha='center', va='center', color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc=CREAM, ec=GREY))

    # --- RIGHT SIDE: GUI ---
    gui_x, gui_y, gui_w, gui_h = 7.0, 1.3, 5.4, 4.5
    screen_right = patches.FancyBboxPatch((gui_x, gui_y), gui_w, gui_h,
                                          boxstyle="round,pad=0.05,rounding_size=0.15",
                                          linewidth=2.5, edgecolor=INK, facecolor=BLUE)
    ax.add_patch(screen_right)

    # Folder Icons on Desktop (left part of desktop screen)
    def draw_folder(x, y, label):
        tab = patches.Rectangle((x, y + 0.35), 0.25, 0.12, facecolor=ORANGE, edgecolor=INK, linewidth=1.2)
        body = patches.Rectangle((x, y), 0.65, 0.4, facecolor=ORANGE, edgecolor=INK, linewidth=1.2)
        ax.add_patch(tab)
        ax.add_patch(body)
        ax.text(x + 0.32, y - 0.22, label, fontsize=14, ha='center', va='center', color=INK,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85))

    draw_folder(7.3, 4.65, "Documents")
    draw_folder(7.3, 3.25, "Pictures")

    # Application Window on Desktop (placed on right side of desktop screen)
    win_x, win_y, win_w, win_h = 8.5, 2.3, 3.6, 2.9
    win = patches.FancyBboxPatch((win_x, win_y), win_w, win_h, boxstyle="square,pad=0.0",
                                linewidth=1.5, edgecolor=INK, facecolor="white")
    ax.add_patch(win)

    # Window Header
    win_hdr_h = 0.4
    win_header = patches.Rectangle((win_x, win_y + win_h - win_hdr_h), win_w, win_hdr_h,
                                   facecolor=LAV, edgecolor=INK, linewidth=1.2)
    ax.add_patch(win_header)
    ax.text(win_x + 0.2, win_y + win_h - win_hdr_h / 2, "File Explorer",
            fontsize=14, fontweight='bold', color=INK, va='center')
    ax.text(win_x + win_w - 0.3, win_y + win_h - win_hdr_h / 2, "✕",
            fontsize=14, color=DEEP["pink"], va='center', fontweight='bold')

    # Inside Window: Files / Content
    # Document icon + text
    doc_icon = patches.Rectangle((win_x + 0.3, win_y + 1.6), 0.45, 0.55, facecolor=CREAM, edgecolor=INK, linewidth=1.2)
    ax.add_patch(doc_icon)
    # fold corner line on doc icon
    ax.plot([win_x + 0.55, win_x + 0.75], [win_y + 1.95, win_y + 1.95], color=INK, lw=1)
    ax.plot([win_x + 0.4, win_x + 0.65], [win_y + 1.8, win_y + 1.8], color=INK, lw=1)
    ax.plot([win_x + 0.4, win_x + 0.65], [win_y + 1.7, win_y + 1.7], color=INK, lw=1)
    ax.text(win_x + 0.95, win_y + 1.88, "Report.txt", fontsize=14, color=INK, va='center')

    # App icon + text
    calc_icon = patches.Rectangle((win_x + 0.3, win_y + 0.55), 0.45, 0.55, facecolor=PINK, edgecolor=INK, linewidth=1.2)
    ax.add_patch(calc_icon)
    ax.text(win_x + 0.52, win_y + 0.82, "±", fontsize=14, color=INK, ha='center', va='center', fontweight='bold')
    ax.text(win_x + 0.95, win_y + 0.82, "Calculator", fontsize=14, color=INK, va='center')

    # Taskbar at bottom of GUI
    tb_h = 0.5
    taskbar = patches.Rectangle((gui_x, gui_y), gui_w, tb_h, facecolor="#e2e8f0", edgecolor=INK, linewidth=1.5)
    ax.add_patch(taskbar)

    # Start button
    start_btn = patches.FancyBboxPatch((gui_x + 0.15, gui_y + 0.08), 1.1, tb_h - 0.16,
                                       boxstyle="round,pad=0.02,rounding_size=0.06",
                                       facecolor=DEEP["blue"], edgecolor=INK, linewidth=1)
    ax.add_patch(start_btn)
    ax.text(gui_x + 0.7, gui_y + tb_h / 2, "Start", fontsize=14, fontweight='bold', color="white", ha='center', va='center')

    # Taskbar clock
    ax.text(gui_x + gui_w - 0.5, gui_y + tb_h / 2, "10:30", fontsize=14, color=INK, ha='center', va='center')

    # Mouse pointer / cursor on GUI (placed in clear open area, pointing towards Report.txt without overlapping)
    pointer_x, pointer_y = 11.2, 3.4
    cursor_poly = np.array([
        [pointer_x, pointer_y],
        [pointer_x, pointer_y - 0.45],
        [pointer_x + 0.13, pointer_y - 0.32],
        [pointer_x + 0.27, pointer_y - 0.52],
        [pointer_x + 0.36, pointer_y - 0.47],
        [pointer_x + 0.22, pointer_y - 0.27],
        [pointer_x + 0.36, pointer_y - 0.27],
    ])
    cursor = patches.Polygon(cursor_poly, closed=True, facecolor="white", edgecolor=INK, linewidth=1.8, zorder=10)
    ax.add_patch(cursor)

    # GUI Caption
    ax.text(9.7, 0.7, "Visual icons & menus: operated via mouse / touch", fontsize=14, ha='center', va='center', color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc=CREAM, ec=GREY))

    save(fig, out)
