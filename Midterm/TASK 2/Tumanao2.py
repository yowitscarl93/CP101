jam01 = ["jamaica, faith, marchel, carl, jommil"]

for x in range(5):
  user_input = input(f"ENTER NAME {x + 1}: ")
  
  jam01.append(user_input.upper())

print("\n list uppercase: ")

for i in jam01:
  print(f" • {i}")


