names = []

for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

# Print each name in uppercase
for name in names:
    print(f"{name.upper()}")
