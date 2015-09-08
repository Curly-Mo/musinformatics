"""
Initialize Flask app

"""
from musinformatics.app import app

app.config.from_pyfile('flaskapp.cfg')

if __name__ == '__main__':
    app.run(debug=True)
