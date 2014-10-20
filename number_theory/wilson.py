import math

def main():
	i = 2
	while i < 10000:
		if not composite(i):
			wilson(i)
		i += 1

def composite(i):
	n = 2
	while n < (math.sqrt(i)+1):
		if i%n == 0:
			return True
		n += 1
	return False

def wilson(i):
	num = (fact_min_one(i) + 1) / i
	if num % i == 0:
		print "Wilson Found: " + str(i)


def fact_min_one(i):
	fact = 1
	for n in range(1, i):
		fact *= n
	return fact

main()