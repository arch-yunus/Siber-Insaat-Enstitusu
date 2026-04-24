import numpy as np
import time

class StructuralHealthMonitor:
    """
    Real-time Structural Health Monitoring (SHM) Handler.
    Simulates sensor data ingestion and anomaly detection.
    """
    def __init__(self, threshold=0.8):
        self.threshold = threshold # Damage indication threshold

    def simulate_sensor_stream(self, duration_sec=5):
        print(f"Starting SHM stream for {duration_sec} seconds...")
        for i in range(duration_sec):
            # Simulate high-frequency vibration data (acceleration)
            vibration = np.random.normal(0, 0.5, 100)
            
            # Simulate a "Damage Event" at second 3
            if i == 3:
                vibration += np.random.uniform(1.0, 5.0, 100)
                print("[WARNING] Seismic anomaly detected at T=3s")

            damage_index = self.analyze_vibration(vibration)
            
            if damage_index > self.threshold:
                print(f"T={i}s: ALERT! Damage Index: {damage_index:.2f} (Threshold Exceeded)")
            else:
                print(f"T={i}s: Status Normal. Damage Index: {damage_index:.2f}")
            
            time.sleep(1)

    def analyze_vibration(self, signal):
        # Simplistic RMS (Root Mean Square) based anomaly detection
        rms = np.sqrt(np.mean(signal**2))
        return rms

if __name__ == "__main__":
    shm = StructuralHealthMonitor(threshold=1.5)
    shm.simulate_sensor_stream()
