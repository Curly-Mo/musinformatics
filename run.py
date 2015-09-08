"""
Initialize Flask app

"""

from musinformatics import generate_keys
generate_keys.main()
#app.config.from_pyfile('flaskapp.cfg')

from musinformatics.app import app

if __name__ == '__main__':
    app.run(debug=True)
