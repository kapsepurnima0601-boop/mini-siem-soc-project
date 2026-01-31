🔐 Mini SIEM – SOC-Level Cyber Security Project

🚀 A Python-based Mini SIEM (Security Information and Event Management) system that simulates real-world SOC (Security Operations Center) workflows used by enterprises to detect and respond to cyber attacks.

This project focuses on brute-force SSH attack detection, centralized log analysis, alert generation, and SOC analyst response simulation.

🧠 What This Project Demonstrates

✅ How organizations collect and analyze authentication logs
✅ How brute-force attacks are detected using correlation rules
✅ How SOC analysts receive alerts and take response actions
✅ How security events are visualized using a dashboard

💡 Designed for students, SOC analyst aspirants, and cyber security portfolios

🏗️ System Components

🔹 Log Generator – Simulates Linux auth.log with normal & attack traffic
🔹 Log Collector – Monitors logs in real time (Filebeat-like behavior)
🔹 Detection Engine – Identifies brute-force attacks using rule-based logic
🔹 Alert Manager – Generates and stores security alerts
🔹 SOC Response Module – Simulates blocking malicious IPs
🔹 Web Dashboard – Displays alerts and attack details

🚨 Detection Logic

⚠️ A brute-force attack is detected when:

❌ More than 5 failed login attempts

🌐 From the same IP address

⏱️ Within 1 minute

An alert is generated with severity, timestamp, source IP, and attack type.

🛠️ Tech Stack

🧑‍💻 Language: Python 3
🌐 Framework: Flask
📄 Data Format: JSON
🔐 Domain: Cyber Security / SOC / SIEM
🖥️ Environment: Linux-style authentication logs

▶️ How to Run
pip install -r requirements.txt
python main.py


🌍 Open browser and visit:

http://127.0.0.1:5000

💼 Real-World Use Case

🏢 This project simulates how banks, IT companies, and SOC teams monitor authentication logs, detect suspicious activity, and respond to cyber threats in real time.

🎯 Ideal for:

SOC Analyst roles

Cyber Security internships

Final-year projects

GitHub portfolios

🚀 Future Enhancements

✨ ELK Stack integration (Elasticsearch, Logstash, Kibana)
✨ Email / SMS alert notifications
✨ Machine Learning–based anomaly detection
✨ Firewall auto-blocking integration

👩‍💻 Author

Purnima Kapse
🔐 Cyber Security Enthusiast | SOC Analyst Aspirant
