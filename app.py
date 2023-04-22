from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

import hydra, etk
app.register_blueprint(hydra.bp)
app.register_blueprint(etk.bp)

@app.route('/')
def home():
    return "Welcome to Dragon"

@app.route('/url_map')
def url_map():
    return app.url_map