from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,MultipleFileField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
import random
from flask_login import current_user
from .models import User

# suggestion function 
def suggestion(s):
    s=str(s)
    if s[-1].isdigit()==True:
        s=s[:len(s)-1]+str(int(s[-1])+1)
    else:
        s=s[:len(s)]+str(random.randint(0,10))
    return s

#forms
class Registration(FlaskForm):
    username=StringField("Username",validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    confirm_password=PasswordField("Confirm your password",validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')
    
    #validations
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'''That username is taken please try another.\n You can try {suggestion(user.username)} as username''')         
    
      
class Login(FlaskForm):
    username=StringField("Username",validators=[DataRequired(),Length(min=2,max=20)])
    password=PasswordField("Password",validators=[DataRequired()])
    submit=SubmitField('Login')
    remember=BooleanField('remember me')

class UploadFile(FlaskForm):
    file=FileField(validators=[FileRequired()])
    submit=SubmitField('Upload')