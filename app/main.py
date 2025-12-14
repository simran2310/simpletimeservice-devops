from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

def get_client_ip():
    xff = request.headers.get('X-Forwarded-For')
    if xff:
        return xff.split(',')[0].strip()
    return request.remote_addr

@app.route("/")
def root():
    return jsonify({
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "ip": get_client_ip()
    })

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
