from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 11)
    
    # 3 rows, 2 columns of subplots
    axes = fig.subplots(3, 2)
    fig.subplots_adjust(left=0.08, right=0.95, top=0.84, bottom=0.06, hspace=0.6, wspace=0.25)

    x = np.linspace(0, 4 * np.pi, 1000)

    # Styling helper for each wave subplot
    def format_ax(ax):
        ax.set_facecolor('white')
        ax.axhline(0, color=GREY, lw=1.2, linestyle='--')
        ax.set_ylim(-1.6, 1.6)
        ax.set_xlim(0, 4 * np.pi)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color(GREY)
            spine.set_linewidth(1.2)

    # --- TOP ROW: Pitch (Frequency comparison) ---
    # High pitch: high frequency, same amplitude
    y_high_pitch = np.sin(4 * x)
    axes[0, 0].plot(x, y_high_pitch, color=DEEP['blue'], lw=3)
    format_ax(axes[0, 0])
    axes[0, 0].set_title("High Pitch\n(High Frequency, Same Amplitude)", fontsize=15, weight='bold', color=INK, pad=10)

    # Low pitch: low frequency, same amplitude
    y_low_pitch = np.sin(x)
    axes[0, 1].plot(x, y_low_pitch, color=DEEP['orange'], lw=3)
    format_ax(axes[0, 1])
    axes[0, 1].set_title("Low Pitch\n(Low Frequency, Same Amplitude)", fontsize=15, weight='bold', color=INK, pad=10)

    # --- MIDDLE ROW: Loudness (Amplitude comparison) ---
    # Loud: large amplitude, same frequency
    y_loud = 1.35 * np.sin(2 * x)
    axes[1, 0].plot(x, y_loud, color=DEEP['pink'], lw=3)
    format_ax(axes[1, 0])
    axes[1, 0].set_title("Loud\n(Large Amplitude)", fontsize=15, weight='bold', color=INK, pad=10)

    # Quiet: small amplitude, same frequency
    y_quiet = 0.45 * np.sin(2 * x)
    axes[1, 1].plot(x, y_quiet, color=DEEP['green'], lw=3)
    format_ax(axes[1, 1])
    axes[1, 1].set_title("Quiet\n(Small Amplitude)", fontsize=15, weight='bold', color=INK, pad=10)

    # --- BOTTOM ROW: Timbre / Quality ---
    # Pure sine wave
    y_pure = np.sin(1.5 * x)
    axes[2, 0].plot(x, y_pure, color=DEEP['blue'], lw=3)
    format_ax(axes[2, 0])
    axes[2, 0].set_title("Pure Tone\n(Simple Sine Wave)", fontsize=15, weight='bold', color=INK, pad=10)

    # Complex wave (fundamental + harmonics ripples)
    y_complex = np.sin(1.5 * x) + 0.22 * np.sin(4.5 * x) + 0.12 * np.sin(7.5 * x)
    axes[2, 1].plot(x, y_complex, color=DEEP['lav'], lw=3)
    format_ax(axes[2, 1])
    axes[2, 1].set_title("Complex Wave\n(Different Quality / Timbre)", fontsize=15, weight='bold', color=INK, pad=10)

    # Row category labels on the left margin
    fig.text(0.5, 0.95, "Comparison of Waveform Characteristics", ha='center', va='center', fontsize=18, weight='bold', color=INK)

    save(fig, out)
