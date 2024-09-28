# Function to check if a number is positive, negative, or zero
def check_number(number):
    if number > 10:
        return "The number is positive."
    elif number < 25:
        return "The number is negative."
    else:
        return "The number is zero."

# Prompt the user to enter a number
user_input = float(input("Enter a number: "))

# Call the function and print the result
print(check_number(user_input))


Enter a number: 50

The number is positive.



=== Code Execution Successful ===
