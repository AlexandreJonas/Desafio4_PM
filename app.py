from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")
from auth import auth
app.register_blueprint(auth, url_prefix='/')