import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
from style import *

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(6.0, 7.0, "Boot Process: Loading OS into RAM", ha="center", va="center",
            fontsize=18, weight="bold", color=INK)

    # 1. Hard Drive Box (Left) - Secondary Storage
    hdd_box = FancyBboxPatch((0.8, 1.2), 3.0, 3.8, boxstyle="round,pad=0.15",
                             fc=CREAM, ec=DEEP["orange"], lw=2.5)
    ax.add_patch(hdd_box)
    ax.text(2.3, 4.6, "Hard Disk Drive (HDD)", ha="center", va="center",
            fontsize=15, weight="bold", color=INK)
    ax.text(2.3, 4.25, "(Secondary Storage)", ha="center", va="center",
            fontsize=14, color=GREY)

    # Disk platter schematic inside HDD
    platter = Circle((2.3, 2.7), 1.1, fc="white", ec=DEEP["orange"], lw=2)
    ax.add_patch(platter)
    platter_inner = Circle((2.3, 2.7), 0.35, fc=CREAM, ec=DEEP["orange"], lw=1.5)
    ax.add_patch(platter_inner)

    # OS on HDD indicator
    os_hdd_badge = FancyBboxPatch((1.3, 1.45), 2.0, 0.55, boxstyle="round,pad=0.08",
                                  fc=ORANGE, ec=DEEP["orange"], lw=1.5)
    ax.add_patch(os_hdd_badge)
    ax.text(2.3, 1.72, "Operating System (OS)", ha="center", va="center",
            fontsize=14, weight="bold", color=INK)

    # 2. RAM Box (Right) - Primary Memory
    ram_box = FancyBboxPatch((8.2, 1.2), 3.0, 3.8, boxstyle="round,pad=0.15",
                             fc=LAV, ec=DEEP["lav"], lw=2.5)
    ax.add_patch(ram_box)
    ax.text(9.7, 4.6, "RAM", ha="center", va="center",
            fontsize=16, weight="bold", color=INK)
    ax.text(9.7, 4.25, "(Primary Memory)", ha="center", va="center",
            fontsize=14, color=GREY)

    # Memory chips schematic inside RAM
    for idx, y_pos in enumerate([3.3, 2.7, 2.1]):
        chip = Rectangle((8.6, y_pos), 2.2, 0.45, fc="white", ec=DEEP["lav"], lw=1.5)
        ax.add_patch(chip)
        label = "Loaded OS Kernel" if idx == 0 else "Free / User Space"
        c_label = DEEP["lav"] if idx == 0 else GREY
        ax.text(9.7, y_pos + 0.22, label, ha="center", va="center",
                fontsize=14, color=c_label, weight="bold" if idx == 0 else "normal")

    # 3. CPU Box (Top Center) - Control & Oversight
    cpu_box = FancyBboxPatch((4.5, 4.5), 3.0, 1.8, boxstyle="round,pad=0.15",
                             fc=BLUE, ec=DEEP["blue"], lw=2.5)
    ax.add_patch(cpu_box)
    ax.text(6.0, 5.75, "Processor (CPU)", ha="center", va="center",
            fontsize=16, weight="bold", color=INK)
    ax.text(6.0, 5.35, "Executes Bootloader (BIOS/UEFI)", ha="center", va="center",
            fontsize=14, color=INK)
    ax.text(6.0, 4.95, "Oversees Data Transfer", ha="center", va="center",
            fontsize=14, style="italic", color=DEEP["blue"])

    # Pins on CPU
    for px in np.linspace(4.8, 7.2, 7):
        ax.plot([px, px], [4.4, 4.5], color=DEEP["blue"], lw=2.5)
        ax.plot([px, px], [6.3, 6.4], color=DEEP["blue"], lw=2.5)

    # 4. Data Flow Arrow (HDD -> RAM)
    ax.annotate("", xy=(8.1, 2.7), xytext=(3.9, 2.7),
                arrowprops=dict(arrowstyle="simple,head_width=1.0,head_length=1.0",
                                facecolor=DEEP["green"], edgecolor="none", lw=0))
    ax.text(6.0, 3.1, "OS Copied to RAM", ha="center", va="center",
            fontsize=15, weight="bold", color=DEEP["green"],
            bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.3", lw=1.5))
    ax.text(6.0, 2.3, "(Data Transfer via Bus)", ha="center", va="center",
            fontsize=14, color=GREY)

    # 5. Control Signals from CPU (Dashed lines / arrows to HDD and RAM)
    # CPU to HDD (Read command)
    ax.annotate("", xy=(2.7, 4.9), xytext=(4.4, 5.2),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.0,
                                linestyle="--", connectionstyle="arc3,rad=-0.15"))
    ax.text(3.1, 5.4, "1. Read OS", ha="center", va="center",
            fontsize=14, color=DEEP["blue"], weight="bold",
            bbox=dict(fc="white", ec="none", pad=1))

    # CPU to RAM (Load / execute instructions)
    ax.annotate("", xy=(9.3, 4.9), xytext=(7.6, 5.2),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.0,
                                linestyle="--", connectionstyle="arc3,rad=0.15"))
    ax.text(8.9, 5.4, "2. Load & Execute", ha="center", va="center",
            fontsize=14, color=DEEP["blue"], weight="bold",
            bbox=dict(fc="white", ec="none", pad=1))

    # Bottom summary caption box
    summary_box = FancyBboxPatch((1.5, 0.25), 9.0, 0.65, boxstyle="round,pad=0.1",
                                 fc="white", ec=GREY, lw=1.2)
    ax.add_patch(summary_box)
    ax.text(6.0, 0.57,
            "During startup, the CPU coordinates copying the OS from secondary storage into volatile RAM.",
            ha="center", va="center", fontsize=14, color=INK)

    save(fig, out)
