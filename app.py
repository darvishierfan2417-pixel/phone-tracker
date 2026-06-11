from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(name)

last_data = {
    "ip": None,
    "time": None
}

@app.route('/ping', methods=['POST'])
def ping():
    ip = request.json.get('ip') or request.headers.get('X-Forwarded-For', request.remote_addr)
    last_data['ip'] = ip
    last_data['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"status": "ok"})

@app.route('/')
def index():
    return render_template('index.html', data=last_data)

if name == 'main':
    app.run(host='0.0.0.0', port=5000)
