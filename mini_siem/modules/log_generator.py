import time
import random
import logging
import os
from datetime import datetime
from . import config

# Ensure log directory exists
os.makedirs(config.LOG_DIR, exist_ok=True)

# Usernames and IPs for simulation
USERNAMES = ['admin', 'root', 'user', 'guest', 'backup', 'service_account']
IPS = ['192.168.1.10', '192.168.1.25', '10.0.0.5', '172.16.0.40']
ATTACKER_IP = '203.0.113.88'  # Fixed attacker IP

def get_timestamp():
    """Returns current timestamp in Linux syslog format (e.g., Jan 31 10:00:00)"""
    return datetime.now().strftime('%b %d %H:%M:%S')

def write_log(message):
    """Writes a single line to the auth.log file"""
    with open(config.AUTH_LOG_PATH, 'a') as f:
        f.write(f"{message}\n")
    print(f"[GENERATOR] Wrote: {message.strip()}")

def generate_success(user, ip):
    """Generates a successful login log entry"""
    timestamp = get_timestamp()
    log = f"{timestamp} debian-server sshd[1234]: Accepted password for {user} from {ip} port 52410 ssh2"
    write_log(log)

def generate_failed(user, ip):
    """Generates a failed login log entry"""
    timestamp = get_timestamp()
    log = f"{timestamp} debian-server sshd[1234]: Failed password for {user} from {ip} port 52410 ssh2"
    write_log(log)

def run_generator():
    print(f"[*] Starting Log Generator. Writing to {config.AUTH_LOG_PATH}...")
    
    while True:
        # 10% chance to trigger a Brute Force Attack
        if random.random() < 0.1:
            print(f"\n[!] SIMULATING BRUTE FORCE ATTACK FROM {ATTACKER_IP}...")
            # Simulate 10-20 failed attempts rapidly
            for _ in range(random.randint(10, 20)):
                user = random.choice(['root', 'admin'])
                generate_failed(user, ATTACKER_IP)
                time.sleep(config.ATTACK_BURST_DELAY)
            
            print("[*] Attack simulation ended. Resuming normal traffic.\n")
        
        else:
            # Normal traffic
            user = random.choice(USERNAMES)
            ip = random.choice(IPS)
            
            # 80% success rate for normal users
            if random.random() < 0.8:
                generate_success(user, ip)
            else:
                generate_failed(user, ip)
            
            time.sleep(config.NORMAL_ACTIVITY_DELAY)

if __name__ == "__main__":
    run_generator()
