'''
		THIS PROGRAM IS USED FOR LOGIN / REGISTER INTO THE DATABASE 
'''
import mysql.connector

class LoginRegister(object):
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
	'''
		**************LOGIN FUNCTION********************************
	'''
	def login():
		while True:
			username = input("Enter Your Username: ")
			if username == "back":
				return
			
			password = input("Enter Your Password:")

			sql = "SELECT EXISTS(select * from users where username = %s and password = %s)"
			val = (username,password)
			mycursor.execute(sql,val)
			r = mycursor.fetchone() #it will contain a tiple such as (1,) or (0,)
			result = ''
			mydb.commit()
			for i in r: # to extract digit from tuple 
				result =i

			if result == 0:
				print("ERROR! Wrong username or Password")
				print()
			
			else:
				sql = "SELECT name FROM users WHERE username = %s AND password = %s"
				val = (username,password)
				mycursor.execute(sql,val)
				r = mycursor.fetchone() 

				if r==None:
					return
				else:
					result = ''
					for i in r:
						result = i
						print("WELCOME",result)
					return username


	'''
		***************REGISTER FUNCTION******************************
	'''
	def register():
		keywords = ["back", "exit", "login", "register", "reminder", "reminders", "h", "delete", "profile"]
		print("Please Register Yourself below:")
			
		def username(): #VERIFIES IF A USERNAME ALREADY EXISTS OR NOT
			while True:
				kw = False
				username = input("Enter the username: ")
				if " " in username:
					print("Username can not contain space, try again!")
				else:
					for i in keywords:
						if username == i:
							kw = True
							break
			
					if kw == True:
						print("OPPS! sorry! You cannot have that username, it is reserverd")
					else:
						sql = "SELECT EXISTS(select * from users where username = %s)"
						val = (username,)
						mycursor.execute(sql,val)
						r = mycursor.fetchone()
						result = ''
						mydb.commit
						for i in r:
							result = i
			
					if result == 1:
						print("ERROR! Username is already taken, Try another one")
					elif result ==0:
						return username

		def phno(): #CROSSCHECKS PHONE NUMBERS!
			while True:
				ph_no = int(input("Enter the Phone number: "))
				if len(str(ph_no)) != 10:
					print("ERROR! INVALID PHONE NUMBER!")

				else:
					ph_no2 = int(input("enter the Phone number again: "))
					if ph_no !=ph_no2:
						print("ERROR! Phone numbers did not match")
					else:
						return str(ph_no)
	
		def pw():  #CROSSCHECKS THE PASSWORD!
			while True:
				pw1 = input("Enter the Password: ")
				if len(str(pw1))<8:
					print("ERROR!! Your password is too short!")
				else:
					pw2 = input("enter the Password again: ")
			
					if pw1 !=pw2:
						print("ERROR! Phone numbers did not match")
					else:
						return pw1

		def email():
			while True:
				email1 = input("Enter your email: ")
				if "@" and ".com" not in email1:
					print("INVALID EMAIL!")

				else:
					email2 = input("enter email again: ")
					if email1 !=email2:
						print("ERROR! Email did not match")
					else:
						return email1

			
		name = input("Enter Your Name: ")
		username = username()
		password = pw()
		phone_number = phno()
		email = email()
		success = False
		
		try:
			sql = "INSERT INTO users (name, username, password, ph_no, email) VALUES(%s,%s,%s,%s,%s)"
			val = (name,username,password,phone_number,email)
			mycursor.execute(sql,val)
			mydb.commit()
			sql = "CREATE TABLE %s () "
			val = (username,)
			mycursor.execute(mycursor.execute(f"CREATE TABLE {username} (document varchar(225), expiry_date date)"))
			mydb.commit()
			print("Congrats! You are Registered Suucessfully")
			success = True
			
		except Exception as e:
			print("ERROR: ",e)	
		
		if success == True:
			print("Please log in:")
			return True
		else:
			print("Sorry! could not register! Please try after sometime :(")
			return
			
			




		



		
		

		
			

	
		
