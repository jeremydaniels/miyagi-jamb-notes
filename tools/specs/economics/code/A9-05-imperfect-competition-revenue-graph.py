from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    
    # Axes setup
    axes_clean(ax, "Quantity", "Revenue / Price", 10, 10)
    
    # Starting vertical intercept
    a = 8.5
    
    # AR curve: P = a - b*Q
    # Let b = 0.8 -> AR reaches 0 at Q = 8.5 / 0.8 = 10.625
    # MR curve: MR = a - 2*b*Q -> reaches 0 at Q = 8.5 / 1.6 = 5.3125
    b = 0.8
    
    q_ar = np.linspace(0, 9.5, 200)
    ar = a - b * q_ar
    
    q_mr = np.linspace(0, 5.8, 200)
    mr = a - 2 * b * q_mr
    
    # Plot lines
    ax.plot(q_ar, ar, color=DEEP["blue"], lw=3.5)
    ax.plot(q_mr, mr, color=DEEP["orange"], lw=3.5)
    
    # Dash the MR line below axis to indicate continuation
    q_mr_neg = np.linspace(5.3125, 6.5, 50)
    mr_neg = a - 2 * b * q_mr_neg
    ax.plot(q_mr_neg, mr_neg, color=DEEP["orange"], lw=2.5, linestyle="--", alpha=0.7)
    
    # Labels for curves
    ax.text(8.8, a - b * 8.8 + 0.3, "AR = Price = Demand", 
            fontsize=15, color=DEEP["blue"], weight="bold",
            ha="left", va="bottom",
            bbox=dict(fc="white", ec="none", pad=2))
            
    ax.text(4.8, a - 2 * b * 4.8 + 0.5, "MR", 
            fontsize=15, color=DEEP["orange"], weight="bold",
            ha="left", va="bottom",
            bbox=dict(fc="white", ec="none", pad=2))
            
    # Highlight the shared vertical intercept
    ax.plot(0, a, 'o', color=INK, markersize=6)
    
    # Optional annotation indicating MR bisects the distance to AR
    # or slopes twice as fast
    ax.annotate("MR falls twice as\nfast as AR", 
                xy=(2.8, a - 2 * b * 2.8), 
                xytext=(1.2, 2.0),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                ha="center", 
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
                
    # Title
    ax.set_title("Revenue Under Imperfect Competition", fontsize=16, color=INK, pad=15, weight="bold")
    
    save(fig, out)
