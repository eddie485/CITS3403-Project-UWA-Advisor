from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    password =  PasswordField("Password", validators = [DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Log In")


class RegistrationForm(FlaskForm): 
    email = StringField("Email", validators=[DataRequired(), Email()])
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    major = StringField("Major", validators=[DataRequired()])
    year = IntegerField("Year", validators=[DataRequired()])
    dateofbirth = DateField("Date of Birth", validators=[DataRequired()])
    studentid = IntegerField("Student ID", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()]) 
    password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register") 

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None: 
                raise ValidationError("That username is already being used. Please select a different username.") 
    
    # validation to check whether the variable entered by the user already exists in the database.
    # asks them to try again if it does
    def validate_studentid(self, studentid):
        if studentid.data != current_user.studentid:
            user = User.query.filter_by(studentid=studentid.data).first()
            if user is not None: 
                raise ValidationError("Please select a different studentid.") 

    def validate_email(self, email): 
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first() 
            if user is not None: 
                raise ValidationError("That email is already being used. Please enter a different email address.")
 

""" EditProfileForm is used in the profileEdit.html page. It allows users to change 
their account details and save them into the database, provided that it does
not already exist. Works practically the same as the register form"""

class EditProfileForm(FlaskForm): 
    email = StringField("Email", validators=[DataRequired(), Email()])
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    major = StringField("Major", validators=[DataRequired()])
    year = IntegerField("Year", validators=[DataRequired()])
    dateofbirth = DateField("Date of Birth", validators=[DataRequired()])
    studentid = IntegerField("Student ID", validators=[DataRequired()])
    submit = SubmitField("Save Changes") 