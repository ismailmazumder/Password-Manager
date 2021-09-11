import os
import os
print("")

print("If you want to make your own volt type volt.")

a = input("For new account type new account or show. : ")

if a == 'new account' or a == 'New account' or a == 'New Account':
    username_in = input("Enter the user name : ")
    password_in = input("Enter the password : ")
    file_name = username_in + '.txt'
    filec = open(file_name,'x')
    filec.write(username_in)
    filec.write(password_in)
    print("Thanks.")


elif a == 'login' or a == 'show' or a=='Show' or a=='Login':
    l14 = input("Enter your username :")
    check = os.path.isfile(l14+".txt")
    print(check)
    if check==False:
        print("At 1st create a new account.")
elif a == 'volt' or a=='volt':

    volt_name1 = input("Enter your volt name :")
    testhere = os.path.isdir(volt_name1)
    if testhere == True:
        print("Oh! Already have volt. We can't try with another account.")
    else:
        #volt_name1 = input("Enter your volt name :")
        makevolt1 = os.mkdir(volt_name1)
        print("Congratulation.")
        path = os.getcwd()
        print("Your volt's location is ",path)