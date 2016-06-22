"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template

from musinformatics.app import app
from musinformatics import views


def load_urls():
    # Home page
    app.add_url_rule('/', 'home', view_func=views.home)

    # Instrument Classification page
    app.add_url_rule('/instrument', 'instrument', view_func=views.instrument, methods=['GET', 'POST'])

    # Genre Classification page
    app.add_url_rule('/genre', 'genre', view_func=views.genre, methods=['GET', 'POST'])

    # Swingify page
    app.add_url_rule('/swingify', 'swingify', view_func=views.swingify, methods=['GET', 'POST'])

    ## Error handlers
    # Handle 404 errors
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    # Handle 500 errors
    @app.errorhandler(500)
    def server_error(e):
        return render_template('500.html'), 500
