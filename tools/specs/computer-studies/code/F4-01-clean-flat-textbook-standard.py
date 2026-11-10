from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Main window dimensions
    win_x, win_y, win_w, win_h = 0.8, 0.8, 8.4, 7.2
    
    # Window drop shadow
    shadow = patches.FancyBboxPatch((win_x + 0.08, win_y - 0.08), win_w, win_h,
                                    boxstyle="round,pad=0,rounding_size=0.15",
                                    fc='#E0E4E8', ec='none', zorder=1)
    ax.add_patch(shadow)

    # Window container
    window = patches.FancyBboxPatch((win_x, win_y), win_w, win_h,
                                   boxstyle="round,pad=0,rounding_size=0.15",
                                   fc='white', ec=GREY, lw=1.5, zorder=2)
    ax.add_patch(window)

    # Title bar
    title_h = 0.65
    title_bar = patches.FancyBboxPatch((win_x, win_y + win_h - title_h), win_w, title_h,
                                      boxstyle="round,pad=0,rounding_size=0.15",
                                      fc=CREAM, ec=GREY, lw=1.5, zorder=3)
    ax.add_patch(title_bar)
    # Square off the bottom of the title bar
    ax.fill_between([win_x, win_x + win_w], win_y + win_h - title_h, win_y + win_h - title_h + 0.15,
                    color=CREAM, zorder=3)
    ax.plot([win_x, win_x + win_w], [win_y + win_h - title_h, win_y + win_h - title_h],
            color=GREY, lw=1.5, zorder=4)

    # Window controls (three small dots)
    dot_y = win_y + win_h - title_h / 2
    for i, c in enumerate([DEEP['pink'], DEEP['orange'], DEEP['green']]):
        dot = patches.Circle((win_x + 0.4 + i * 0.3, dot_y), 0.09, fc=c, ec='none', zorder=5)
        ax.add_patch(dot)

    # Title text
    ax.text(win_x + win_w / 2, dot_y, "New Message", color=INK, fontsize=15,
            weight='bold', ha='center', va='center', zorder=5)

    # Header fields: To, Cc, Bcc, Subject
    fields = [
        ("To", "recipient@example.com"),
        ("Cc", "team@example.com"),
        ("Bcc", ""),
        ("Subject", "Project Update and Deliverables")
    ]
    
    header_start_y = win_y + win_h - title_h - 0.55
    row_h = 0.55
    left_x = win_x + 0.4
    line_right_x = win_x + win_w - 0.4

    for i, (label, val) in enumerate(fields):
        curr_y = header_start_y - i * row_h
        ax.text(left_x, curr_y, f"{label}:", color=INK, fontsize=15,
                weight='bold', va='center', zorder=5)
        if val:
            ax.text(left_x + 1.4, curr_y, val, color=INK, fontsize=14,
                    va='center', zorder=5)
        # Separator line
        sep_y = curr_y - row_h / 2
        ax.plot([left_x, line_right_x], [sep_y, sep_y], color=GREY, lw=1.0, zorder=4)

    # Large message body area
    body_text = (
        "Hi Team,\n\n"
        "Please find the latest project files attached for review.\n"
        "Let me know if you have any questions or feedback before\n"
        "tomorrow's meeting.\n\n"
        "Best regards,\n"
        "Alex"
    )
    body_y = header_start_y - len(fields) * row_h - 0.1
    ax.text(left_x, body_y, body_text, color=INK, fontsize=14,
            va='top', ha='left', linespacing=1.6, zorder=5)

    # Bottom bar separator
    bottom_bar_y = win_y + 0.9
    ax.plot([left_x, line_right_x], [bottom_bar_y, bottom_bar_y], color=GREY, lw=1.0, zorder=4)

    # "Send" Button
    send_x = left_x
    send_y = win_y + 0.22
    send_w, send_h = 1.35, 0.48
    btn = patches.FancyBboxPatch((send_x, send_y), send_w, send_h,
                                boxstyle="round,pad=0,rounding_size=0.1",
                                fc=DEEP['blue'], ec='none', zorder=5)
    ax.add_patch(btn)
    ax.text(send_x + send_w / 2, send_y + send_h / 2, "Send",
            color='white', fontsize=15, weight='bold', ha='center', va='center', zorder=6)

    # Paperclip Icon
    clip_cx = send_x + send_w + 0.5
    clip_cy = send_y + send_h / 2
    
    # Parametric paperclip
    t1 = np.linspace(np.pi, 0, 30)
    t2 = np.linspace(0, np.pi, 30)
    t3 = np.linspace(np.pi, 0, 30)
    
    # Dimensions for clip
    w1, w2 = 0.08, 0.05
    clip_pts = []
    # Start inside inner curve
    clip_pts.extend(zip(clip_cx - w2 + w2 * np.cos(t3), clip_cy - 0.06 + 0.07 * np.sin(t3)))
    # Down inner leg
    clip_pts.extend([(clip_cx - w2, clip_cy - 0.15)])
    # Outer bottom turn
    clip_pts.extend(zip(clip_cx + 0.015 - (w2 + 0.015) * np.cos(t2), clip_cy - 0.15 - 0.08 * np.sin(t2)))
    # Up outer leg
    clip_pts.extend([(clip_cx + w1, clip_cy + 0.1)])
    # Outer top turn
    clip_pts.extend(zip(clip_cx + w1 * np.cos(t1), clip_cy + 0.1 + 0.1 * np.sin(t1)))
    # Down straight leg
    clip_pts.extend([(clip_cx - w1, clip_cy - 0.15)])

    # Simple clean standard paperclip polyline
    px = [
        clip_cx + 0.03, clip_cx + 0.03,
        clip_cx - 0.03, clip_cx - 0.03,
        clip_cx + 0.07, clip_cx + 0.07,
        clip_cx - 0.07, clip_cx - 0.07
    ]
    py = [
        clip_cy - 0.05, clip_cy + 0.08,
        clip_cy + 0.08, clip_cy - 0.12,
        clip_cy - 0.12, clip_cy + 0.15,
        clip_cy + 0.15, clip_cy - 0.18
    ]
    ax.plot(px, py, color=INK, lw=2.4, solid_capstyle='round', zorder=5)

    # Annotation arrow pointing to paperclip
    ax.annotate("Attachment icon",
                xy=(clip_cx + 0.08, clip_cy),
                xytext=(clip_cx + 1.8, clip_cy),
                fontsize=15, color=INK, weight='bold',
                va='center', ha='left',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8),
                bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3', lw=1.2),
                zorder=6)

    save(fig, out)
