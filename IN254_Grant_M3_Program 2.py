# IN254_M3 / Assessment 3 / Program 2

#Print Initial message - R1
print("Assessment 3 - Logging Exceptions to a File.")
print("Testing Try/Catch for Divide by Zero, File Does Not Exist,"
      " Array Out of Bounds, and Array is Null scenarios")
print("All  console error messages are printed from error log file.")

import logging

# Setting up logging to write a file -R2
logging.basicConfig(filename='error_log.text', level=logging.ERROR)

# Error message redirect to the error message. -R3
import sys
sys.stderr = open('error_log.text', 'a')

#Function to handle divide by zero exception -R4
def DivideByZero(dividend, divisor):
      if divisor == 0:
            raise Exception("Divide by Zero")
      return dividend / divisor # return result if the divisor is not 0.

#Function to attempt opening a non-existent file -R5
def FileDoesNotExist():
    with open("NoFileNamedThis.txt", "r") as file:
         content = file.read() # to read content

#Function to create an array and access a non-existent index - R6
def ArrayOutOfBounds():
      nba_teams = ["Lakers", "Warriors", "Bulls", "Celtics", "Heat"] #Array Example
      print(nba_teams[5])

#Function to create an array.-R7
def ArrayIsNull():
      nba_teams = None # Set the array to none.
      try:
            print(nba_teams[0])
      except TypeError as e:
            print(f"Error: Object reference not set to an instance of an object.")
            logging.error(f"Error: Object reference not set to an instance of an object.")

#Function To handle divide by Zero exception R8
def DivideByZero(dividend, divisor):
    if divisor ==0:
        raise Exception("Divide by Zero")
    return dividend / divisor

# Create a try/catch block for Divide by Zero
def TestDivideByZero():
    try:
        result = DivideByZero(10, 0)
        print(result)
    except Exception as e:
        print(f"Error: {str(e)}")
        logging.error(f"Error: {str(e)}")

# Call function to test
TestDivideByZero()

# Function to open a non-existent file R9
def TestFileDoesNotExist():
    try:
        with open ("FileDoesNotExist.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
          print(f"Error: {str(e)}")
          logging.error(f"Error: {str(e)}")

# Create a try/catch block for FileDoesNotExist
def TestFileDoesNotExist():
          try:
              FileDoesNotExist()
          except Exception as e:
              print(f"Error: {str(e)}")
              logging.error(f"Error: {str(e)}")

#Call The function to test
TestFileDoesNotExist()

# Function for out-of-bounds error
def ArrayOutOfBounds():
    nba_teams = ["Lakers", "Celtics", "Heat", "Warriors", "Bulls"]
    print(nba_teams[10])

# Create a try/catch block for Array Out Of Bounds
def TestArrayOutOfBounds():
    try:
        ArrayOutOfBounds()
    except Exception as e:
        print(f"Error: {str(e)}")
        logging.error(f"Error: {str(e)}")

# Call the function to test it
TestArrayOutOfBounds()

import logging
import sys

#Set up logging to write file
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

#Redirect error message
sys.stderr = open('error_log.txt', 'a')

# Function to raise error
def ArrayIsNull():
    my_array = None
    print(my_array[0])

#create a try/catch block for ArrayIsNull
def TestArrayIsNull():
    try:
        ArrayIsNull()
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        logging.error(f"Error: {str(e)}")

#Call the function to test
TestArrayIsNull()


#************************
#References
#***********************

#Python documentation on assertions. Retrieved from
     # https://docs.python.org/3/reference/simple_stmts.html#assert

# Python IndexError documentation. Retrieved from
    # https://docs.pythin.org/3/library/exceptions.html#IndexError

#Python FileNotFoundError documentation. Retrieved from
    #  https://docs.python.org/3/library/exceptions.html#FileNotFoundError

# Python Custom Exceptions. Retrieved from
    # https://realpython.com/python-exceptions/#defining-your-own-exceptions

# Logging module documentation. Retrieved from
  # https://docs.python.org/3/library/logging.html

# W3Resource - Python Exception Handling. Retrieved from
  # https://www.w3resource.com/python/python-exception-handling.php

#Programiz Python Logging. Retrieved from
   # https://www.programiz.com/python-ptogramming/logging
