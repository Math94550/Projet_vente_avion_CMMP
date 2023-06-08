from flask import *
from flask import render_template

@app.route('/')
def acceuil():
    return render_template('acceuil.html')