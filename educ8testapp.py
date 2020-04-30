from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import StudentRegistrationForm, TeacherRegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



class TeacherInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_first_name = db.Column(db.String(100), nullable=False)
    teacher_last_name = db.Column(db.String(100), nullable=False)
    teacher_email=db.Column(db.String(100), unique=True, nullable=False)
    teacher_password=db.Column(db.String(60), nullable=False)
    teacher_subject = db.Column(db.String(120), nullable=False)
    teacher_examBoard = db.Column(db.String(120), nullable=False)
    teacher_timezone = db.Column(db.String(10), nullable=False)
    teacher_first_language = db.Column(db.String(100), nullable=False)
    teacher_other_lang= db.Column(db.String(100), nullable=False)
    teacher_min_year= db.Column(db.String(100), nullable=False)
    teacher_max_year= db.Column(db.String(100), nullable=False)
    def __teach__(self):
        return f"TeacherInfo('{self.teacher_first_name}','{self.teacher_last_name}', '{self.teacher_email}','{self.teacher_password}','{self.teacher_subject}', '{self.teacher_examBoard}','{self.teacher_timezone}',''{self.teacher_first_language}','{self.teacher_other_lang}', '{self.teacher_min_year}', '{self.teacher_max_year}')"

#database structure for making a student account
class StudentInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_first_name = db.Column(db.String(100), nullable=False)
    student_last_name= db.Column(db.String(100), nullable=False)
    student_email=db.Column(db.String(120), unique=True, nullable=False)
    student_password=db.Column(db.String(60), nullable=False)
    student_subject = db.Column(db.String(100), nullable=False)
    student_examBoard= db.Column(db.String(100), nullable=False)
    student_timezone = db.Column(db.String(10), nullable=False)
    student_first_language = db.Column(db.String(100), nullable=False)
    student_other_lang= db.Column(db.String(100), nullable=False)
    student_year_group= db.Column(db.String(100), nullable=False)
    student_accessibility = db.Column(db.String(100), nullable=False)
    
    def __stud__(self):
        return f"StudentInfo('{self.student_first_name}','{self.student_last_name}', '{self.student_email}','{self.student_password}','{self.student_subject}', '{self.student_examBoard}','{self.student_timezone}','{self.student_first_language}','{self.student_other_lang}','{self.student_year_group}', '{self.student_accessibility}')"
    


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
        if User.query.filter(db.and_(User.email==form.email.data, User.password==form.password.data)).first():
            #flash('You have been logged in!', 'success')
            return redirect(url_for('studenthome'))
        #else:
            #flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



@app.route('/studentsignup', methods=['GET', 'POST'])
def studentsignup():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        if StudentInfo.query.filter(StudentInfo.student_email==form.student_email.data).first():
            #flash('Account already exists!', 'danger')
            return render_template('signup.html', title='Sign Up',form=form)
    
        theuser=StudentInfo(student_first_name=form.student_first_name.data, student_last_name=form.student_last_name.data, student_email=form.student_email.data,student_password=form.student_password.data, student_subject=form.student_subject.data, student_examBoard=form.student_examBoard.data,student_timezone=form.student_timezone.data, student_first_language=form.student_first_language.data, student_other_lang=form.student_other_lang.data, student_year_group=form.student_year_group.data, student_accessibility=form.student_accessibility.data)
        db.session.add(theuser)
        db.session.commit()
        #flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('studentverify'))
    return render_template('studentsignup.html', title='Sign Up', form=form)


@app.route('/teachersignup', methods=['GET', 'POST'])
def teachersignup():
    form = TeacherRegistrationForm()
    if form.validate_on_submit():
        if TeacherInfo.query.filter(TeacherInfo.teacher_email==form.teacher_email.data).first():
            #flash('Account already exists!', 'danger')
            return render_template('signup.html', title='Sign up',form=form)
    
        theuser=TeacherInfo(teacher_first_name=form.teacher_first_name.data, teacher_last_name=form.teacher_last_name.data, teacher_email=form.student_email.data,teacher_password=form.teacher_password.data, teacher_subject=form.teacher_subject.data, teacher_examBoard=form.teacher_examBoard.data,teacher_timezone=form.teacher_timezone.data, teacher_first_language=form.student_first_language.data, teacher_other_lang=form.student_other_lang.data, teacher_min_year=form.teacher_min_year.data, teacher_max_year=form.teacher_max_year.data)
        db.session.add(theuser)
        db.session.commit()
        #flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('teacherverify'))
    return render_template('teachersignup.html', title='Sign Up', form=form)



##@app.route('/unistudentsignup',  methods=['GET', 'POST'])
##def unistudentsignup():
##    form = RegistrationForm()
##    if form.validate_on_submit():
##        if User.query.filter(db.or_(User.username==form.username.data, User.email==form.email.data)).first():
##            #flash('Account already exists!', 'danger')
##            return render_template('register.html', title='Register',form=form)
##    
##        theuser=User(username=form.username.data, password=form.password.data, email=form.email.data)
##        db.session.add(theuser)
##        db.session.commit()
##        #flash(f'Account created for {form.username.data}!', 'success')
##        return redirect(url_for('unistudentverify'))
##    return render_template('register.html', title='Register', form=form)


@app.route('/studentverify')
def studentverify():
    return('Email Verified')

##@app.route('/unistudentverify')
##def unistudentverify():
##    return('Email Verified')

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
    db.create_all()
    app.run()
