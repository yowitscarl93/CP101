#PART 1


# Set up student details
class Student:
    def __init__(self,name,age,course,section,year):
        
        self.name = name
        self.age = age
        self.course = course
        self.section = section
        self.year = year
        
# Show student information
    def introduce(self):
        print("ENTER NAME: " + self.name)
        print("ENTER AGE: " + self.age)
        print("ENTER COURSE: " + self.course)
        print("ENTER SECTION: " + self.section)
        print("ENTER YEAR: " + self.year)
        
listOfStudents = []
 
# Loop to add multiple students       
while True:
    print("\n")
    name = input("ENTER NAME: ")
    age = input("ENTER AGE: ")
    course = input("ENTER COURSE: ")
    section = input("ENTER SECTION: ")
    year = input("ENTER YEAR: ")
    student = Student(name,age,course,section,year)
    listOfStudents.append(student)
    
    # Print a friendly introduction for the student
    print("\n")
    print(f"Hello everyone! My name is {name} I'm {age} years of age I'm currently enrolled in the {course} in section {section} and I'm a {year} student I'm excited to be here and look forward to getting to know all of you!") 
    
    print("\n")
    create_another = input("Do you want to Create Another Student? [Y/Any Students]: ")
    if create_another =="Y" or create_another =="y": pass
    else: break
    print("\n")

# Show all students' details    
s = 1
for student in listOfStudents:
    print()
    print("STUDENT #" + str(s))
    student.introduce()
    s = s + 1


#PART 2
item = "laptop"
price = 999999999
place = "behind the planet"
brand = "CARLACER"


almightycarl = "I flex my {} and the price is {} and place to a buy the laptop is {} and also  the brand of my laptop is {}.".format(item,price,place,brand)

print(almightycarl)



#PART 3
name = "CARL"
number = 999999999999
# Use the % operator
print("Si %s ay napaka pangit sa buong mundo ang kanyang pagkapangit hindi mababayaran ng %d sa buong mundo." % (name,number))
