import math
print("Santiago Sala")
print("Week 2 Tasks")
print("Exercise 3: How long it takes to reach the goal")
print("This program will calculate the the amount of time for a car to reach a distance given the cars speed and distance")

while True:
    speed = input("To proceed enter the cars speed in km/h: ")
    try:
        val = int(speed)
        break;
    except ValueError:
        try:
            float(speed)
            break;
        except ValueError:
            print("This is not a number. Please enter a valid number")


while True:
    distance = input("Next, what is the distance that the car must travel: ")
    try:
        val = int(distance)
        break;
    except ValueError:
        try:
            float(distance)
            break;
        except ValueError:
            print("This is not a number. Please enter a valid number")

time_total = int(distance) / int(speed)
minutes = (time_total - math.floor(time_total)) * 60
print("The total time in hours is: " + str(round(time_total, 2)) + "hour(s)")
print("The car will take " + str(math.floor(time_total)) + "hour(s) and " + str(round(minutes)) + "minutes.")
print("Thank you. Have a nice day.")




