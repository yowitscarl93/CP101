# Program to take 5 names and print each in uppercase using f-strings

# Taking input for 5 names
names = [input(f"Enter name {i+1}: ") for i in range(5)]

# Printing each name in uppercase using a for loop and f-strings
for name in names:
    print(f"{name.upper()}")
