# Validate User Registration Data Using simple if/elif/else

reserved = ['admin', 'root', 'user']

username = input("Enter username: ")
email = input("Enter email: ")
phone = input("Enter phone: ")
password = input("Enter password: ")
password_repeat = input("Repeat password: ")




validation = True




if (len(username) < 5 or len(username) > 20):
	print("Username should be between 5 and 20 characters long.")
	validation = False

elif not username.isalnum():
	print("Username can only contain alphanumeric characters.")
	validation = False

elif username.lower() in reserved:
	print("Username is busy. Try another one.")
	validation = False




if '@' not in email or '.' not in email:
	print("Email format is not valid.")
	validation = False




if not (phone.startswith('+') or phone.startswith('0')):
	print("Phone number must start from '+' or '0'.")
	validation = False
elif not phone[1:].isdigit():
	print("Phone number is not digit.")
	validation = False
elif not (len(phone) == 12 or len(phone) == 9):
	print("Phone number is not Armenian)")
	validation = False




if len(password) < 8:
	print("Password must be at least 8 characters long.")
	validation = False
elif not any(i.isupper() for i in password):
	print("Password must have at least one uppercase letter.")
	validation = False
elif not any(i.islower() for i in password):
	print("Password must have at least one uppercase letter.")
	validation = False
elif not any(i.islower() for i in password):
	print("Password must have at least one digit number.")
	validation = False
elif not any(i in '!@#$%^&*' for i in password):
	print("Password must have at least one special symbol.")
	validation = False




if password != password_repeat:
	print("Password doesn't match the previous one.")
	validation = False




if validation:
	print(f"Welcome to the system, {username}")
else:
	print("Fix errors")
