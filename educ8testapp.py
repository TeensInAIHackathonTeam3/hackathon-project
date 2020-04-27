from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


teachersaccepted= [
    {
        'name': 'Ahmed Kingston', 
        'subject' : 'GCSE chemistry',
        'timezone': 'BST',
        'language':'English'
    }   
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('welcome_screen.html')
    
@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@project.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('studenthome'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/signup')
def signup():
    return("Student, teacher or uni student?")

@app.route('/studentsignup', methods=['GET', 'POST'])
def studentsignup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('studentverify'))
    return render_template('register.html', title='Register', form=form)


@app.route('/teachersignup', methods=['GET', 'POST'])
def teachersignup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('teacherverify'))
    return render_template('register.html', title='Register', form=form)


@app.route('/unistudentsignup',  methods=['GET', 'POST'])
def unistudentsignup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('unistudentverify'))
    return render_template('register.html', title='Register', form=form)

@app.route('/studentverify')
def studentverify():
    return('Email Verified')

@app.route('/unistudentverify')
def unistudentverify():
    return('Email Verified')

@app.route('/teacherverify')
def teacherverify():
    return('Email Verified')

@app.route('/studenthome')
def studenthome():
    return render_template('studenthome.html', teachersaccepted = teachersaccepted)

@app.route('/teacherhome')
def teacherhome():
    return('Teacher Homepage')

if __name__ == '__main__':
    app.run()
