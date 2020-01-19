#from routing import not_visited
from db_connect import all_ids,add_to_db
from distance import sort_dist

#def next_place(key,dvr):
place_name="Quadrangle"
dvr=sort_dist(place_name)
print(dvr)
all_id=all_ids()
mydict={}
key=4
mydict[1]=dvr
mydict[2]=dvr
if(len(all_id)==len(dvr)):
    #new user adding to dictionary
    visi=dvr.pop(0)
    mydict[key]=dvr
    print(mydict)
    print(visi)
    add_to_db(key,visi)
    print("place visisted has been stored in db")
elif(mydict[key]==[]):
    #empty values deleted
    del mydict[key]
    print("your travel is over")
else:
    print(mydict)
    #telling next place
    print(mydict[key])
    list=mydict[key]
    next=list[0]
    print("This is the new place")
    print(next)
    print("store this in dabatabse")
    add_to_db(key,next)
    print("added to db")
    list.pop(0)
    print("new place_id")
    print(list)
    mydict[key]=list
    
    #return next

