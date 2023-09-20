
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def titlepage():
    return render_template('dojo.html', dojos = Dojo.get_all())

@app.route('/dojo/create', methods = ['POST'])
def create_dojo():
    Dojo.get_info(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojo_titlepage(id):
    data = {
        "id": id
    }
    return render_template('all_ninjas.html', dojo = Dojo.save_info(data))