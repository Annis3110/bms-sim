import numpy as np

class BatteryCell:
    def __init__(self, capacity_ah, soc=1.0, temp_c=25.0):
        self.capacity = capacity_ah
        self.soc = soc
        self.temp_c = temp_c
        self.voltage = self.compute_voltage()

    def compute_voltage(self):
        return 3.0 + 1.2 * self.soc - 0.005 * (self.temp_c - 25)

    def update(self, current_a, dt_s):
        delta_ah = (current_a * dt_s) / 3600
        self.soc = max(0.0, min(1.0, self.soc - delta_ah / self.capacity))
        self.voltage = self.compute_voltage()
        self.temp_c += 0.01 * abs(current_a)

class BatteryPack:
    def __init__(self, num_cells=4, capacity_ah=2.0):
        self.cells = [BatteryCell(capacity_ah) for _ in range(num_cells)]

    def update(self, currents, dt_s):
        for cell, current in zip(self.cells, currents):
            cell.update(current, dt_s)

    def get_state(self):
        return [(c.soc, c.voltage, c.temp_c) for c in self.cells]