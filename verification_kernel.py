import numpy as np

def ict_v11_velocity(radius_kpc, visible_mass_solar):
    # --- UNIVERSAL CONSTANTS ---
    G_GALACTIC = 4.30e-6  
    L_CONST = 1.2e-10     
    RHO_CRIT = 1e-22      
    C_INDEX = 1.5         
    
    # Conversion Factors
    KPC_TO_M = 3.086e19
    MSUN_TO_KG = 1.989e30
    KPC_TO_M3 = (KPC_TO_M)**3

    # 1. NEWTONIAN COMPONENT
    v_newton = np.sqrt((G_GALACTIC * visible_mass_solar) / radius_kpc)

    # 2. QUARTIC SCREENING (The Switch)
    vol_kpc = (4/3) * np.pi * (radius_kpc**3)
    rho_si = (visible_mass_solar / vol_kpc) * (MSUN_TO_KG / KPC_TO_M3)
    
    # Corrected Screen logic: 1 / (1 + (rho/rho_crit)^4)
    screen = 1.0 / (1.0 + (rho_si / RHO_CRIT)**4)

    # 3. ICT COMPLEXITY BOOST
    r_meters = radius_kpc * KPC_TO_M
    v_boost_kms = (np.sqrt(L_CONST * C_INDEX * r_meters) / 1000.0) * screen

    return v_newton + v_boost_kms

# Verification: Milky Way Test at 25 kpc
vm = ict_v11_velocity(25, 6.0e10)
print(f"ICT V11 Prediction at 25 kpc: {vm:.2f} km/s")
