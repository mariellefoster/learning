def abundant():
	for i in range(2, 1000):
		if i < sum_divisors(i):
			print "abundant: " + str(i)
			if i%2 == 1:
				print "ODD"

def sum_divisors(n):
	summ = 0
	for i in range(1, n/2+1):
		if n%i == 0:
			summ += i
	return summ

abundant()