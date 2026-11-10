import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, Polygon
from style import *

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)

    # --- Draw Victim (Left: Laptop + User icon) ---
    # User Icon
    user_x, user_y = 2.0, 4.3
    # Head
    head = Circle((user_x, user_y + 0.5), 0.35, facecolor=BLUE, edgecolor=DEEP['blue'], lw=2.5, zorder=3)
    ax.add_patch(head)
    # Body
    body = FancyBboxPatch((user_x - 0.5, user_y - 0.4), 1.0, 0.7, boxstyle="round,pad=0.2",
                          facecolor=BLUE, edgecolor=DEEP['blue'], lw=2.5, zorder=3)
    ax.add_patch(body)

    # Laptop
    lap_x, lap_y = 2.0, 2.7
    # Screen
    screen = FancyBboxPatch((lap_x - 0.7, lap_y), 1.4, 0.95, boxstyle="round,pad=0.05",
                            facecolor='white', edgecolor=DEEP['blue'], lw=2.5, zorder=3)
    ax.add_patch(screen)
    # Inner display
    inner_screen = Rectangle((lap_x - 0.6, lap_y + 0.1), 1.2, 0.75, facecolor=LAV, edgecolor='none', zorder=4)
    ax.add_patch(inner_screen)
    # Base/Keyboard
    base = Polygon([[lap_x - 0.95, lap_y - 0.15], [lap_x + 0.95, lap_y - 0.15],
                    [lap_x + 0.75, lap_y], [lap_x - 0.75, lap_y]],
                   closed=True, facecolor=GREY, edgecolor=DEEP['blue'], lw=2.2, zorder=3)
    ax.add_patch(base)

    # Victim Label Box
    ax.text(user_x, 1.8, "Victim\n(User)", ha='center', va='center', fontsize=16, weight='bold',
            color=INK, bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=DEEP['blue'], lw=2))

    # --- Draw Target Server (Right: Bank Server Rack) ---
    srv_x, srv_y = 10.0, 3.2
    # Server Tower Body
    srv_box = FancyBboxPatch((srv_x - 0.9, srv_y - 0.9), 1.8, 2.8, boxstyle="round,pad=0.1",
                             facecolor=CREAM, edgecolor=DEEP['green'], lw=2.5, zorder=3)
    ax.add_patch(srv_box)

    # Server Rack Slots
    for i in range(4):
        slot_y = srv_y - 0.6 + i * 0.65
        slot = Rectangle((srv_x - 0.75, slot_y), 1.5, 0.45, facecolor='white',
                         edgecolor=DEEP['green'], lw=1.8, zorder=4)
        ax.add_patch(slot)
        # Server LEDs & Details
        led1 = Circle((srv_x + 0.45, slot_y + 0.225), 0.05, facecolor=DEEP['green'], edgecolor='none', zorder=5)
        led2 = Circle((srv_x + 0.25, slot_y + 0.225), 0.05, facecolor=DEEP['orange'], edgecolor='none', zorder=5)
        ax.add_patch(led1)
        ax.add_patch(led2)
        # Vent lines
        ax.plot([srv_x - 0.6, srv_x], [slot_y + 0.225, slot_y + 0.225], color=DEEP['green'], lw=2, zorder=5)

    # Bank sign on top of server
    bank_sign = FancyBboxPatch((srv_x - 0.8, srv_y + 2.1), 1.6, 0.5, boxstyle="round,pad=0.08",
                               facecolor=GREEN, edgecolor=DEEP['green'], lw=2, zorder=4)
    ax.add_patch(bank_sign)
    ax.text(srv_x, srv_y + 2.35, "BANK", ha='center', va='center', fontsize=14, weight='bold', color=DEEP['green'])

    # Target Server Label Box
    ax.text(srv_x, 1.6, "Target Server\n(Bank)", ha='center', va='center', fontsize=16, weight='bold',
            color=INK, bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=DEEP['green'], lw=2))

    # --- Draw Attacker (Middle: Hacker with Computer) ---
    atk_x, atk_y = 6.0, 5.2
    # Hacker Icon
    # Hood / Head
    hacker_head = Circle((atk_x, atk_y + 0.45), 0.35, facecolor=PINK, edgecolor=DEEP['pink'], lw=2.5, zorder=3)
    ax.add_patch(hacker_head)
    # Body
    hacker_body = FancyBboxPatch((atk_x - 0.5, atk_y - 0.45), 1.0, 0.7, boxstyle="round,pad=0.2",
                                 facecolor=PINK, edgecolor=DEEP['pink'], lw=2.5, zorder=3)
    ax.add_patch(hacker_body)

    # Attacker Laptop
    alap_x, alap_y = 6.0, 4.0
    ascreen = FancyBboxPatch((alap_x - 0.5, alap_y), 1.0, 0.65, boxstyle="round,pad=0.04",
                             facecolor='white', edgecolor=DEEP['pink'], lw=2.2, zorder=4)
    ax.add_patch(ascreen)
    ainner = Rectangle((alap_x - 0.43, alap_y + 0.08), 0.86, 0.5, facecolor=PINK, edgecolor='none', zorder=5)
    ax.add_patch(ainner)
    abase = Polygon([[alap_x - 0.7, alap_y - 0.12], [alap_x + 0.7, alap_y - 0.12],
                     [alap_x + 0.55, alap_y], [alap_x - 0.55, alap_y]],
                    closed=True, facecolor=GREY, edgecolor=DEEP['pink'], lw=2.0, zorder=4)
    ax.add_patch(abase)

    # Attacker Label Box
    ax.text(atk_x, 6.75, "Attacker\n(Man-in-the-middle)", ha='center', va='center', fontsize=16, weight='bold',
            color=INK, bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=DEEP['pink'], lw=2))

    # Wi-Fi / Interception Signal waves near attacker
    for r in [0.4, 0.65, 0.9]:
        arc_theta = np.linspace(np.pi * 1.1, np.pi * 1.9, 30)
        ax.plot(atk_x + r * np.cos(arc_theta), (atk_y - 0.3) + r * np.sin(arc_theta),
                color=DEEP['pink'], lw=2.2, ls=':')

    # --- Arrows and Communication paths ---

    # 1. Normal intended connection (severed / bypassed at the bottom)
    ax.annotate("", xy=(8.8, 2.7), xytext=(3.2, 2.7),
                arrowprops=dict(arrowstyle="<->", color=GREY, lw=2.5, linestyle="dashed"))
    ax.text(6.0, 2.7, "✕ Intended Direct Connection ✕", ha='center', va='center', fontsize=14,
            weight='bold', color=GREY, bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=GREY, lw=1.5))

    # 2. Data from Victim -> Attacker
    ax.annotate("", xy=(4.9, 4.2), xytext=(2.9, 3.4),
                arrowprops=dict(arrowstyle="-|>", color=DEEP['pink'], lw=3.2,
                                mutation_scale=22, shrinkA=8, shrinkB=8))
    ax.text(3.6, 4.3, "Intercepted\nData / Credentials", ha='center', va='center', fontsize=14,
            weight='bold', color=DEEP['pink'], bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=DEEP['pink'], lw=1.5))

    # 3. Data from Attacker -> Server (relay / altered data)
    ax.annotate("", xy=(8.8, 3.6), xytext=(7.1, 4.4),
                arrowprops=dict(arrowstyle="-|>", color=DEEP['pink'], lw=3.2,
                                mutation_scale=22, shrinkA=8, shrinkB=8))
    ax.text(8.4, 4.6, "Relayed / Altered\nRequests", ha='center', va='center', fontsize=14,
            weight='bold', color=DEEP['pink'], bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=DEEP['pink'], lw=1.5))

    save(fig, out)
