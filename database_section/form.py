from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, RadioField, SelectField, TextAreaField

class AddForm(FlaskForm):
    name = StringField('Name of Puppy: ')
    age = IntegerField('Age of Puppy: ')
    breed = StringField('Breed of Puppy: ')
    submit = SubmitField('Add Puppy')
    
class DelForm(FlaskForm):
    id = IntegerField('ID Number of Puppy to Remove: ')
    submit = SubmitField('Remove Puppy')
    
class AddOwner(FlaskForm):
    name = StringField('Name of Owner: ')
    id = IntegerField('ID Number of Puppy: ')
    submit = SubmitField('Add Owner')
    