item = "pizza"
price = 10.9

SampleText1 = "The product is {} and the cost is {}".format(item, price)

print(SampleText1)

sampleText2 = "My name is {}, I am {} years old, I love {}"
sampleText2a = sampleText2.format("Av", "18", "Sketching")
print(sampleText2a)

sampleText3 = "My name is {0}, I am {1} years old, I love {3}"
sampleText3a = sampleText3.format("Av", "18", "Science", "my baby")
print(sampleText3a)

sampleText4 = "My name is {name}, I love {foodie}, I am {age}."
sampleText4a = sampleText4.format(age="18", name="Av", foodie="chicken curry")
print(sampleText4a)


product  = "Bag"
cost = 100
SampleText5 = f"The product is a {product} and the cost is {cost * 10} pesos."
print(SampleText5)
