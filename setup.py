from setuptools import setup

setup(
    name='musinformatics',
    version='1.0',
    description='Musinformatics',
    author='Colin Fahy',
    author_email='colin@cfahy.com',
    url='https://github.com/Curly-Mo/musinformatics',
    install_requires=[
        'Flask',
        'Flask_Cache',
        'Flask-WTF',
        'WTForms',
        'python-dateutil',
        'pyparsing',
        'six>=1.9.0',
        'matplotlib',
        'numpy',
        'scipy',
        'scikit-learn',
        'audioread',
        'librosa',
        'future',
    ],
)
