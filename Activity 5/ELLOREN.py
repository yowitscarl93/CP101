def count_characters(s):
    counts = {'lowercase': 0, 'uppercase': 0, 'digits': 0, 'special_symbols': 0}

    for char in s:
        if char.islower():
            counts['lowercase'] += 1
        elif char.isupper():
            counts['uppercase'] += 1
        elif char.isdigit():
            counts['digits'] += 1
        elif not char.isalnum():
            counts['special_symbols'] += 1
            
    return counts

# Example usage
input_string = "Hello World! 123"
print(count_characters(input_string))
