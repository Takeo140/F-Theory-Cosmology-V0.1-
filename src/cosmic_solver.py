import numpy as np
from scipy.constants import G, c, parsec, year

# Define Physical Constants and Current Cosmological Parameters
# H0: Hubble Constant (70 km/s/Mpc)
H0_per_Mpc = 70.0 * 1000  # m/s/Mpc

# Convert Mpc to m
Mpc_to_m = parsec * 1e6

# H0 in SI units (1/s)
H0 = H0_per_Mpc / Mpc_to_m 

# Density Parameters (Obverse: Psi_phys input)
# [cite_start]Includes dark matter and dark energy [cite: 16]
OMEGA_M_0 = 0.31  # Matter Density Parameter
OMEGA_L_0 = 0.69  # Dark Energy Density Parameter (Λ term)

def get_friedmann_rhs(a, H0, omega_m0, omega_l0):
    """
    Calculates the Right Hand Side (RHS) of the Friedmann Equation.
    [cite_start]This equation is the specific realization of the Reverse (Psi_math)[cite: 18, 25].
    
    H^2 = (a_dot / a)^2 = H0^2 * [Omega_m,0 * a^-3 + Omega_L,0]
    
    Arguments:
        a (float): Scale factor a(t)
        H0 (float): Hubble constant (1/s)
        omega_m0 (float): Matter density parameter
        omega_l0 (float): Dark energy density parameter
        
    Returns:
        float: (a_dot / a)^2
    """
    # Matter density dependence: a^-3
    rho_matter_term = omega_m0 * a**(-3)
    
    # Dark Energy (Lambda) density dependence: a^0
    rho_lambda_term = omega_l0
    
    # Assuming flat universe (k=0)
    
    H_squared = H0**2 * (rho_matter_term + rho_lambda_term)
    
    return H_squared

def da_dt(t, a):
    """
    Calculates the time derivative of the scale factor, da/dt.
    
    da/dt = a * H = a * sqrt(H^2)
    
    Arguments:
        t (float): Time
        a (float): Scale factor
        
    Returns:
        float: da/dt
    """
    # Calculate H^2 using the Obverse parameters
    H_squared = get_friedmann_rhs(a, H0, OMEGA_M_0, OMEGA_L_0)
    
    # H = sqrt(H^2)
    H = np.sqrt(H_squared)
    
    # da/dt
    return a * H
