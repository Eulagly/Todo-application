import hashlib
username1 = "somedude"
password1 = "somedudespassword"
username2 = "anotherdude"
password2 = "anotherdudespassword"
in1 = input("create username:")
in2 = input("create password:")
def hash(password):
    global out
    password = bytes(password, "UTF-8")
    x = hashlib.sha512()
    x.update(password)
    out = x.hexdigest()
    print(out)
    return(out)
hash(in2)
database = {in1: out, username1: password1, username2: password2}
print(database)
print("LOGIN FORM")
in3 = input("What is your username?")
correctpassword = database[in3]
in4 = input("what is your password?")
if hash(in4) == correctpassword:
    print("Access granted!")
else:
    print("Access denied.")