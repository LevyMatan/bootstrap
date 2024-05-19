'''
Connecting Flask, SQL, and HTML

An ORM (Object Relational Mapper) is a tool that allows you to interact with a database using an object-oriented programming language. SQLAlchemy is a popular ORM for Python. It allows you to interact with a database using Python objects.
'''

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_migrate import Migrate
from form import AddForm, DelForm, AddOwner

# Set up SQL database in flask app
# Create a Model in Flask App
# Perform basic CRUD (Create, Read, Update, Delete) operations

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretKey'

# SQL DATABASE SECTION
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

############################################################################################
# Create a Model in Flask App
class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)
    owner = db.Column(db.Text)
    
    def __init__(self, name, age, breed, owner=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner
        
    def __repr__(self):
        pup_str = f"Puppy {self.name} "
        if self.age:
            pup_str += f"is {self.age} years old"
        if self.breed:
            if self.age:
                pup_str += " and"
            pup_str += f" is a {self.breed}."
        if self.owner:
            pup_str += f"His owner name is {self.owner}"
        else:
            pup_str += "It currently has no owner."
        return pup_str


def create_app():
    return app

############################################################################################
# VIEW FUNCTIONS
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()
    
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        breed = form.breed.data
        
        new_pup = Puppy(name, age, breed)
        db.session.add(new_pup)
        db.session.commit()
        
        flash(f'Puppy added: {name}', 'success')
        
        return redirect(url_for('list_pup'))
    
    return render_template('add.html', form=form)

@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['GET', 'POST'])
def del_pup():
    form = DelForm()
    
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        if not pup:
            flash(f'ERROR: Puppy with ID: {id} not found.', 'warning')
            return redirect(url_for('list_pup'))
        db.session.delete(pup)
        db.session.commit()
        
        flash(f'Puppy with ID: {id} removed.', 'primary')
        
        return redirect(url_for('list_pup'))
    
    return render_template('delete.html', form=form)

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    form = AddOwner()
    
    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        pup = Puppy.query.get(id)
        
        if pup:
            pup.owner = name
            db.session.commit()
            flash(f'Owner added to {pup.name}', 'success')
            return redirect(url_for('list_pup'))
        else:
            flash(f'ERROR: Puppy with ID: {id} not found.', 'warning')
            return redirect(url_for('list_pup'))
    
    return render_template('owner.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)