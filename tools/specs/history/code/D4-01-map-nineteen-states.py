from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(12, 10.5)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')

    # Continuous polygonal tessellation matching Nigeria's 1976 19-state structure + FCT.
    # FCT is in the centre.
    states = {
        'Sokoto': {
            'poly': [(3.6, 9.5), (3.6, 10.5), (3.8, 11.7), (4.2, 12.0), (4.5, 13.7),
                     (5.5, 13.8), (7.2, 13.1), (7.2, 11.5), (6.0, 11.0), (5.0, 11.0),
                     (4.3, 10.0), (3.6, 9.5)],
            'color': CREAM
        },
        'Kano': {
            'poly': [(7.2, 13.1), (8.5, 13.0), (9.8, 13.0), (10.0, 11.4), (8.8, 11.0),
                     (7.6, 11.2), (7.2, 11.5), (7.2, 13.1)],
            'color': LAV
        },
        'Borno': {
            'poly': [(9.8, 13.0), (12.0, 13.0), (13.5, 13.7), (14.2, 12.8), (14.6, 12.3),
                     (14.0, 11.5), (13.2, 10.5), (11.8, 10.5), (10.8, 11.2), (10.0, 11.4),
                     (9.8, 13.0)],
            'color': GREEN
        },
        'Bauchi': {
            'poly': [(8.8, 11.0), (10.0, 11.4), (10.8, 11.2), (11.8, 10.5), (11.4, 9.6),
                     (10.2, 9.4), (9.0, 9.6), (8.6, 10.1), (8.8, 11.0)],
            'color': BLUE
        },
        'Kaduna': {
            'poly': [(6.0, 11.0), (7.2, 11.5), (7.6, 11.2), (8.8, 11.0), (8.6, 10.1),
                     (8.4, 9.3), (7.5, 9.3), (7.2, 9.6), (6.5, 9.8), (6.0, 11.0)],
            'color': PINK
        },
        'Niger': {
            'poly': [(3.6, 9.5), (4.3, 10.0), (5.0, 11.0), (6.0, 11.0), (6.5, 9.8),
                     (7.2, 9.6), (7.2, 8.8), (7.0, 8.6), (6.7, 8.4), (5.6, 8.5),
                     (4.5, 8.7), (3.6, 9.0), (3.6, 9.5)],
            'color': ORANGE
        },
        'FCT (Abuja)': {
            'poly': [(7.2, 9.4), (7.8, 9.4), (7.8, 8.7), (7.2, 8.7), (7.2, 9.4)],
            'color': CREAM
        },
        'Plateau': {
            'poly': [(7.8, 9.4), (8.4, 9.3), (8.6, 10.1), (9.0, 9.6), (10.2, 9.4),
                     (10.2, 8.7), (9.8, 8.0), (8.2, 8.0), (7.8, 8.7), (7.8, 9.4)],
            'color': LAV
        },
        'Gongola': {
            'poly': [(11.8, 10.5), (13.2, 10.5), (12.5, 9.5), (12.0, 8.5), (11.5, 7.0),
                     (10.2, 6.8), (10.2, 7.6), (10.2, 8.7), (10.2, 9.4), (11.4, 9.6),
                     (11.8, 10.5)],
            'color': CREAM
        },
        'Kwara': {
            'poly': [(3.6, 9.0), (4.5, 8.7), (5.6, 8.5), (6.7, 8.4), (7.0, 8.6),
                     (7.0, 8.0), (6.5, 7.6), (5.8, 7.5), (4.7, 7.8), (3.8, 8.0),
                     (2.8, 8.2), (3.6, 9.0)],
            'color': GREEN
        },
        'Oyo': {
            'poly': [(2.7, 7.5), (2.8, 8.2), (3.8, 8.0), (4.7, 7.8), (4.5, 7.1),
                     (3.5, 7.0), (2.7, 7.5)],
            'color': BLUE
        },
        'Ondo': {
            'poly': [(4.7, 7.8), (5.8, 7.5), (6.1, 7.3), (5.7, 6.3), (4.8, 6.5),
                     (4.5, 7.1), (4.7, 7.8)],
            'color': LAV
        },
        'Ogun': {
            'poly': [(2.7, 6.6), (3.5, 7.0), (4.5, 7.1), (4.8, 6.5), (4.5, 6.4),
                     (3.5, 6.4), (2.7, 6.6)],
            'color': ORANGE
        },
        'Lagos': {
            'poly': [(2.7, 6.4), (3.5, 6.4), (4.5, 6.4), (4.0, 6.2), (2.7, 6.3),
                     (2.7, 6.4)],
            'color': PINK
        },
        'Bendel': {
            'poly': [(4.8, 6.5), (5.7, 6.3), (6.1, 7.3), (6.5, 7.2), (6.6, 5.8),
                     (5.8, 5.3), (5.0, 5.5), (4.8, 6.5)],
            'color': CREAM
        },
        'Benue': {
            'poly': [(7.0, 8.6), (7.2, 8.7), (7.2, 9.4), (7.8, 9.4), (7.8, 8.7), (8.2, 8.0), (9.8, 8.0), (10.2, 8.7),
                     (10.2, 7.6), (10.2, 6.8), (9.0, 6.8), (8.3, 7.0), (7.4, 7.1),
                     (6.5, 7.2), (6.5, 7.6), (7.0, 8.0), (7.0, 8.6)],
            'color': ORANGE
        },
        'Anambra': {
            'poly': [(6.5, 7.2), (7.4, 7.1), (7.8, 6.2), (6.6, 6.1), (6.5, 7.2)],
            'color': BLUE
        },
        'Imo': {
            'poly': [(6.6, 6.1), (7.8, 6.2), (7.6, 5.3), (6.8, 5.4), (6.6, 6.1)],
            'color': GREEN
        },
        'Rivers': {
            'poly': [(5.8, 5.3), (6.6, 5.8), (6.6, 6.1), (6.8, 5.4), (7.6, 5.3),
                     (7.6, 4.5), (6.0, 4.3), (5.8, 5.3)],
            'color': LAV
        },
        'Cross River': {
            'poly': [(7.4, 7.1), (8.3, 7.0), (9.0, 6.8), (9.3, 6.5), (8.5, 4.7),
                     (7.6, 4.5), (7.6, 5.3), (7.8, 6.2), (7.4, 7.1)],
            'color': PINK
        }
    }
    
    # Fix topology for adjacent states around FCT
    states['Niger']['poly'] = [(3.6, 9.5), (4.3, 10.0), (5.0, 11.0), (6.0, 11.0), (6.5, 9.8),
                     (7.2, 9.6), (7.2, 8.7), (7.0, 8.6), (6.7, 8.4), (5.6, 8.5),
                     (4.5, 8.7), (3.6, 9.0), (3.6, 9.5)]
    states['Kaduna']['poly'] = [(6.0, 11.0), (7.2, 11.5), (7.6, 11.2), (8.8, 11.0), (8.6, 10.1),
                     (8.4, 9.3), (7.8, 9.4), (7.2, 9.4), (7.2, 9.6), (6.5, 9.8), (6.0, 11.0)]
    states['Benue']['poly'] = [(7.0, 8.6), (7.2, 8.7), (7.8, 8.7), (8.2, 8.0), (9.8, 8.0), (10.2, 8.7),
                     (10.2, 7.6), (10.2, 6.8), (9.0, 6.8), (8.3, 7.0), (7.4, 7.1),
                     (6.5, 7.2), (6.5, 7.6), (7.0, 8.0), (7.0, 8.6)]

    # Draw all state patches
    for name, info in states.items():
        patch = Polygon(info['poly'], closed=True, facecolor=info['color'],
                        edgecolor=INK, linewidth=1.5, zorder=2)
        ax.add_patch(patch)

    # State labels
    internal_labels = {
        'Sokoto': (5.3, 12.0),
        'Kano': (8.5, 12.1),
        'Borno': (12.2, 11.8),
        'Bauchi': (10.1, 10.3),
        'Kaduna': (7.5, 10.3),
        'Niger': (5.3, 9.6),
        'Plateau': (8.9, 8.8),
        'Gongola': (11.5, 8.6),
        'Kwara': (5.0, 8.3),
        'Oyo': (3.6, 7.6),
        'Ondo': (5.2, 7.0),
        'Bendel': (5.8, 6.1),
        'Benue': (8.5, 7.5),
        'Rivers': (6.7, 4.8)
    }

    for name, pos in internal_labels.items():
        ax.text(pos[0], pos[1], name, fontsize=14, weight='bold', color=INK,
                ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.65),
                zorder=4)

    # Pointer labels
    ax.annotate("FCT (Abuja)", xy=(7.5, 9.05), xytext=(5.6, 10.4),
                fontsize=14, weight='bold', color=INK, ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=INK, lw=1.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=5)

    ax.annotate("Lagos", xy=(3.5, 6.35), xytext=(2.3, 5.6),
                fontsize=14, weight='bold', color=INK, ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=INK, lw=1.0),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3), zorder=5)

    ax.annotate("Ogun", xy=(3.5, 6.7), xytext=(2.2, 6.7),
                fontsize=14, weight='bold', color=INK, ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=INK, lw=1.0),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3), zorder=5)

    ax.annotate("Anambra", xy=(7.1, 6.6), xytext=(6.5, 7.7),
                fontsize=14, weight='bold', color=INK, ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=INK, lw=1.0),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3), zorder=5)

    ax.annotate("Imo", xy=(7.2, 5.75), xytext=(7.2, 5.0),
                fontsize=14, weight='bold', color=INK, ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=INK, lw=1.0),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3), zorder=5)

    ax.annotate("Cross River", xy=(8.3, 5.9), xytext=(10.5, 5.5),
                fontsize=14, weight='bold', color=INK, ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=INK, lw=1.0),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3), zorder=5)

    # Title and notes
    ax.text(8.5, 14.5, "Nigeria: 19-State Structure (1976)", fontsize=18,
            weight='bold', color=INK, ha='center', va='center')
    ax.text(8.5, 3.8, "Sketch map: zones are approximate", fontsize=14,
            style='italic', color=INK, ha='center', va='center')

    ax.set_xlim(1.2, 15.2)
    ax.set_ylim(3.4, 15.0)

    save(fig, out)
