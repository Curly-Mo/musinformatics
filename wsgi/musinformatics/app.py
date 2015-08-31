"""
Initialize Flask app

"""
from flask import Flask

app = Flask(__name__)

app.config.from_object('musinformatics.settings.Production')

# Enable jinja2 loop controls extension
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# Pull in URL dispatch routes
import urls

urls.load_urls()
