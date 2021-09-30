from flaskr import create_app
from flask_jwt_extended import JWTManager
from flaskr.vistas.vistaconsultas import VistaConsultas
from flask_restful import Api

app = create_app('consulta_cita')
app_context = app.app_context()
app_context.push()

jwt = JWTManager(app)

api = Api(app)
api.add_resource(VistaConsultas, '/consulta')