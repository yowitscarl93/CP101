class Compute:
    
    def __init__(self, number):
        self.number = number

    def compute(self):
        print("ENTER A NUMBER: " + str(self.number))


while True:
    user_input = int(input("ENTER A NUMBER: "))
    
    print()

    if user_input > 0:
        
        print("THE NUMBER IS POSITIVE [+]")
        
    elif user_input < 0:
        
        print("THE NUMBER IS NEGATIVE [-]") 
        
    else:
        print("THE NUMBER IS ZERO [0]")
    
    print()
    
    
    add_input = input("ADD ANOTHER NUMBER? [Y/ANY NUMBER]: ")
    
    print()
    
    if add_input == "Y" or add_input =="y":
        pass
    
    else:
        break
