renjun_string = "SI RENJUN03232000 batumbakal junior IS DA ONLY DA LOVE OF MY LIFE SHEEEESH $&#####!!!!"

lowercaseCount = 0
uppercaseCount = 0
digitCount = 0
specialCount = 0

for renjun in renjun_string:
    if renjun.islower():
        lowercaseCount += 1
    elif renjun.isupper():
        uppercaseCount += 1
    elif renjun.isdigit():
        digitCount += 1
    else:
        specialCount += 1
        
print("Lowercase letters:", lowercaseCount)
print("Uppercase letters:", uppercaseCount)
print("Digits:", digitCount)
print("Special Characters:", specialCount)
