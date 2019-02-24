import sqlite3
from sqlite3 import Error
import product
conn = sqlite3.connect('database.db')
c1=conn.cursor()

def read():
   lic = product.main()
   c1.execute('SELECT * FROM number_plate where plate_number=?',(lic,))
   r=c1.fetchone()
   if(r!=None):
      print("Number Plate Detected")
      print("The details of the Car Owner are as follows:")
      print("1. Number_Plate = " +r[0])
      print("2. Name Of the Car Owner : " +r[1])
      print("3. Phone_number : " +str(r[2]))
      print("4. Address : " +r[3])
   else:
      print("Unauthorized vehicle")
read()      
