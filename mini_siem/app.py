from flask import Flask, render_template, jsonify
import json
import os
from modules import config

app = Flask(__name__, template_folder='templates')

def load_json(filepath, default_value):
    if not os.path.exists(filepath):
        return default_value
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return default_value

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/stats')
def get_stats():
    stats = load_json(config.STATS_JSON_PATH, {
        'total_events': 0, 'blocked_ips': [], 'alerts_count': 0
    })
    return jsonify(stats)

@app.route('/api/alerts')
def get_alerts():
    alerts = load_json(config.ALERTS_JSON_PATH, [])
    return jsonify(alerts)

if __name__ == "__main__":
    print("[*] Starting Dashboard on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
