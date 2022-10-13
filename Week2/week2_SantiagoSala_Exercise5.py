import math
print("Santiago Sala")
print("Week 2 Tasks")
print("Exercise 5: Convert Dollars to Euros")
print("This program will convert Dollars to Euros.")


while True:
    current_exchange = input("To proceed enter what is the current dollar-euro exchange? ")    
    try:
        val = float(current_exchange)
        print("The current exchange rate is: " + current_exchange)
        break;
    except ValueError:
        print("This is not a number. Please enter a valid number")


while True:
    dollars = input("Next, how many dollar(s) do you want to exchange to euros? ")
    try:
        val = float(dollars)
        break;
    except ValueError:
        print("This is not a number. Please enter a valid number")

total = float(current_exchange) * (float(dollars))
                                   
print("With the exchabge rate of " + current_exchange + " , " + dollars + "$ is " + str(round(total, 2)) + "€.")

print("Thank you. Have a nice day.")




