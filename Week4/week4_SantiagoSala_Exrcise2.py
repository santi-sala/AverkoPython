print("Santiago Sala")
print("Week 4 Exercise 2: Calculate the sum of even numbers")
print("This program will calculate the sum of even numbers values from 2 to 40")

initial_value = 2
while_result = initial_value

while initial_value < 40:    
    initial_value += 2
    while_result += initial_value
    


for_result = 0
for x in range(1, 41):
    if x % 2:
        continue        
    else:
        for_result += x
        print(x)
        
    

print("The result of the WHILE loop is: " + str(while_result))
print("The result of the FOR loop is: " + str(for_result))

print("Thank you for playing")
