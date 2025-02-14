import numpy as np

def estimate_aoa_rssi(P1_dB, P2_dB, d, K=1.0):
    """
    Estimate Angle of Arrival (AoA) using signal strength (RSSI).

    Parameters:
        P1_dB (float): Received signal strength at antenna 1 (dB)
        P2_dB (float): Received signal strength at antenna 2 (dB)
        d (float): Distance between the two antennas (meters)
        K (float): Calibration factor (default = 1.0)

    Returns:
        float: Estimated angle of arrival (degrees)
    """
    delta_P = P1_dB - P2_dB  # Difference in received power levels

    print(delta_P, (K * d), delta_P / (K * d))

    try:
        theta_rad = np.arcsin(delta_P / (K * d))  # Compute angle in radians
        theta_deg = np.degrees(theta_rad)  # Convert to degrees
    except ValueError:
        theta_deg = np.sign(delta_P) * 90  # If out of domain, assume max angle

    return theta_deg
