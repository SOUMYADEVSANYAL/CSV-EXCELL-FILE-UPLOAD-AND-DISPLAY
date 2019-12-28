#table name
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
    query = "DELETE t1 FROM " + table_name + " t1 INNER JOIN " + table_name + " t2 WHERE t1.id>t2.id AND t1.Roll_Number = t2.Roll_Number"
    mycursor.execute(query)
    mydb.commit()
    print("Duplicates Removed Successfully :-) ")
except mysql.connector.ProgrammingError as e:
    print("Please enter a valid table name !! ")