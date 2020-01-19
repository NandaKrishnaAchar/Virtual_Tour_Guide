import googlemaps
from datetime import datetime
import  urllib.request, json
import db_connect
gmaps = googlemaps.Client(key="AIzaSyDPhQDt6hkdyeWaYO0FtFwqZSHBCaN6L0M")


def dist_time(cur_place,dst_place):
    now = datetime.now()
    directions_result = gmaps.directions(cur_place,
                                         dst_place,
                                         mode="transit",
                                         departure_time=now)
    
    dir1=directions_result[0]
    dir2=dir1['legs']
    dir2=dir2[0]
    
    return dir2['distance']['text'],dir2['duration']['text']


def placeid(place_name):
    p1=gmaps.geocode(place_name)[0]
    return p1['place_id']



def placeinfo(place_name):
    
    pid=placeid(place_name)
    url = "https://maps.googleapis.com/maps/api/place/details/json?place_id="+pid+"&fields=name,rating,formatted_phone_number,opening_hours&key=AIzaSyDPhQDt6hkdyeWaYO0FtFwqZSHBCaN6L0M"

    response = urllib.request.urlopen(url)
    
    data = json.loads(response.read())
    t=data['result']['opening_hours']['periods']
    
    return data['result']['rating'],t[datetime.datetime.today().weekday()-1]


def sort_dist(place_name):
    placeid= db_connect.plname_to(place_name)
    placeid=placeid[0][0]

    cords=db_connect.latlng_rad(placeid)
    distance=[]
    for i in range(len(cords)):
        dstname=db_connect.plid_to(cords[i])
        dstname=dstname[0][0]
        print(place_name+"\t"+dstname)
        now = datetime.now()
        directions_result = gmaps.directions("Sri Shivaratari Swamiji Statue",
                                        "Golden Jublee Bhavan",
                                         mode="transit",
                                             departure_time=now)

        dir1=directions_result[0]
        dir2=dir1['legs']
        dir2=dir2[0]
        print(dir2['distance']['text']+"\n")

        print(dir2['duration']['text']+"\n")



        distance.append(dis)
    print(distance)


'''
url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJ____T-l6rzsRetB4_MuX1xo&fields=name,rating,formatted_phone_number,opening_hours&key=AIzaSyDPhQDt6hkdyeWaYO0FtFwqZSHBCaN6L0M"

response = urllib.request.urlopen(url)

data = json.loads(response.read())

print(data)
'''
