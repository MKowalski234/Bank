def Register():
    pass

def Login(username,password):
    un=input("podaj login: ")
    pw=input("podaj hasło: ")
    if un==username and pw==password:
        print("access granted")
        return True
    else:
        print("fuck off")
        exit()
        return False

while Login("admin","admin"):
    pass