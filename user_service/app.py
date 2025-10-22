from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(f'{app.name}_http_requests_total', 'Toplam HTTP istek sayısı')

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return jsonify({"service": f"{app.name} is running", "message": "OK"})

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)