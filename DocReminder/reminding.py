import mysql.connector #for mysql
from win10toast import ToastNotifier as tn #for windows notifications
import email_alert as ea #FILE! fot e-mail alert
import datetime as dt #for dates
import time #to sleep program for 1 day
#---------- for SMS-------------------------------
from twilio.rest import Client
account_sid = "AC92cadcfb53a7806bf498ab05534f8cbb"
auth_token = "ca1effa695f1c9e6b44a174aca98f112"
#-------------------------------------------------

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
		
while True:
	mycursor.execute("SELECT username FROM users")
	mydb.commit()
	myresult = mycursor.fetchall() #List of all tables

	for table_tuple in myresult:
		for table in table_tuple:
			print()
			sql = f"SELECT * from {table}" #table is the username
			mycursor.execute(sql)
			mydb.commit()
			all_rows = mycursor.fetchall() #It has both document and expiry date

			if all_rows == None:
				continue
			else:
				todays_date = dt.date.today() 

				for row in all_rows: #row[0]=document and row[1]=expiry date
					alert_dates = []
					for day in range(7):
						to_append = row[1] - dt.timedelta(days=day)
						alert_dates.append(str(to_append))
		
					expiry_date =str(row[1])

					if str(todays_date) in alert_dates:
						sql = "SELECT ph_no,email from users where username =%s"
						val = (table,)
						mycursor.execute(sql,val)
						mydb.commit()
						phone_tuple = mycursor.fetchone()

						phone_no = f"+91{phone_tuple[0]}"
						
						email = phone_tuple[1]

		#---------- Below is the dostribution of the notification ----------------------
						
						#---- This message will go to everywhere------------------------
						if expiry_date==todays_date:
							notification = f"Your document '{row[0]}' had been expired today!!"
						else:
							notification = f"Your document '{row[0]}' will be expired on {expiry_date}"
						
						#----- Print Alert ----------------------------------------------
						print(F"DOCUMENT EXPIRED!!! {notification}")
						
						#----- Notification Alert ---------------------------------------
						n=tn()
						n.show_toast("DOCUMENT EXPIRED!",notification, duration= 10,
										icon_path="icon.ico")
						
						#----- Message alert -----------------------------------------
						client = Client(account_sid,auth_token)
						client.messages.create(from_='+15713217004',
											body =notification,
											to = phone_no)
						
						#----- E-mail Alert ------------------------------------------
						ea.email_alert("YOUR DOCUMENT HAS EXPIRED!",notification,email)

#------ Sleeping program for 24 hours----------
	print("went to sleep for 24 hours")	#	   |
	time.sleep(86400)			#			  |
#----------------------------------------------