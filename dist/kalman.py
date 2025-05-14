class KalmanSOC:
    def __init__(self, initial_soc=1.0):
        self.soc = initial_soc
        self.P = 1.0

    def update(self, current, dt, measured_voltage):
        R = 0.01
        Q = 0.001

        delta_soc = -(current * dt) / (3600 * 2.0)
        self.soc += delta_soc
        self.P += Q

        expected_voltage = 3.0 + 1.2 * self.soc
        K = self.P / (self.P + R)
        self.soc += K * (measured_voltage - expected_voltage) / 1.2
        self.P *= (1 - K)

        return max(0.0, min(1.0, self.soc))