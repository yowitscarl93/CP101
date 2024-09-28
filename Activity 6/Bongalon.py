print("Welcome to your personalized journey!")

name = input("Enter your name: ")
age = input("Enter your age: ")
passion = input(" Whats one thing you're passionate about? ")
print(f"Greetings, {name}! You are {age} years old. You have a passion for {passion}.")


item = "IPhoneGalaxy"
count = 1
sentence = " You just treated yourself to a {} {}!".format(count, item)
print(sentence)


Barangay = "Sicayab"
Temperature = 22
print("The current temperature in %s is %d°C." % (Barangay, Temperature))


if input("Would you like to explore more details? (yes/no): ").lower() == "yes":
    print("Great! Stay tuned for more surprises!")
else:
    print("Alright! Have a fantastic day!")
