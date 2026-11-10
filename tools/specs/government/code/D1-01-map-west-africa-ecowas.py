from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def draw(out):
    # Generous vertical space to completely separate title and map
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    
    # Configure axes limits to frame West Africa with sufficient headroom and padding
    ax.set_xlim(-19.0, 16.5)
    ax.set_ylim(2.5, 27.5)
    ax.set_aspect("equal")
    ax.axis("off")
    
    # Official 15 ECOWAS members
    ecowas_names = [
        "Benin", "Burkina Faso", "Cape Verde", "Cabo Verde", "Côte d'Ivoire", "Ivory Coast",
        "Gambia", "The Gambia", "Ghana", "Guinea", "Guinea-Bissau",
        "Liberia", "Mali", "Niger", "Nigeria", "Senegal", "Sierra Leone", "Togo"
    ]
    
    # Surrounding non-ECOWAS countries
    non_ecowas_names = [
        "Mauritania", "Algeria", "Chad", "Cameroon", "Central African Republic",
        "Equatorial Guinea", "Gabon", "Republic of the Congo", "Libya", "Morocco",
        "Western Sahara"
    ]
    
    # Draw surrounding countries
    surrounding_polys = country_polys(*non_ecowas_names)
    for poly in surrounding_polys:
        coords = np.array(poly)
        ax.fill(coords[:, 0], coords[:, 1], color=GREY, alpha=0.35, zorder=1)
        ax.plot(coords[:, 0], coords[:, 1], color="white", lw=1.2, zorder=2)
        
    # Draw ECOWAS countries
    ecowas_polys = country_polys(*ecowas_names)
    for poly in ecowas_polys:
        coords = np.array(poly)
        ax.fill(coords[:, 0], coords[:, 1], color=GREEN, alpha=0.85, zorder=3)
        ax.plot(coords[:, 0], coords[:, 1], color=DEEP["green"], lw=1.2, zorder=4)
        
    # Title placed high with white bbox to avoid any overlap with northern Mali / Algeria border
    ax.text(
        -18.0, 26.8, "Economic Community of West African States (ECOWAS)",
        fontsize=16, weight="bold", color=INK, ha="left", va="top",
        bbox=dict(fc="white", ec="none", pad=3.0)
    )
    
    # Legend with explicit spacing and clear labels to prevent any text collisions
    legend_elements = [
        Patch(facecolor=GREEN, edgecolor=DEEP["green"], label="ECOWAS Member States", alpha=0.85),
        Patch(facecolor=GREY, edgecolor="none", label="Surrounding Countries", alpha=0.35)
    ]
    ax.legend(
        handles=legend_elements,
        loc="lower left",
        bbox_to_anchor=(0.04, 0.08),
        frameon=True,
        facecolor="white",
        edgecolor=GREY,
        fontsize=14,
        framealpha=0.95,
        borderpad=1.0,
        labelspacing=1.2,
        handlelength=1.8,
        handleheight=1.2
    )
    
    # Small note / caption
    ax.text(
        15.8, 3.2, "Sketch map: zones are approximate",
        fontsize=14, color=INK, ha="right", va="bottom", style="italic",
        bbox=dict(fc="white", ec="none", pad=2.0)
    )
    
    save(fig, out)
