i = 1
num = 0
while i < 500:
	if (i**i -1) % 17 == 0:
		print "divisible by 17: " + str(i)
		print i % 17
		num += 1
	i += 1
	if i % 10000 == 0:
		print i

print num

