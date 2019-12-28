import mysql.connector
import sys
mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='student_db')
mycursor=mydb.cursor()
from csv import DictReader
table_name=sys.argv[1]
csv_file=sys.argv[2]
with open(csv_file,'r') as f:
	reader = DictReader(f)
	reader=list(reader)
	for dic in reader:
		read_name=dic['Name']
		read_roll=dic['Roll_Number']
		read_roll=str(read_roll)
		read_email=dic['Email']
		read_email_sent='0'
		query = "INSERT INTO "+table_name+" (Name,Roll_Number,Email,Email_Sent) VALUES ('"+read_name+"','"+read_roll+"','"+read_email+"','"+read_email_sent+"')"
		try:
			mycursor.execute(query)
		except mysql.connector.errors.IntegrityError as e:
			print(read_roll+" roll already exists")
			continue
		except mysql.connector.errors.ProgrammingError as f:
			print("Table does not exist")
		# for atr,val in dic.items():
			# query2="UPDATE "+table_name+" SET "+atr+" = '"+val+"' WHERE Roll_Number = "+read_roll
			# mycursor.execute(query2)
	f.close()
	mydb.commit()