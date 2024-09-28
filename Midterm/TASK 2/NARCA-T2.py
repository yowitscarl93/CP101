shiela = [ ]

for x in range(5):
	shielas_input = input(f"ENTER NAME {x + 1}: ")
	
	shiela.append(shielas_input.upper())

print("\n LIST OF UPPERCASE NAMES: ")

for i in shiela:
	print(f" > {i}")
