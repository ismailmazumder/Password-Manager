import os
print("(1) New password import.\n"
      "(2)Show password.\n"
      "(3)Exit")
input1 = int(input("Option : "))
tf = True
while tf:
    if input1 == 3:
        tf = False
    if input1 == 1 :
        input_2 = input("Enter the app name : ")
        input_3 = input("Enter the username : ")
        input_4 = input("Enter the password : ")
