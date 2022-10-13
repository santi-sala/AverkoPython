print("Santiago Sala")
print("Week 2 Tasks")
print("Exercise 2: Ohm's Law")
print("This program will calculate the resistance using Ohm's Law")

while True:
    voltage = input("To proceed enter the voltage: ")
    try:
        val = int(voltage)
        break;
    except ValueError:
        try:
            float(voltage)
            break;
        except ValueError:
            print("This is not a number. Please enter a valid number")


while True:
    current = input("Next, what is the current: ")
    try:
        val = int(current)
        break;
    except ValueError:
        try:
            float(current)
            break;
        except ValueError:
            print("This is not a number. Please enter a valid number")

resistance = int(current) * int(voltage)
print("The resistance is: " + str(resistance))
print("Thank you. Have a nice day.")




