from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 5.5)
    
    # Left subplot: Musical Note
    ax1 = fig.add_subplot(1, 2, 1)
    # Right subplot: Noise
    ax2 = fig.add_subplot(1, 2, 2)
    
    # Time vector
    t = np.linspace(0, 4 * np.pi, 1000)
    
    # Musical note: clean, periodic, harmonic wave
    wave_music = np.sin(2 * t) + 0.3 * np.sin(4 * t)
    
    # Noise: irregular, non-repeating, jagged waveform using multiple incommensurate frequencies + noise
    np.random.seed(42)
    t_noise = np.linspace(0, 4 * np.pi, 250)
    random_offsets = np.random.uniform(-0.8, 0.8, size=len(t_noise))
    wave_noise_raw = (
        0.6 * np.sin(1.7 * t_noise)
        + 0.5 * np.cos(3.9 * t_noise)
        + 0.4 * np.sin(7.3 * t_noise)
        + 0.3 * np.cos(11.1 * t_noise)
        + random_offsets
    )
    # Scale slightly to match amplitude range
    wave_noise = wave_noise_raw / np.max(np.abs(wave_noise_raw)) * 1.25

    for ax, wave, x_vals, title, col in [
        (ax1, wave_music, t, "Musical Note", DEEP["blue"]),
        (ax2, wave_noise, t_noise, "Noise", DEEP["orange"])
    ]:
        ax.set_facecolor("white")
        # Horizontal centerline (equilibrium)
        ax.axhline(0, color=GREY, lw=1.5, linestyle="--")
        
        # Plot waveform
        ax.plot(x_vals, wave, color=col, lw=2.8)
        
        # Styling and limits
        ax.set_ylim(-1.8, 1.8)
        ax.set_xlim(0, 4 * np.pi)
        
        # Remove tick numbers but keep clean box / style
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ["top", "right"]:
            ax.spines[spine].set_visible(False)
        ax.spines["left"].set_color(INK)
        ax.spines["bottom"].set_color(INK)
        ax.spines["left"].set_linewidth(1.5)
        ax.spines["bottom"].set_linewidth(1.5)
        
        ax.set_xlabel("Time", fontsize=15, color=INK, labelpad=8)
        ax.set_ylabel("Displacement", fontsize=15, color=INK, labelpad=8)
        ax.set_title(title, fontsize=18, color=INK, weight="bold", pad=15)

    # Descriptive textbook annotations below titles / waveforms
    ax1.text(0.5, -0.22, "Regular, periodic waveform", transform=ax1.transAxes,
             ha="center", fontsize=14, color=INK,
             bbox=dict(boxstyle="round,pad=0.3", fc=CREAM, ec=GREY, lw=1))
             
    ax2.text(0.5, -0.22, "Irregular, non-repeating waveform", transform=ax2.transAxes,
             ha="center", fontsize=14, color=INK,
             bbox=dict(boxstyle="round,pad=0.3", fc=CREAM, ec=GREY, lw=1))

    plt.subplots_adjust(bottom=0.22, top=0.85, wspace=0.25, left=0.08, right=0.96)
    save(fig, out)
