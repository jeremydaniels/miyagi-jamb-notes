from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 8)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # Title
    ax.text(7, 7.4, "Basic Components of a Computer System", 
            ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

    # Box styles
    box_kw = dict(boxstyle="round,pad=0.5", lw=2)

    # 1. Input Devices Box (Left)
    input_box = patches.FancyBboxPatch(
        (0.6, 3.7), 2.8, 2.2,
        boxstyle="round,pad=0.2",
        facecolor=CREAM, edgecolor=DEEP["orange"], lw=2
    )
    ax.add_patch(input_box)
    ax.text(2.0, 4.8, "Input Devices\n(Keyboard, Mouse,\nSensors)",
            ha="center", va="center", fontsize=14, color=INK, fontweight="semibold")

    # 2. CPU Box (Center, Larger)
    cpu_outer = patches.FancyBboxPatch(
        (4.7, 3.2), 4.6, 3.2,
        boxstyle="round,pad=0.2",
        facecolor=LAV, edgecolor=DEEP["lav"], lw=2.5
    )
    ax.add_patch(cpu_outer)
    ax.text(7.0, 6.0, "Central Processing Unit (CPU)",
            ha="center", va="center", fontsize=15, fontweight="bold", color=INK)

    # Inside CPU: Control Unit & Arithmetic Logic Unit
    cu_box = patches.FancyBboxPatch(
        (5.0, 4.6), 4.0, 0.9,
        boxstyle="round,pad=0.15",
        facecolor="white", edgecolor=DEEP["lav"], lw=1.5
    )
    ax.add_patch(cu_box)
    ax.text(7.0, 5.05, "Control Unit",
            ha="center", va="center", fontsize=14, color=INK)

    alu_box = patches.FancyBboxPatch(
        (5.0, 3.5), 4.0, 0.9,
        boxstyle="round,pad=0.15",
        facecolor="white", edgecolor=DEEP["lav"], lw=1.5
    )
    ax.add_patch(alu_box)
    ax.text(7.0, 3.95, "Arithmetic Logic Unit",
            ha="center", va="center", fontsize=14, color=INK)

    # 3. Output Devices Box (Right)
    output_box = patches.FancyBboxPatch(
        (10.6, 3.7), 2.8, 2.2,
        boxstyle="round,pad=0.2",
        facecolor=GREEN, edgecolor=DEEP["green"], lw=2
    )
    ax.add_patch(output_box)
    ax.text(12.0, 4.8, "Output Devices\n(Monitor, Printer)",
            ha="center", va="center", fontsize=14, color=INK, fontweight="semibold")

    # 4. Storage Box (Bottom)
    storage_box = patches.FancyBboxPatch(
        (4.9, 0.6), 4.2, 1.4,
        boxstyle="round,pad=0.2",
        facecolor=BLUE, edgecolor=DEEP["blue"], lw=2
    )
    ax.add_patch(storage_box)
    ax.text(7.0, 1.3, "Storage\n(Hard Drive, Flash Drive)",
            ha="center", va="center", fontsize=14, color=INK, fontweight="semibold")

    # Arrows
    # Input -> CPU
    ax.annotate(
        "", xy=(4.65, 4.8), xytext=(3.45, 4.8),
        arrowprops=dict(arrowstyle="-|>", color=INK, lw=2.5, mutation_scale=20)
    )

    # CPU -> Output
    ax.annotate(
        "", xy=(10.55, 4.8), xytext=(9.35, 4.8),
        arrowprops=dict(arrowstyle="-|>", color=INK, lw=2.5, mutation_scale=20)
    )

    # CPU <-> Storage (Two-way arrow)
    ax.annotate(
        "", xy=(7.0, 3.15), xytext=(7.0, 2.05),
        arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=2.5, mutation_scale=20)
    )

    save(fig, out)
