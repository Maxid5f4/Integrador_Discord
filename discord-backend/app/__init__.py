from flask import Flask
from config import Config


def init_app():
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER)
    
    # AQUI lleva los BLUEPRINTS ---
    app.register_blueprint()
    app.register_blueprint()
    app.register_blueprint()
    app.register_blueprint()

    return app 