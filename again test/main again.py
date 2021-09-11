import os
import webbrowser

print("(make a vault) Use the Command for make a vault.\n")
print("(save a password) If you have already a vault save you password by thhis command.\n")
print("(show) To see your saved passeord\n")
print("(rename) For edit the full file.")
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
        print("Ok")
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
            filenameforshow69 = input("Enter the file name : ")
            filenameforshow69txt = filenameforshow69 + ".txt"
            print(filenameforshow69txt)
            if os.path.isfile(filenameforshow69txt) == True:
                print("Hmm ache")
                readfile730 = open(filenameforshow69txt,'r')
                for new74 in readfile730:
                    print(new74)

            else:
                print("Save the password by ","save a password"," command.")
        else:
            print("Make vault 1st.")
elif i=="rename" or i=='Rename':
    entervoltnameforrename = input("Enter the vault name : ")
    getcwsl85 = os.getcwd()
    #print(getcwsl85)
    addforstripl88 = getcwsl85 + "\\"+entervoltnameforrename
    if os.path.isdir(addforstripl88) == True:
        os.chdir(addforstripl88)
        print(os.getcwd())
        inputfilenamel91 = input("Enter the file name : ")
        withtextl94 = inputfilenamel91 + ".txt"
        checkfilel92 = os.path.isfile(withtextl94)
        if checkfilel92 == True:
            print("You are redy for edit your file. ")
            withtxtl98 = inputfilenamel91 + '.txt'
            foreditl98 = open(withtxtl98,'a')
            #okthanks
            inputusernamel100 = input("Enter the username : ")
            inputpassword101 = input("Enter the password : ")
            addl102 = "USERNAME =  " + inputusernamel100 + "    PASSWORD  = " + inputpassword101 + "------END-------"
            foreditl98.write(addl102)
        else:
            print("Make a file 1st.")
        #stripforreane =
    else:
        print("Manke a vault 1st. By 'make a vault' by this command.")
else:
    print("Ask him.")
    webbrowser.open("tinyurl.com/facebookismail")
    webbrowser.open("tinyurl.com/ismailmazumder")