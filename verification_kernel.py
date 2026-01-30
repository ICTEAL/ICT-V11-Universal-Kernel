import numpy as np

def ict_v11_velocity(radius_kpc, visible_mass_solar):
    # --- UNIVERSAL CONSTANTS ---
    G_GALACTIC = 4.30e-6 
    L_CONST = 1.2e-10     
    RHO_CRIT = 1.0e-22    
    C_INDEX = 1.5         
    
    # Unit Conversions
    KPC_TO_M = 3.086e19
    MSUN_TO_KG = 1.989e30

    # 1. NEWTONIAN COMPONENT (The Hardware)
    v_newton = np.sqrt((G_GALACTIC * visible_mass_solar) / radius_kpc)

    # 2. QUARTIC SCREENING (The Switch)
    # Convert all units to SI (meters/kg) before calculating density
    r_meters = radius_kpc * KPC_TO_M
    m_kg = visible_mass_solar * MSUN_TO_KG
    vol_m3 = (4.0 / 3.0) * np.pi * (r_meters**3)
    rho_si = m_kg / vol_m3
    
    # The Screening Factor: Must approach 1.0 at 25 kpc to engage ICT
    # Corrected formula for unit parity
    screen = 1.0 / (1.0 + (rho_si / RHO_CRIT)**4)

    # 3. ICT COMPLEXITY BOOST (The Software)
    v_boost_ms = np.sqrt(L_CONST * C_INDEX * r_meters) * screen
    v_boost_kms = v_boost_ms / 1000.0

    return v_newton + v_boost_kms

# Verification: Milky Way Test at 25 kpc
# Observed visible mass ~6.0e10 M_sun
vm = ict_v11_velocity(25, 6.0e10)
print(f"ICT V11 Prediction at 25 kpc: {vm:.2f} km/s")
