def print_names_in_uppercase():
    names = [input(f"Enter name {i+1}: ") for i in range(5)]

    for i, name in enumerate(names, start=1):
        print(f"Name {i}: {name.upper()}")

print_names_in_uppercase()
