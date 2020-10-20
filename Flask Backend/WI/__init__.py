import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# from datetime import datetime

#Configs
app = Flask(__name__)

app.config['SECRET_KEY']='d45eec911428443e6d6c6c7d45eec911428443e6d6c6c7'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
os.makedirs(os.path.join(app.instance_path, 'localFileFolder'), exist_ok=True)


from WI import routes


