import mysql.connector
import xlrd
import sys

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="student_db")

mycursor=mydb.cursor()

lst=[]
table_name=sys.argv[1]
loc=sys.argv[2]
table_name=str(table_name) #Just for safety to make it a string.
workbook=xlrd.open_workbook(loc)
sheet=workbook.sheet_by_index(0)
row_num=sheet.ncols

#Storing the atributes of the file in a list.
for i in range(row_num):
    lst.append(sheet.cell_value(0,i))

for i in range(1,sheet.nrows):
    # query="INSERT INTO customers (name, address) VALUES (%s, %s)"

    query="INSERT INTO "+table_name+" (id"

    #Making the atribute part of the query
    for atr in lst:
        query=query+","+atr
    query=query+") VALUES (''"

    #Making the value part of the query
    for j in range(sheet.ncols):
        query=query+",'"+str(sheet.cell_value(i,j))+"'"
    query=query+")"
    mycursor.execute(query)
mydb.commit()