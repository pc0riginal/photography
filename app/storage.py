import boto
import boto.s3

conn = boto.s3.connect_to_region('us-east-2')

def list_objects(bucket):
    bucket = conn.get_bucket(bucket)
    folders = bucket.list("","/")
    return folders

def files(bucket,name):
    bucket = conn.get_bucket(bucket)
    photos = []
    j = 0
    for i in bucket.list(name,"/"):
        if j!=0:
            photos.append(str(i).split(",")[1][:-1])
        j=1
    return photos
    
