from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, URL

class PetForm(FlaskForm):
    '''Pet information form'''
    name = StringField('Name: ', validators=[InputRequired()])
    species = SelectField('Species: ', validators=[InputRequired()], choices=[('cat', 'Cat'),('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField('Photo URL: ', validators=[URL(), Optional()])
    age = StringField('Age: ')
    notes = StringField('Notes: ')
    available = BooleanField('Available: ')
