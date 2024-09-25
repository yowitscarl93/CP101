sampleText1 = "My name is {}. i love {}. and playing. {}"
sampleText1a = sampleText1.format("Rey", "burger", "frisbee")
print(sampleText1a)

sampleText2 = "My name is {1} i love {0} and playing {2}"
sampleText2a = sampleText2.format("Dog", "Rey", "Dota2")
print(sampleText2a)

Meow3 = "My name is {name}, and i love eating {food} and I also love to play {sport}"
Meow3a = Meow3.format(food="burger", sport="frisbee", name="Rey")
print(Meow3a)

item = "burger"
cost = 75.5
Dog4 = "The product is %s the cost is %.5f." % (item, cost)
print(Dog4)

item = "cellphone"
cost = 6999
back5 = f"the item is {item} and it will cost {cost} dollars"
print(back5)
