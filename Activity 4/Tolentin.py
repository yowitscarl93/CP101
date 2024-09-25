sampleText1 = "My Name is {}. I love {}. i love playing {}. {}"
sampleText1a = sampleText1.format("Jaeyun", "Fries", "MLBB", "Melon")
print(sampleText1a)

sampleText2 = "My name is {1}. I love {2}. i love playingh {0}."
sampleText2a = sampleText2.format("ROS", "Jaeyun", "Fries", "MLBB", "Melon")
print(sampleText2a)

sampleText3 = "My name is {name}. I love {food}. I love playing {play}." 
sampleText3a = sampleText3.format(food="Fries", play="MLBB", name="Jaeyun")
print(sampleText3a)


item = "Iphone_xr"
cost = 18,000

SampleText5 = f"The item is {item} and the cost is {cost * 100} pesos."
print(SampleText5)  
