# Part 1: Basic f-string Formatting 

print("Bakit ka nandito? magpakilala ka!")

name = input("Ano ang pangalan mo? ")
age = int(input("Ilang taon kana? "))

print(f"Hello {name}, ikaw ay {age} taong gulang na. wow legal kana")

# Part 2: Using .format()

print("I ate one Apple, Banana, Orange today. Mag kano nagasto ko?Ibigay ang Item at ang price")

items = ["Apple", "Banana", "Orange"]
prices = [20,15, 20]

print("-" * 25)
print("Item\tPrice")
print("-" * 25)

for i in range(len(items)):
    print("{}\tphp{:.2f}".format(items[i], prices[i]))

print("-" * 25)

# Part 3: Legacy % formatting 

print("Omg, gibagyo ang dipolog, perting tugnawa! ")

temperature = 20

print("Ang temperature sa dipolog kay %.1f degrees Celsius." % temperature)
