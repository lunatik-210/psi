from wtforms import *
from wtforms.validators import Required

class SigninForm(Form):
    username = TextField('Username', validators=[Required(),
                                                 validators.Length(min=3, message=(
                                                 u'Your username must be a minimum of 3'))])
    password = PasswordField('Password', validators=[Required(),
                                                     validators.Length(min=1, message=(
                                                     u'Please give a longer password'))
    ])
    remember_me = BooleanField('Remember me', default=False)