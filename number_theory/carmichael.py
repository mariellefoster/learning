#a program to calculate carmichael numbers
#takes a while, looking into faster algorithms
import math

def carmichael(i):
	n = 2
	while n < i:
		if (n**i % i) != n:
			return
		n += 1
	print "carmichael: " + str(i)

def composite(i):
	n = 2
	while n < (math.sqrt(i)+1):
		if i%n == 0:
			return True
		n += 1

	return False

def main():
	i = 6
	while i < 10000000: #0000000000000000000000000000:
		if composite(i) == True:
			carmichael(i)
		i += 1

main()
