# ( == Code 2 of 2 for Midterm Exam == )

# This determines if user wants to input 5 names
enter_input = input("Do you want to Enter Five Names in Uppercase? (yes/no): ")
if enter_input == "yes":
    
# This lets the user input the names 
        names = []
        for i in range(5):
            name = input(f"Enter name {i+1}: ")
            names.append(name)

# This prints the names, in uppercase, in string format, and in loops
        for name in names:
            print(f"{name.upper()}")
