# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
    username = StringField("用户名", validators=[DataRequired("用户名不能为空")])
    password = PasswordField("密码", validators=[DataRequired("密码不能为空")])
    remember = BooleanField("记住我")