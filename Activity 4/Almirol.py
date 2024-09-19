# String placeholders
# Example 1 using {}format
message_1 = "Hello, my name is {}. My favorite color is {} and I love {}."
name = input(str("Enter name: "))
color = input(str("Enter color: "))
work = input(str("Enter work: "))
message_1a = message_1.format(name, color, work)
print (message_1a)

# Example using index number
message_2 = "Hello, my name is {2}, my favorite color is {1} and I love {0}."
name = input(str("Enter name: "))
color = input(str("Enter color: "))
work = input(str("Enter work: "))
message_2a = message_2.format(work, color, name)
print (message_2a)

# Example using a % function
item = "milk"
cost = 35.50
sampletext4 = "The product %s cost %.2f" % (item, cost)
print (sampletext4)
