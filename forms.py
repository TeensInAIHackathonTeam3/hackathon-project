from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class TeacherRegistrationForm(FlaskForm):
    teacher_first_name= StringField('First Name', 
                          validators=[DataRequired(), Length(min=2, max=200)])
    teacher_last_name= StringField('Last Name', 
                                  validators=[DataRequired(), Length(min=2, max=200)])
    teacher_email= StringField('Email', 
                       validators=[DataRequired(), Email()])
    teacher_password= PasswordField('Password', validators=[DataRequired()])
    teacher_confirm_password= PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])
    teacher_subject= StringField('Subjects',
                             validators= [DataRequired()])
    teacher_examBoard=StringField('Exam Board', validators=[DataRequired()])
    
    teacher_timezone=StringField('Time Zone',
                                validators=[DataRequired()])
    
    teacher_language=StringField('Language', 
                                 validators=[DataRequired()])
    #make it so there are multiple subjects and examboards you can fill in
    #make a drop down menu for timezone, year group and accessibility
    
    submit=SubmitField('Sign Up')

class StudentRegistrationForm(FlaskForm):
    student_first_name= StringField('First Name', 
                          validators=[DataRequired(), Length(min=2, max=200)])
    student_last_name= StringField('Last Name', 
                                  validators=[DataRequired(), Length(min=2, max=200)])
    student_email= StringField('Email', 
                       validators=[DataRequired(), Email()])
    student_password= PasswordField('Password', validators=[DataRequired()])
    student_confirm_password= PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])
    student_subject= StringField('Subjects',
                             validators= [DataRequired()])
    student_examBoard=StringField('Exam Board', validators=[DataRequired()])
    
    student_timezone=StringField('Time Zone',
                                validators=[DataRequired()])
    
    student_language=StringField('Language', 
                                 validators=[DataRequired()])
    #make it so there are multiple subjects and examboards you can fill in
    #make a drop down menu for timezone, year group and accessibility
    
    submit=SubmitField('Sign Up')
    
    
    

class LoginForm(FlaskForm):
    email= StringField('Email', 
                       validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit=SubmitField('Login')