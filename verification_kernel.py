import numpy as np

def ict_v11_velocity(radius_kpc, visible_mass_solar):
    """
    ICT V11 Kernel: Calculates orbital velocity using Quartic Screening.
    Target: Milky Way Edge (25 kpc) -> ~230 km/s
    """
    # --- UNIVERSAL CONSTANTS ---
    G_GALACTIC = 4.30e-6  # kpc (km/s)^2 / M_sun [cite: 38]
    L_CONST = 1.2e-10     # Langian Constant (m/s^2) [cite: 39]
    RHO_CRIT = 1e-22      # Critical Density Threshold (kg/m^3) [cite: 40]
    C_INDEX = 1.5         # Complexity Index for barred-spiral structure 
    
    # Conversion Factors [cite: 43, 44, 45]
    KPC_TO_M = 3.086e19
    MSUN_TO_KG = 1.989e30
    KPC_TO_M3 = (KPC_TO_M)**3

    # --- 1. NEWTONIAN COMPONENT (Hardware) ---
    v_newton = np.sqrt((G_GALACTIC * visible_mass_solar) / radius_kpc) [cite: 47]

    # --- 2. QUARTIC SCREENING (The Switch) ---
    # Calculated based on spherical volume [cite: 49, 50]
    vol_kpc = (4/3) * np.pi * (radius_kpc**3)
    rho_si = (visible_mass_solar / vol_kpc) * (MSUN_TO_KG / KPC_TO_M3)
    
    # The Screen: 1 / (1 + (rho/crit)^4) [cite: 13, 52]
    # This must be ~0.99 at 25 kpc to trigger the boost.
    screen = 1.0 / (1.0 + (rho_si / RHO_CRIT)**4)

    # --- 3. ICT COMPLEXITY BOOST (The Software) ---
    r_meters = radius_kpc * KPC_TO_M [cite: 54]
    v_boost_kms = (np.sqrt(L_CONST * C_INDEX * r_meters) / 1000.0) * screen [cite: 55]

    return v_newton + v_boost_kms [cite: 56]

# Verification: Milky Way Test at 25 kpc [cite: 58]
vm = ict_v11_velocity(25, 6.0e10)
print(f"ICT V11 Prediction at 25 kpc: {vm:.2f} km/s")
