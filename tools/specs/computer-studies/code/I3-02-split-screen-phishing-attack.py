import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style import *

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.set_aspect('equal')
    ax.axis('off')

    # Main Title
    ax.text(6, 6.55, "Phishing Attack: SMS Smishing to Fake Login", 
            ha='center', va='center', fontsize=18, weight='bold', color=INK)

    # ----------------------------------------------------
    # LEFT PANEL: Mobile Phone with SMS Phishing (Smishing)
    # ----------------------------------------------------
    # Subtitle Left
    ax.text(2.6, 6.05, "1. Fraudulent SMS (Smishing)", 
            ha='center', va='center', fontsize=15, weight='bold', color=DEEP['orange'])

    # Phone Outer Body
    phone_outer = patches.FancyBboxPatch((0.9, 0.8), 3.4, 5.0,
                                         boxstyle="round,pad=0.0,rounding_size=0.4",
                                         facecolor=CREAM, edgecolor=INK, lw=2.5)
    ax.add_patch(phone_outer)

    # Phone Inner Screen
    phone_screen = patches.FancyBboxPatch((1.1, 1.3), 3.0, 4.2,
                                          boxstyle="round,pad=0.0,rounding_size=0.15",
                                          facecolor="white", edgecolor=GREY, lw=1.5)
    ax.add_patch(phone_screen)

    # Speaker notch & home button indicator
    ax.plot([2.3, 2.9], [5.6, 5.6], color=INK, lw=3, solid_capstyle='round')
    ax.plot([2.3, 2.9], [1.05, 1.05], color=GREY, lw=3, solid_capstyle='round')

    # SMS Header inside screen
    sms_hdr = patches.Rectangle((1.1, 5.0), 3.0, 0.5, facecolor=LAV, edgecolor=None)
    ax.add_patch(sms_hdr)
    ax.text(2.6, 5.25, "Messages: Bank Alert", ha='center', va='center', 
            fontsize=14, weight='bold', color=INK)

    # SMS Chat Bubble
    bubble = patches.FancyBboxPatch((1.3, 2.6), 2.6, 2.1,
                                    boxstyle="round,pad=0.0,rounding_size=0.2",
                                    facecolor=PINK, edgecolor=DEEP['pink'], lw=1.5)
    ax.add_patch(bubble)

    # Urgent Warning Icon / Text inside bubble
    ax.text(2.6, 4.35, "⚠️ URGENT NOTICE", ha='center', va='center', 
            fontsize=14, weight='bold', color=DEEP['pink'])
    
    msg_body = "Your Bank ATM is\nblocked. Click here\nto verify:"
    ax.text(2.6, 3.55, msg_body, ha='center', va='center', 
            fontsize=14, color=INK, linespacing=1.2)

    # Phishing link inside bubble
    link_rect = patches.FancyBboxPatch((1.45, 2.75), 2.3, 0.4,
                                       boxstyle="round,pad=0.0,rounding_size=0.1",
                                       facecolor="white", edgecolor=DEEP['blue'], lw=1.2)
    ax.add_patch(link_rect)
    ax.text(2.6, 2.95, "bank-verify-atm.com", ha='center', va='center', 
            fontsize=14, weight='bold', color=DEEP['blue'])

    # ----------------------------------------------------
    # CONNECTING ARROW: User clicks link
    # ----------------------------------------------------
    ax.annotate("Victim clicks link\nin message",
                xy=(6.3, 3.8), xytext=(4.6, 4.4),
                ha="center", va="center", fontsize=14, weight='bold', color=DEEP['orange'],
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP['orange'], lw=1.5),
                arrowprops=dict(arrowstyle="->", color=DEEP['orange'], lw=2.5,
                                connectionstyle="arc3,rad=-0.15"))

    # ----------------------------------------------------
    # RIGHT PANEL: Computer Screen with Fake Bank Login
    # ----------------------------------------------------
    # Subtitle Right
    ax.text(9.2, 6.05, "2. Spoofed Bank Webpage", 
            ha='center', va='center', fontsize=15, weight='bold', color=DEEP['pink'])

    # Monitor Stand & Base
    stand_base = patches.FancyBboxPatch((8.2, 0.7), 2.0, 0.3,
                                        boxstyle="round,pad=0.0,rounding_size=0.1",
                                        facecolor=GREY, edgecolor=INK, lw=2)
    ax.add_patch(stand_base)
    stand_neck = patches.Rectangle((8.9, 0.95), 0.6, 0.6, facecolor=GREY, edgecolor=INK, lw=2)
    ax.add_patch(stand_neck)

    # Monitor Outer Frame
    monitor_outer = patches.FancyBboxPatch((6.4, 1.45), 5.4, 4.3,
                                           boxstyle="round,pad=0.0,rounding_size=0.3",
                                           facecolor=CREAM, edgecolor=INK, lw=2.5)
    ax.add_patch(monitor_outer)

    # Monitor Screen Area
    monitor_screen = patches.Rectangle((6.6, 1.65), 5.0, 3.8,
                                       facecolor="white", edgecolor=GREY, lw=1.5)
    ax.add_patch(monitor_screen)

    # Browser Top Bar
    browser_bar = patches.Rectangle((6.6, 4.95), 5.0, 0.5,
                                    facecolor=GREY, edgecolor=GREY, lw=1)
    ax.add_patch(browser_bar)

    # Window dots
    for i, c in enumerate([DEEP['pink'], DEEP['orange'], DEEP['green']]):
        dot = patches.Circle((6.85 + i * 0.22, 5.2), 0.07, facecolor=c, edgecolor=None)
        ax.add_patch(dot)

    # Suspicious URL bar (highlighted)
    url_box = patches.FancyBboxPatch((7.4, 5.03), 4.05, 0.35,
                                     boxstyle="round,pad=0.0,rounding_size=0.08",
                                     facecolor="white", edgecolor=DEEP['pink'], lw=2.0)
    ax.add_patch(url_box)
    ax.text(9.4, 5.2, "http://bank-verify-atm.com/login", ha='center', va='center',
            fontsize=14, color=DEEP['pink'], weight='bold')

    # Suspicious URL callout
    ax.annotate("Suspicious URL (unsecured / fake domain)",
                xy=(9.4, 5.4), xytext=(9.4, 5.75),
                ha="center", va="center", fontsize=14, weight='bold', color=DEEP['pink'],
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP['pink'], lw=1.5),
                arrowprops=dict(arrowstyle="->", color=DEEP['pink'], lw=2))

    # Webpage Header / Fake Bank Logo
    bank_logo_bg = patches.Rectangle((7.0, 4.45), 4.2, 0.38, facecolor=BLUE, edgecolor=None)
    ax.add_patch(bank_logo_bg)
    ax.text(9.1, 4.64, "TRUST BANK - ONLINE PORTAL", ha='center', va='center',
            fontsize=14, weight='bold', color=DEEP['blue'])

    # Login Form
    ax.text(9.1, 4.15, "Account Verification Login", ha='center', va='center',
            fontsize=14, weight='bold', color=INK)

    # Input Field 1: Username / Card
    f1 = patches.FancyBboxPatch((7.8, 3.45), 2.6, 0.38,
                                boxstyle="round,pad=0.0,rounding_size=0.08",
                                facecolor="white", edgecolor=GREY, lw=1.5)
    ax.add_patch(f1)
    ax.text(7.2, 3.64, "Username:", ha='right', va='center', fontsize=14, color=INK)
    ax.text(7.95, 3.64, "cardholder123", ha='left', va='center', fontsize=14, color=GREY)

    # Input Field 2: Password / PIN
    f2 = patches.FancyBboxPatch((7.8, 2.85), 2.6, 0.38,
                                boxstyle="round,pad=0.0,rounding_size=0.08",
                                facecolor="white", edgecolor=GREY, lw=1.5)
    ax.add_patch(f2)
    ax.text(7.2, 3.04, "PIN / Pass:", ha='right', va='center', fontsize=14, color=INK)
    ax.text(7.95, 3.04, "••••••••", ha='left', va='center', fontsize=14, color=INK)

    # Login Button
    btn = patches.FancyBboxPatch((8.3, 2.15), 1.6, 0.42,
                                 boxstyle="round,pad=0.0,rounding_size=0.1",
                                 facecolor=GREEN, edgecolor=DEEP['green'], lw=1.8)
    ax.add_patch(btn)
    ax.text(9.1, 2.36, "VERIFY", ha='center', va='center',
            fontsize=14, weight='bold', color=DEEP['green'])

    # Warning text at bottom
    ax.text(9.1, 1.85, "Stolen credentials sent to attacker", ha='center', va='center',
            fontsize=14, weight='bold', color=DEEP['pink'])

    save(fig, out)
