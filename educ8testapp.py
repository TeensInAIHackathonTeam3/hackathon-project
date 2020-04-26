from flask import Flask, render_template, url_for
app = Flask(__name__)


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

@app.route('/login')
def login():
    return('Sign in')

@app.route('/signup')
def signup():
    return('Teacher, student, or uni student?')

@app.route('/studentsignup')
def studentsignup():
    return('Student Signup')

@app.route('/teachersignup')
def teachersignup():
    return('Teacher Signup')

@app.route('/unistudentsignup')
def unistudentsignup():
    return('Uni Student Signup')

@app.route('/studentverify')
def studentverify():
    return('Email Verified')

@app.route('/teacherverify')
def studentverify():
    return('Email Verified')

@app.route('/studenthome')
def studenthome():
    return render_template('studenthome.html')

@app.route('/teacherhome')
def teacherhome():
    return('Teacher Homepage')

if __name__ == '__main__':
    app.run()
