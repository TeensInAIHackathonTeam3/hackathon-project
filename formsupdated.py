##import all modules
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#create classes for User, Post
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,  db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    
    ##need to make it so after the login, it goes to something that's useful

posts = [
    {
        'author': 'Teacher A',
        'Subject': 'Maths',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Teacher B',
        'Subject': 'Physics',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

#route to homepage
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

#route to about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')

#route to register form
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter(db.or_(User.username==form.username.data, User.email==form.email.data)).first():
            flash('Account already exists!', 'danger')
            return render_template('register.html', title='Register',form=form)
    
        theuser=User(username=form.username.data, password=form.password.data, email=form.email.data)
        db.session.add(theuser)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

#route to login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if User.query.filter(db.and_(User.email==form.email.data, User.password==form.password.data)).first():
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
