import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
from keras.preprocessing import image
import numpy as np
from keras.models import load_model
import os
import db_connect as db
import link as lk

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file/', methods=['POST'])
def upload_file():
        # check if the post request has the file part
        if 'file' not in request.files:
                resp = jsonify({'message' : 'No file part in the request'})
                resp.status_code = 400
                return resp
        file = request.files['file']
        if file.filename == '':
                resp = jsonify({'message' : 'No file selected for uploading'})
                resp.status_code = 400
                return resp
        if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                
                os.rename(filename,"im.jpeg")
                clf=image_identifier()
                os.remove("im.jpeg")
                record = db.read(clf)
                monument=record[0][2]
                lat=record[0][4]
                log=record[0][5]
                print(monument,lat,log)

                #https://www.google.com/maps/dir/?api=1&origin=12.311570,76.613735&destination=12.316117,76.614168

                o_ltlng=db.latlong(1)
                d_ltlng=db.latlong(2)

                resp = jsonify({'message' : 'File successfully uploaded','clas': monument, 'link':lk.url(o_ltlng[0],o_ltlng[1],d_ltlng[0],d_ltlng[1]) })
                resp.status_code = 201
                return resp
        else:
                resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
                resp.status_code = 400
                return resp


def image_identifier():
    clf = load_model('my_model_sjce.h5')
    img = image.load_img('im.jpeg', target_size=(64,64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    classes = clf.predict_classes(x, batch_size=10)
    return int(classes)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
