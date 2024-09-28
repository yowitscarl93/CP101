tina_string = "Hi my name is Cristine, I was born in Aurora, Zamboanga Del Sur on february 3 2006 and I'm currently 18 years old. I live in Upper Disakan, Manukan, Zamboanga Del Norte and I'm now pursuing the course BSIT or Bachelor of science in Information Technology@02032006"

lowercaseCount = 0
uppercaseCount = 0
digitCount = 0
specialCount = 0

for tina in tina_string:
    if tina.islower():
        lowercaseCount += 1
    elif tina.isupper():
        uppercaseCount += 1
    elif tina.isdigit():
        digitCount += 1
    else:
        specialCount += 1
        
print("Lowercase letters:", lowercaseCount)
print("Uppercase letters:", uppercaseCount)
print("Digits:", digitCount)
print("Special Characters:", specialCount)
