#from flask import Flask, render_template
#app = Flask(__name__, template_folder="templates")
from flask import Blueprint, render_template, url_for, request, flash
auth = Blueprint('auth', __name__)

@auth.route("/")
@auth.route("/index")
def hello_world():
    return render_template('index.html')

@auth.route("/contato")
def contato():
    return render_template('contato.html')

@auth.route('/contato', methods=["GET", "POST"])
def gfg():
    from database import create_db, InsertDB
    if request.method == "POST":
        email = str(request.form.get("email"))
        assunto = str(request.form.get("assunto"))
        descr = str(request.form.get("descricao"))
        create_db()
        InsertDB(email, assunto, descr)
        print(email)
        print(assunto)
        print(descr)
    return render_template('contato.html')

@auth.route("/quem_somos")
def quem_somos():
    return render_template('quem_somos.html')

@auth.route('/consultar')
def consultar():
    from database import teste
    try:
        contatos = teste()
    except:
        pass
    return render_template('consultar.html', contatos = contatos)