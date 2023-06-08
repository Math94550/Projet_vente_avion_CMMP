from main import *
from Flask import redirect, render_template
@app.route('/ajout_avion',methods=['GET','POST²'])
def ajout_avion():
    if request.method=='Post':
         = request.form['']


        return redirect('/confirmation')
    return render_template('ajout_aviion')

@app.route('/confirmation')
def confirmation():
     return render_template('confirmation')