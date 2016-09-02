"""
Initialize Flask app

"""
import os
import sys


sys.path.insert(1, os.path.join(os.path.abspath('.'), 'libs'))


from musinformatics.app import app


from musinformatics import generate_keys
generate_keys.main()
#app.config.from_pyfile('flaskapp.cfg')


if __name__ == '__main__':
    app.run(debug=True)
