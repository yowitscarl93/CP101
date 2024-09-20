def count_characters(s):
    lowercase_count = sum(1 for c in s if c.islower())
    uppercase_count = sum(1 for c in s if c.isupper())
    digit_count = sum(1 for c in s if c.isdigit())
    special_symbol_count = sum(1 for c in s if not c.isalnum())
    return lowercase_count, uppercase_count, digit_count, special_symbol_count

s = "Carlryan Jaye A. Agustin_93    "
lowercase_count, uppercase_count, digit_count, special_symbol_count = count_characters(s)
print("Lowercase characters:", lowercase_count)
print("Uppercase characters:", uppercase_count)
print("Digits:", digit_count)
print("Special symbols:", special_symbol_count)
