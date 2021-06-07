import flask
import werkzeug
import cv2
import numpy as np
app = flask.Flask(__name__)

# CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
#     "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
#     "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
#     "sofa", "train", "tvmonitor"]
# COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)
    try:
        return "image uploaded. Size is " + str(cv2.imread(filename).shape)
    except:
        return "image uploaded"



app.run(host="0.0.0.0", port=5000, debug=True)
