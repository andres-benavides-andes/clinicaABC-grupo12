from flask import Flask

def create_app(config_name):
  app= Flask(__name__)

  app.config["JWT_SECRET_KEY"] = "gurpo_12_arquitectura_agil"
  app.config["PROPAGATE_EXECPTIONS"] = True
  return app