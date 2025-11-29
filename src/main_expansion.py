import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from cosmic_solver import da_dt, H0

# Define Time Range
SECONDS_PER_YEAR = 365.25 * 24 * 3600
BILLION_YEARS = 1e9 * SECONDS_PER_YEAR
T_SPAN = (0, 15 * BILLION_YEARS)

# Initial Condition: Present time (t=0), scale factor a=1
A_INITIAL = [1.0]

def run_simulation():
    """
    Solves the Friedmann equations and simulates cosmic expansion.
    [cite_start]This demonstrates the unified Obverse-Reverse structure [cite: 9] where the laws 
    (Reverse) [cite_start]govern the observable phenomena (Obverse)[cite: 37].
    """
    print("--- Starting Cosmic Expansion Simulation ---")
    print(f"H0 (1/s): {H0:.2e}")
    print(f"Time Range: 0 to 15 Billion Years ({T_SPAN[1]/BILLION_YEARS:.0f} Giga-years)")

    # Solve the Ordinary Differential Equation using RK45 method
    sol = solve_ivp(da_dt, T_SPAN, A_INITIAL, method='RK45', 
                    dense_output=True, rtol=1e-6, atol=1e-9)

    if sol.success:
        print("Simulation successful.")
        
        # Visualization of the results
        time_sec = sol.t
        scale_factor = sol.y[0]
        
        # Convert time to 'Years' for plotting
        time_gyr = time_sec / BILLION_YEARS
        
        plt.figure(figsize=(10, 6))
        plt.plot(time_gyr, scale_factor, label='$a(t)$ - Scale Factor')
        plt.axhline(1.0, color='gray', linestyle='--', label='Present Universe ($a=1$)')
        plt.xlabel('Time (Billions of Years)')
        plt.ylabel('Scale Factor $a(t)$')
        plt.title('Time Evolution of Scale Factor $a(t)$ ($\Lambda$CDM)')
        plt.legend()
        plt.grid(True)
        plt.savefig('cosmic_expansion_plot.png')
        print("Results saved to cosmic_expansion_plot.png.")
    else:
        print(f"Simulation failed: {sol.message}")

if __name__ == "__main__":
    run_simulation()
