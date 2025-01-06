from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from app.auth.models import User


def email_exist(form,field):
        email = User.query.filter_by(user_email=field.data).first()
        if email:
            raise ValidationError("Email already exists")
        
class RegistrationForm(FlaskForm):
    name = StringField("name",validators=[DataRequired(),Length(4,16,message="Between 4 to 16 characters")])
    email = StringField("email",validators=[DataRequired(),Email(),email_exist()])
    password = PasswordField("password",validators=[DataRequired(),EqualTo("confirm",message="Password must match")])
    confirm = PasswordField("confirm",validators=[DataRequired()]) 
    submit = SubmitField("Register")
    
class LoginForm(FlaskForm):
    email = StringField("email",validators=[DataRequired(),Email()])
    password = PasswordField("password",validators=[DataRequired()])
    stay_loggeding = BooleanField("remember me")
    submit = SubmitField("Login")