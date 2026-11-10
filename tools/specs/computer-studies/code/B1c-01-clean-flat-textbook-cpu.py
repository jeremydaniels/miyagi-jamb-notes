import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style import *

def draw(out):
    # Canvas with plenty of width for CPU, wide Bus zone, and Memory
    fig = canvas(14, 8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')

    # CPU Outer Box (x: 0.6 to 5.6)
    cpu_rect = patches.FancyBboxPatch((0.6, 0.8), 5.0, 6.4, boxstyle="round,pad=0.1,rounding_size=0.2",
                                      facecolor="#F8FAFC", edgecolor=INK, linewidth=2.5)
    ax.add_patch(cpu_rect)
    ax.text(0.9, 6.8, "CPU (Central Processing Unit)", fontsize=16, fontweight='bold', color=INK)

    # Main Memory Outer Box (x: 11.2 to 13.4)
    mem_rect = patches.FancyBboxPatch((11.2, 0.8), 2.2, 6.4, boxstyle="round,pad=0.1,rounding_size=0.2",
                                      facecolor="#F0FDF4", edgecolor=DEEP['green'], linewidth=2.5)
    ax.add_patch(mem_rect)
    ax.text(12.3, 6.8, "Main Memory\n(RAM)", fontsize=16, fontweight='bold', color=INK, ha='center')

    # Memory contents illustration
    for i in range(5):
        y_pos = 1.4 + i * 0.95
        slot = patches.Rectangle((11.5, y_pos), 1.6, 0.65, facecolor="white", edgecolor=GREY, linewidth=1.5)
        ax.add_patch(slot)
        ax.text(12.3, y_pos + 0.32, f"0x{i*4:02X} : Data", fontsize=14, color=DEEP['blue'], ha='center', va='center')

    # ALU Block inside CPU (x: 0.9 to 3.0)
    alu_box = patches.FancyBboxPatch((0.9, 1.2), 2.1, 3.2, boxstyle="round,pad=0.08,rounding_size=0.15",
                                     facecolor=CREAM, edgecolor=DEEP['orange'], linewidth=2.0)
    ax.add_patch(alu_box)
    ax.text(1.95, 4.0, "ALU", fontsize=15, fontweight='bold', color=INK, ha='center')
    ax.text(1.95, 3.65, "(Arithmetic Logic Unit)", fontsize=14, color=DEEP['blue'], ha='center')

    # Accumulator (inside ALU)
    acc_box = patches.Rectangle((1.05, 1.5), 1.8, 1.6, facecolor="white", edgecolor=INK, linewidth=1.8)
    ax.add_patch(acc_box)
    ax.text(1.95, 2.5, "Accumulator", fontsize=14, fontweight='bold', color=INK, ha='center')
    ax.text(1.95, 1.9, "(ACC)", fontsize=14, color=DEEP['blue'], ha='center')

    # PC Box (x: 1.05 to 2.85)
    pc_box = patches.Rectangle((1.05, 4.9), 1.8, 1.4, facecolor="white", edgecolor=INK, linewidth=1.8)
    ax.add_patch(pc_box)
    ax.text(1.95, 5.8, "PC", fontsize=15, fontweight='bold', color=INK, ha='center')
    ax.text(1.95, 5.25, "Program Counter", fontsize=14, color=DEEP['blue'], ha='center')

    # MAR Box (x: 3.5 to 5.3)
    mar_box = patches.Rectangle((3.5, 4.9), 1.8, 1.4, facecolor="white", edgecolor=INK, linewidth=1.8)
    ax.add_patch(mar_box)
    ax.text(4.4, 5.8, "MAR", fontsize=15, fontweight='bold', color=INK, ha='center')
    ax.text(4.4, 5.25, "Mem. Addr. Reg.", fontsize=14, color=DEEP['blue'], ha='center')

    # MDR Box (x: 3.5 to 5.3)
    mdr_box = patches.Rectangle((3.5, 2.9), 1.8, 1.4, facecolor="white", edgecolor=INK, linewidth=1.8)
    ax.add_patch(mdr_box)
    ax.text(4.4, 3.8, "MDR", fontsize=15, fontweight='bold', color=INK, ha='center')
    ax.text(4.4, 3.25, "Mem. Data Reg.", fontsize=14, color=DEEP['blue'], ha='center')

    # CIR Box (x: 3.5 to 5.3)
    cir_box = patches.Rectangle((3.5, 1.2), 1.8, 1.3, facecolor="white", edgecolor=INK, linewidth=1.8)
    ax.add_patch(cir_box)
    ax.text(4.4, 2.05, "CIR", fontsize=15, fontweight='bold', color=INK, ha='center')
    ax.text(4.4, 1.5, "Current Instr. Reg.", fontsize=14, color=DEEP['blue'], ha='center')

    # Arrow from PC to MAR
    ax.annotate("", xy=(3.5, 5.6), xytext=(2.85, 5.6),
                arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.45", lw=2.2, color=INK))

    # Arrow from MDR to CIR
    ax.annotate("", xy=(4.4, 2.5), xytext=(4.4, 2.9),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.4", lw=2.0, color=INK))

    # System Bus Section (Between CPU right edge x=5.6 and Main Memory left edge x=11.2)
    # Center of bus section is x = 8.4
    bus_center_x = 8.4

    # System Bus Header
    ax.text(bus_center_x, 6.8, "System Bus", fontsize=16, fontweight='bold', color=INK, ha='center',
            bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.3"))

    # Address Bus: Unidirectional from MAR (x=5.3) through CPU boundary (x=5.6) to Main Memory (x=11.2)
    ax.annotate("", xy=(11.2, 5.6), xytext=(5.3, 5.6),
                arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.55", lw=3.0, color=DEEP['blue']))
    ax.text(bus_center_x, 5.9, "Address Bus", fontsize=15, fontweight='bold', color=DEEP['blue'], ha='center',
            bbox=dict(fc="white", ec="none", pad=2))
    ax.text(bus_center_x, 5.15, "Address Flow: MAR \u2192 Memory", fontsize=14, color=INK, ha='center',
            bbox=dict(fc="white", ec="none", pad=2))

    # Data Bus: Bidirectional between MDR (x=5.3) through CPU boundary (x=5.6) and Main Memory (x=11.2)
    ax.annotate("", xy=(11.2, 3.6), xytext=(5.3, 3.6),
                arrowprops=dict(arrowstyle="<->,head_width=0.45,head_length=0.55", lw=3.0, color=DEEP['pink']))
    ax.text(bus_center_x, 3.9, "Data Bus", fontsize=15, fontweight='bold', color=DEEP['pink'], ha='center',
            bbox=dict(fc="white", ec="none", pad=2))
    ax.text(bus_center_x, 3.15, "Data Flow: MDR \u2194 Memory", fontsize=14, color=INK, ha='center',
            bbox=dict(fc="white", ec="none", pad=2))

    save(fig, out)
