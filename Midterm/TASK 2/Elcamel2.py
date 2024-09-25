# Prompt the user to enter a list of 5 names
names = input("Enter 5 names, separated by commas: ")

# Split the input string into a list of names
names_list = [name.strip() for name in names.split (",")]

# Check if the user entered exactly 5 names
if len(names_list) != 5:
    print("Error: Please enter exactly 5 names.")
else:
    # Use a for loop to print each name in upper case format using string formatting
    for i, name in enumerate(names_list, 1):
        print("Name {}: {}".format(i, name.upper()))
        
