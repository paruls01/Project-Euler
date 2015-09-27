def problem1():
	multiples = (range(0,1000))
	three = 0
	five = 0
	fifteen = 0
	for x in multiples:
		if x % 3 == 0:
			three += x
	for y in multiples:
		if y % 5 == 0:
			five += y
	for z in multiples:
		if z % 15 == 0:
			fifteen += z


	return three + five - fifteen

print problem1()
