''' One line password validation'''

import re
password = input("Enter the password\n")

def error():
	print("password doesnot match validaton pattern")

if (len(password)>8) and (re.search("[a-z]",password)) and (re.search("[A-Z]",password)) and (re.search("[0-9]",password)):
	print("Success")
else:
	error()
