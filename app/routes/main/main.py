from flask import Flask, render_template
from app.routes.main import main_routes
from config import basedir

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/healthcheck')
def health():
    return 'Ok'
