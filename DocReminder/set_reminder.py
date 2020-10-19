import mysql.connector

#files:
from functions import CommandFunctions as cf
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

print(''' 
*****************************************************************************
*********************** WELCOME TO DOCUMENT REMINDER ************************
 IT REMINDS YOU OF YOUR EXPIRING DOCUMENTS SO YOU NEVER FORGET TO RENEW THEM!
*****************************************************************************

FOR HELP WITH COMMANDS, TYPE "h", TO GET BACK TO PREVIOUS MENU, TYPE "back" AND TO EXIT, TYPE "exit"

*****************************************************************************
	''')
'''
		Below function is the main function that will be using all functions in " function.

'''

def reminder_setting(username):
	print() 
	print("Please enter your command below:")
	
	while True:
		main_input=input(">>")
		#To show all reminder from database
		if main_input == 'show reminder':
			x=cf.display_reminder(username)
			print()
		#To add a reminder in database
		elif main_input == "add reminder":
			x=cf.insert(1,username)
			print()
		#To add more than one reminder into the database
		elif main_input == "add reminders":
			no = int(input("How many Documents You want to insert : "))
			x=cf.insert(no,username)
			print()
		#To delete a reminder from database
		elif main_input == "delete reminder" :
			x=cf.delete(1,username)
			print()
		#To delete all reminder from database
		elif main_input == "delete reminder all" :
			x=cf.delete(2,username)	
			print()
		#To edit any reminder form databse
		elif main_input == "edit reminder" :
			x=cf.update(username)
			print()
		#To show all the inputs that can be given to the program	
		elif main_input == "h":
			x=cf.help()
			print()
		#To edit the profile
		elif main_input == "edit profile":
			x=cf.edit_profile(username)
			print()
		#To show user his/her profile
		elif main_input == "show profile":
			x=cf.show_profile(username)
		#To delete the profile
		elif main_input == "delete profile":
			x= cf.delete_profile(username)
			break
		#It is self explainatory :)
		elif main_input == "logout":
			print("logging out..")
			break
		else:
			print("!!! Error Invalid Input !!!")

#******************************************************
	

while True:
	main_input = input("Type 'login' to log in and 'register' to register yourself: ")
	print()
	if main_input == 'login':
		print ("Please fill the informaition below: ")
		username =lr.login()
		reminder_setting(username)

		if username == None:
			continue

	elif main_input == 'register':
		username = lr.register()
		if username == True:
			username = lr.login()
		elif username == False:
			print("Some error occured! Please Try after some time!")
			reminder_setting(username)
		if username == None:
			continue
		else:
			break

	elif main_input == 'exit':
		break
	else:
		print("ERROR! WORNG INPUT!")
		print()
#****************************************************************************
		






			



