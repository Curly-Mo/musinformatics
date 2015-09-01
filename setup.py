from setuptools import setup

setup(
    name='musinformatics',
    version='1.0',
    description='Musinformatics Application',
    author='Colin Fahy',
    author_email='colin@cfahy.com',
    url='https://github.com/Curly-Mo/musinformatics',
    install_requires=[
        'Flask==0.10.1',
        'Flask_Cache==0.13.1',
        'Flask-WTF==0.12',
        'WTForms==2.0.2',
        'numpy',
        'scipy',
        'librosa',
    ],
)
