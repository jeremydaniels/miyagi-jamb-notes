from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 10)
    
    # Subplot 1: Upper area for cell and virus anatomy
    ax_top = fig.add_axes([0.05, 0.44, 0.90, 0.52])
    ax_top.set_xlim(0, 100)
    ax_top.set_ylim(0, 56)
    ax_top.axis("off")
    
    # --- Left: HIV Particle Cross-Section ---
    # Center at (18, 25), radius ~ 10
    cx, cy, r_env = 18, 25, 9.5
    
    # Outer envelope (lipid membrane)
    envelope = patches.Circle((cx, cy), r_env, facecolor=PINK, edgecolor=DEEP["pink"], lw=2.5)
    ax_top.add_patch(envelope)
    
    # Surface proteins (gp120 knobs)
    num_spikes = 16
    for i in range(num_spikes):
        angle = i * (2 * np.pi / num_spikes)
        sx_inner = cx + r_env * np.cos(angle)
        sy_inner = cy + r_env * np.sin(angle)
        sx_outer = cx + (r_env + 2.2) * np.cos(angle)
        sy_outer = cy + (r_env + 2.2) * np.sin(angle)
        ax_top.plot([sx_inner, sx_outer], [sy_inner, sy_outer], color=DEEP["orange"], lw=2.2)
        ax_top.plot(sx_outer, sy_outer, marker='o', markersize=5.5, color=DEEP["orange"])
        
    # Capsid (hexagonal / conical capsule)
    capsid_poly = np.array([
        [cx - 4.2, cy - 5.0],
        [cx + 4.2, cy - 5.0],
        [cx + 5.0, cy],
        [cx + 3.8, cy + 5.0],
        [cx - 3.8, cy + 5.0],
        [cx - 5.0, cy]
    ])
    capsid = patches.Polygon(capsid_poly, facecolor=CREAM, edgecolor=DEEP["blue"], lw=2.2)
    ax_top.add_patch(capsid)
    
    # Two strands of RNA (wavy lines inside capsid)
    rna_y = np.linspace(cy - 3.2, cy + 3.2, 40)
    rna_x1 = cx - 1.4 + 0.5 * np.sin(rna_y * 2.5)
    rna_x2 = cx + 1.4 + 0.5 * np.cos(rna_y * 2.5)
    ax_top.plot(rna_x1, rna_y, color=DEEP["pink"], lw=2.2)
    ax_top.plot(rna_x2, rna_y, color=DEEP["pink"], lw=2.2)
    
    # Reverse transcriptase enzymes
    rt1 = patches.Circle((cx - 1.2, cy - 1.0), 0.7, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5)
    rt2 = patches.Circle((cx + 1.2, cy + 1.0), 0.7, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5)
    ax_top.add_patch(rt1)
    ax_top.add_patch(rt2)
    
    # Labels for Virus Cross-section
    # Surface protein
    sp_x, sp_y = cx + (r_env + 2.2) * np.cos(np.pi * 0.75), cy + (r_env + 2.2) * np.sin(np.pi * 0.75)
    ax_top.annotate("Surface protein", xy=(sp_x, sp_y), xytext=(sp_x - 6, sp_y + 8),
                    fontsize=11.5, color=INK, ha="right",
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.2),
                    bbox=dict(fc="white", ec="none", pad=1))
    
    # Envelope
    env_edge_x, env_edge_y = cx + r_env * np.cos(np.pi * 0.95), cy + r_env * np.sin(np.pi * 0.95)
    ax_top.annotate("Envelope", xy=(env_edge_x, env_edge_y), xytext=(env_edge_x - 5, env_edge_y + 1),
                    fontsize=11.5, color=INK, ha="right",
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.2),
                    bbox=dict(fc="white", ec="none", pad=1))

    # Capsid (protein coat)
    ax_top.annotate("Capsid (protein coat)", xy=(cx - 4.5, cy + 2.5), xytext=(cx - 12, cy - 7),
                    fontsize=11.5, color=INK, ha="right",
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.2),
                    bbox=dict(fc="white", ec="none", pad=1))
    
    # RNA
    ax_top.annotate("RNA", xy=(cx - 0.5, cy + 2.0), xytext=(cx - 3, cy + 15),
                    fontsize=11.5, color=INK, ha="center",
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.2),
                    bbox=dict(fc="white", ec="none", pad=1))
    
    # Reverse transcriptase
    ax_top.annotate("Reverse transcriptase", xy=(cx + 1.2, cy - 1.0), xytext=(cx + 15, cy - 16),
                    fontsize=11.5, color=INK, ha="center",
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.2),
                    bbox=dict(fc="white", ec="none", pad=1))

    # --- Right: CD4 T-helper cell and infection lifecycle ---
    cell_cx, cell_cy = 72, 25
    cell_w, cell_h = 36, 36
    cell_patch = patches.FancyBboxPatch((cell_cx - cell_w/2, cell_cy - cell_h/2), cell_w, cell_h,
                                        boxstyle="round,pad=3,rounding_size=10",
                                        facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, alpha=0.6)
    ax_top.add_patch(cell_patch)
    
    # Large nucleus inside T-cell
    nuc = patches.Ellipse((cell_cx + 4, cell_cy - 1), 16, 17, facecolor=LAV, edgecolor=DEEP["lav"], lw=2, alpha=0.7)
    ax_top.add_patch(nuc)
    
    # Label cell
    ax_top.text(cell_cx + 4, cell_cy - 1, "CD4 T-helper cell", fontsize=12.5, weight="bold",
                color=INK, ha="center", va="center", bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    # Helper to draw small virus icon
    def draw_mini_virus(vx, vy, r=1.7, budding=False):
        v = patches.Circle((vx, vy), r, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.5)
        ax_top.add_patch(v)
        for ang in np.linspace(0, 2*np.pi, 8, endpoint=False):
            if budding and np.cos(ang) > 0.3:
                continue
            ax_top.plot([vx + r*np.cos(ang), vx + (r+0.8)*np.cos(ang)],
                        [vy + r*np.sin(ang), vy + (r+0.8)*np.sin(ang)],
                        color=DEEP["orange"], lw=1.4)
            ax_top.plot(vx + (r+0.8)*np.cos(ang), vy + (r+0.8)*np.sin(ang), 'o', color=DEEP["orange"], markersize=2.5)

    # 1. HIV attaching to the CD4 cell
    draw_mini_virus(52, 32)
    ax_top.plot([54.5, 54.5], [31, 33], color=DEEP["blue"], lw=2)
    
    # 2. Virus inside the cell
    draw_mini_virus(60, 22, r=1.4)
    
    # 3. New viruses budding from cell surface (placed on right side)
    draw_mini_virus(91.5, 30, r=1.7, budding=True)
    draw_mini_virus(95, 20, r=1.7)
    draw_mini_virus(89, 39, r=1.7, budding=True)
    
    # Annotation for budding positioned cleanly to the top-right
    ax_top.annotate("New viruses budding", xy=(91.5, 32), xytext=(88, 45),
                    fontsize=11.5, weight="bold", color=INK, ha="center",
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.2),
                    bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Section Headers (placed high at y=54, well clear of any labels)
    ax_top.text(18, 53.5, "HIV Virus Structure", fontsize=13, weight="bold", color=INK, ha="center")
    ax_top.text(72, 53.5, "Infection of CD4 T-Helper Cell", fontsize=13, weight="bold", color=INK, ha="center")

    # --- Subplot 2: Lower area for the progression graph ---
    ax_bot = fig.add_axes([0.10, 0.08, 0.82, 0.31])
    
    years = np.linspace(0, 11, 300)
    
    # CD4 cell count: gradual decline, sharp drop near AIDS phase
    cd4 = 1000 - 150 * np.exp(-((years - 0.6)**2) / 0.15) - 65 * years - 15 * (np.maximum(0, years - 8)**2.2)
    cd4 = np.clip(cd4, 40, 1050)
    
    # HIV in blood (viral load): high at first, drop, then rebound
    virus = 800 * np.exp(-years / 0.5) + 80 + 35 * years + 28 * (np.maximum(0, years - 7.5)**2.5)
    virus = np.clip(virus, 30, 1050)
    
    # Shaded section marked "AIDS"
    ax_bot.axvspan(8.5, 11, color=PINK, alpha=0.45)
    ax_bot.text(9.75, 520, "AIDS", fontsize=15, weight="bold", color=DEEP["pink"], ha="center", va="center")
    
    # Curves
    ax_bot.plot(years, cd4, color=DEEP["blue"], lw=3.2)
    ax_bot.plot(years, virus, color=DEEP["orange"], lw=3.2)
    
    ax_bot.set_xlim(0, 11)
    ax_bot.set_ylim(0, 1100)
    ax_bot.set_xlabel("Years after infection", fontsize=12, labelpad=6)
    ax_bot.set_ylabel("Relative concentration", fontsize=12, labelpad=6)
    
    ax_bot.set_xticks(np.arange(0, 12, 2))
    ax_bot.set_yticks([])
    
    ax_bot.spines['top'].set_visible(False)
    ax_bot.spines['right'].set_visible(False)
    ax_bot.spines['left'].set_color(GREY)
    ax_bot.spines['bottom'].set_color(GREY)
    
    # Direct curve annotations
    ax_bot.annotate("CD4 cell count", xy=(4.5, cd4[np.argmin(np.abs(years - 4.5))]),
                    xytext=(3.5, 820), fontsize=12, weight="bold", color=DEEP["blue"],
                    arrowprops=dict(arrowstyle="-", color=DEEP["blue"], lw=1.5),
                    bbox=dict(fc="white", ec="none", pad=1))
    
    ax_bot.annotate("Amount of virus", xy=(0.5, virus[np.argmin(np.abs(years - 0.5))]),
                    xytext=(1.8, 960), fontsize=12, weight="bold", color=DEEP["orange"],
                    arrowprops=dict(arrowstyle="-", color=DEEP["orange"], lw=1.5),
                    bbox=dict(fc="white", ec="none", pad=1))
    
    save(fig, out)
