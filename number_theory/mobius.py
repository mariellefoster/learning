def prime_factors(i):
	n = 2
	power = 0
	lst = []
	num = i
	while n <= i/2:
		while i%n == 0:
			power += 1
			i = i/n
		if power > 0:
			lst.append([n, power])
		power = 0
		n += 1
	return lst


def main():
	i = 3
	
	mstr = []
	# while i < 100000:
	# 	mobius = False
	# 	factors = prime_factors(i)
	# 	for entry in factors:
	# 		if entry[1] > 1:
	# 			mobius = True
	# 			mstr.append(i)
	# 			break
	# 	if mobius == False and len(mstr) > 0:
	# 		if len(mstr) > 4:
	# 			print mstr	
	# 		mstr = []
	# 	i += 1

	lst = [96675, 96676, 96677, 96678, 96679, 96680]
	for entry in lst:
		print entry, prime_factors(entry)

		


main()