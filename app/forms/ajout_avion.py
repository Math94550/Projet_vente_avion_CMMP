from main import *
from flask import redirect, render_template, request
import sqlite3

@app.route('/ajout_avion',methods=['GET','POST'])
def ajout_avion():
    if request.method =='Post':
        immatriculation = request.form['immatriculation']
        type_avion = request.form['Type_avion']
        modele = request.form['modele']
        constructeur = request.form['constructeur']
        Anneedefabrication = request.form['anneedefabrication']
        capacitePassager = request.form['capacitePassager']
        volumesoute = request.form['volumesoute']
        vitesse = request.form['vitesse']
        description = request.form['description']

        conn = sqlite3.connect('static/avions.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO avions (immatriculation, type_avion, modele, constructeur, Anneedefabrication, capacitePassager, volumesoute, vitesse, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (immatriculation, type_avion, modele, constructeur, Anneedefabrication, capacitePassager, volumesoute, vitesse, description))

        conn.commit()
        conn.close()

        return redirect('/confirmation')
    return render_template('ajout_avion')


@app.route('/confirmation')
def confirmation():
     return render_template('confirmation.html')