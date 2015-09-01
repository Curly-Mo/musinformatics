from setuptools import setup

setup(
    name='musinformatics',
    version='1.0',
    description='Musinformatics',
    author='Colin Fahy',
    author_email='colin@cfahy.com',
    url='https://github.com/Curly-Mo/musinformatics',
    install_requires=[
        'Flask>=0.10.1',
        'Flask_Cache>=0.13.1',
        'Flask-WTF>=0.12',
        'WTForms>=2.0.2',
        'python-dateutil>=2.4.2',
        'pyparsing>=2.0.3',
        'matplotlib>=1.4.3',
        'numpy>=1.9.2',
        'scipy>=0.15.1',
        'scikit-learn>=0.16.1',
        'audioread>=1.2.1',
        'librosa',
        'future',
    ],
)
