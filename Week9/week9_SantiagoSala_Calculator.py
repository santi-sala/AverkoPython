import tkinter as tk

calculation = ""

def add_calculation(symbol):
    global calculation
    calculation += str(symbol)

    #deleting everything from the text result field
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "ERROR!")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

    


root = tk.Tk()

#Size of the window
root.geometry("300x275")

#Size of the viewport
text_result = tk.Text(root, height = 2, width = 20, font = ("Arial", 24))
text_result.grid(columnspan=7)

#Buttons --> Numbers
btn_1 = tk.Button(root, text = "1", command = lambda: add_calculation(1), height = 2, width = 4, font = ("Arial", 14))
btn_1.grid(row = 2, column = 1)

btn_2 = tk.Button(root, text = "2", command = lambda: add_calculation(2), height = 2, width = 4, font = ("Arial", 14))
btn_2.grid(row = 2, column = 2)

btn_3 = tk.Button(root, text = "3", command = lambda: add_calculation(3), height = 2, width = 4, font = ("Arial", 14))
btn_3.grid(row = 2, column = 3)

btn_4 = tk.Button(root, text = "4", command = lambda: add_calculation(4), height = 2, width = 4, font = ("Arial", 14))
btn_4.grid(row = 3, column = 1)

btn_5 = tk.Button(root, text = "5", command = lambda: add_calculation(5), height = 2, width = 4, font = ("Arial", 14))
btn_5.grid(row = 3, column = 2)

btn_6 = tk.Button(root, text = "6", command = lambda: add_calculation(6), height = 2, width = 4, font = ("Arial", 14))
btn_6.grid(row = 3, column = 3)

btn_7 = tk.Button(root, text = "7", command = lambda: add_calculation(7), height = 2, width = 4, font = ("Arial", 14))
btn_7.grid(row = 4, column = 1)

btn_8 = tk.Button(root, text = "8", command = lambda: add_calculation(8), height = 2, width = 4, font = ("Arial", 14))
btn_8.grid(row = 4, column = 2)

btn_9 = tk.Button(root, text = "9", command = lambda: add_calculation(9), height = 2, width = 4, font = ("Arial", 14))
btn_9.grid(row = 4, column = 3)

btn_0 = tk.Button(root, text = "0", command = lambda: add_calculation(0), height = 2, width = 4, font = ("Arial", 14))
btn_0.grid(row = 5, column = 2)

#Buttons --> Symbols
btn_plus = tk.Button(root, text = "+", command = lambda: add_calculation("+"), height = 1, width = 3, font = ("Arial", 14))
btn_plus.grid(row = 2, column = 4)

btn_minus = tk.Button(root, text = "-", command = lambda: add_calculation("-"), height = 1, width = 3, font = ("Arial", 14))
btn_minus.grid(row = 3, column = 4)

btn_multiply = tk.Button(root, text = "*", command = lambda: add_calculation("*"), height = 1, width = 3, font = ("Arial", 14))
btn_multiply.grid(row = 4, column = 4)

btn_division = tk.Button(root, text = "/", command = lambda: add_calculation("/"),  height = 1,width = 3, font = ("Arial", 14))
btn_division.grid(row = 5, column = 4)

btn_open = tk.Button(root, text = "(", command = lambda: add_calculation("("), height = 1, width = 3, font = ("Arial", 14))
btn_open.grid(row = 5, column = 1)

btn_close = tk.Button(root, text = ")", command = lambda: add_calculation(")"), height = 1, width = 3, font = ("Arial", 14))
btn_close.grid(row = 5, column = 3)

btn_equals = tk.Button(root, text = "=", command = evaluate_calculation, width = 16, font = ("Arial", 14))
btn_equals.grid(row = 6, column = 1, columnspan = 3)

btn_clear = tk.Button(root, text = "C", command = clear_field, width =3, font = ("Arial", 14))
btn_clear.grid(row = 6, column = 4)

root.mainloop()