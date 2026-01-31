import os

# Base Directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Log Paths
LOG_DIR = os.path.join(BASE_DIR, 'logs')
AUTH_LOG_PATH = os.path.join(LOG_DIR, 'auth.log')
ALERTS_LOG_PATH = os.path.join(LOG_DIR, 'alerts.log')
ALERTS_JSON_PATH = os.path.join(LOG_DIR, 'alerts.json')
STATS_JSON_PATH = os.path.join(LOG_DIR, 'stats.json')

# SIEM Rules
MAX_FAILED_LOGIN_ATTEMPTS = 5
TIME_WINDOW_SECONDS = 60

# Simulation Settings
NORMAL_ACTIVITY_DELAY = 2  # Seconds between normal logs
ATTACK_BURST_DELAY = 0.2   # Seconds between attack logs
