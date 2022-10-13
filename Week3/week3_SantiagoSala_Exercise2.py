print("Santiago Sala")
print("Week 3 Exercise 2: Which day is it?")
print("This program will tell which weekday is it by a given number between 1 and 7")

while True:
    week_number = input("Give me a number between 1 and 7 (both included): ")
    try:
        value = int(week_number)
        if value > 7 or value < 1:
            print("Please enter a number between 1 and 7")
        else:
            break
    except ValueError:
        print("This is not a number. Please enter a valid number.")

if value == 1:
    print("Your entered  week number is MONDAY.")
elif value == 2:
    print("Your entered  week number is TUESDAY.")
elif value == 3:
    print("Your entered  week number is WEDNESDAY.")
elif value == 4:
    print("Your entered  week number is THURSDAY.")
elif value == 5:
    print("Your entered  week number is FRIDAY.")
elif value == 6:
    print("Your entered  week number is SATURDAY.")
else:
    print("Your entered  week number is SUNDAY.")

print("Thank you for playing.")
