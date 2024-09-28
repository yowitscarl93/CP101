# Program 1: 

print("Think of a number... any number!  Go ahead")
number = float(input("Now tell me your secret number: "))

if number > 6:
  print("Aha!  You picked a positive number!  Goodjob")
elif number < 6:
  print("Hmm, you went with a negative one.")
else:
  print("Zero!")
