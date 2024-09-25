def get_names():
    names = []
    for i in range(5):
        name = input(f"Please enter name {i + 1}: ")
        names.append(name)
    return names

def print_names_uppercase(names):
    print("Using string formatting:")
    for name in names:
        print("Name: {}".format(name.upper()))
    
    print("Using f-string:")
    for name in names:
        print(f"Name: {name.upper()}")

if __name__ == "__main__":
    names_list = get_names()
    print_names_uppercase(names_list)
