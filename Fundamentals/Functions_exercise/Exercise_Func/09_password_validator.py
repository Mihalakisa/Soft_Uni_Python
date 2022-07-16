import re


def password_validator(passwd):
    is_valid = True
    special_ = re.search("\W+", passwd)
    if len(passwd) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if special_:
        print("Password must consist only of letters and digits")
        is_valid = False
    if len([x for x in passwd if x.isdigit()]) < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


current_password = input()
password_validator(current_password)
