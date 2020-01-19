import db_connect
import googlemaps
from datetime import datetime
import  urllib.request, json
import gmao

def sort_dist(place_name):
    placeid= db_connect.plname_to(place_name)
    placeid=placeid[0][0]
    cur_address=db_connect.pid_to_address(placeid)
    cur_address=cur_address[0][0]
    cords=db_connect.latlng_rad(placeid)
    distance=[]
    for i in range(len(cords)):
        dstname=db_connect.plid_to(cords[i])
        dstname=dstname[0][0]
        dstaddr=db_connect.pid_to_address(cords[i])
        dstaddr=dstaddr[0][0]
        dis=gmao.dist_time(cur_address,dstaddr)
        dis_lis=list(dis)
        dis_lis.insert(0,dstname)
        dis_lis.insert(0,cords[i])
        ltlg=db_connect.latlong(cords[i])
        dis_lis.insert(2,float(ltlg[0]))
        dis_lis.insert(3,float(ltlg[1]))
        distance.append(dis_lis)
    distance=sorted(distance, key = lambda x: x[4])

    return distance
     
