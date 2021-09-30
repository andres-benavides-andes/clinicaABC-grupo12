from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity

class VistaConsultas(Resource):
  
  @jwt_required()
  def get(self):
    return self.consultar(self.getIdUsuario())

  def consultar(self,user_id):
    citas = []
    cita ={
      "user_id":1,
      "date":"2020-09-30",
      "hour":"15:30",
      "especiality":"medicina general"
    }
    cita2 ={
      "user_id":2,
      "date":"2020-09-30",
      "hour":"08:45",
      "especiality":"medicina general"
    }
    citas.append(cita)
    citas.append(cita2)

    citas_usuario = []
    for c in citas:
      if c['user_id'] == user_id:
          citas_usuario.append(c)
    return citas_usuario

  def getIdUsuario(self):
    jwt = get_jwt_identity()
    user_id = jwt.get("user_id")
    return user_id