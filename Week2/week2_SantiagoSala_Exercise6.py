import math
print("Santiago Sala")
print("Week 2 Tasks")
print("Exercise 6: Convert seconds to hours, minutes and seconds")
print("This program will convert given seconds to hours, minutes and seconds.")

hours = 0
minutes = 0
seconds = 0

while True:
    total = input("To proceed enter how many seconds do you want to convert? ")    
    try:
        total_converted = int(total)
        break;
    except ValueError:
        print("Please enter a whole number.")


if total_converted >= 3600:
    hours = total_converted / 3600
    total_converted = total_converted - math.floor(hours) * 3600

if total_converted >= 60:
    minutes = total_converted / 60
    total_converted = total_converted - math.floor(minutes) * 60
    
if total_converted > 0:
    seconds = total_converted
    
print(total + " second(s) is: " + str(math.floor(hours)) + " hour(s), " + str(math.floor(minutes)) + " minute(s) and " + str(math.floor(seconds)) + " second(s).")

print("Thank you. Have a nice day.")




