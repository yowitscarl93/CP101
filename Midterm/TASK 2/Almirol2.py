#midterm activity 2

names = [] #store the names

for i in range(5): #loop to run 5 times
    name = input(f"name {i+1}: ")  #prompt for each value i a name
    names.append(name) #add the names at the end for each loop

print("\nYour selected five names: ") #\n moving it to next line
for name in names:  #loops per name list
    print (f"{name.upper()}")  #output in upper case in f-string format
