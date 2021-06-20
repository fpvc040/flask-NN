import flask
import werkzeug
import cv2
import numpy as np
import json
from minio import Minio
from minio.error import S3Error 
app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    
    data = flask.request.form.to_dict()
    json_data = json.loads(data['json'])
    imagefile.save(json_data['imageName'])
    try:
        print("image uploaded. Size is " + str(cv2.imread(filename).shape))
    except:
        return "image uploaded. Save was wrong"

    client = Minio(
        "192.168.1.193:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )
    print("Client Initiated")

    found = client.bucket_exists("distattrip")
    print("Found:", found)
    if not found:
        client.make_bucket("distattrip")
    else:
        print("Found distattrip bucket")

    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
    client.fput_object(
        "distattrip", json_data['imageName'], json_data['imageName'],
    )
    return "image is successfully uploaded as " + \
        "object '" + json_data['imageName'] + "'' to bucket 'distattrip'."
    




app.run(host="0.0.0.0", port=5000, debug=True)
