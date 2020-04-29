from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import TeacherRegistrationForm, StudentRegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#database structure for making user account
#class User(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  first_name = db.Column(db.String(20), unique=True, nullable=False)
  #  last_name = db.Column(db.String(20), unique=True, nullable=False)
 #   email = db.Column(db.String(120), unique=True, nullable=False)
  #  password = db.Column(db.String(60), nullable=False)
    
#function which adds this to the data base in this format. Username, email
 #   def __repr__(self):
  #      return f"User('{self.username}', '{self.email}')"

#databse structure for making teacher account. correspond with forms.py
class TeacherInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_first_name = db.Column(db.String(100), unique=True, nullable=False)
    teacher_last_name = db.Column(db.String(100), unique=True, nullable=False)
    teacher_email=db.Column(db.String(100), unique=True, nullable=False)
    teacher_password=db.Column(db.String(60), nullable=False)
    teacher_subject = db.Column(db.String(120), nullable=False)
    teacher_timezone = db.Column(db.String(10), nullable=False)
    teacher_language = db.Column(db.String(100), nullable=False)
    
    def __teach__(self):
        return f"TeacherInfo('{self.teacher_first_name}','{self.teacher_last_name}', '{self.teacher_email}','{self.teacher_password}','{self.teacher_subject}', '{self.teacher_examBoard}','{self.teacher_timezone}','{self.teacher_language}')"

#database structure for making a student account
class StudentInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_first_name = db.Column(db.String(20), nullable=False)
    student_last_name= db.Column(db.String(100), unique=True, nullable=False)
    student_email=db.Column(db.String(120), nullable=False)
    student_password=db.Column(db.String(60), nullable=False)
    student_subject = db.Column(db.String(100), nullable=False)
    student_examBoard= db.Column(db.String(100), nullable=False)
    student_timezone = db.Column(db.String(10), nullable=False)
    student_language = db.Column(db.String(100), nullable=False)
    
    def __stud__(self):
        return f"StudentInfo('{self.student_first_name}','{self.student_last_name}', '{self.student_email}','{self.student_password}','{self.student_subject}', '{self.student_examBoard}','{self.student_timezone}','{self.student_language}')"

#make it so that when you are in the sign up pag
@app.route('/studentsignup', methods=['GET', 'POST'])
def studentsignup():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        if student_user.query.filter(student_user.email==form.student_email.data).first(): 
            flash('Account already exists!', 'danger')
            return render_template('register.html', title='Register',form=form)
   
    #if the account details are unique
        student_user=StudentInfo(student_first_name=form.student_first_name.data, student_last_name=form.student_last_name.data, student_email=form.student_email.data,student_password=form.student_password.data, student_subject=form.student_subject.data, student_examBoard=form.student_examBoard.data,student_timezone=form.student_timezone.data, student_language=form.student_language.data)
        db.session.add(StudentInfo)
        db.session.commit()
        #flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('studentverify'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/teachersignup')
def teachersignup():


    form = TeacherRegistrationForm()
    if form.validate_on_submit():
        if teacher_user.query.filter(teacher_user.email==form.teacher_email.data).first(): 
            flash('Account already exists!', 'danger')
            return render_template('signupteachers.html', title='Sign Up',form=form)
   
    #if the account details are unique
        teacher_user=TeacherInfo(teacher_first_name=form.teacher_first_name.data, teacher_last_name=form.teacher_last_name.data, teacher_email=form.student_email.data,teacher_password=form.teacher_password.data, teacher_subject=form.teacher_subject.data, teacher_examBoard=form.teacher_examBoard.data,teacher_timezone=form.teacher_timezone.data, teacher_language=form.teacher_language.data)
        db.session.add(TeacherInfo)
        db.session.commit()
        #flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('teacherverify'))
    return render_template('signupteachers.html', title='Sign Up', form=form)


@app.route('/unistudentsignup')
def unistudentsignup():
    return('Uni Student Signup')

@app.route('/studentverify')
def studentverify():
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
    db.create_all()
    app.run(debug=True)

