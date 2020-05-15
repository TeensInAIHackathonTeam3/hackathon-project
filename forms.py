from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import datetime


class TeacherRegistrationForm(FlaskForm):
    teacher_first_name= StringField('First Name', 
                          validators=[DataRequired(), Length(min=2, max=200)])
    teacher_last_name= StringField('Last Name', 
                                  validators=[DataRequired(), Length(min=2, max=200)])
    teacher_email= StringField('Email', 
                       validators=[DataRequired(), Email()])
    teacher_password= PasswordField('Password', validators=[DataRequired()])
    teacher_confirm_password= PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('teacher_password')])
    
    
    teacher_examBoard=SelectField(u'Exam Board', choices=[('ocra', 'OCR A'), ('aqa','AQA'), ('edx','EDEXCEL'), ('ocrb','OCR B')])
    
    teacher_timezone = SelectField(u'Time Zone', choices=[('utc','UTC'), ('bst','UTC+01:00'), ('cdt','UTC+09:00')])
    
    teacher_subject = SelectField(u'Subject', choices=[('phy','Physics'), ('mat','Maths'), ('che','Chemistry'), ('eng','English'), ('bio','Biology')])
    
    teacher_first_language = SelectField(u'Language', choices=[('fre','French'), ('eng','English'), ('spa','Spanish')])
    
    teacher_other_lang= SelectField(u'Other languages?', choices=[('fre','French'), ('eng','English'), ('spa','Spanish'),('na','N/A')])
    
    teacher_min_year = SelectField(u'Min Student Year', choices=[('yr10','Year10'), ('yr11','Year11'), ('yr12','Year12'), ('yr13','Year13')])
    
    teacher_max_year = SelectField(u'Max Student Year', choices=[('yr10','Year10'), ('yr11','Year11'), ('yr12','Year12'),('yr13','Year13')])
    

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
                                    validators=[DataRequired(), EqualTo('student_password')])
    student_examBoard=SelectField(u'Exam Board', choices=[('ocra', 'OCR A'), ('aqa','AQA'), ('edx','EDEXCEL'), ('ocrb','OCR B') ])
    
    student_timezone = SelectField(u'Time Zone', choices=[('utc','UTC'), ('bst','UTC+01:00'), ('cdt','UTC+09:00')])
    
    student_subject = SelectField(u'Subject', choices=[('phy','Physics'), ('mat','Maths'), ('che','Chemistry'), ('eng','English'), ('bio','Biology')])
    
    student_first_language = SelectField(u'Language', choices=[('fre','French'), ('eng','English'), ('spa','Spanish')])
    
    student_other_lang= SelectField(u'Other languages?', choices=[('fre','French'), ('eng','English'), ('spa','Spanish'),('na','N/A')])
    
    student_year_group= SelectField(u'Year Group', choices =[('yr10', 'Year 10'), ('yr11', 'Year 11'), ('yr12', 'Year 12'), ('yr13', 'Year 13')])  
                                    
    student_accessibility= StringField('Do you have any accessibility requirements?',
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

class NewClassForm(FlaskForm):
    #all of these would normally have validators=[DataRequired()]
    subject = StringField('Subject')
    link = StringField('Link')
    description = StringField('Description')
    time = StringField('dd/mm/yyyy HH:MM')
    submit=SubmitField('Submit')
    #COMMENTED VALIDATION OUT FOR DEMO
##    def validate(self):
##        try:
##            datetimevalue = datetime.datetime.strptime(str(self.time.data), '%d/%m/%Y %H:%M')
##            self.time.data = datetimevalue
##            return True
##        except ValueError:
##            return False
