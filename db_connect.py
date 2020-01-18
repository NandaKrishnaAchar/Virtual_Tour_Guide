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
         sql_fetch_query = """insert into place_visited value(%s,%s)"""
         record1=(userid,placeid)
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query,record1)
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



