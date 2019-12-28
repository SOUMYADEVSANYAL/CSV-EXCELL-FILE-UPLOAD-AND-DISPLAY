#tablename rollno(update) email rollno(new) name
import mysql.connector
import sys
# def update(x):
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd="",
#         database="student_db"
#     )
#     id_no = str(x)
#     # print(type(id_no))
#     mycursor = mydb.cursor()
#     name = input("Enter Name : ")
#     email = input("Enter Email : ")
#     roll = input("Enter Roll Number : ")
#     query = "UPDATE cse SET Name = '"+name+"', Email = '"+email+"', Roll_Number = "+roll+" WHERE id = "+id_no
#
#     mycursor.execute(query)
#     mydb.commit()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="student_db"
)
try:

    new_name = ''
    table_name = sys.argv[1]
    roll_info = sys.argv[2]
    # int(input("Enter id : "))
    # print(type(id_no))
    mycursor = mydb.cursor()
    name = sys.argv[5:]
    email = sys.argv[3]
    roll = sys.argv[4]

    for i in name:
        new_name = new_name + i + ' '
    new_name = new_name.strip().lower().title()
    print(new_name)

    query = "UPDATE "+table_name+" SET Name = '"+new_name+"', Email = '"+email+"', Roll_Number = "+roll+" WHERE Roll_Number = "+str(roll_info)

    mycursor.execute(query)
    mydb.commit()
    print("Successfully Updated :->")

except mysql.connector.ProgrammingError as e:
    print("Something Went Wrong :-( ,\nThis table does not exists")

