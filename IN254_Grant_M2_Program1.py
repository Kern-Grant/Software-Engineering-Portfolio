#Kern Grant IN254-M2
#GUI Calculator
#Assessment 2 / Program 1 /
#References below
#=================================

import tkinter as tk


#create the main calculator window
root = tk.Tk()
root.title("GUI calculator ") #set window title
root.geometry("550x500") #window size

#*************************************
#Assessment / Program 1 / Section 2
#*************************************

#create an entry widget for user input and result display
txt_display = tk.Entry(root, font=("Arial, 24"), justify="right", bd=10, width=15)


#place display box at the top of window
txt_display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=20)



#**************************
#Assessment 2 / Program 1 / Section 3
#Button click handling
#***********************************

#Number button to display
def button_click(number):
    current = txt_display.get()
    txt_display.delete(0, tk.END) #clear the entry
    txt_display.insert(0, current + str(number)) #append clicked number

#***************
#Assessment 2 / Program 1 / Section 4
#*******************************

#list to store button objects
buttons = {}

# create buttons for numbers 0-9
for num in range(10):
    buttons[num] = tk.Button(root, text=str(num), padx=20, pady=10, font=("Arial", 18),
                       width=5, height=2, command=lambda n=num: button_click(n))


#Arrange buttons in a grid layout
buttons[1].grid(row=1, column=0)
buttons[2].grid(row=1, column=1)
buttons[3].grid(row=1, column=2)
buttons[4].grid(row=2, column=0)
buttons[5].grid(row=2, column=1)
buttons[6].grid(row=2, column=2)
buttons[7].grid(row=3, column=0)
buttons[8].grid(row=3, column=1)
buttons[9].grid(row=3, column=2)
buttons[0].grid(row=4, column=1)


#***************************
#Assessment 2 / Program 1 / Section 5
#*************************************


# operations function
def button_operation(op):
    current = txt_display.get()
    print(f"Clicked operator: {op}, Current display: {current}")
    txt_display.delete(0, tk.END)
    txt_display.insert(0, current + op)

operators = ['+', '-', '*', '/']
operator_buttons = {} # dictionary to store operator buttons.

#Create operator buttons
for i, op in enumerate(operators):
    operator_buttons[op] = tk.Button(root, text=op, padx=20, pady=10, font=("Arial", 18),
                                     width=5, height=2, command=lambda o=op: button_operation(o))



#Arrange operator buttons in grid
operator_buttons['+'].grid(row=1, column=3) #Addition
operator_buttons['-'].grid(row=2, column=3) #Substraction
operator_buttons['*'].grid(row=3, column=3) #Multiplication
operator_buttons['/'].grid(row=4, column=3) #division


#********************
#Assessment 2 / Program 1 / Section 6
#**********************************


#Add equal and clear button
def calculate_results():
    try:
        expression = txt_display.get()
        result = eval(expression)
        txt_display.delete(0, tk.END)
        txt_display.insert(0, str(result))

    except:
        txt_display.delete(0,tk.END)
        txt_display.insert(0, "Error")

#Function to clear the display
def clear_display():
    txt_display.delete(0, tk.END)


#Create the '=' button to calculate result
equal_button = tk.Button(root, text="=", padx=20, pady=10, font=("Arial", 18),
                         width=5, height=2, command=calculate_results)


#Create the C button to clear display
Clear_button = tk.Button(root, text="C", padx=20, pady=10, font=("Arial", 18),
                         width=5, height=2, command=clear_display)


# Place = and C button in the grid layout
equal_button.grid(row=4, column=2)
Clear_button.grid(row=4, column=0)

#Tkinter event loop to keep the window open
root.mainloop()


#=================================
#References
#================================

#Python Software Foundation. (2024). Tkinter 8.5 reference: A GUI for Python
#       https://docs.python.org/3/library/tkinter.html

#W3Schools. (2023). Python Tkinter tutorial.
#       https://www.w3schools.com/python/python_gui_tkinter.asp

#GeeksforGeeks. (2024). Python GUI - Tkinter basics.
#       https://www.geeksforgeeks.org/python-gui-tkinter/

#Real Python. (2024). Python Tkinter by example.
#       https://realpython.com/python-gui-tkinter/


