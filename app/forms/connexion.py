from main import *
from flask import redirect, render_template, request

@app.route('/connexion',methods=['GET','POST'])

def connexion():
    if request.method=='Post':
        
        email = request.form['email']
        password = request.form['password']

        return redirect('/confirmation')
    
    return render_template('connexion')

@app.route('/confirmation')

def confirmation():
     return render_template('confirmation')