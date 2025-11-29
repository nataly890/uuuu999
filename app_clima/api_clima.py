from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"mensaje": "API Clima funcionando"})

@app.route('/clima/<ciudad>')
def obtener_clima(ciudad):
    return jsonify({
        "ciudad": ciudad,
        "temperatura": 25,
        "humedad": 65,
        "viento": 12,
        "presion": 1013,
        "descripcion": "Soleado",
        "pais": "ES"
    })

@app.route('/ciudades')
def ciudades():
    return jsonify({
        "Europa": ["Madrid", "Barcelona", "Paris", "London"],
        "America": ["New York", "Mexico City", "Buenos Aires"]
    })

if __name__ == '__main__':
    print("API corriendo en http://localhost:5000")
    app.run(debug=True, port=5000)
