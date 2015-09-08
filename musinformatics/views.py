"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>'
  must be passed *username* as the argument.

"""
from flask import render_template, url_for, redirect, request, jsonify
from flask_cache import Cache
import tempfile


from musinformatics.app import app
from musinformatics.forms import InstrumentForm

from musinformatics.mir_tools import test


cache = Cache(app)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['wav', 'mp3', 'aiff'])
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def home():
    return redirect(url_for('instrument'))


def instrument():
    """Instrument Classificaiton App"""
    form = InstrumentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            file = request.files['file']
            if file and allowed_file(file.filename):
               # filename = secure_filename(file.filename)
                with tempfile.NamedTemporaryFile('w') as temp:
                    file.save(temp.name)
                    return jsonify(test.test(temp.name))
        else:
            return jsonify({'instrument': 'error'})
    return render_template('instrument.html', form=form)
