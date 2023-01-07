from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Dev'}
    posts=[
        {'author':{'username':'John'},
        'body':'Wonderful education in Cardiff!'},
        
        {'author':{'username':'David'},
         'body':'Avatar 2 was pretty good'}
    ]
    return render_template('index.html', user=user,posts=posts)

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',title='Sign In', form=form)