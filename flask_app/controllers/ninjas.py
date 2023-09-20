from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo, ninja



@app.route('/ninjas')
def ninjaindex():
    return render_template('ninja_create.html', dojos = dojo.Dojo.get_all())

@app.route('/ninja/create',methods=['POST'])
def ninja_create():
    ninja.Ninja.get_info(request.form)
    return redirect('/')