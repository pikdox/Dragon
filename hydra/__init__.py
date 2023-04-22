from flask import Blueprint, render_template, redirect, request

bp = Blueprint("hydra", __name__, url_prefix="/hydra",template_folder='./templates')
               
@bp.route('/')
def root():
    return redirect('search')

@bp.route('/search',methods=['GET','POST'])
def search():
    return render_template('search.html')

@bp.route('/term/<string:id>')
def get_term(id):
    global terms
    return terms[id]

@bp.route('/create/term',methods=['GET','POST'])
def create_term():
    print(terms)
    if request.method == 'POST':
        key = request.form.get('key')
        content = request.form.get('content')
        if not terms.get(key):
            terms[key] = content
            print(terms)
        else:
            return 'The terms is be catched'
    
    return render_template('create_term.html')


@bp.route('/login')
def login():
    return 'Sucess'


if __name__ == '__main__':
    bp.run(debug=True,host='0.0.0.0')