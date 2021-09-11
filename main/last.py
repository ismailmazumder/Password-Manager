import os
while True:
    print("(make a vault) Use the Command for make a vault.\n")
    print("(Save a password) If you have already a vault save you password by thhis command.\n")
    print("(show) To see your saved passeord\n")
    #command
    i = input("Welcome! What do you want :")#if you want to print / use //
    if i == "make a vault":
        j = input("Enter the vault name : ")
        make = os.mkdir(j)
        check  = os.path.isdir("j")
        if check == 'True':
            print("Try with another account.")
        else:
            link = os.getcwd() + "\\" + j
            print(link)
            print("Note this link")
            print("Remember the file name.")
    elif i == 'save a password' or i == 'make a file':

        ifyouhavevault = input("If you have any vault tell me the name or no : ")
        if ifyouhavevault == 'no' or ifyouhavevault == 'No':
            print("1st make vault.")
        else:
            chdir =  input("Enter your vault link : ")
            os.chdir(chdir)
            print(os.getcwd())
            file_name = input("Enter the file name :")
            file_name1  = file_name + ".txt"
            make_file = open(file_name1, 'x')
            write = open(file_name1,'a')
            user_name = input("Enter the username :")
            password = input("Enter the password : ")
            write.write("USERNAME : "+ user_name + "    " + "PASSWORD : " + password + "                   ------------End------------------")
            #write.append( user_name + "    " + password)
    elif i== ("show") or i == "Show":
        print(os.getcwd())
        input_name_vault_show = input("Enter the vault name or link  :")
        now_link = os.getcwd()
        if  now_link in input_name_vault_show :

            checkisdir38  = os.path.isdir(input_name_vault_show)
            print(checkisdir38)#bieber is changed
            if checkisdir38 == True:
                os.chdir(input_name_vault_show)
                print(os.getcwd())
                print("Hmm, have.")
                inputthefilename42 = input("Enter the user name or file name : ")
                nownameoffile46 = inputthefilename42 + ".txt"
                checkisdir43 = os.path.isfile(nownameoffile46)
                if checkisdir43 == True:

                    print(nownameoffile46)
                    openfileread45  = open(nownameoffile46,'r')
                    for new46 in openfileread45:
                        print(new46)
                else:
                    print("Make a vault 1st, Save password 2nd.")
            else:
                print("Make a vault 1st")
        else:
            addlinkwithuserinput = os.getcwd() +"\\"+ input_name_vault_show
            print(addlinkwithuserinput)
            trfisdirl41 = os.path.isdir(input_name_vault_show)
            if trfisdirl41 == True:
                os.chdir(addlinkwithuserinput)
                print(os.getcwd())
                print("Hmm, have.")
            else:
                print("Make vault 1st.")
