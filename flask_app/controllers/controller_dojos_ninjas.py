from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_ninja import Dojo
from flask_app.models.ninja import Ninja
from flask_app.models import dojo_ninja, ninja


# Default Directory
@app.route('/')
def index():
    return redirect('/dojos')

# Display all dojos
@app.route('/dojos')
def dojos():
    dojos=Dojo.get_all()
    return render_template("index.html", dojos=dojos)

# Create Dojos
@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/')

# Show Dojos
@app.route('/show/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
    'id' : dojo_id
    }
    dojo = Dojo.get_ninjas(data)
    return render_template('show_dojo.html', dojo=dojo)


# --------------------------------------------------------------------------------------------------------
# Ninjas:
# Show Ninjas
@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template('show_ninja.html', dojos=dojos)

# Create Ninjas
@app.route('/create_ninja', methods=['POST'])
def create_ninjas():
    ninja.Ninja.create_ninja(request.form)
    return redirect('/')

