#table name
import mysql.connector,sys

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="student_db"
)
try:
    mycursor = mydb.cursor()
    table_info = sys.argv[1]
    query = "SELECT * FROM cse"
    mycursor.execute(query)
    myresults = mycursor.fetchall()
    print()
    print("NAME".center(30,' ')+"ROLL NUMBER".center(15,' ')+"EMAIL".center(30,' '))
    # print("ID".center(5,' ')+"NAME".center(30,' ')+"ROLL NUMBER".center(15,' ')+"EMAIL".center(30,' '))
    print("".center(80,'='))
    for row in myresults:
        # print(str(row[0]).center(5,' '),end='')
        print(row[1].center(30,' '),end='')
        print(str(row[2]).center(15, ' '),end='')
        print(row[3].center(30, ' '))
    print("".center(80,'='))
except mysql.connector.ProgrammingError as e:
    print("Something Went Wrong :-( ,\nThis table does not exists")