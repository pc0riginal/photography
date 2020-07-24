from app import app
from flask import render_template,send_from_directory,url_for,request
from app import storage


bucket = 'pc0riginal'

@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html')

@app.route('/photography',methods=['POST','GET'])
def photography():
   contents = storage.list_objects(bucket)
   return render_template('photography/index.html',contents=contents)
   
@app.route('/category',methods=['POST','GET'])
def category(cat=None):
   cat = request.args.get('cat')
   photos = storage.files(bucket,cat)
   return render_template('photography/category.html',photos=photos)
   
