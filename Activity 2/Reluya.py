# Get the student's grades for each subject
math = float(input("Enter your Math grade: "))
science = float(input("Enter your Science grade: "))
english = float(input("Enter your English grade: "))

# Calculate the average
average = (math + science + english) / 3

# Print the average
print(f"Your average grade is: {average:.2f}")

# Now this will print the average of the subjects
print(average)
