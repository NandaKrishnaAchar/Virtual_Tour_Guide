import mysql.connector
from math import sin, cos, sqrt, atan2,radians
from mysql.connector import Error
def read(key):
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="tour_guide",user= "ec2-user@13.233.208.238",password= "Hello123@") 
         cursor = connection.cursor()
         sql_fetch_query = """SELECT * from tour1 where place_id=%s"""
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query,(key,))
         record = cursor.fetchall()

         
         return record 
    
    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



def all_ids():
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="tour_guide",user= "ec2-user@13.233.208.238",password= "Hello123@") 
         cursor = connection.cursor()
         sql_fetch_query = """select place_id from tour1"""
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query)
         record = cursor.fetchall()
         return record 
    
    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



def visited(key):
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="tour_guide",user= "ec2-user@13.233.208.238",password= "Hello123@") 
         cursor = connection.cursor()
         sql_fetch_query = """SELECT place_id from place_visited where userid=%s"""
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query,(key,))
         record = cursor.fetchall()
         return record 
    
    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



def add_to_db(userid,placeid):
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="tour_guide",user= "ec2-user@13.233.208.238",password= "Hello123@") 
         cursor = connection.cursor()
         sql_fetch_query = """insert into place_visited (userid,place_id) values(%s,%s)"""
         record1=(userid,placeid)
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query,record1)
         print("stored in db_connect")
         connection.commit()
         
    
    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def latlng_rad(pid):
    try:
    
            connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="tour_guide",user= "ec2-user@13.233.208.238",password= "Hello123@")
            cursor = connection.cursor()
            sql_fetch_query = """select latitude,longitude,place_id from tour1 where place_id<>%s"""
            print(sql_fetch_query)
            cursor.execute(sql_fetch_query,(pid,))
            record = cursor.fetchall()
            sql_fetch_query = """select latitude,longitude,place_id from tour1 where place_id=%s"""
            print(sql_fetch_query)
            cursor.execute(sql_fetch_query,(pid,))
            record1 = cursor.fetchall()
            R = 6373.0
            print(record1)
            lat1 = radians(float(record1[0][0]))
            lon1 = radians(float(record1[0][1]))
            print(lat1)
            print(lon1)
            place_id=[]
            for i in range(len(record)):
                placeid=record[i][2]
                lat2 = radians(float(record[i][0]))
                lon2 = radians(float(record[i][1]))
                
                dlon = lon2 - lon1
                dlat = lat2 - lat1
                
                a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))
                
                distance = R * c
                if distance<2:
                    place_id.append(placeid)
            return place_id


    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def latlong(key):
    
                            #Code from Nanda
    try:
        
        connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="tour_guide",user= "ec2-user@13.233.208.238",password= "Hello123@") 
        cursor = connection.cursor()
        sql_fetch_query = """select latitude,longitude from tour1 where place_id=%s"""
        print(sql_fetch_query)
        cursor.execute(sql_fetch_query,(key,))
        record = cursor.fetchall() 
        return record[0] 
    except mysql.connector.Error as error:
        print("Failed to read data from MySQL table {}".format(error))
        return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def plname_to(place_name):
     try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="tour_guide",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         sql_fetch_query = """SELECT place_id from tour1 where place_name=%s"""
         cursor.execute(sql_fetch_query,(place_name,))
         record = cursor.fetchall()


         return record

     except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

     finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def plid_to(place_id):
     try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="tour_guide",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         sql_fetch_query = """SELECT place_name from tour1 where place_id=%s"""
         cursor.execute(sql_fetch_query,(place_id,))
         record = cursor.fetchall()


         return record

     except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1
     finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def pid_to_address(place_id):
     try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="tour_guide",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         sql_fetch_query = """SELECT address from tour1 where place_id=%s"""
         cursor.execute(sql_fetch_query,(place_id,))
         record = cursor.fetchall()


         return record

     except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1
     finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



def auth(email,pas):
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="tour_guide",user= "ec2-user@13.233.208.238",password= "Hello123@") 
         cursor = connection.cursor()
         sql_fetch_query = """select password from usr where email=%s"""
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query,(email,))
         o_pass = cursor.fetchall()

         try:
             
             if(o_pass[0][0]==str(pas)):
                return email
             return 0
         except:
             return 0 
    
    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def signup(name,email,pas):
    try:
        connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="tour_guide",user= "ec2-user@13.233.208.238",password= "Hello123@") 
        cursor = connection.cursor()
        sql_fetch_query = """insert into usr(name,email,password) values(%s,%s,%s);
"""
        print(sql_fetch_query)
        print(cursor.execute(sql_fetch_query,(name,email,pas,)))
        connection.commit()
        return email

    except mysql.connector.Error as error:
        print("Failed to read data from MySQL table {}".format(error))
        return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

print(auth('email2','123'))
