import random
print("***************MAIN MENU********************")
print('______________________________________________________________________________________________')
print("Please make sure you have made a account or have signed in to be able to access your account!")
print('______________________________________________________________________________________________')
print(' ')

def SignUp():

    while 1:
        user_username = input("Please choose a UserName: ")
        if len(user_username) == 0:
            print("Make sure you have written something in the username box.")
            print(' ')
        else:
            break

    while 2:
        user_password = input("Please Choose a password (e.g 4xCi88po0): ")
        if len(user_password) == 0:
            print("Make sure you have written something in the password box.")
            print(' ')
        else:
            break

    print(' ')
    print("You have created a account - You are now able to access your bank.")
    print("Welcome %s!" % user_username)
    print(' ')


SignUp()

choice = ("""
[1] = Check Balance:
[2] = Deposit Money:
[3] = WithDraw Money:
[4] = Recieve monthly Paycheck:
[5] = LogOut/Exit Bank:
""")



user_balance = 0

while 3:
    print("Please select a option from above that you would like to process: ")
    user_choice = input(choice)
    if user_choice == '1':
        print(user_balance)
    elif user_choice == '2':
        print("How much money would you like to add into your bank account: ")
        new_money = int(input("Please enter the amount of money you want to Deposit: "))
        user_balance = user_balance + new_money
        print("Your new balance is: £%s.00" % user_balance)
    elif user_choice == '3':
        print("How much money would you like to WithDraw: ")
        money_WithDraw = int(input("Please enter the amount of money you want to WithDraw: "))
        user_balance = user_balance - money_WithDraw
        print("Your new balance is: £%s.00" % user_balance)
    elif user_choice == '4':
        print("This month you have earned: ")
        pay_check = random.randint(300,1000)
        print("You have earned £%s.00" % pay_check)
        user_balance = user_balance + pay_check
        print("Your new balance is: £%s.00" % user_balance)
    elif user_choice == '5':
        print("You are exiting your bank")
        break


