from flask import Flask
from config import Config
import os 
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = 'app/tmp'
app.jinja_env.filters['zip'] = zip
from app import routes 