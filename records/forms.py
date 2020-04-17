from flask_wtf import FlaskForm
from wtfforms import StringField, PasswordField, BooleanField, SubmitField
from wtfforms.validators  import DataRequired

class LoginForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired()])
    remember_me= BooleanField('Remeber Me')
    submit= StringField("Sign In")


TODO: Create a login form 
