import random

print("Santiago Sala")
print("Week 5 Exercise 6: Array methods.")
print("This program will provide examples of the most used array methods.\n")

def generateArray(max_elements, min_number, max_number):
    current_index = 0
    number_array = []
    while current_index < max_elements:
        random_number = random.randint(min_number, max_number)
        current_index += 1
        number_array.append(random_number)
        
    return number_array
initial_array = generateArray(10, 0, 20)

print(f"Your initial array is: {initial_array}. \n")
print(f"APPEND. This will add an element at the end of an array. In this case we going to add \"BANANA\" at the end of the array.")
initial_array.append("BANANA")
print(f"The result after APPEND is: {initial_array}\n")
print(f"EXTEND. This will append a new sequence to our array. First we create a new array:")
new_array = generateArray(3, 60,66)
print(f"The new array is {new_array}")
initial_array.extend(new_array)
print(f"Ffter using extend in our initial array the result is this: {initial_array}\n")
initial_array.insert(2, "APPLE")
print(f"INSERT. Insert will add an element to the array on the provided index. For example if we want to add \"APPLE\" to index 2 this is the result: {initial_array}.\n")
print(f"REMOVE. Will remove the given first element. For example if we insert \"BANANA\" in index 4 the second banana will not be removed")
initial_array.insert(4, "BANANA")
print(f"Adding \"BANANA\" at index 4: {initial_array}")
initial_array.remove("BANANA")
print(f"Removing the first encountered \"BANANA\" elelement : {initial_array}\n")


print("\nThank you for playing.")
