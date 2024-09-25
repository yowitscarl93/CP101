def classify_number():
    user_input = input("Enter a number: ")
    try:
        num = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if num == 0:
        print("The number is zero.")
    elif num > 0:
        print("The number is positive.")
    else:
        print("The number is negative.")

classify_number()
