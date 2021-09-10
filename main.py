import os
import firebase_admin
import random
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, request

app = Flask(__name__)
# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
'projectId': 'miso-arquitectura-325522',
})
db = firestore.client()

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route("/facturador")
def facturador():
    id_paciente = request.args.get('id_paciente', type=int)
    # pacientes_ref = db.collection(u'pacientes')
    # pacientes = pacientes_ref.stream()
    # for paciente in pacientes:
    #     pacienteData = paciente.to_dict()
    #     if(pacienteData.get('id_paciente') == id_paciente):
    #         return { "total": random.randint(212,999)  }
    return { "total2": ((((id_paciente % 9) * 626 + 2) / 9) * 7   )  }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))