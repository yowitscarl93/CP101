#2.
names = []
for i in range(5):
    name = input(f"Enter name {i+1} (in uppercase): ")
    names.append(name.upper())


print("The list of names is:")
for name in names:
    print(f"- {name}")
