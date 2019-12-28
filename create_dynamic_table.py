#This is a basic python code to to create an empty table in the database (name mentioned below) 
#with atributes according to the .xlsx file imported.
#Points to be noted:

#File with extension .xlsx or .xls will be accepted here.
#This code will take realtive path of the file.
#The file should not have any atribute named as 'id'. If any, then this code will show duplicacy error. Table will not be created.

import mysql.connector
import xlrd
import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="student_db"
)

mycursor = mydb.cursor()

lst=[]
table_name=sys.argv[1]
loc=sys.argv[2]
table_name=str(table_name) #Just for safety
workbook=xlrd.open_workbook(loc)
sheet=workbook.sheet_by_index(0)
row_num=sheet.ncols

#Storing the atributes of the file in a list.
for i in range(row_num):
    lst.append(sheet.cell_value(0,i))

# Initializing the query with some general common phrases.
query="CREATE TABLE "+table_name+" (id INT AUTO_INCREMENT PRIMARY KEY "

# Forming the query, to create the table, according to the .xlsx file, uploaded.
for i in lst:
    query=query+", "+i+" VARCHAR(255)"
query=query+");"
mycursor.execute(query)

import excell_value_insert