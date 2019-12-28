#table name
import mysql.connector
import sys
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='student_db'
)
try:
    table_name = sys.argv[1]
    #input("Enter table name : ")
    mycursor = mydb.cursor()

    query = "CREATE TABLE `student_db`.`" + table_name + "` ( `id` INT(255) NOT NULL AUTO_INCREMENT , `Name` VARCHAR(255) NOT NULL , `Roll_Number` INT(255) NOT NULL , `Email` VARCHAR(255) NOT NULL , `Email_Sent` INT(255) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB"
    mycursor.execute(query)
    mydb.commit()
except mysql.connector.errors.ProgrammingError as e:
    print("Table Already exist !!!")





