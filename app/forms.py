
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, \
    TextAreaField, SelectField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length

from app.models import User


class RecordForm(FlaskForm):
    card_no = IntegerField('Card Number', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
    firstname = StringField('First name', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Mobile Number', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    address = StringField('Adress', validators=[DataRequired()])
    gender = SelectField(
        'Gender',
        choices=(('male', 'Male'), ('female', 'Female'),
                 ('null', 'Prefer not to answer')),
        validators=[DataRequired()]
    )
    employment = SelectField(
        'Employment',
        choices=(('student', 'Student'), ('employed', 'Employed'),
                 ('self employed', 'Self Employed'),
                 ('unemployed', 'Unemployed'),
                 ('ful time', 'Full Time Job'), ('part time', 'Part time job'),
                 ('null', 'Prefer not to answer')),
        validators=[DataRequired()]
    )
    password = StringField('Password', validators=[DataRequired()])
    password2 = StringField('Repeat Password',
        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')
