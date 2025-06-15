#Kern Grant IN254-M2
#Produce List
# Assessment 2 / Program 4 /Total sections=3
#============================================

#Assessment 2 Program 4 Section 1
#************************************
from tkinter.font import names

#Create a produce list
produce_list = [
    ("bananas", 0.59),
    ("apples", 1.49),
    ("grapes", 2.99),
    ("pears", 1.39),
    ("lettuce", 0.99),
    ("onions", 0.79),
    ("potatoes", 0.59),
    ("peaches", 1.59)
]

#Produce price.
with open("ProducePrice.txt", "w") as file:
    for item, price in produce_list:
        file.write(f"{item} {price}\n")

#File count
def filelinecount(filename):
    count = 0
    with open(filename, "r") as file:
        for _ in file:
         count +=1
        return count

#Display number of items in file
print(f"There are {filelinecount('ProducePrice.txt')} products in the file ")


#*************************************
#Assessment 2 Program 4 Section 2
#***************************************

#New items to ProducePrice.txt
new_items = [
    ("peppers", 0.99),
    ("celery", 1.29),
    ("cabbage", 0.79),
    ("tomatoes", 1.19)
]

with open("ProducePrice.txt", "a") as file:
    for item, price in new_items:
        file.write(f"{item} {price}\n")

#Display update number of items
print(f"There are {filelinecount('ProducePrice.txt')} products in the fil")


#***********************************
#Assessment 2 Program 4 Section 3
#************************************

#Import Pandas dataframe to read ProducePrice.txt content
import pandas as pd

#Reading file into Dataframe
produce_prices = pd.read_csv("ProducePrice.txt", sep=" ", names=["Item", "Price"],
                             header=None)
#Display Dataframe with line numbers
produce_prices.index +=1
print(produce_prices)

#Display final count of products
print(f"There are {len(produce_prices)} products in the ProducePrices list.")

#=======================
#References (6)
# Beginning Programmiong: All-In-One Desk Reference for Dummies. (n.d.).
#                         chapter II.8: Reading and Saving Files

#Code Complete. (n.d.). Chapter 26.3: Data Transformations.

#Python Basics. (n.d.). Chapter 18: Introduction to NumPy.

#Learn Python in 7 days.   (n.d.). Chapter 9: File Handling and Exceptions.

#W3Resource. (n.d.). Python file handling exercises. Retrieved March 5th 2025,
                    # from https://www.w3resource.com/python-exercises/file/

#Pansad Documentation. (n.d.). pandas.read_cvs. Retrieved March 5, 2025,
                    # from https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

