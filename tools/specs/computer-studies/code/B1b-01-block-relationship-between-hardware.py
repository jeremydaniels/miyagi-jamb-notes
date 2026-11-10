from style import *
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Styles
    box_ec = INK
    box_lw = 2.0
    arrow_props = dict(arrowstyle="-|>", color=INK, lw=2.2, mutation_scale=20)
    bi_arrow_props = dict(arrowstyle="<|-|>", color=INK, lw=2.2, mutation_scale=20)

    # 1. Input Devices (Left)
    input_box = patches.FancyBboxPatch((0.6, 3.4), 2.2, 2.2,
                                       boxstyle="round,pad=0.1,rounding_size=0.15",
                                       fc=CREAM, ec=box_ec, lw=box_lw)
    ax.add_patch(input_box)
    ax.text(1.7, 4.5, "Input\nDevices", ha="center", va="center",
            fontsize=16, weight="bold", color=INK)

    # 2. Central Processing Unit (Center-Top)
    cpu_box = patches.FancyBboxPatch((3.8, 3.1), 4.4, 2.9,
                                     boxstyle="round,pad=0.1,rounding_size=0.2",
                                     fc=LAV, ec=box_ec, lw=box_lw)
    ax.add_patch(cpu_box)
    ax.text(6.0, 5.6, "Central Processing Unit", ha="center", va="center",
            fontsize=16, weight="bold", color=INK)

    # Inner boxes inside CPU: ALU and Control Unit
    alu_box = patches.FancyBboxPatch((4.1, 3.5), 1.8, 1.5,
                                     boxstyle="round,pad=0.08,rounding_size=0.1",
                                     fc=BLUE, ec=box_ec, lw=1.6)
    ax.add_patch(alu_box)
    ax.text(5.0, 4.25, "Arithmetic\n& Logic Unit\n(ALU)", ha="center", va="center",
            fontsize=14, color=INK)

    cu_box = patches.FancyBboxPatch((6.1, 3.5), 1.8, 1.5,
                                    boxstyle="round,pad=0.08,rounding_size=0.1",
                                    fc=PINK, ec=box_ec, lw=1.6)
    ax.add_patch(cu_box)
    ax.text(7.0, 4.25, "Control\nUnit\n(CU)", ha="center", va="center",
            fontsize=14, color=INK)

    # 3. Output Devices (Right)
    output_box = patches.FancyBboxPatch((9.2, 3.4), 2.2, 2.2,
                                        boxstyle="round,pad=0.1,rounding_size=0.15",
                                        fc=GREEN, ec=box_ec, lw=box_lw)
    ax.add_patch(output_box)
    ax.text(10.3, 4.5, "Output\nDevices", ha="center", va="center",
            fontsize=16, weight="bold", color=INK)

    # 4. Storage Media (Bottom)
    storage_box = patches.FancyBboxPatch((4.7, 0.6), 2.6, 1.4,
                                         boxstyle="round,pad=0.1,rounding_size=0.15",
                                         fc=ORANGE, ec=box_ec, lw=box_lw)
    ax.add_patch(storage_box)
    ax.text(6.0, 1.3, "Storage\nMedia", ha="center", va="center",
            fontsize=16, weight="bold", color=INK)

    # Connecting Arrows
    # Arrow: Input Devices -> CPU
    ax.annotate("", xy=(3.8, 4.5), xytext=(2.8, 4.5), arrowprops=arrow_props)

    # Arrow: CPU -> Output Devices
    ax.annotate("", xy=(9.2, 4.5), xytext=(8.2, 4.5), arrowprops=arrow_props)

    # Two-way Arrow: CPU <-> Storage Media
    ax.annotate("", xy=(6.0, 3.1), xytext=(6.0, 2.0), arrowprops=bi_arrow_props)

    # Diagram Title
    ax.text(6.0, 6.5, "Computer Hardware Architecture", ha="center", va="center",
            fontsize=18, weight="bold", color=INK)

    save(fig, out)
