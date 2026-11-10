from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(11, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1.9, 2.2)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.axis('off')

    R = 1.0

    # In standard textbook diagrams of climatic zones, latitudes are spaced linearly along the vertical axis (y = lat / 90 * R)
    # or proportionally, so polar caps (66.5° to 90°) have substantial height and are clearly visible and demarcated.
    # Using linear vertical projection:
    lat_deg = {
        'north_pole': 90.0,
        'arctic': 66.5,
        'cancer': 23.5,
        'equator': 0.0,
        'capricorn': -23.5,
        'antarctic': -66.5,
        'south_pole': -90.0
    }
    
    y_vals = {k: (v / 90.0) * R for k, v in lat_deg.items()}

    def get_slice_polygon(y_low, y_high, n=300):
        # Sample boundary along the circle x^2 + y^2 = R^2
        y_pts = np.linspace(y_low, y_high, n)
        x_right = np.sqrt(np.maximum(0, R**2 - y_pts**2))
        x_left = -x_right
        xs = np.concatenate([x_right, x_left[::-1]])
        ys = np.concatenate([y_pts, y_pts[::-1]])
        return xs, ys

    # Shading zones
    # Frigid zones (shaded blue)
    xs_nf, ys_nf = get_slice_polygon(y_vals['arctic'], y_vals['north_pole'])
    ax.fill(xs_nf, ys_nf, color=BLUE, alpha=0.6, ec='none')

    xs_sf, ys_sf = get_slice_polygon(y_vals['south_pole'], y_vals['antarctic'])
    ax.fill(xs_sf, ys_sf, color=BLUE, alpha=0.6, ec='none')

    # Temperate zones (shaded green)
    xs_nt, ys_nt = get_slice_polygon(y_vals['cancer'], y_vals['arctic'])
    ax.fill(xs_nt, ys_nt, color=GREEN, alpha=0.6, ec='none')

    xs_st, ys_st = get_slice_polygon(y_vals['antarctic'], y_vals['capricorn'])
    ax.fill(xs_st, ys_st, color=GREEN, alpha=0.6, ec='none')

    # Torrid zone (shaded red/pink)
    xs_tz, ys_tz = get_slice_polygon(y_vals['capricorn'], y_vals['cancer'])
    ax.fill(xs_tz, ys_tz, color=PINK, alpha=0.7, ec='none')

    # Draw Earth outer circle
    full_theta = np.linspace(0, 2 * np.pi, 500)
    ax.plot(R * np.cos(full_theta), R * np.sin(full_theta), color=INK, lw=2.2)

    # Latitude lines (dashed) inside the globe
    lines_info = [
        ('Arctic Circle', '66.5° N', y_vals['arctic']),
        ('Tropic of Cancer', '23.5° N', y_vals['cancer']),
        ('Equator', '0°', y_vals['equator']),
        ('Tropic of Capricorn', '23.5° S', y_vals['capricorn']),
        ('Antarctic Circle', '66.5° S', y_vals['antarctic']),
    ]

    for name, deg, y in lines_info:
        x_edge = np.sqrt(max(0.0, R**2 - y**2))
        # Draw horizontal dashed line across the globe
        ax.plot([-x_edge, x_edge], [y, y], color=INK, lw=1.8, ls='--', dashes=(6, 3), zorder=3)
        
        # Pointer or guide tick line to label
        ax.plot([x_edge, 1.08], [y, y], color=GREY, lw=1.2, ls=':')

        # Right label (Line name and degrees)
        label_text = f"{name} ({deg})"
        ax.text(1.12, y, label_text, va='center', ha='left', fontsize=14, color=INK,
                bbox=dict(boxstyle="square,pad=0.15", fc="white", ec="none", alpha=0.85))

    # Zone labels inside the bands
    # Exact prompt labels: "Frigid Zone", "North Temperate Zone", "Torrid Zone", "South Temperate Zone", "Frigid Zone"
    y_nf_center = (y_vals['north_pole'] + y_vals['arctic']) / 2.0
    ax.text(0, y_nf_center, "Frigid Zone",
            va='center', ha='center', fontsize=14, fontweight='bold', color=INK,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=DEEP["blue"], lw=1.2, alpha=0.9))

    y_nt_center = (y_vals['arctic'] + y_vals['cancer']) / 2.0
    ax.text(0, y_nt_center, "North Temperate Zone",
            va='center', ha='center', fontsize=15, fontweight='bold', color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP["green"], lw=1.2, alpha=0.9))

    y_torrid_center = (y_vals['cancer'] + y_vals['capricorn']) / 2.0
    ax.text(0, y_torrid_center, "Torrid Zone",
            va='center', ha='center', fontsize=16, fontweight='bold', color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["pink"], lw=1.2, alpha=0.9))

    y_st_center = (y_vals['capricorn'] + y_vals['antarctic']) / 2.0
    ax.text(0, y_st_center, "South Temperate Zone",
            va='center', ha='center', fontsize=15, fontweight='bold', color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP["green"], lw=1.2, alpha=0.9))

    y_sf_center = (y_vals['antarctic'] + y_vals['south_pole']) / 2.0
    ax.text(0, y_sf_center, "Frigid Zone",
            va='center', ha='center', fontsize=14, fontweight='bold', color=INK,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=DEEP["blue"], lw=1.2, alpha=0.9))

    # Title
    ax.text(0, 1.18, "Greek Climatic Zones of the Earth", ha='center', va='center',
            fontsize=17, fontweight='bold', color=INK)

    save(fig, out)
