def isemail(x):
    if "." not in x:
        return False
    elif "@" not in x:
        return False
    else:
        return True


email = input("Please enter you email: ")
if isemail(email):
    print("Your email is valid.")
else:
    print("You entered an invalid email.")
