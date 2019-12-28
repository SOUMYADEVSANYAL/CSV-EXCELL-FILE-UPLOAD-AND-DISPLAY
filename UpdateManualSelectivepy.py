#tablename choice(name,roll,email) rollno new_value(name||roll||email)
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
    t=0
    var=''
    new_name = ''
    table_name = sys.argv[1]
    roll_info = sys.argv[3]
    choice_2 = sys.argv[2]
    new_value = sys.argv[4:]

    for i in new_value:
        new_name = new_name + i + ' '
    new_name = new_name.strip().lower().title()
    # print(new_name)

    lst = choice_2.split()
    for i in lst:

        if t >=1 :
            var = var + '_' + i.title()
        else:
            var = var + i.title()
        t = t + 1

    p = str(lst)
    # print(var)
    query2 = "UPDATE "+table_name+" SET "+var+" = '"+new_name+"' WHERE Roll_Number = "+str(roll_info)
    mycursor.execute(query2)
    mydb.commit()
    print("Updated .....")
    # print(len(sys.argv))
except mysql.connector.ProgrammingError as e:
    print("Something Went Wrong :-( ,\nThis table does not exists")