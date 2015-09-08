"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flask.ext.wtf import Form
from wtforms.fields import FileField
from wtforms.validators import Required


class InstrumentForm(Form):
    file = FileField('Audio File', validators=[Required()])
