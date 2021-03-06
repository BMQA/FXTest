from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import lod
from apscheduler.schedulers.background import BackgroundScheduler
from config import jobstores, executors
from flask_admin import Admin
from flask_moment import Moment

app = Flask(__name__)
conf = lod()
loginManager = LoginManager(app)
app.config.from_object(conf)
bootstrap = Bootstrap(app)
loginManager.session_protection = "strong"
loginManager.login_view = 'home.login'
loginManager.login_message = u'测试平台必须登录，请登录！'
db = SQLAlchemy(app)
moment = Moment(app)
sched = BackgroundScheduler(jobstores=jobstores, executors=executors)
admin = Admin(app, name=u'质量管理系统后台', template_mode='bootstrap3')
from app import views, models, url, apiadmin
