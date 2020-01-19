import mysql.connector
from mysql.connector import Error
#def not_visi(id):
connection=mysql.connector.connect(host="ec2-13-233-208.ap-south-1.compute.amazonaws.com",port=3306,database="tour_guide",user="ec2-user@13.233.208.238",password="Hello123@")
cursor=connection.cursor()
#ids=1
sql_places_visited="""select place_id visited from place_visited where user_id=1"""
cursor.execute(sql_places_visited)
visited=cursor.fetchall()
print(visited)

all_places="""select id from tour1"""
cursor.execute(all_places)
places_id=cursor.fetchall()
cursor.close()
print(places_id)

