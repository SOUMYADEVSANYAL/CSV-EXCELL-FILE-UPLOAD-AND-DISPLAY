#table name
import mysql.connector, sys

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="student_db"
)

mycursor = mydb.cursor()

try:

    query2 = "SELECT * FROM " + sys.argv[1] + " WHERE Name = '' or Email = '' or Roll_Number = 0"
    mycursor.execute(query2)
    vacant = mycursor.fetchall()
    if vacant is not []:
        print("You have some vacant columns ! ! ")
    query3 = "DELETE FROM " + sys.argv[1] + " WHERE Name = '' or Email = '' or Roll_Number = 0"
    mycursor.execute(query3)
    mydb.commit()
except mysql.connector.ProgrammingError as e:
    print("Something Went Wrong :-( ,\nThis table does not exists")
