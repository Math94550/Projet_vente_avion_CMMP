from main import *
from flask import redirect, render_template,request
@app.route('/ajout_avion',methods=['GET','POST'])
def ajout_avion():
    if request.method=='Post':
        email= request.form['email']
        return redirect('/confirmation')
    return render_template('ajout_aviion')

@app.route('/confirmation')
def confirmation():
     return render_template('confirmation')