for i in range(1, 6):
    name = input(f"What is your name {i}, your name is? ")
    names = [name] if i == 1 else names + [name]

print("These are the names! :")
for name in names:
    print(f"NAME IN UPPERCASE: {name.upper()}")
