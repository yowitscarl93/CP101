#Will promp the user to input a statement
statement = input("Please type any statement: ")
total_char_in_the_statement = len(statement) # will calculate total characters
count_of_upper_case_char = sum(1 for char in statement if char.isupper()) # will calculate count of upper char
count_of_lower_case_char = sum(1 for char in statement if char.islower()) # will calculate count of lower char
count_of_all_digits = sum(1 for char in statement if char.isdigit()) # will calculate total number of digits
count_of_special_char = sum(1 for char in statement if not char.isalnum() and not char.isspace()) # will calculate total special char

# will print all the total characters in specified areas
print ("You said: ", statement)
print ("Total of characters: ", total_char_in_the_statement)
print ("Total count of upper case letters: ", count_of_upper_case_char)
print ("Total count of lower case letters: ", count_of_lower_case_char)
print ("Total count of all digits: ", count_of_all_digits)
print ("Total count of special characters: ", count_of_special_char)
