meows = []

for me in range(5):
  meow = input(f"Enter meows {me+1}: ")
  meows.append(meow)

print("\nMeows in uppercase:")
for meow in meows:
  print(f"{meow.upper()}")
