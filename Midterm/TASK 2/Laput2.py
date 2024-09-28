names = input("Enter 5 names separated by commas or spaces: ").replace(',', ' ').split()
while len(names) != 5:
    names = input("Please enter exactly 5 names: ").replace(',', ' ').split()
for i, name in enumerate(names, start=1):
    print(f"Name {i}: {name.strip().upper()}"
