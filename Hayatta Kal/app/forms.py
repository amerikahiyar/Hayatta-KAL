from flask_wtf import FlaskForm
from wtforms import StringField ,IntegerField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired ,Length,NumberRange

class Registration(FlaskForm):
    username = StringField('Username',  validators=[DataRequired(),Length(min=2,max=20)])
    complaint = StringField('Complaint',  validators=[DataRequired()])  
    age =IntegerField('Age', validators=[DataRequired(),NumberRange(min=0,max=120)])

    submit =SubmitField('Create a new User')
