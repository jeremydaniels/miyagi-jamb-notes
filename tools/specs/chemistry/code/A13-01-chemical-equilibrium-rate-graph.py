from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6)
    ax = fig.add_subplot(111)
    
    # Clean axes
    axes_clean(ax, "Time", "Reaction Rate", 10, 10)
    
    # Equilibrium point and rate
    t_eq = 5.2
    r_eq = 5.0
    
    # Generate time points
    t_before = np.linspace(0, t_eq, 150)
    t_after = np.linspace(t_eq, 9.5, 100)
    
    # Curves before equilibrium
    # Forward: starts at 9.0, decays exponentially to r_eq
    k = 0.8
    r_forward_before = r_eq + (9.0 - r_eq) * np.exp(-k * t_before)
    # Adjust exactly to r_eq at t_eq smoothly
    decay_f = np.exp(-0.85 * t_before)
    norm_f = (decay_f - decay_f[-1]) / (decay_f[0] - decay_f[-1])
    r_forward_before = r_eq + (9.0 - r_eq) * norm_f
    
    # Backward: starts at 0.0, rises to r_eq
    decay_b = 1.0 - np.exp(-0.85 * t_before)
    norm_b = (decay_b - decay_b[0]) / (decay_b[-1] - decay_b[0])
    r_backward_before = r_eq * norm_b
    
    # Combined curves
    t_full = np.concatenate([t_before, t_after])
    r_forward = np.concatenate([r_forward_before, np.full_like(t_after, r_eq)])
    r_backward = np.concatenate([r_backward_before, np.full_like(t_after, r_eq)])
    
    # Plot curves
    ax.plot(t_full, r_forward, color=DEEP["blue"], lw=3.5, label="Forward reaction rate")
    ax.plot(t_full, r_backward, color=DEEP["orange"], lw=3.5, label="Backward reaction rate")
    
    # Vertical dashed line at equilibrium
    ax.axvline(x=t_eq, ymin=0, ymax=0.92, color=GREY, linestyle="--", lw=2)
    
    # Text annotation for equilibrium established
    ax.text(
        t_eq, 9.5, "Equilibrium established",
        fontsize=14, color=INK, ha="center", va="center",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35", lw=1.2)
    )
    
    # Labels directly on or near curves
    ax.text(
        1.8, 7.8, "Forward reaction rate",
        fontsize=14, color=DEEP["blue"], ha="left", va="bottom",
        fontweight="bold",
        bbox=dict(fc="white", ec="none", pad=0.2)
    )
    ax.text(
        1.8, 2.2, "Backward reaction rate",
        fontsize=14, color=DEEP["orange"], ha="left", va="top",
        fontweight="bold",
        bbox=dict(fc="white", ec="none", pad=0.2)
    )
    
    # Equilibrium state label
    ax.text(
        7.3, 5.4, "Rates are equal\n(Dynamic equilibrium)",
        fontsize=14, color=INK, ha="center", va="bottom",
        bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.3", lw=1)
    )
    
    save(fig, out)
