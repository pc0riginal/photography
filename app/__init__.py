from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = 'app\static\\temp'
from app import routes 