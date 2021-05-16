from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    password =  PasswordField("Password", validators = [DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")

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
        user = User.query.filter_by(username=username.data).first()
        if user is not None: 
            raise ValidationError("Please select a different username.") 
    
    def validate_email(self, email): 
        user = User.query.filter_by(email=email.data).first() 
        if user is not None: 
            raise ValidationError("Please enter a different email address.")