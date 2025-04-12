from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import uuid

app = Flask(__name__, static_folder='static')
CORS(app)  # 🔥 Activa CORS para permitir conexiones desde el frontend (Vercel)

# Base de datos en memoria
requests_db = {}

@app.route("/create-request", methods=["POST"])
def create_request():
    data = request.get_json()
    req_id = str(uuid.uuid4())
    requests_db[req_id] = {
        "id": req_id,
        "song": data.get("song"),
        "dedication": data.get("dedication"),
        "dj": data.get("dj"),
        "paid": False
    }
    return jsonify({"request_id": req_id})

@app.route("/requests", methods=["GET"])
def get_requests():
    dj = request.args.get("dj")
    if dj:
        filtered = [r for r in requests_db.values() if r["dj"] == dj]
        return jsonify(filtered)
    return jsonify(list(requests_db.values()))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)
