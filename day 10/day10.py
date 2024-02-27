registered_password = "saba1234"
authorized = False 

while authorized != True:
    user_input = input("please enter your password: ")

    if user_input == registered_password:
         print("accses granted")
         authorized = True 
    else:
         print("password incorrect please try again")