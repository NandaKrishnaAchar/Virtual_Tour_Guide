from db_connect import visited,all_ids
import numpy as np
def not_visited(userid):
    vis=[]
    record=visited(userid)
    print(record)

    vis=np.asarray(record)
    print(vis)

    if(vis[0]==1):
        print("YASS")

    record=all_ids()
    print(record)

    all=np.asarray(record)
    print(all)

    i=len(all)
    j=len(vis)
    print(i,j)
    not_vis=[]
    while i!=0:
        j=len(vis)
        for x in vis:
            if(all[i-1]!=vis[j-1]):
                j=j-1
                if(j==0):
                    not_vis.append(all[i-1])
                continue
            elif(all[i-1]==vis[j-1]):
                break
        i=i-1

    print(not_vis)
    return not_vis
