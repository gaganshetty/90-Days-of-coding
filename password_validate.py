''' Password verification and time calculation'''
import time

def error():
	print("Invalid password pattern")


s = input("Enter the password: \n")
start = time.time()
if len(s)< 8:
	error()
elif  not any(c.isalnum()  for c in s):
	error();
elif  not any(c.isalpha() for c in s):
	error();
elif  not any(c.isdigit() for c in s):
	error();
elif  not any(c.islower() for c in s):
	error();
elif  not any(c.isupper() for c in s):
	error();
else:
	print('Success')

time.sleep(1)
end = time.time()
total = end-start

print("Total", total, "s" )
