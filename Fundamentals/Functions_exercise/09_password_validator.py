import re


def password_check(passwd):
    special_character = re.search("\W+", passwd)
    return_val = True
    if len(passwd) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        return_val = False
    if special_character:
        print("Password must consist only of letters and digits")
        return_val = False
    if len([x for x in passwd if x.isdigit()]) < 2:
        print("Password must have at least 2 digits")
        return_val = False
    if return_val:
        print("Password is valid")


current_password = input()
password_check(current_password)
