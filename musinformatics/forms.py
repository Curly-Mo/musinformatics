"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flask_wtf import FlaskForm
from wtforms.fields import FileField, RadioField
from wtforms.validators import InputRequired


class InstrumentForm(FlaskForm):
    file = FileField('Audio File', validators=[InputRequired()])


class GenreForm(FlaskForm):
    file = FileField('Audio File', validators=[InputRequired()])


class SwingifyForm(FlaskForm):
    file = FileField('Audio File', validators=[InputRequired()])
    factors = [(1.5, 'light swing'), (2, 'medium swing'), (3, 'hard swing')]
    factor = RadioField('Swing Factor', choices=factors, default=2, coerce=float, validators=[InputRequired()])
