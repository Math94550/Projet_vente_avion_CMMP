from main import *
from flask import render_template

@app.route('/catalogue/aviondelocation')

def acceuil():
    return render_template('/catalogue/aviondelocation')