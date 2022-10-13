import math
print("Santiago Sala")
print("Week 2 Tasks")
print("Exercise 6: Convert euros to bills")
print("This program will convert given euros to 5, 10, 20, 50, 100, 200, 500 euros bills")

remain = 0
five_bill = 0
ten_bill = 0
twenty_bill = 0
fifty_bill = 0
one_hundred_bill = 0
two_hundred_bill = 0
five_hundred_bill = 0 

while True:
    total = input("To proceed enter how many euros do you want to convert? ")    
    try:
        total_converted = float(total)
        break;
    except ValueError:
        print("Please enter a valid number.")


if total_converted >= 500:
    five_hundred_bill = total_converted / 500
    total_converted = total_converted - math.floor(five_hundred_bill) * 500

if total_converted >= 200:
    two_hundred_bill = total_converted / 200
    total_converted = total_converted - math.floor(two_hundred_bill) * 200
    
if total_converted >= 100:
    one_hundred_bill = total_converted / 100
    total_converted = total_converted - math.floor(one_hundred_bill) * 100

if total_converted >= 50:
    fifty_bill = total_converted / 50
    total_converted = total_converted - math.floor(fifty_bill) * 50

if total_converted >= 20:
    twenty_bill = total_converted / 20
    total_converted = total_converted - math.floor(twenty_bill) * 20

if total_converted >= 10:
    ten_bill = total_converted / 10
    total_converted = total_converted - math.floor(ten_bill) * 10

if total_converted >= 5:
    five_bill = total_converted / 5
    total_converted = total_converted - math.floor(five_bill) * 5
    
if total_converted < 5:
    remain = total_converted
    
print(total + " euro(s) is: " + str(math.floor(five_hundred_bill)) + "x500 bill(s), "
      + str(math.floor(two_hundred_bill)) + "x200 bill(s), "
      + str(math.floor(one_hundred_bill)) + "x100 bill,"
      + str(math.floor(fifty_bill)) + "x50 bill,"
      + str(math.floor(twenty_bill)) + "x20 bill(s),"
      + str(math.floor(ten_bill)) + "x10 bill(s),"
      + str(math.floor(five_bill)) + "x5 bill and " + str(remain) + "."   )

print("Thank you. Have a nice day.")




