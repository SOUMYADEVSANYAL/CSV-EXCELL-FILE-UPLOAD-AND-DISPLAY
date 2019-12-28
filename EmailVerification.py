#table name
import mysql.connector
import smtplib
import sys
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="student_db"
)
try:
    EMAIL_ADDRESS = 'havenszen@gmail.com'
    EMAIL_PASSWORD = 'zenhavens2019.'

    table_name = sys.argv[1]
    #input("Enter table Name : ")
    mycursor = mydb.cursor()
    query2 = "SELECT * FROM " + table_name
    mycursor.execute(query2)
    myresults = mycursor.fetchall()

    for row in myresults:
        #print(row)
        if (row[4] == 0):
            query = "UPDATE " + table_name + " SET Email_Sent = '1' WHERE Name = '" + row[1] + "'"
            mycursor.execute(query)
            mydb.commit()

            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

                subject = "Congratulations ...."
                body = "This is to notify you that you have been SUCCESSFULLY REGISTERED to out Network :-) "

                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail(EMAIL_ADDRESS, row[3], msg)
                print("Your Email has been sent successfully to " + row[1])
        else:
            print("Your Verification Email has Already been sent to "+row[1])
except mysql.connector.errors.ProgrammingError as e :
    print("Something Went Wrong :-( ,\nThis table does not exists")

