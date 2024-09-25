# Function to check the number
def check_number(number):
    if number > 0:
        return "The number is positive."
    elif number < 0:
        return "The number is negative."
    else:
        return "The number is zero."

# Get user input
number = float(input("Enter a number: "))

# Call the function and print the result
print(check_number(number))
