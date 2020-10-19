import mysql.connector
import random
from Login_register import LoginRegister as lr
try:
	x = open("password.txt","r").readline() #extracting password from different text file

	global mydb
	mydb = mysql.connector.connect(host = 'localhost',
								database = 'reminder_database',
								user = 'root',
								password = x)
		
	global mycursor
	mycursor = mydb.cursor(buffered = True)

except Exception as e:
	print("Error in code: ",e)
###############################################################################################

''' Below function contains all the functionsd required in setreminder.py '''
class CommandFunctions(object):

	#***************
	def help(): #Showing all the commands
		print('''
		h -> help

		-show reminder -> shows all reminder

		-delete reminder all -> delete all your reminders

		-delete reminder -> delete specific reminder

		-add reminder -> adds one reminder

		-add reminders -> add more than one reminders

		-edit reminder -> edit specific reminder

		-*edit profile -> edit your user profile

		-show profile -> shows your user profile

		-logout -> log out of the profile

		delete profile -> delete your profile with reminders
			''')
	#*************************************************************************
	
	def insert(number,username): #Gotta insert reminder into the database
		try:
			for i in range(number):

				doc_name =(input("Enter The Document name: "))
				date = input("Enter the Expiry Date (in yyyy-mm-dd format): ")
				x = (doc_name, date,)
				sql = f"INSERT INTO {username} VALUES (%s,%s)"
				mycursor.execute(sql, x)
				mydb.commit()
				
				print(mycursor.rowcount, "Reminder inserted.")				
		
		
		except Exception as e: #"e" variable will store any error (If occurs)
			print(e)
	#****************************************************************

	def display_reminder(username): #To display all the reminder
		print('DOCUMENTS \t\t Expiry date')
		
		mycursor.execute(f"SELECT * FROM {username}")

		myresult = mycursor.fetchall()

		for i in myresult:
			for j in i:
				print(j,end='\t\t')
			print()		
	#******************************************************************

	def delete(number,username): #To delete n number of reminder
		if number == 1:
			CommandFunctions.display_reminder(username)
			doc = input("Enter the name of Document :")
			sql = f"DELETE FROM {username} WHERE document = %s"
			val = (doc,)
			mycursor.execute(sql,val)
		
		elif number == 2:
			sql = f"TRUNCATE TABLE {username}"
			mycursor.execute(sql)	
		
		mydb.commit()
		print(mycursor.rowcount, "record(s) deleted")
	#********************************************************************
	
	def update(username): #To edit reminder
		change = input("What you want to change?(document/date): ")
		
		if change == 'document':
			col_name ="document"
			doc = input("Enter the document name :")
			b = input("Enter Changed name: ")
		elif change == 'date':
			col_name = "expiry_date"
			doc = input("Enter the document name :")
			b = input("Enter the date: ")
		else:
			print("error! Wrong Command")
		sql = f"UPDATE {username} SET {col_name} = %s WHERE document = %s"
		val = (b, doc)

		mycursor.execute(sql, val)

		mydb.commit()

		print(mycursor.rowcount, "record(s) affected")

	def edit_profile(username):
		print("calling function")
		i=1
		while i==1:
			change = "What you want to change?(name/password/phone no)"

			if change == 'username':
				print("Sorry! You cannot chnage your username")

			elif change=="name":
				change_row="name"
				change_cell = input("Enter New name: ")
				break

			elif change=="password":
				chnage_row = "password"
				change_cell=lr.register().pw()
				break
			elif change =="phone no":
				change_row = "ph_no"
				change_cell =lr.register().ph_no()
				break
			else:
				print("Error! Wrong input!")
				
		sql ="UPDATE users SET %s=%s WHERE username = %s"
		val = (change_cell,change_row,username) 
		mycursor.execute(sql, val)

		mydb.commit()
	def show_profile(username):
		sql = "SELECT * FROM users WHERE username =%s"
		val = (username,)
		mycursor.execute(sql,val)
		mydb.commit()
		
		result = mycursor.fetchone()
		print('Name \t\t username \t\t password \t\t Phone Number')
		for i in result:
			print(i,end="\t \t")
		print()

	def delete_profile(username):
		confirmation = input(" Are you sure?(Y/n) : ")
		if confirmation == 'n':
			print("Deleting process Terminated")
			return
		elif confirmation == 'Y':
			x=random.randint(1,20)
			y=random.randint(1,20)
			z=x+y
			print("Please answer the question below: ")
			chance =0
			while True:
				test = int(input(f"what is {x}+{y}?: "))
				if test ==z:
					sql = f"DROP TABLE {username}"
					mycursor.execute(sql)
					mydb.commit()
					sql = "DELETE FROM users WHERE username =%s"
					val = (username,)
					
					mycursor.execute(sql,val)
					mydb.commit()
					print("Your profile is Deleted!")
					return
				elif chance == 2:
					print("sorry! try again!")
					return
				else:
					print("Wrong answer! You have only one more try: ")

					chance+=1
