# 🛡️ SOC-Level Mini SIEM System

## 📌 Abstract
This project serves as a clear, functional demonstration of how a **Security Information and Event Management (SIEM)** system operates in a real-world SOC environment. It simulates the complete lifecycle of a cyber attack detection:
1.  **Attack Simulation**: Generating malicious traffic (SSH Brute Force).
2.  **Log Collection**: Real-time monitoring of system logs.
3.  **Detection**: Analyzing patterns to identify threats.
4.  **Response**: Automatically "blocking" the attacker.
5.  **Visualization**: Displaying alerts on a live dashboard.

## 🚀 Project Structure
```
mini_siem/
├── logs/               # Stores generated logs (auth.log) and alerts
├── modules/
│   ├── log_generator.py  # Simulates valid users and attackers
│   ├── siem_engine.py    # The "Brain": Parses logs, detects attacks, fires alerts
│   └── config.py         # Configuration (Paths, Thresholds, IPs)
├── templates/
│   └── dashboard.html    # Frontend for the SOC Dashboard
├── app.py              # Flask Web Server
├── main.py             # One-click launcher for all modules
└── README.md
```

## 🛠️ How to Run
**Prerequisites**: Python 3.x installed.

1.  **Open a Terminal** in the `mini_siem` folder.
2.  **Run the Launcher**:
    ```bash
    python main.py
    ```
    *This will automatically open 3 separate console windows.*

3.  **Monitor the Dashboard**:
    Open your browser and navigate to: `http://localhost:5000`

## 🧪 Simulation Scenario
*   **Normal Traffic**: You will see occasional "Accepted" and "Failed" logins from valid users (Admin, Backup, etc.).
*   **The Attack**: Every ~30-60 seconds, the **Log Generator** will launch a "Brute Force Attack" from IP `203.0.113.88`.
*   **The Defense**:
    1.  The **SIEM Engine** detects >5 failures in <60 seconds.
    2.  It prints a **CRITICAL ALERT** to its console.
    3.  It adds the IP to the **Block List**.
    4.  The **Dashboard** updates immediately to show the Alert and the Blocked status.

## 🧠 Educational Value (Viva/Interview Keys)
*   **Log Parsing**: Uses Regex (`re` module) to extract structured data from unstructured text logs.
*   **Sliding Window**: Uses `collections.deque` to efficiently track events per IP within a specific time window.
*   **Real-Time Monitoring**: Implements a file tailing mechanism similar to `tail -f` to process logs as they are written.
*   **Architecture**: Demonstrates the decoupled nature of SIEMs (Collector -> Processor -> Storage -> UI).

## ⚠️ Disclaimer
This tool is for **EDUCATIONAL PURPOSES ONLY**. It simulates attacks locally and does not interact with real external networks or attackers.
