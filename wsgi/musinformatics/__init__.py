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


def main():
    urls.load_urls()
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == "__main__":
    main()
