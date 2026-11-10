from style import *
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 6.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.5)

    # Title / Context
    ax.text(5.0, 5.9, "Microsoft Access: Datasheet View", ha='center', va='center', 
            fontsize=18, weight='bold', color=INK)

    # Table layout parameters
    # Left edge, top edge
    x0, y0 = 1.0, 4.8
    row_h = 0.55
    col_w = [1.2, 2.4, 2.2]  # ID, First Name, Date of Birth
    total_w = sum(col_w)     # 5.8
    num_rows = 5             # Header + 4 data rows

    headers = ["ID", "First Name", "Date of Birth"]
    data = [
        ["1", "Alice", "12/04/2005"],
        ["2", "Benjamin", "03/11/2004"],
        ["3", "Chloe", "28/08/2005"],
        ["4", "Daniel", "15/01/2005"],
    ]

    # Draw table container / base
    table_rect = patches.Rectangle((x0, y0 - num_rows * row_h), total_w, num_rows * row_h,
                                   facecolor="white", edgecolor=GREY, linewidth=1.5)
    ax.add_patch(table_rect)

    # Highlight: Record (Row 2 data -> index 1, i.e., Benjamin)
    highlight_row_idx = 2  # 0 is header, 1 is Alice, 2 is Benjamin
    rec_y = y0 - (highlight_row_idx + 1) * row_h
    rec_rect = patches.Rectangle((x0, rec_y), total_w, row_h,
                                 facecolor=LAV, edgecolor=DEEP['lav'], linewidth=2.0, zorder=2)
    ax.add_patch(rec_rect)

    # Highlight: Field (Column 1 -> First Name)
    field_col_idx = 1
    col_x = x0 + sum(col_w[:field_col_idx])
    field_rect = patches.Rectangle((col_x, y0 - num_rows * row_h), col_w[field_col_idx], num_rows * row_h,
                                   facecolor='none', edgecolor=DEEP['blue'], linewidth=2.5, linestyle='--', zorder=3)
    ax.add_patch(field_rect)

    # Draw Header background (except over highlights if needed, but header is distinct)
    header_rect = patches.Rectangle((x0, y0 - row_h), total_w, row_h,
                                    facecolor=CREAM, edgecolor=GREY, linewidth=1.5, zorder=1)
    ax.add_patch(header_rect)

    # Grid lines - Horizontal
    for i in range(num_rows + 1):
        y = y0 - i * row_h
        ax.plot([x0, x0 + total_w], [y, y], color=GREY, lw=1.2, zorder=4)

    # Grid lines - Vertical
    curr_x = x0
    for w in col_w:
        ax.plot([curr_x, curr_x], [y0, y0 - num_rows * row_h], color=GREY, lw=1.2, zorder=4)
        curr_x += w
    ax.plot([curr_x, curr_x], [y0, y0 - num_rows * row_h], color=GREY, lw=1.2, zorder=4)

    # Render Header Text
    curr_x = x0
    for col_idx, h_text in enumerate(headers):
        w = col_w[col_idx]
        ax.text(curr_x + w / 2, y0 - row_h / 2, h_text,
                ha='center', va='center', fontsize=14, weight='bold', color=INK, zorder=5)
        curr_x += w

    # Render Data Text
    for r_idx, row_values in enumerate(data):
        curr_x = x0
        y_text = y0 - (r_idx + 1.5) * row_h
        for c_idx, val in enumerate(row_values):
            w = col_w[c_idx]
            # Center ID, left-align names and dates with slight padding
            if c_idx == 0:
                ax.text(curr_x + w / 2, y_text, val, ha='center', va='center', fontsize=14, color=INK, zorder=5)
            else:
                ax.text(curr_x + 0.25, y_text, val, ha='left', va='center', fontsize=14, color=INK, zorder=5)
            curr_x += w

    # Annotations & Arrows
    # 1. Field (Column) annotation pointing to top/center of "First Name" column
    arrow_field = dict(arrowstyle="->", lw=2.2, color=DEEP['blue'])
    target_field = (col_x + col_w[field_col_idx] / 2, y0)
    ax.annotate("Field (Column)",
                xy=target_field,
                xytext=(col_x + col_w[field_col_idx] / 2, y0 + 0.7),
                ha='center', va='bottom',
                fontsize=15, weight='bold', color=DEEP['blue'],
                arrowprops=arrow_field,
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP['blue'], lw=1.5))

    # 2. Record (Row) annotation pointing to right edge of highlighted row
    arrow_record = dict(arrowstyle="->", lw=2.2, color=DEEP['lav'])
    target_record = (x0 + total_w, rec_y + row_h / 2)
    ax.annotate("Record (Row)",
                xy=target_record,
                xytext=(x0 + total_w + 1.3, rec_y + row_h / 2),
                ha='left', va='center',
                fontsize=15, weight='bold', color=DEEP['lav'],
                arrowprops=arrow_record,
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP['lav'], lw=1.5))

    # Optional descriptive caption at bottom
    ax.text(5.0, 1.2, "A database table stores data in fields (vertical columns) and records (horizontal rows).",
            ha='center', va='center', fontsize=14, color=INK)

    save(fig, out)
