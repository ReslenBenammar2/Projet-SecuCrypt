from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
import os
import sys
import webbrowser

# Obtenir le chemin du dossier contenant le script ou le .exe
base_path = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__))

# Construire le chemin vers Untitled-1.html
html_path = os.path.join(base_path, 'login.html')

# Créer l'URL locale
url = f"file:///{html_path}"

# Ouvrir dans le navigateur
webbrowser.open(url)
app = Flask(__name__, static_folder='public')
CORS(app)

# Connexion MongoDB Atlas
uri = "mongodb+srv://reslen:0000@cluster0.ioe1o5g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client['cryptage']
users = db['users']

# Route pour servir le HTML
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'login.html')

# Inscription
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({ "message": "Email et mot de passe sont requis." }), 400

    if users.find_one({ "email": email }):
        return jsonify({ "message": "Cet email est déjà utilisé." }), 409

    users.insert_one({ "email": email, "password": password })
    return jsonify({ "message": "Inscription réussie !" }), 201

# Connexion
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = users.find_one({ "email": email, "password": password })
    if user:
        return jsonify({ "message": "Connexion réussie" }), 200
    else:
        return jsonify({ "message": "Email ou mot de passe invalide" }), 401

if __name__ == '__main__':
    app.run(port=3000)
