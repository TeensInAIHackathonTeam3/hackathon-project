from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
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
    
    teacher_examBoard=SelectField(u'Exam Board', choices=[('ocra', 'OCR A'), ('aqa','AQA'), ('edx','EDEXCEL'), ('ocrb','OCR B') ])
    
    teacher_timezone = SelectField(u'Time Zone', choices=[('utc','UTC'), ('bst','BST'), ('cdt','CDT')])
    
    teacher_subject = SelectField(u'Subject', choices=[('phy','Physics'), ('mat','Maths'), ('che','Chemistry'), ('eng','English'), ('bio','Biology')])
    
    teacher_language = SelectField(u'Language', choices=[('fre','French'), ('eng','English'), ('spa','Spanish')])
    
    
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
    student_examBoard=SelectField(u'Exam Board', choices=[('ocra', 'OCR A'), ('aqa','AQA'), ('edx','EDEXCEL'), ('ocrb','OCR B') ])
    
    student_timezone = SelectField(u'Time Zone', choices=[('utc','UTC'), ('bst','BST'), ('cdt','CDT')])
    
    student_subject = SelectField(u'Subject', choices=[('phy','Physics'), ('mat','Maths'), ('che','Chemistry'), ('eng','English'), ('bio','Biology')])
    
    student_language = SelectField(u'Language', choices=[('fre','French'), ('eng','English'), ('spa','Spanish')])
    
                                 
    #make it so there are multiple subjects and examboards you can fill in
    #make a drop down menu for timezone, year group and accessibility
    
    submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email= StringField('Email', 
                       validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit=SubmitField('Login')
