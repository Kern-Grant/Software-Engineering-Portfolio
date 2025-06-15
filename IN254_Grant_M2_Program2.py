#==================================================
#Manipulating multi-dimensional arrays & array-lists
#Assessment 2 Program 2 / Total sections =2
#Refences below
#=====================================================


#****************************
#Assessment 2 Program 2 - Section 1
#***********************************

# Sales Region Two-dimensional string array
sales_regions = [
    ["North", "Bob", "Stef", "Ron"],
    ["South", "Sue", "Janice", "Will"],
    ["East", "Nathan", "Henry", "Kimmy"],
    ["West", "Wanda", "Charles", "Pete"]
]

# Display the sales regions array using for nested loops
print("\n Section1:Two-Dimensional Array.\n")

for row in sales_regions:
    print(row[0])
    for col in row[1:]:
        print(col)
    print()

 #*************************************
 #Program 2 Section 2
 #************************************


print("\nSection 2: Array-list\n")

# Creating sales team.
sales_team = []

#Add north region employees (excluding "north")
sales_team.extend(sales_regions[0][1:])


#Print number of elements in the sales team array-list
print(f"There are {len(sales_team)} names in the sales team arraylist.")

#Add the south region employees to the sales team array-list
sales_team.extend(sales_regions[1][1:])

#REMOVE
#for region in sales_regions:
 #    sales_team.extend(region[1:])
print(f"There are {len(sales_team)} names in the sales team array-list")

# Checking for Step in the sales Team
if "Stef" in sales_team:
    print("Stef is in the sales team array-list.")
else: print("Stef is NOt on the sales team list.")

#I will remove specific names from sales team array-list
names_to_remove = ["Janice", "Ron"]

#Keep only the names not in name_to_remove
sales_team = [name for name in sales_team if name not in ["Janice", "Ron"]]
print(f"There are {len(sales_team)} names in the sales team.")

#Display the names in sales team array-list.
print("\nNames currently in the sales team array-list.")
for member in sales_team:
    print(member)









