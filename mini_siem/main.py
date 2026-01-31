import os
import sys
import threading
import time
import subprocess

def run_script(script_name):
    """Runs a python script in a subprocess"""
    print(f"[*] Launching {script_name}...")
    if sys.platform == 'win32':
        subprocess.Popen(['python', script_name], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        # For linux/mac, might want to just run in background or use multiple tabs
        subprocess.Popen(['python3', script_name])

def main():
    print("=" * 50)
    print(" Mini SIEM - Automated Launcher")
    print("=" * 50)
    print("This script will open 3 new console windows:")
    print("1. Log Generator (Simulates attacks)")
    print("2. SIEM Engine (The detection logic)")
    print("3. Dashboard (The Web Server)")
    print("\nPress Enter to start systems...")
    input()
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Start Dashboard
    dashboard_path = os.path.join(base_path, 'app.py')
    run_script(dashboard_path)
    time.sleep(2)
    
    # 2. Start Engine
    engine_path = os.path.join(base_path, 'modules', 'siem_engine.py')
    run_script(engine_path)
    time.sleep(1)

    # 3. Start Generator
    gen_path = os.path.join(base_path, 'modules', 'log_generator.py')
    run_script(gen_path)
    
    print("\n[*] All systems launched!")
    print("[*] Open your browser and go to: http://localhost:5000")
    print("[*] Watch the console windows for activity.")

if __name__ == "__main__":
    main()
