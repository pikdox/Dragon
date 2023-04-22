from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Dragon"

if __name__ == '__main__':
    import hydra, etk
    app.register_blueprint(hydra.bp)
    app.register_blueprint(etk.bp)
    app.run(debug=True)