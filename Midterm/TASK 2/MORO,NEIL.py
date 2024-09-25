strings = ("neil, ardie, hitoyoshi, mark, jumary")

print("Welcome to the Name Program!")
print("In this program, you will be asked to enter all 5 names.")
print("After you enter the names, they will be displayed in uppercase letters.")

for i in range(5):
    string = input(f"Please enter the name {i + 1}: ")

print(f"- {strings.upper()}")
