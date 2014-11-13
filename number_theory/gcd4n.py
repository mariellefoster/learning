def main():
	
	for n in range (300):
		n = 21 + 29*n
		x = 4 * n + 3
		y = 3 * n - 5
		print "n: " + str(n) + " x: " + str(x) + ", y: " + str(y)

		x = abs(x)
		y = abs(y)

		if (x>y):
			gcd(x, y, 1)
		else:
			gcd(y, x, 1)

def gcd(a, b, prev_r):
	if b == 0:
		print "gcd: " +  str(prev_r)
		return
	q = a/b
	r = a - b*q
	if r != 0:
		prev_r = r
	
	#print "r: " + str(r)
	if (r > b):
		gcd(r, b, prev_r)
	else:
		gcd(b, r, prev_r)

main()