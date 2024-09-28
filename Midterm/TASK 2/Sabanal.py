# Prompt the user to enter a list of names
names_input = input("Enter a list of names separated by commas ( Shawn,Michael,Tumimpa,Sabanal,Dox): ")

# Split the input string into a list of names
names = [name.strip() for name in names_input.split(',')]

# Print each name in uppercase using a for loop and f-strings
for name in names:
    print(f"{name.upper()}")
