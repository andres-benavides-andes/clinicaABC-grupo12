import os
import firebase_admin
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_jwt_extended import get_jwt
from flask_jwt_extended import current_user
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
    return "Microservicio para crear las citas"

@app.route("/crear-cita", methods=["POST"])
@jwt_required()
def crear():
    claims = get_jwt()
    id_paciente = claims["id_paciente"]
    content = request.json
    cita = {
        u'especialidad': content['especialidad'],
        u'fecha': content['fecha'],
        u'hora': content['hora'],
        u'id_paciente': id_paciente
    }
    db.collection(u'citas').add(cita)
    return jsonify({"mensaje":"cita creada con éxito"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))