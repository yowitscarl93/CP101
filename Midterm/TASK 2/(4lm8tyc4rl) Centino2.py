#1 UPPERCASE NAMES
carlNames1 = []


for i in range(5):
    add_input1 = input(f"ENTER A UPPERCASE NAME {i + 1}: ")
    carlNames1.append(add_input1.upper())

print()

print("LIST OF NAMES IN UPPERCASE:")
for carl1 in carlNames1:
    print(f"- {carl1}")


while True:
    print()

    choice = input("ADD ANOTHER LOWERCASE NAME? [Y/N]: ")
    
    print()
    
    if choice.lower() == "y" or choice == "Y":
        break
    
    elif choice.lower() == "n" or choice == "Y":
        print("Exiting...")
        exit()
        

#2 LOWERCASENAMES
carlNames2 = []

for x in range(5):
    add_input2 = input(f"ENTER A LOWERCASE NAME {x + 1}: ")
    carlNames2.append(add_input2.lower())
    
print()

print("LIST OF NAMES IN LOWERCASE:")
for carl2 in carlNames2:
    print(f"- {carl2}")
