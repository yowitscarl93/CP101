# Program 2:  

print("Alright, let's get this started!  Five names, coming right up!")
names = []
for i in range(5):
  name = input(f"Person number {i+1}, what's your name? ")
  names.insert(i, name)

print("Time to shout out these names!  Get ready to hear them loud and clear:")
for name in names:
  print(f"NAME IN UPPERCASE: {name.upper()}")
