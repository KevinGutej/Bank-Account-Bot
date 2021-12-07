print("**********MAIN MENU**********")
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
        user_password = input("Please Choose a password: ")
        if len(user_password) == 0:
            print("Make sure you have written something in the password box.")
            print(' ')
        else:
            break


    print("You have created a account - You are now able to access your bank.")


SignUp()

choice = ("""
[1] = Check Balance:
[2] = Deposit Money:
[3] = WithDraw Money:
[4] = View transaction Details:
[5] = LogOut/Exit Bank:
""")



user_balance = 0

while 3:
    print("Please select a option from above that you would like to process.")
    user_choice = input(choice)
    if user_choice == '1':
        print(user_balance)
    elif user_choice == '2':
        print("How much money would you like to add into your bank account: ")
        new_money = int(input("Please enter the amount of money you want to Deposit: "))
        user_balance = user_balance + new_money
        print("Your new balace is: %s " % user_balance)
    elif user_choice == '3':
        print(user_balance)
    elif user_choice == '4':
        print(user_balance)
    elif user_choice == '5':
        print("You are exiting your bank")
        break


