import sys
import re

def validate_phone_number(str_1):
    expression = ("^(0?(77|55|98|91))(\-|\ )?([\d]{6}|([\d]){3}(\-|\ )[\d]{3}|([\d]){2}(\-|\ )[\d]{2}(\-|\ )[\d]{2})$")
    if re.fullmatch(expression, str_1):
        return True
    return False

def validate_email(str_2):
    expression = ("^[a-z0-9][a-z0-9.+-]*\@[a-z][a-z.-]*\.[a-z]*$")
    if re.fullmatch(expression, str_2):
        return True
    return False



if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('''Type one of the following commands.
        email
        phone_number''')

    elif len(sys.argv) == 3:
        if sys.argv[1] == "phone_number":
            if validate_phone_number(sys.argv[2]):
                print("Yes")
            else:
                print("No")
        elif sys.argv[1] == "email":
            if validate_email(sys.argv[2]):
                print("Yes")
            else:
                print("No")
        else:
            print("No such command")
    else:
        print("No value passed")