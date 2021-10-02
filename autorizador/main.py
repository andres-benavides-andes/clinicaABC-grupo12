import os
import firebase_admin
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_jwt_extended import create_access_token
from firebase_admin import credentials
from firebase_admin import firestore
import json

app= Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "gurpo_12_arquitectura_agil"
jwt = JWTManager(app)

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
'projectId': 'miso-arquitectura-325522',
})
db = firestore.client()


@app.route("/", methods=["GET"])
def home():
    return "Microservicio para generar los tokens de autorizacion"

@app.route("/generar-token", methods=["POST"])
def token():
    username = request.json.get("usuario", None)
    password = request.json.get("password", None)
    # Obtener referencia a los usuarios de la BD
    usuario_ref = db.collection(u'usuarios').document(username)
    usuario = usuario_ref.get()
    if not usuario.exists:
        return jsonify({"error": "Usuario no existe"}), 401
    else:
        usuarioData = usuario.to_dict()
        if (usuarioData.get('password') != password) :
            return jsonify({"error": "Contraseña incorrecta"}), 401
        additional_claims = {"profile": usuarioData.get('profile'), "id_paciente":usuarioData.get('id_paciente') }  
        access_token = create_access_token(identity=usuarioData.get('id_paciente'), additional_claims=additional_claims)
        return jsonify(access_token=access_token)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))