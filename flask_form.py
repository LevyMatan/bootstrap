from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you?', validators=[DataRequired()], render_kw={'placeholder': 'Enter breed', 'class': 'form-control'})
    neutered = BooleanField('Have you been neutered?', render_kw={'class': 'form-check-input'})
    mood = RadioField('What is your mood?', choices=[('mood_one', 'Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField(u'Pick your favorite food:', choices=[('chi', 'Chicken'), ('bf', 'Beef'), ('fish', 'Fish')], render_kw={'class': 'form-select'})
    feedback = TextAreaField(render_kw={'class': 'form-control'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-primary'})
    
    
@app.route('/', methods=['GET', 'POST'])
def index():
    breed = False
    form = InfoForm()
            
    if request.method == 'POST':
        if form.validate_on_submit():
            breed = form.breed.data
            form.breed.data = ''
            # Debug
            print('Breed entered:', breed)
            # Falsh message to confirm form submission
            flash(f'You have successfully changed the breed name to {breed}!')
        else:
            # Form is invalid
            print('Form validation failed:', form.errors)
        
    return render_template('home.html', form=form, breed=breed)

if __name__ == '__main__':
    app.run(debug=True)