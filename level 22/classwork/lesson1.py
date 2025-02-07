my_password = "Squid game 2"
count=0
while count <= 3:
    user_password=input("enter the password: ")
    if my_password==user_password:
        print("correct")
    else:
        count=count+1
if count==3:
    print("out of trys")