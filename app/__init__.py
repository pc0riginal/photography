from flask import Flask
from config import Config
import os 
MYDIR = os.path.dirname(__file__)

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = 'app/static/images'
from app import routes 