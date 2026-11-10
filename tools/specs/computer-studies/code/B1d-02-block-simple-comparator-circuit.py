from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)

    # Gates
    # gate(ax, kind, x, y, w=1.6, h=1.0)
    g_xor = gate(ax, 'XOR', 3.2, 2.5, w=1.8, h=1.2)
    g_nor = gate(ax, 'NOR', 7.0, 2.5, w=1.8, h=1.2)

    xor_in1, xor_in2 = g_xor['in']
    xor_out = g_xor['out']

    nor_in1, nor_in2 = g_nor['in']
    nor_out = g_nor['out']

    # Inputs A and B
    ax.plot([0.8, xor_in1[0]], [xor_in1[1], xor_in1[1]], color=INK, lw=2.4)
    ax.text(0.6, xor_in1[1], 'A', fontsize=18, va='center', ha='right', color=INK, fontweight='bold')

    ax.plot([0.8, xor_in2[0]], [xor_in2[1], xor_in2[1]], color=INK, lw=2.4)
    ax.text(0.6, xor_in2[1], 'B', fontsize=18, va='center', ha='right', color=INK, fontweight='bold')

    # Connection between XOR and NOR
    # XOR out goes horizontally to a split point, then branches to both NOR inputs
    split_x = (xor_out[0] + nor_in1[0]) / 2.0
    ax.plot([xor_out[0], split_x], [xor_out[1], xor_out[1]], color=INK, lw=2.4)

    # Vertical branch
    ax.plot([split_x, split_x], [nor_in1[1], nor_in2[1]], color=INK, lw=2.4)
    # Branch point dot
    ax.plot(split_x, xor_out[1], marker='o', markersize=6, color=INK)

    # Horizontal lines to NOR inputs
    ax.plot([split_x, nor_in1[0]], [nor_in1[1], nor_in1[1]], color=INK, lw=2.4)
    ax.plot([split_x, nor_in2[0]], [nor_in2[1], nor_in2[1]], color=INK, lw=2.4)

    # Output wire and label
    out_end_x = 8.5
    ax.plot([nor_out[0], out_end_x], [nor_out[1], nor_out[1]], color=INK, lw=2.4)
    ax.text(out_end_x + 0.2, nor_out[1], 'A = B (Equality)', fontsize=16, va='center', ha='left', color=INK, fontweight='bold')

    # Gate type labels for clarity
    ax.text(3.2, 1.3, 'XOR', fontsize=14, ha='center', va='center', color=INK)
    ax.text(7.0, 1.3, 'NOR', fontsize=14, ha='center', va='center', color=INK)

    save(fig, out)
