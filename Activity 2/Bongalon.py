import math

# Prompt the user for grades
math_subject = float(input("Grade in Math: "))
science_subject = float(input("Grade in Science: "))
english_subject = float(input("Grade in English: "))

# Calculate the total sum using math.sum
sum_of_all_subjects = sum((math_subject, science_subject, english_subject))

# Calculate the average
total_average = sum_of_all_subjects / 3

# Print the average grade
print (f"The total average grade is: {total_average}")
