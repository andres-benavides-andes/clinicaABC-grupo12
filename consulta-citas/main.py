import os
import firebase_admin
from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
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

@app.route("/consulta-citas", methods=["GET"])
#@jwt_required()
def facturador():
    id_paciente = request.args.get('id_paciente', type=int)
    citas_ref = db.collection(u'citas')
    citas = citas_ref.stream()
    citasResponse = []
    for cita in citas:
       citaData = cita.to_dict()
       citasResponse.append(citaData)
    #    if(pacienteData.get('id_paciente') == id_paciente):
    #        return { "total": random.randint(212,999)  }
    #return { "total": ((((id_paciente % 9) * 626 + 2) / 9) * 7   )  }
    return json.dumps(citasResponse)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))