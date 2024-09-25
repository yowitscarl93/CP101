# Part 1: Basic f-string Formatting
def part_1():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello, my name is {name} and I am {age} years old.")

# Part 2: Using .format()
def part_2():
    items = ["Apple", "Banana", "mangoosten"]
    prices = [0.99, 0.50, 0.70]
    
    print("{:<10} {:>10}".format("Item", "Price"))
    print("-" * 20)
    for item, price in zip(items, prices):
        print("{:<10} ${:>9.2f}".format(item, price))

# Part 3: Legacy % formatting
def part_3():
    temperature = 24.5
    print("The current temperature is %.1f degrees Celsius." % temperature)

# Execute the parts
if __name__ == "__main__":
    part_1()
    print()  # Just for spacing
    part_2()
    print()  # Just for spacing
    part_3()
