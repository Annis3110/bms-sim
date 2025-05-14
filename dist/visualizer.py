import pandas as pd

def to_dataframe(log, num_cells):
    cols = ["Time"]
    for i in range(num_cells):
        cols += [f"Cell{i+1}_SOC", f"Cell{i+1}_SOC_Est", f"Cell{i+1}_V", f"Cell{i+1}_Temp"]
    return pd.DataFrame(log, columns=cols)

def load_fault_log():
    return pd.read_csv("fault_log.csv")