from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    #validators用于验证输入字段是否符合预期。DataRequired验证器仅验证字段输入是否为空
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    remenber_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')