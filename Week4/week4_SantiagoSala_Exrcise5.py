import random

print("Santiago Sala")
print("Week 4 Exercise 5: Accpount manager")
print("This program will let you check your account, add and remove balance")

balance = 50
while True:    
    players_command = input("What would you like to do: (c)heck your balance, (r)emove from your balance, (a)dd to your balance or (e) to exit? ")
    if players_command == "c" or players_command == "r" or players_command == "a":
        if players_command == "c":
            print("Your current balance is: " + str(balance))
        elif players_command == "r":
            while True:                
                remove_amount = input("How much would you like to REMOVE? ")
                try:
                    val_remove = round(float(remove_amount), 2)                
                    if balance - val_remove < 0:
                        print("Sorry can't do that, you do not have enough balance.")
                        break
                    else:
                        balance -= val_remove
                        print("It's been removed: " + remove_amount + " from your balance.")
                        break
                except ValueError:
                    print("Please enter a valid number.")
        else:
            while True:                
                add_amount = input("How much would you like to ADD? ")
                try:
                    val_add = round(float(add_amount), 2)  
                    balance += val_add
                    print("It's been added: " + add_amount + " from your balance.")
                    break
                except ValueError:
                    print("Please enter a valid number.")
        
    elif players_command == "e":
        break
    else:
        print("Command not recognized. please type \"c\" for cheking your account, \"r\" to remove from your account, \"a\" to add to you account or \"e\" to exit the program.")
    
print("Thank you for playing")
