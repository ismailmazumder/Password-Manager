account  = input("If you want to creat a new account type 'account new' : "+"Else type show.  ")
count = 0
file_name = 'saved',count
if account== 'account new':
    account_new = input("Enter a username : ")
    account_new_pass = input("Enter the password :")
    print("User name and Password = ",account_new,account_new_pass)
    count = count + 1
    creat_file_count = open('test.txt','x')
    #vag kore dite hobe
    #vag1 = account_new_1[1]
    creat_file_count.write(account_new)
    creat_file_count.write(account_new_pass)
    print(file_name)
elif account == 'show' or account == 'Show':
    login = input("Enter user name and password like (username) (password)")
    loginsplit = login.split()
    print(loginsplit)
