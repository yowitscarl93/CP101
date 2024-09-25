
names = []
for int in range(1,6):
    name = input(f"Enter name {int}: ")
    names.append(name.strip())

for int, name in enumerate(names, start=1):
    print(f"Name {int}: {name.upper()}")
    
  
