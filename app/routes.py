from app import app
from flask import render_template,send_from_directory,url_for,request,flash
from app import storage
from app.forms import Upload
import os
from app import signed
# MYDIR = os.path.dirname(__file__)
parent_path = os.getcwd()
parent_path = os.path.join(parent_path)
bucket = 'pc0riginal'

@app.route('/')
@app.route('/index')
def index():
   print(parent_path)
   return render_template('index.html')

@app.route('/photography',methods=['POST','GET'])
def photography():
   contents = storage.list_objects(bucket)
   photoListUrl = []
   for i in contents:
      url = signed.sign('pc0riginal',str(i.name)+'thumbnail.jpg')
      photoListUrl.append((i.name,url))
   return render_template('photography/index.html',contents=photoListUrl)
   
@app.route('/category',methods=['POST','GET'])
def category(cat=None):
   cat = request.args.get('cat')
   photos = storage.files(bucket,cat)
   return render_template('photography/category.html',photos=photos)
   
@app.route('/upload',methods=['POST','GET'])
def upload():
   form = Upload()
   if form.validate_on_submit():
      files = request.files.getlist(form.files.name)
      if files:
         for f in files:
            if f.filename:
               if f.filename.split(".")[1].lower() in ['png','jpg']:
                  l = os.listdir(app.config['UPLOAD_FOLDER'])
                  if f.filename not in l:
                     k = f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
                  file_name = os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
                  response = storage.upload(bucket,form.folderName.data,file_name,f.filename)
                  if response == 1:
                     os.remove(file_name)
                     flash("successfully uploaded"+" "+f"{f.filename}","success")
                  else:
                     flash(response,"danger")
               else:
                  flash("select image only jpg and png"+" "+f"{f.filename}","danger")
   return render_template('upload.html',form=form)