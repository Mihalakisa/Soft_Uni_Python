username = input()
password = input()

# повтаряме: въвеждаме парола
# спираме: въведената парола == password
# продължаваме: въведената парола != password
entered_password = input()

while entered_password != password:
    entered_password = input()
else:
    print(f"Welcome {username}!")