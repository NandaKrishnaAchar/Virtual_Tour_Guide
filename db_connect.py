import mysql.connector
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
print(read(2))
