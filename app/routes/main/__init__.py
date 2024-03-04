from flask import Blueprint

main_routes = Blueprint('images', __name__, template_folder='templates')

from app.routes.main import main