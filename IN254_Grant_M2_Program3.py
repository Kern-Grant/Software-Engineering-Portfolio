#Kern Grant IN254-M2
#Manipulating Various Container Structures
#Assessment 2 / Program 2 / Total sections =5
#================================================



#*******************
#Assessment 2 Program 3 Section 1
# Array structures for tracking approved cars
#**************************************


#Define a structure for storing car details (Make, Model, Year)
class ApproveCar:
    def __init__(self,brand,model_name,year):
        self.brand = brand
        self.model_name = model_name
        self.year = year

#Car details
    def display_info(self):
        return f"Brand: {self.brand} | Model: {self.model_name} | Year {self.year}"

# A list of approved cars
car_inventory = [
    ApproveCar("Chevy","Silverado", 2008),
    ApproveCar("Ford", "Mustang", 2010),
    ApproveCar("Dodge", "Charger", 2012)
]
#Display approved cars
print("Section 1:Array of Structures")
for car in car_inventory:
    print(car.display_info())


#*******************************************
#Assessment 2 Program 3 Section 2
#**********************************

#Dictionary to store the number of available cars by model
car_stock = {
    "Mustang": 9,
    "Silverado": 13,
    "Charger": 4
}

#Display inventory count for the car model.
print("\nSection 2: Inventory Count")
for model, count in car_stock.items():
    print("There are", count, model + "s in stock.") #Manual string Format



#*******************************
#Assessment 2 Program 3 Section 3
#Days of the week
#****************************************

#List containing all days of the week
week_days = \
    ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Display the full week
print("\n Section 3: Days Of The Week")
for day in week_days:
    print(day)


#Display the days in reverse order
print("\nReversed Days of the week:")
for day in reversed(week_days):
    print(day)

#Workdays list (Mon to Friday)
work_days = week_days.copy()
work_days.remove("Saturday")
work_days.remove("Sunday")



#Display only workdays
print("\nWorkdays:")
for day in work_days:
    print(day)


#*************************************
#Assessment 2 Program 3 Section 4
#Inventory stack

#Stack data structure
inventory_stack =[]

#Adding stack values
inventory_stack.append(10)
inventory_stack.append(24)
inventory_stack.append(31)
inventory_stack.append(45)
inventory_stack.append(19)
inventory_stack.append(76)

# Display current stack size
print("\n Section 4: Stack")
print(f"current stack size: {len(inventory_stack)} items.")

#removing pop items from the stack
if inventory_stack:
    inventory_stack.pop()
if inventory_stack:
    inventory_stack.pop()
if inventory_stack:
    inventory_stack.pop()



#Display updated stack size
print(f"Updates stack size: {len(inventory_stack)} items")


#Display the next item to be removed (top of the stack)
if inventory_stack:
    print(f"Next item to be removed: {inventory_stack[-1]}")




#********************
#Assessment 2 Program 3 Section 5
#Queue
#********************************************

from collections import deque

#Queue values
task_queue = deque([10, 24, 31, 45, 19, 76])

#Display current queue size
print("\nsection 5: Queue")
print(f"current queue size: {len(task_queue)} items.")




#Dequeue three items of the list
if task_queue:
    task_queue.popleft()
if task_queue:
    task_queue.popleft()
if task_queue:
    task_queue.popleft()

#Display updated queue size
print(f"Updated ques size:{len(task_queue)} items")

#display the next item to be dequeued
if task_queue:
    print(f"Next item to be dequeued: {task_queue[0]}")


#=====================================
#Program 3 References
#=======================================

# Code Complete. (n.d.). Chapter 12.8 Arrays.

# Beginning Programming: All-in-One Desk Reference for Dummies. (n.d.).
# Chapter III.1: Structures and Arrays

#Python Basics. (n.d.). Chapters 16 & 18: Linked List and NumPy.

# Learn Python in 7days. (n.d.). Chapter 5: Dictionary.

#W3Resource. (n.d.). Python: Collections - Exercises, Practice, Solution.
#Retrived March 5th, 2025,from https://www.w3resource.com/python-exercises/collections
