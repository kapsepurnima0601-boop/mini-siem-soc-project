import time
import re
import json
import logging
import os
from collections import defaultdict, deque
from datetime import datetime
from . import config

# Clean start: remove old stats
if os.path.exists(config.STATS_JSON_PATH):
    os.remove(config.STATS_JSON_PATH)
if os.path.exists(config.ALERTS_JSON_PATH):
    os.remove(config.ALERTS_JSON_PATH)

# Global State
failed_attempts = defaultdict(deque)  # Store timestamps of failures per IP
blocked_ips = set()
alerts_history = []
total_events_processed = 0

# Regex for parsing sshd logs
# Example: Jan 31 10:00:00 debian-server sshd[1234]: Failed password for root from 192.168.1.10 port 52410 ssh2
LOG_PATTERN = re.compile(
    r'(?P<timestamp>[A-Za-z]{3}\s+\d+\s+\d+:\d+:\d+)\s+'
    r'(?P<hostname>\S+)\s+'
    r'sshd\[\d+\]:\s+'
    r'(?P<status>Failed|Accepted)\s+password\s+for\s+'
    r'(?P<user>\S+)\s+from\s+'
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+'
)

def update_stats():
    """Updates the shared stats.json for the dashboard"""
    stats = {
        'total_events': total_events_processed,
        'blocked_ips': list(blocked_ips),
        'alerts_count': len(alerts_history)
    }
    # Write atomic update simulation (simple overwrite for this demo)
    with open(config.STATS_JSON_PATH, 'w') as f:
        json.dump(stats, f)
    
    # Also dump alerts
    with open(config.ALERTS_JSON_PATH, 'w') as f:
        json.dump(alerts_history[-10:], f) # Keep last 10 for dashboard

def trigger_alert(ip, attempts):
    """Triggers a security alert"""
    if ip in blocked_ips:
        return  # Already blocked

    alert = {
        'id': len(alerts_history) + 1,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'type': 'Brute Force Attempt',
        'source_ip': ip,
        'attempts': attempts,
        'status': 'BLOCKED',
        'severity': 'HIGH'
    }
    
    alerts_history.append(alert)
    blocked_ips.add(ip)
    
    # 1. Console Output
    print(f"\n[!!!] ALERT TRIGGERED: Brute Force Detected from {ip}")
    print(f"      Action: IP {ip} has been BLOCKED by Firewall.")
    print("-" * 50)
    
    # 2. Log to File
    with open(config.ALERTS_LOG_PATH, 'a') as f:
        f.write(json.dumps(alert) + "\n")
    
    update_stats()

def process_log(line):
    """Parses and analyzes a single log line"""
    global total_events_processed
    match = LOG_PATTERN.search(line)
    
    if not match:
        return

    total_events_processed += 1
    data = match.groupdict()
    ip = data['ip']
    status = data['status']
    current_time = time.time()

    if status == 'Failed':
        # Add current failure timestamp
        failed_attempts[ip].append(current_time)
        
        # Clean up old attempts (outside time window)
        while failed_attempts[ip] and failed_attempts[ip][0] < current_time - config.TIME_WINDOW_SECONDS:
            failed_attempts[ip].popleft()
            
        # Check Condition
        if len(failed_attempts[ip]) > config.MAX_FAILED_LOGIN_ATTEMPTS:
            trigger_alert(ip, len(failed_attempts[ip]))
            
    elif status == 'Accepted':
        # Optional: Reset failure count on success? 
        # For strict security, we often don't reset immediately to catch "low and slow" attacks, 
        # but for this simple demo, we can verify if a blocked IP tries to login (it shouldn't).
        if ip in blocked_ips:
            print(f"[!] WARNING: Blocked IP {ip} managed to login! (Simulation Artifact)")
            
    if total_events_processed % 10 == 0:
        update_stats()

def tail_logs(filepath):
    """Generator that yields new lines from a file"""
    # Create file if not exists
    if not os.path.exists(filepath):
        print(f"[*] Waiting for {filepath} to be created...")
        while not os.path.exists(filepath):
            time.sleep(1)
            
    print(f"[*] Monitoring {filepath}...")
    with open(filepath, 'r') as f:
        # Move to end of file
        f.seek(0, os.SEEK_END)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line

def run_engine():
    print("[*] SIEM Engine Started.")
    print(f"[*] Rules: > {config.MAX_FAILED_LOGIN_ATTEMPTS} attempts in {config.TIME_WINDOW_SECONDS}s")
    
    # Initialize stats
    update_stats()
    
    try:
        for line in tail_logs(config.AUTH_LOG_PATH):
            process_log(line)
    except KeyboardInterrupt:
        print("\n[*] Stopping SIEM Engine.")

if __name__ == "__main__":
    run_engine()
