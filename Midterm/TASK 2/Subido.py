# def print_names_in_uppercase():
names = []
for i in range(5):
    while True:
        name = input(f"Enter name {i+1}: ")
        if name.strip():  # check if the input is not empty
            names.append(name)
            break
        else:
            print("Name cannot be empty. Please try again.")

    print("\nHere are the names in uppercase:")
    for i, name in enumerate(names, start=1):
        print(f"{i}. {name.upper()}")

# print_names_in_uppercase()
