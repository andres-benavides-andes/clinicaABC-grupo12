import os
import firebase_admin
from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_jwt_extended import get_jwt
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
    return "Microservicio para consultar las citas"

@app.route("/consulta-citas", methods=["GET"])
@jwt_required()
def consulta():
    # id_paciente = request.args.get('id_paciente', type=int)
    claims = get_jwt()
    id_paciente = claims["id_paciente"]
    perfil = claims["profile"]
    citasResponse = []
    if perfil == 0:
        citas_ref = db.collection(u'citas')
        citas = citas_ref.stream()
        
        for cita in citas:
            citaData = cita.to_dict()
            if(citaData.get('id_paciente') == id_paciente):
                citasResponse.append(citaData)

        
        return json.dumps(citasResponse)
    elif perfil == 1:
        citas_ref = db.collection(u'citas')
        citas = citas_ref.stream()
        for cita in citas:
            citaData = cita.to_dict()
            citasResponse.append(citaData)
        return json.dumps(citasResponse)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))