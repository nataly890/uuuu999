from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "ok", "message": "API funcionando"})

@app.route('/test')
def test():
    return jsonify({"ciudad": "Madrid", "temp": 25, "humedad": 65})

if __name__ == '__main__':
    print("API en http://localhost:5000")
    app.run(port=5000, debug=True)
