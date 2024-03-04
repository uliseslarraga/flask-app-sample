from flask import Flask
from dotenv import load_dotenv
from app.routes.main import main_routes
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_routes, url_prefix='/')
    return app