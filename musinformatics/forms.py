"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flask.ext.wtf import Form
from wtforms.fields import FileField, RadioField
from wtforms.validators import Required


class InstrumentForm(Form):
    file = FileField('Audio File', validators=[Required()])


class SwingifyForm(Form):
    file = FileField('Audio File', validators=[Required()])
    factors = [(1.5, 'light swing'), (2, 'medium swing'), (3, 'hard swing')]
    factor = RadioField('Swing Factor', choices=factors, default=2, coerce=float, validators=[Required()])
