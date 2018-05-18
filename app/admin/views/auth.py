# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user
from app.admin import admin
from app.admin.forms.auth import LoginForm


@admin.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.index"))
    from app.models.user import User
    form = LoginForm()
    if form.validate_on_submit():
        user = User.getbyname(form.username.data)
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("admin.index"))
        flash("账号或密码错误")
    form.remember.data = True
    return render_template("admin/tf_login.html", form=form, site=current_app.site)


@admin.route("/register", methods=["GET", "POST"])
def register():
    return render_template("admin/tf_register.html", site=current_app.site)


@admin.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("admin.login"))
