import random

def main():
	print_5_digit_numbers()


def print_5_digit_numbers():
	x = random.randrange(10000, 99999)
	for i in range (20):
		if x%3 == 0:
			print x
		x = random.randrange(10000, 99999)


main()