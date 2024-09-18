#strings where we want want to count

myString = "Hi, Im Av and I Love le4rningg<33334566"

lowerCase = 0
upperCase = 0
digitCount = 0
specialCharacters = 0

for av in myString:
    
    #for lowercase
    if av.islower():
        lowerCase += 1
        
     #for uppercase   
    elif av.isupper():
        upperCase += 1
    
    #for digit
    elif av.isdigit():
        digitCount += 1
        
    else:
        specialCharacters += 1

 #outcome
print("Lowercase letters: ", lowerCase)
print("Uppercase letters: ", upperCase)
print("Digits: ", digitCount)
print("Special Characters: ", specialCharacters)
