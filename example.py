from rf_units import rfconv


p_dbm = 12.5
vswr = 3.1


print(f"{p_dbm} dBm is {rfconv.dbm_to_watts(p_dbm):.3f} Watts")
print(f"{p_dbm} dBm is {rfconv.dbm_to_vrms(p_dbm):.3f} Vrms (at 50 Ohm)")
print(f"A VSWR of {vswr} has a Reflection Coefficient of {rfconv.vswr_to_rho(vswr):.3f}")
print(f"20 dB is equivalent to {rfconv.db_to_neper(20):.3f} Nepers")