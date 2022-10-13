print("Santiago Sala")
print("Week 4 Exercise 7: Print a semi-pyramid")
print("This program will print a semipyramid given the rows.\n")

first_row = 1
row_string = "X"

while True:
    x = input("To proceed, how many rows does you pyramid? ")    
    try:
        val_x = int(x)
        print("")
        while first_row <= val_x:
            first_row +=1
            print(row_string)
            row_string += "X"
        break;
    except ValueError:
        print("This is not a number. Please enter a valid WHOLE number")


print("\nThank you for playing")
