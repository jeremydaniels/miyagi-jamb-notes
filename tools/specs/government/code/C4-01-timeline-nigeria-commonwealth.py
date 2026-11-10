from style import *
import numpy as np

def draw(out):
    fig = canvas(12, 6.5)
    ax = fig.add_subplot(111)
    
    # Hide standard axes
    ax.axis("off")
    ax.set_xlim(1955, 2008)
    ax.set_ylim(-3.8, 4.0)
    
    # Title
    ax.text(
        1981.5, 3.5,
        "Nigeria's Involvement in the Commonwealth",
        ha="center", va="center",
        fontsize=18, fontweight="bold", color=INK
    )
    
    # Main timeline axis
    timeline_y = 0.0
    ax.annotate(
        "",
        xy=(2007.5, timeline_y),
        xycoords="data",
        xytext=(1956.5, timeline_y),
        textcoords="data",
        arrowprops=dict(
            arrowstyle="->,head_width=0.4,head_length=0.6",
            color=INK,
            lw=2.5
        )
    )
    
    events = [
        {
            "year": 1960,
            "desc": "Joined at\nindependence",
            "color": DEEP["green"],
            "side": 1,
            "h": 1.2
        },
        {
            "year": 1990,
            "desc": "Emeka Anyaoku becomes\nSecretary-General",
            "color": DEEP["blue"],
            "side": -1,
            "h": 1.2
        },
        {
            "year": 1995,
            "desc": "Suspended under military rule\nover human rights abuses",
            "color": DEEP["pink"],
            "side": 1,
            "h": 1.9
        },
        {
            "year": 1999,
            "desc": "Readmitted after\nreturn to democracy",
            "color": DEEP["green"],
            "side": -1,
            "h": 1.9
        },
        {
            "year": 2003,
            "desc": "Hosted CHOGM\nin Abuja",
            "color": DEEP["orange"],
            "side": 1,
            "h": 0.5
        }
    ]
    
    for ev in events:
        x = ev["year"]
        side = ev["side"]
        stem_top = side * ev["h"]
        
        # Stem line
        ax.plot([x, x], [timeline_y, stem_top], color=ev["color"], lw=2, linestyle="--")
        
        # Dot on main timeline
        ax.plot(x, timeline_y, marker="o", markersize=9, color=ev["color"], zorder=4)
        ax.plot(x, timeline_y, marker="o", markersize=5, color="white", zorder=5)
        
        # Year pill / badge
        badge_y = stem_top + (0.15 if side > 0 else -0.15)
        va_badge = "bottom" if side > 0 else "top"
        ax.text(
            x, badge_y, f" {x} ",
            ha="center", va=va_badge,
            fontsize=15, fontweight="bold", color="white",
            bbox=dict(boxstyle="round,pad=0.25", fc=ev["color"], ec="none")
        )
        
        # Event description box
        box_y = badge_y + (0.45 if side > 0 else -0.45)
        va_box = "bottom" if side > 0 else "top"
        
        ax.text(
            x, box_y,
            ev["desc"],
            ha="center", va=va_box,
            fontsize=14, color=INK,
            bbox=dict(
                boxstyle="round,pad=0.35",
                fc="white",
                ec=ev["color"],
                lw=1.5
            )
        )
        
    save(fig, out)
