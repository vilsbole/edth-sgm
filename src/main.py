
from aoa import estimate_aoa_rssi

# Example Usage
P1 = -100  # dB
P2 = -98  # dB
d = 0.1  # meters (assuming d < lambda/2 for 1 GHz)
K = 200  # Calibration factor (tuned experimentally)

aio_angle = estimate_aoa_rssi(P1, P2, d, K)
print(f"Estimated AoA: {aio_angle:.2f} degrees")
