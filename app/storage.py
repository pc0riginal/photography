import boto
import boto.s3
import boto3
import PIL
from PIL import Image
from botocore.exceptions import NoCredentialsError
import math
from app import app
from app import signed
from botocore.client import Config


conn = boto.s3.connect_to_region('us-east-2')
s3 = boto3.resource('s3')
client = boto3.client('s3')

def list_objects(bucket):
    bucket = conn.get_bucket(bucket)
    folders = bucket.list("","/")
    return folders

def files(bucket,name):
    # bucket = conn.get_bucket(bucket)
    photos = []
    obj = client.list_objects_v2(Bucket=bucket,Prefix=name)
    for i in obj['Contents']:
        rs = signed.sign(bucket,str(i['Key']))
        photos.append(rs)
    return photos
    
def compress_file(file_name):
    foo = Image.open(file_name)
    x,y = foo.size
    x2,y2 = math.floor(x-50),math.floor(y-20)
    foo = foo.resize((x2,y2),Image.ANTIALIAS)
    foo.save(file_name,quality=75)

def upload(bucket,folder,f,file_name):
    bucket = conn.get_bucket(bucket)
    errors= ['folder not exist','file already there','error']
    # l = files('pc0riginal',folder)
    l = []
    for i in bucket.list(folder,"/"):
        l.append(str(i))
    if bucket.list(folder,"/"):
        try:
            if len(l) == 0:
                ext = file_name.split(".")[1]
                if ext.lower() in ['png']:
                    im1 = Image.open(f)
                    if im1.mode in ("RGBA", "P"):
                        im1 = im1.convert("RGB")
                    im1.save(os.path.join(app.config['UPLOAD_FOLDER'],"thumbnail.jpg"))
                    f = os.path.join(app.config['UPLOAD_FOLDER'],"thumbnail.jpg")
                file_name = "thumbnail.jpg"
                # file_name = 'thumbnail'+'.'+file_name.split(".")[1]
            # files = s3.Bucket('pc0riginal').objects.filter(Prefix=folder+'/')
            compress_file(f)
            response = s3.meta.client.upload_file(Filename=f,Bucket='pc0riginal',Key=folder+'/'+file_name)
        except FileNotFoundError:
            return "The file was not found"
        except NoCredentialsError:
            return "Credentials not available"
    else:
        return errors[0]
    return 1


