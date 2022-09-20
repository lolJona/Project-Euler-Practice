for a in range(1, 1000):
	for b in range(1, 1000):
		for c in range(1, 1000):
			if (a < b < c) and (a**2 + b**2 == c**2) and (a + b + c == 1000):
				print("The value of a is " + str(a) + ", the value of b is " + str(b) + ", and the value of c is " + str(c) + "."
                "  The answer is " + str(a*b*c))
