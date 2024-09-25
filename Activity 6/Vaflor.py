name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, my name is {name} and I am {age} years old.")

items = ["Apple", "Mango", "Orange"]
prices = [10, 10, 10]

print("{:<10} {:<10}".format("Item", "Price"))
for item, price in zip(items, prices):
    print("{:<10} {:<10.2f}".format(item, price))

item = "Mango"
count = 3

sentence = "I have 100 Pesos and I bought {} {} today.".format(count, item)
print(sentence)

city = "Dipolog"
temperature = 30

print("The temperature in %s is %d degrees Celsius." % (city, temperature))
