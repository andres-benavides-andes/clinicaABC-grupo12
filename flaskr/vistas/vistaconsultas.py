from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

class VistaConsultas(Resource):
  def get(self):
    return "Hola mundo"