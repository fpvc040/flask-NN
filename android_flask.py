import flask
import werkzeug
import cv2
import numpy as np
import json 
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
        return "image uploaded. Size is " + str(cv2.imread(filename).shape)
    except:
        return "image uploaded"



app.run(host="0.0.0.0", port=5000, debug=True)
