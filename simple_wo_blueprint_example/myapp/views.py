# myapp/views.py

from myapp import app

from models import Member

from forms import LoginForm

from flask import render_template

@app.route('/')
def index():
    # query db now
    firstmember = Member.query.first()
    return '<h1>The first member is: '+firstmember.name +'</h1>'
    #return '<h1>You are on index page!</h1>'

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('index.html', form=form)