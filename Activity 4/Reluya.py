sampleText1 = "My name is {}. I love {}. I love  {}."
sampleText1a = sampleText1.format("Rod", "Sleeping", "Moon", "Grapes")
print(sampleText1a)

sampleText2 = "My name is {1}. I love {2}. I love playing {0}."
sampleText2a = sampleText2.format("Rice", "Rod", "Hiking", "Mobile Legends", "Grapes")
print(sampleText2a)

sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(food="Adobo", play="Mobile Legends", name="Rod")
print(sampleText3a)

item = "milk"
cost = 35.5
SampleText4 = "The product is %s the cost is %.5f." % (item, cost)
print(SampleText4) 

item = "iphone12"
cost = 6000
SampleText5 = f"The item is {item} and the cost is {cost * 100} pesos."
print(SampleText5)
