number = input("Enter a number: ")

try:
    number = float(number)  # Convert input to a float

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

except ValueError:
    print("Invalid input. Please enter a valid number.")
