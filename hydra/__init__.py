from flask import Blueprint

bp = Blueprint("hydra", __name__, url_prefix="/hydra",template_folder='./templates')
               
@bp.route('/')
def root():
    return 'test'