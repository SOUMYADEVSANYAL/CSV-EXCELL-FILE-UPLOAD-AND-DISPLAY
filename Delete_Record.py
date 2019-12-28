#table name, roll no
import mysql.connector
import sys
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="student_db"
)

try:
    mycursor = mydb.cursor()
    table_name = sys.argv[1]
    roll_info = sys.argv[2]
    # int(input("Enter ID : "))

    query = "DELETE FROM " + table_name + " WHERE Roll_Number = " + str(roll_info)
    mycursor.execute(query)
    mydb.commit()
    print("Deleted Successfully .... ")
except mysql.connector.ProgrammingError as e:
    print("Please enter a valid table Name ->")