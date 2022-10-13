print("Santiago Sala")
print("Week 4 Exercise 3: Calculate the sum of increasing numbers")
print("This program will calculate the sum of numbers increasing by 5 from 5 to 100")

initial_value = 5
while_result = initial_value

while initial_value < 100:    
    initial_value += 5
    while_result += initial_value
    


for_result = 0
for x in range(1, 101):
    if x % 5:
        continue        
    else:
        for_result += x
        #print(x)
        
    

print("The result of the WHILE loop is: " + str(while_result))
print("The result of the FOR loop is: " + str(for_result))

print("Thank you for playing")
