def check_number(num):
  """Checks if a number is positive, negative, or zero."""
 
  if num > 0:
    return " The number is positive."
  elif num < 0:
    return " The number is negative."
  else:
    return " The number is zero."

num = float(input("enter number:"))
print(check_number(num))
