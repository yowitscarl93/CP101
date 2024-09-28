# Part 1: Basic f-string Formatting 
# Prompt the user for input and display it using f-strings. 
# Example: Display a name and age.
name = input("what is your name?: ")
age = int(input("how old are you?: "))
print(f"Hello {name}! You are {age} years old!")


# Part 2: Using  .format() 
item = "basket"
cost = 60_000
sentence = "i bought {} today and it costs {}".format(item,cost)
print(sentence)


# Part 3: Legacy % formatting
## Use the % formatting for displaying a string.
City = "Tokyo"
Temp = 18
print("The temperature in %s is %d Degree Celcius." %(City,Temp))
