import random

print("Santiago Sala")
print("Week 5 Exercise 3: Search a value from an Array.")
print("This program will search a value from an array and gives its index.")

number_array = []
current_index = 0

while current_index < 10:
    random_number = random.randint(0, 10)
    #print(str(random_number))
    current_index += 1
    number_array.append(random_number)

print(f"This is your array: {number_array}")

while True:
    value = input("Which number from the array you want to know the index? ")
    try:
        val_value = int(value)
        if val_value in number_array:
            index = 0
            index_result = []
            while index < len(number_array):
                if val_value == number_array[index]:
                    index_result.append(index)
                index += 1
           
            break
        else:
            print("The number you chose is not in the array.")
            break
    except ValueError:
        print("Please enter a valid WHOLE number.")

print(f"The the index of {val_value} in the array is/are: {index_result}")

print("Thank you for playing.")
