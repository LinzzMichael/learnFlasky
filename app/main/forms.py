from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired,Required, Length


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')



class EditProfileForm(Form):
	name = StringField('Real name', validators=[Length(1,64)])
	location = StringField('location', validators=[Length(0,64)])
	about_me = TextAreaField('about_me')
	submit = SubmitField('Submit')