from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/healthcheck')
def health():
    return 'Ok'