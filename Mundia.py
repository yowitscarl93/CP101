# Activity in programming 
# create a code that will count all lower case,upper case,digits,and special symbols from given string.
statement = "Hi My name is Gerald F. Mundia. I LOVE PLAYING MOBILE LEGEND! My favourite main heroes is beatrix 12345 matches!"
total_char_in_the_statement = len(statement ) # calculate total characters 
total_number_of_upper_case = sum(1 for char in statement if char.isupper()) #  calculate total number of upper char
total_number_of_lower_case = sum(1 for char in statement if char.islower()) # calculate total number of lower char
total_of_all_digits = sum(1 for char in statement if char.isdigit()) # calculate total number of digits
total_of_special_char = sum(1 for char in statement if not char.isalnum() and not char.isspace()) # calculate total space 

# will print all the total characters in specified areas
print (statement)
print ("Total of characters: ", total_char_in_the_statement)
print ("Total number of upper case letters: ", total_number_of_upper_case)
print ("Total number of lower case letters: ", total_number_of_lower_case)
print ("Total number of all digits: ", total_of_all_digits)
print ("Total of number of special characters: ", total_of_special_char)
