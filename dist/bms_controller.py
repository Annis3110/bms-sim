import csv
import os

class BMS:
    def __init__(self, pack):
        self.pack = pack
        self.fault_log_file = "fault_log.csv"
        if not os.path.exists(self.fault_log_file):
            with open(self.fault_log_file, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['Time', 'Cell', 'Fault'])

    def monitor(self, time_s):
        faults = []
        avg_soc = sum(c.soc for c in self.pack.cells) / len(self.pack.cells)
        for i, cell in enumerate(self.pack.cells):
            if cell.voltage > 4.2:
                faults.append((time_s, i, "Overvoltage"))
            elif cell.voltage < 2.5:
                faults.append((time_s, i, "Undervoltage"))
            elif cell.soc < 0.1:
                faults.append((time_s, i, "Low SOC"))
            elif cell.temp_c > 60:
                faults.append((time_s, i, "Overtemperature"))
            if cell.soc > avg_soc + 0.05:
                cell.soc -= 0.005

        with open(self.fault_log_file, 'a') as f:
            writer = csv.writer(f)
            for fault in faults:
                writer.writerow(fault)
        return faults