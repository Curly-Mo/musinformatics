"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>'
  must be passed *username* as the argument.

"""
from flask import render_template, url_for, redirect, request, jsonify, send_file
from flask_cache import Cache
from werkzeug import secure_filename
import tempfile
import os
import logging
import sys

from musinformatics.app import app
from musinformatics.forms import InstrumentForm, GenreForm
from musinformatics.forms import SwingifyForm

import musinformatics.mir_tools.machine_learning as machine_learning
from musinformatics.swingify import swingify as swing
from musinformatics.tf_sandbox.tflearn import model_wrapper
from musinformatics.tf_sandbox.tflearn import cnn
sys.modules['cnn'] = cnn
import joblib


cache = Cache(app)
genre_model = model_wrapper.Model.load('all_genre1')
labels = joblib.load('models/all_genre1/all_genre_labels_labels.p')


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['wav', 'mp3', 'aiff', 'aif', 'flac', 'ogg', 'au'])
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def home():
    return redirect(url_for('swingify'))


def instrument():
    """Instrument Classificaiton App"""
    form = InstrumentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            file = request.files['file']
            if file:  # and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                logging.info(filename)
                with tempfile.NamedTemporaryFile(suffix=os.path.splitext(filename)[1]) as temp:
                    file.save(temp.name)
                    prediction, predictions = machine_learning.predict_file(temp.name)
                    json_obj = {
                        'instrument': prediction,
                        'instruments': predictions,
                    }
                    return jsonify(json_obj)
        else:
            return jsonify({'success':False, 'error': 'Errored!', 'status': 515})
    return render_template('instrument.html', form=form)


def genre():
    """Genre Classificaiton App"""
    form = GenreForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            file = request.files['file']
            if file:  # and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                logging.info(filename)
                with tempfile.NamedTemporaryFile(suffix=os.path.splitext(filename)[1]) as temp:
                    file.save(temp.name)
                    y, Y = cnn.predict(genre_model.model, temp.name, labels, 10)
                    logging.info(temp.name)
                    logging.info(Y)
                    json_obj = {
                        'predictions': Y,
                    }
                    return jsonify(json_obj)
        else:
            return jsonify({'success':False, 'error': 'Errored!', 'status': 515})
    return render_template('genre.html', form=form)


def swingify():
    """Swingify App"""
    form = SwingifyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            file = request.files['file']
            factor = float(request.form['factor'])
            logging.info(factor)
            if file:  # and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                outputname = os.path.splitext(filename)[0]+'_swing.wav'
                logging.info(filename)
                with tempfile.NamedTemporaryFile(suffix=os.path.splitext(filename)[1]) as temp:
                    file.save(temp.name)
                    swing.swingify(temp.name, temp.name, factor, format='wav', max_length=120)
                    logging.info(temp.name)
                    return send_file(temp.name, as_attachment=True, attachment_filename=outputname)
        else:
            return jsonify({'success':False, 'error': 'Errored!', 'status': 515})
    return render_template('swingify.html', form=form)
