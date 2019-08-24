from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField,TextAreaField,BooleanField, SelectField
from wtforms.validators import DataRequired,Required, Length, Email, Regexp
from ..models import Role, User


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')



class EditProfileForm(Form):
	name = StringField('Real name', validators=[Length(1,64)])
	location = StringField('location', validators=[Length(0,64)])
	about_me = TextAreaField('about_me')
	submit = SubmitField('Submit')




class EditProfileAdminForm(Form):
	email = StringField('Email', validators=[Required(), Length(1,64), Email()])
	username = StringField('username', validators=[Required(), Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or undersocres')])
	confirmed = BooleanField('Confirmed')
	role = SelectField('Role', coerce=int)
	name = StringField('Real name', validators=[Length(1,64)])
	loacation = StringField('Location', validators=[Length(1,64)])
	about_me = TextAreaField('About_me')
	submit = SubmitField('Submit')

	def __init__(self, user, *args, **kwargs):
		super(EditProfileAdminForm, self).__init__(*args, **kwargs)
		self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
		self.user = user

	def vaildate_email(self, field):
		if field.data != self.user.email and \
				User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')

	def vaildate_username(self, field):
		if field.data != sefl.user.username and \
				User.query.filter_by(username=field.data).first():
			raise VaildationError('username already in use.')


#博客发表的表单
class PostForm(Form):
	body = TextAreaField("what's on your mind?", validators=[Required()])
	submit = SubmitField('Submit')