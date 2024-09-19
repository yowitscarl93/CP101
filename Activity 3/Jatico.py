# this declares computation for gross pay
def multiply(x, y):
    return x * y


while True:
    # take input from user
    calculate = input("Calculate the gross pay? (yes/no): ")
    # check if calculate is picked
    if calculate == "yes":
        num1 = float(input("Enter Hours: "))
        num2 = float(input("Enter Rate: "))
        print("GROSS PAY:", num1 * num2)
        break
