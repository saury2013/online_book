# -*- coding: utf-8 -*-

from os import path
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import datetime

from app.config_default import Config as DefaultConfig

basedir = path.abspath(path.dirname(__file__))

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()

def template_filters(app):
    @app.template_filter("friendly_time")
    def friendly_time(date):
        now = datetime.now()
        delta = now - date
        if delta.days >= 365:
            return u'%d年前' % (delta.days / 365)
        elif delta.days >= 30:
            return u'%d个月前' % (delta.days / 30)
        elif delta.days > 0:
            return u'%d天前' % delta.days
        elif delta.days < 0:
            return u"0秒前"
        elif delta.seconds < 60:
            return u"%d秒前" % delta.seconds
        elif delta.seconds < 60 * 60:
            return u"%d分钟前" % (delta.seconds / 60)
        else:
            return u"%d小时前" % (delta.seconds / 60 / 60)


def create_app():
    app = Flask(__name__)

    app.config.from_object(DefaultConfig)

    bootstrap.init_app(app)
    db.init_app(app)

    app.site = {}

    def site_context_processor():
        return dict(site=app.site)

    app.context_processor(site_context_processor)

    login_manager.init_app(app)

    from app.web import web
    app.register_blueprint(web)

    from app.admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    from app.api import api
    app.register_blueprint(api, url_prefix="/api")

    template_filters(app)

    login_manager.login_view = "admin.login"
    login_manager.login_message = "请先登录!!!"

    return app


def init_site_user(app):
    from app.models.site import SiteMeta
    from app.models.user import User
    # metas = {
    #     "name": 'site1',
    #     "description": "这是一个书籍站点",
    #     "about": "这个地方可以用来介绍您自己，或者您的网站。"
    # }
    # SiteMeta.add(metas)
    # User.add('allen', '123')
    app.start = True
    # set_site(app)



