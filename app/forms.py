from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FloatField, DateField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Optional, NumberRange, Regexp

# Simple email check — must contain @ and a dot after it
EMAIL_REGEX = r'^[^@\s]+@[^@\s]+$'

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Email is required'),
        Regexp(EMAIL_REGEX, message='Enter a valid email (must contain @)')
    ])
    password = PasswordField('Password', validators=[DataRequired(message='Password is required')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    badge_id = StringField('Badge ID', validators=[DataRequired(), Length(min=3, max=20)])
    full_name = StringField('Full Name', validators=[DataRequired(), Length(max=100)])
    rank = StringField('Rank', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[
        DataRequired(message='Email is required'),
        Regexp(EMAIL_REGEX, message='Enter a valid email (must contain @)')
    ])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message='Password must be at least 6 characters')])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')


class ViolationForm(FlaskForm):
    vehicle_number = StringField('Vehicle Number', validators=[DataRequired(), Length(max=20)])
    violation_type = SelectField('Violation Type', choices=[
        ('No Helmet', 'No Helmet'),
        ('Overspeeding', 'Overspeeding'),
        ('Signal Jump', 'Signal Jump'),
        ('No Seatbelt', 'No Seatbelt'),
        ('Drunk Driving', 'Drunk Driving'),
        ('Wrong Parking', 'Wrong Parking'),
        ('Other', 'Other')
    ], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), Length(max=200)])
    date = DateField('Date', validators=[DataRequired()])
    fine_amount = FloatField('Fine Amount', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Save Violation')


class UpdateStatusForm(FlaskForm):
    status = SelectField('Status', choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], validators=[DataRequired()])
    payment_reference = StringField('Payment Reference', validators=[Optional(), Length(max=100)])
    submit = SubmitField('Update Status')