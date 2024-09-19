# We will use import math for this code
import math

# We will create first a prompt for the user to enter the grades of each subject.
# We use float because grades sometimes have decimal points.
math_subject = float(input("Grade in Math: "))
science_subject = float(input("Grade in Science: "))
english_subject = float(input("Grand in English: "))

# Now we will calculate the total sum of grades in all subjects using the function math.fsum().
# We can use concantenation by adding directly the 3 subjects into one variable
sum_of_all_subjects = math_subject + science_subject + english_subject

# We can also calculate the total sum of grades in all subjects using the function math.fsum().
#sum_of_all_subjects = math.fsum([math_subject, science_subject, english_subject])


# Now we will calculatate the average using the variable sum_of_all subjects by 3.
total_average = sum_of_all_subjects / 3

#Finally we can print the total average.
#Here I use f-string format and .2f, it looks neat to me and I like it.
print (f"The total average grade is: {total_average:.2f}")
