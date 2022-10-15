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
print(f"After using extend in our initial array the result is this: {initial_array}\n")

initial_array.insert(2, "APPLE")
print(f"INSERT. Insert will add an element to the array on the provided index. For example if we want to add \"APPLE\" to index 2 this is the result: {initial_array}.\n")

print(f"REMOVE. Will remove the given first element. For example if we insert \"BANANA\" in index 4 the second banana will not be removed")
initial_array.insert(4, "BANANA")
print(f"Adding \"BANANA\" at index 4: {initial_array}")
initial_array.remove("BANANA")
print(f"Removing the first encountered \"BANANA\" elelement : {initial_array}\n")

print(f"POP. Will removes AND returns the last item of the list if no index is specified")
pop_item = initial_array.pop()
print(f"Poping an element without specifying an index: {pop_item}")
print(f"The original array also has changed: {initial_array} \n")

print(f"CLEAR. This method will just wipe put all the elements of an array.")
print(f"This is the array: {initial_array}")
initial_array.clear()
print(f"And this is the array after using the method clear(): {initial_array} \n")

print("INDEX. This will give the index of the element searched in an array.")
my_array = ["helmet", "cap", "pipo", "sombrero", "pipo"]
print(f"Lets create a new array: {my_array}")
my_index = my_array.index("pipo")
print(f"Second, lets find the index of pipo(if any) in the array: {my_index} \n")

print(f"COUNT. As name suggests, will count the amount of times an elements is repeated in an array.")
my_count = my_array.count("pipo")
print(f"The word pipo is reapeated {my_count} times in the array. \n")

print("SORT. This will sort the elements of an array alphabetically, numerically or reversed.")
my_array.sort()
print(f"The sorted array is: {my_array} \n")
my_array.reverse()

print(f"REVERSE. This method will revese the order of the array: {my_array} \n")
new_array = my_array.copy()
print(f"COPY. This method will make a shallow copy of an array: {new_array}.")

print("\nThank you for playing.")
