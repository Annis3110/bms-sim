import streamlit as st
from battery_model import BatteryPack
from bms_controller import BMS
from kalman import KalmanSOC
from simulation import run_simulation
from visualizer import to_dataframe, load_fault_log

num_cells = 4
pack = BatteryPack(num_cells)
bms = BMS(pack)
kalman_estimators = [KalmanSOC() for _ in range(num_cells)]
duration = 300
current_profile = [[0.5 if i % 60 < 30 else -0.2] * num_cells for i in range(duration)]

log = run_simulation(pack, bms, kalman_estimators, current_profile)
df = to_dataframe(log, num_cells)
fault_df = load_fault_log()

st.title("🔋 Advanced BMS Simulation Dashboard")
st.line_chart(df.set_index("Time")[[f"Cell{i+1}_SOC" for i in range(num_cells)]])
st.line_chart(df.set_index("Time")[[f"Cell{i+1}_V" for i in range(num_cells)]])
st.line_chart(df.set_index("Time")[[f"Cell{i+1}_Temp" for i in range(num_cells)]])
st.dataframe(fault_df)
st.success("Simulation complete.")