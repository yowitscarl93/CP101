# Prompt the user to enter a list of 5 names.
names = []

for i in range(5):
    names.append(input(f"Enter name {i + 1}: ").upper())
for n in names:
    print(n)
