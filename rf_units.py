import numpy as np

class rfconv:
    """
    A class for common RF Engineering unit conversions.
    """
    
    @staticmethod
    def dbm_to_dbw(dbm):
        """Converts dBm to dBW."""
        return dbm - 30

    @staticmethod
    def dbm_to_watts(dbm):
        """Converts dBm to Watts."""
        return 10**((dbm - 30) / 10)

    @staticmethod
    def watts_to_dbm(watts):
        """Converts Watts to dBm."""
        if watts <= 0:
            raise ValueError("Power in Watts must be greater than zero.")
        return 10 * np.log10(watts) + 30

    @staticmethod
    def dbm_to_vrms(dbm, z0=50):
        """
        Converts dBm to Root Mean Square Voltage (Vrms).
        Default impedance is 50 Ohms.
        """
        watts = rfconv.dbm_to_watts(dbm)
        return np.sqrt(watts * z0)

    @staticmethod
    def vswr_to_rho(vswr):
        """Converts VSWR to Reflection Coefficient (Magnitude)."""
        if vswr < 1:
            raise ValueError("VSWR cannot be less than 1.")
        return (vswr - 1) / (vswr + 1)

    @staticmethod
    def rho_to_vswr(rho):
        """Converts Reflection Coefficient magnitude (rho) to VSWR."""
        if rho >= 1:
            return float('inf')
        return (1 + rho) / (1 - rho)

    @staticmethod
    def db_to_neper(db):
        """
        Converts Decibels to Nepers.
        Based on the relationship: 1 Np ≈ 8.686 dB
        """
        return db / (20 / np.log(10))

    @staticmethod
    def neper_to_db(neper):
        """Converts Nepers to Decibels."""
        return neper * (20 / np.log(10))