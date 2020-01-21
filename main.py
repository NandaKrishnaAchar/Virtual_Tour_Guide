import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify,render_template
from werkzeug.utils import secure_filename
from keras.preprocessing import image
import numpy as np
from keras.models import load_model
import os
import db_connect as db
import link as lk
import distance
from db_connect import all_ids,add_to_db,for_admin,name_to_id

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
mydict={}
place_name_global=""
new_visinity=[]
def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/comment_fetch/',methods=['GET'])
def comment_fetch():
    return jsonify({'comment':[['Testing Comment1'],['Testing Comment2']]})


@app.route('/comment_write/',methods=['POST'])
def comment():
    data = request.get_json()
    print(data['userid'])
    print(data['comment'])
    print(data['placeid'])
    return jsonify({'comment':[['Testing Comment1'],['Testing Comment2']]})



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
                print("Jevaaaaaaaaaaaaaaaaaaaa "+ filename)
                userid=filename[:-7]
                usr_id=name_to_id(userid)
                print(userid)
                os.rename(filename,"im.jpeg")
                clf=image_identifier()
                os.remove("im.jpeg")
                record = db.read(clf)
                place_name=record[0][1]
                monument=record[0][2]
                lat=record[0][4]
                log=record[0][5]
                """
                data=request.form['ke']
                print("Yesssssssssssss " + data)
                """
                print(monument,lat,log)

                visinity=distance.sort_dist(place_name)
            
                o_ltlng=db.latlong(clf) #origin place id
                #d_ltlng=db.latlong(visinity[0][0]) #destination place id
                
                global mydict
                if userid in mydict:
                    global new_visinity
                    places=mydict[userid]
                    print("nihal*******************************************",places)
                    print("))))))))))))))))))))))))))))))))))))))))))))",clf)
                    #print(type(places)
                    # places=np.asarray(places)
                    try:
                        #places=np.delete(places,clf)
                    
                        places.remove((clf,))
                    except:
                        print("Baaaaddddd")
                        return {}
                    
                    mydict[userid]=places
                    add_to_db(usr_id,clf)
                    if (mydict[userid])==[]:
                        del mydict[userid]
                        #global 
                        
                        new_visinity.clear()
                        

                        v1='None'
                        d1='None'
                        t1='None'
                        l1='None'
                        v2='None'
                        d2='None'
                        t2='None'
                        l2='None'
                
                        resp = jsonify({'message' : 'File successfully uploaded',
                        'clas': monument,'place_id':clf,'place_name':place_name, 
                        'v1':v1,'d1':d1,'t1':t1,'l1':l1,'v2':v2,'d2':d2,'t2':t2,'l2':l2 })
                        resp.status_code = 201
                        return resp 
                        #resp=jsonify({'message':"the tour is over bye"})
                        #return resp
                    
                    #visinity=distance.sort_dist(place_name_global)
                    i=0
                                    
                    visinity=new_visinity
                    for v in visinity:
                        if v[0] not in mydict[userid]:
                            new_visinity.remove(v)
                    if(len(mydict[userid])==0):
                        new_visinity=[]

                        v1='None'
                        d1='None'
                        t1='None'
                        l1='None'
                        v2='None'
                        d2='None'
                        t2='None'
                        l2='None'
                
                        resp = jsonify({'message' : 'File successfully uploaded',
                        'clas': monument,'place_id':clf,'place_name':place_name, 
                        'v1':v1,'d1':d1,'t1':t1,'l1':l1,'v2':v2,'d2':d2,'t2':t2,'l2':l2 })
                        resp.status_code = 201
                        return resp 

                else:
                    places=all_ids()
                    print(places)
                    #places=np.asarray(places)
                    #places=np.delete(places,clf)
                    print(places)
                    print(clf)
                    try:
                        places.remove((clf,))
                    except:
                        return resp
                    mydict[userid]=places
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",mydict[userid])
                    
                    place_name_global=place_name
                    add_to_db(usr_id,clf)
                    new_visinity=distance.sort_dist(place_name_global)
                d_ltlng=db.latlong(visinity[0][0]) #destination placeid bro       
                
                for v in new_visinity:
                    lnk=lk.url(o_ltlng[0],o_ltlng[1],v[2],v[3])
                    v.append(lnk)
                print(visinity)
                places=all_ids()
                                
                if(len(new_visinity)==len(places)-1):
                
                    v1=new_visinity[0][1]
                    d1=new_visinity[0][4]
                    t1=new_visinity[0][5]
                    l1=new_visinity[0][6]
                    v2=new_visinity[1][1]
                    d2=new_visinity[1][4]
                    t2=new_visinity[1][5]
                    l2=new_visinity[1][6]
                
                elif(len(new_visinity)==len(places)-2):
                    v1=new_visinity[0][1]
                    d1=new_visinity[0][4]
                    t1=new_visinity[0][5]
                    l1=new_visinity[0][6]
                    v2='None'
                    d2='None'
                    t2='None'
                    l2='None'
                else:
                    v1='None'
                    d1='None'
                    t1='None'
                    l1='None'
                    v2='None'
                    d2='None'
                    t2='None'
                    l2='None'
                
                resp = jsonify({'message' : 'File successfully uploaded',
                    'clas': monument,'place_id':clf,'place_name':place_name, 
                    'v1':v1,'d1':d1,'t1':t1,'l1':l1,'v2':v2,'d2':d2,'t2':t2,'l2':l2 })
                resp.status_code = 201
                return resp 
        else:
                resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
                resp.status_code = 400
                return resp

@app.route('/auth/', methods=['POST'])
def addOne():
    data = request.get_json()
    print(data['email'],data['pass'])
    return jsonify({'auth' : db.auth(data['email'],data['pass'])})

@app.route('/signup/',methods=['POST'])
def signup():
    data = request.get_json()
    return jsonify({'auth':db.signup(data['name'],data['email'],data['pass'])})
@app.route('/admin',methods=["get"])
def admin():
    records=for_admin()
    return render_template("list_page.html",records=records)

def image_identifier():
    clf = load_model('my_model_sjce.h5')
    img = image.load_img('im.jpeg', target_size=(64,64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    classes = clf.predict_classes(x, batch_size=10)
    return int(classes)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
