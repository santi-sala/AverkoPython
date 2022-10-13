import math
print("Santiago Sala")
print("Week 3 Exercise 4: How many days in a month.")
print("This program will tell how many has a given month.")

while True:
    month_number = input("Give me a number between 1 and 12 (both included): ")
    try:
        value = int(month_number)
        if value > 12 or value < 1:
            print("Please enter a number between 1 and 12")
        else:
            break
    except ValueError:
        print("This is not a number. Please enter a valid number.")
 
match value:
    case 1:
        month = "January"
    case 2:
        month = "Febraury"
    case 3:
        month = "March"
    case 4:
        month = "April"
    case 5:
        month = "May"
    case 6:
        month = "June"
    case 7:
        month = "July"
    case 8:
        month = "August"
    case 9:
        month = "September"
    case 10:
        month = "October"
    case 11:
        month = "November"
    case 12:
        month = "December"
    

if value == 2:
    print("Your chosen month is: " + month + " and it has 28 days.")
elif value % 2:
    print("Your chosen month is: " + month + " and it has 31 days.")
else:
    print("Your chosen month is: " + month + " and it has 30 days.")
    


print("Thank you for playing.")
