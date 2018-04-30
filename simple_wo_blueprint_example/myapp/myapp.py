# myapp/myapp.py
#barebones that going to initialize everything for your app.

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

# from views import * : mistake initializing views before app won;t run

# initialize the db
db = SQLAlchemy()

app = Flask(__name__)

# load configs from python file ..config.py
app.config.from_pyfile('config.py')

from views import *

if __name__ == '__main__':
    app.run()