from style import *
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 10)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.0, 9.5, "Three-Sector Circular Flow", ha='center', va='center',
            fontsize=18, fontweight='bold', color=INK)

    # Box coordinates and dimensions
    # Households (Left), Firms (Right), Government (Center), Financial Sector (Bottom)
    hh_box = patches.FancyBboxPatch((0.8, 4.6), 2.4, 1.4, boxstyle="round,pad=0.1,rounding_size=0.15",
                                    fc=BLUE, ec=DEEP["blue"], lw=2, zorder=3)
    firm_box = patches.FancyBboxPatch((8.8, 4.6), 2.4, 1.4, boxstyle="round,pad=0.1,rounding_size=0.15",
                                      fc=GREEN, ec=DEEP["green"], lw=2, zorder=3)
    gov_box = patches.FancyBboxPatch((4.7, 4.6), 2.6, 1.4, boxstyle="round,pad=0.1,rounding_size=0.15",
                                     fc=ORANGE, ec=DEEP["orange"], lw=2, zorder=3)
    fin_box = patches.FancyBboxPatch((4.2, 0.8), 3.6, 1.3, boxstyle="round,pad=0.1,rounding_size=0.15",
                                     fc=LAV, ec=DEEP["lav"], lw=2, zorder=3)

    ax.add_patch(hh_box)
    ax.add_patch(firm_box)
    ax.add_patch(gov_box)
    ax.add_patch(fin_box)

    # Text inside boxes
    ax.text(2.0, 5.3, "Households", ha='center', va='center', fontsize=16, fontweight='bold', color=INK, zorder=4)
    ax.text(10.0, 5.3, "Firms", ha='center', va='center', fontsize=16, fontweight='bold', color=INK, zorder=4)
    ax.text(6.0, 5.3, "Government", ha='center', va='center', fontsize=16, fontweight='bold', color=INK, zorder=4)
    ax.text(6.0, 1.45, "Financial Sector\n(Banks)", ha='center', va='center', fontsize=15, fontweight='bold', color=INK, zorder=4)

    # Helper function for drawing labeled curved/straight arrows
    def draw_arrow(start, end, rad, label, label_pos, text_color=INK, arrow_color=INK):
        arrow = patches.FancyArrowPatch(
            start, end,
            connectionstyle=f"arc3,rad={rad}",
            arrowstyle="-|>,head_length=8,head_width=5",
            lw=2, color=arrow_color, zorder=1
        )
        ax.add_patch(arrow)
        if label:
            ax.text(label_pos[0], label_pos[1], label, ha='center', va='center',
                    fontsize=14, color=text_color, zorder=10,
                    bbox=dict(fc='white', ec='none', pad=3.0))

    # 1. Outer Loop: Basic loop between Households and Firms
    # Top arc: Consumer Expenditure / Goods & Services (Households -> Firms)
    draw_arrow((2.0, 6.1), (10.0, 6.1), -0.4, "Consumer Spending / Goods & Services", (6.0, 8.65),
               text_color=DEEP["blue"], arrow_color=DEEP["blue"])
    # Bottom outer arc: Factor Payments / Wages, Rent, Profit (Firms -> Households)
    draw_arrow((10.0, 4.5), (2.0, 4.5), -0.52, "Factor Payments (Wages, Rent, Profit)", (6.0, 2.7),
               text_color=DEEP["green"], arrow_color=DEEP["green"])

    # 2. Government interactions
    # Taxes (T): Households -> Government
    draw_arrow((3.3, 5.6), (4.6, 5.6), -0.15, "Taxes (T)", (3.95, 6.05),
               text_color=INK, arrow_color=INK)
    # Government Spending (G): Government -> Households
    draw_arrow((4.6, 5.0), (3.3, 5.0), -0.15, "Government Spending (G)", (3.95, 4.5),
               text_color=INK, arrow_color=INK)

    # Taxes (T): Firms -> Government
    draw_arrow((8.7, 5.6), (7.4, 5.6), 0.15, "Taxes (T)", (8.05, 6.05),
               text_color=INK, arrow_color=INK)
    # Government Spending (G): Government -> Firms
    draw_arrow((7.4, 5.0), (8.7, 5.0), 0.15, "Government Spending (G)", (8.05, 4.5),
               text_color=INK, arrow_color=INK)

    # 3. Financial Sector interactions
    # Savings (S): Households -> Financial Sector
    draw_arrow((1.6, 4.5), (4.1, 1.45), 0.2, "Savings (S)", (2.2, 2.3),
               text_color=DEEP["lav"], arrow_color=DEEP["lav"])
    # Investment (I): Financial Sector -> Firms
    draw_arrow((7.9, 1.45), (10.4, 4.5), 0.2, "Investment (I)", (9.8, 2.3),
               text_color=DEEP["lav"], arrow_color=DEEP["lav"])

    save(fig, out)
