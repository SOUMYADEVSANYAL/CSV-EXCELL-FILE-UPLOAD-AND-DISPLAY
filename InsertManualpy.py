#table name email rollno name
import mysql.connector , sys

import mysql.connector
import sys
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="student_db"
)
try:
    new_name=''
    mycursor = mydb.cursor()
    table_name = sys.argv[1]
    name = sys.argv[4:]

    for i in name:
        new_name = new_name + i + ' '
    new_name = new_name.strip().lower().title()
    print(new_name)
    email = sys.argv[2]
    roll = sys.argv[3]
    query = "INSERT INTO "+table_name+"(Name,Roll_Number,Email) VALUES('"+new_name+"',"+roll+",'"+email+"')"
    mycursor.execute(query)
    mydb.commit()
except mysql.connector.ProgrammingError as e:
    print("Something Went Wrong :-( ,\nThis table does not exists")