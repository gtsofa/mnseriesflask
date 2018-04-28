# myapp/myapp.py
#barebones that going to initialize everything for your app.

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if __name__ == '__main__':
    app.run()