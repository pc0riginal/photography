from app import app
from flask import render_template,send_from_directory,url_for,request,flash
from app import storage
from app.forms import Upload
import os
MYDIR = os.path.dirname(__file__)
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
   
@app.route('/upload',methods=['POST','GET'])
def upload():
   form = Upload()
   if form.validate_on_submit():
      files = request.files.getlist(form.files.name)
      if files:
         for f in files:
            if f.filename:
               if f.filename.split(".")[1].lower() in ['png','jpg']:
                  l = os.listdir(MYDIR + "/" +app.config['UPLOAD_FOLDER'])
                  if f.filename not in l:
                     k = f.save(os.path.join(MYDIR , app.config['UPLOAD_FOLDER'],f.filename))
                  file_name = os.path.join(MYDIR ,app.config['UPLOAD_FOLDER'],f.filename)
                  response = storage.upload(bucket,form.folderName.data,file_name,f.filename)
                  if response == 1:
                     os.remove(file_name)
                     flash("successfully uploaded"+" "+f"{f.filename}","success")
                  else:
                     flash(response,"danger")
               else:
                  flash("select image only jpg and png"+" "+f"{f.filename}","danger")
   return render_template('upload.html',form=form)