import sys
import subprocess
import os

try:
    script_path = os.path.join(os.path.dirname(__file__), "dashboard.py")
    print("Launching Streamlit dashboard...")
    subprocess.run([sys.executable, "-m", "streamlit", "run", script_path])
except Exception as e:
    print(f"Error occurred: {e}")
    input("Press Enter to exit...")
