
# IN254_M3 / Assessment 3 / Program 1 /
#**************************************

import logging   # logging module

logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("logging is set up.")

# Define test variables
string_var = "Hello"
integer_var = 5

#print(f"String variable: {string_var}")
#print(f"Integer Variable: {integer_var}")

#try:
#    assert string_var != "", "Parameter must not be empty or null."
#   assert integer_var > 0, "Parameter must be greater than zero."

#     print("Assertion passed. Variables are valid.")

#except AssertionError as e:
 #   # Log the assertion error
#   error_message = f"Assertion Failed: {str(e)}"
#    logging.error(error_message)
 #   print(f"Error: {error_message}. check error_log.txt for details.")


# Function Definition - Validate Inputs
def validate_inputs(string_input, integer_input):
    """
    Validates input values.
    :param string_input: Must not be empty.
    :param integer_input:Must be greater than zero.
    :return:Success message if valid
    :raises AssertionError: If validation fails.
    """

    try: #Input Validation
        assert string_input !="", "Parameter must not be empty or null."
        assert integer_input > 0, "Parameter must be greater than zero."
        print("Inputs are valid.")

    except AssertionError as e:
        error_message = f"Assertion Failed: {str(e)}"
        logging.error(error_message)
        print(f"error: {error_message}. Check error_log.txt for details.")

# Call function with test values
validate_inputs("Hello", 5)
validate_inputs("", 0)


#*********************************
# Assessment 3 Program 1 Section 2
#***********************************

#Define an array of nba teams
nba_teams = ["Lakers", "warriors", "Bulls", "Celtics", "Heats"]

try: #Loop through the list
    for i in range(len(nba_teams) + 1):
        print(f"NBA Team: {nba_teams[i]}")

except IndexError as e:
    #Print error message to the console
    print("Array out of bounds error occurred.")
    print(f"Error: {str(e)}")

# Log the error
    logging.error(f"Array out of bounds error: {str(e)}")


#************************************
# Assessment 3 / Program 1 / Section 3
#*************************************

try:
    # Attempt to open a non-existent file
    with open("NoFileNamedThis.txt", "r") as file:
        content = file.read()

except FileNotFoundError as e:
    print("File not found error occurred.")
    print(f"Error: {str(e)}")

    #Log the error
    logging.error(f"File not found error {str(e)}")

#*****************************
# Assessment 3 / Program 1 / Section 4
#***************************************

def DivideByZero(dividend, divisor):
    if divisor ==0:
        raise Exception("Divide by Zero")
    return dividend / divisor

try:
    result = DivideByZero(10, 0)
    print(f"Result: {result}")

except Exception as e:
    print("DivideByZero error occurred.")
    print(f"Error: {str(e)}")


#***************************
# References
#*********************

# Python documentation on assertions. Retrieved from
  # https://docs.python.org/3/reference/simple_stmts.html#assert

# Python IndexError documentation. Retrieved from
  # https://docs.python.org/3/library/exceptions.html#IndexError

# Python FileNotFoundError documentation. Retrieved from
  # https://docs.python.org/3/library/exceptions.html#FileNotFoundError

# Python Custom Exceptions. Retrieved from
  # https://realpython.com/python-exceptions/#defining-your-own-exceptions

#Logging module documentation. Retrieved from https://doc.python.org/3/library/logging.html
