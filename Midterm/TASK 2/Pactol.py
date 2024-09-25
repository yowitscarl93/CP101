
names = []

for i in range(5):
    name = input(f"Please enter name {i + 1}: ")
    names.append(name)  
 
print("\nNames in uppercase:")
for name in names:
    print(name.upper())
