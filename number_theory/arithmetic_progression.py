
import math

def composite(i):
	n = 2
	while n < (math.sqrt(i)+1):
		if i%n == 0:
			return True
		n += 1
	return False

def main():
	string = ""
	for i in range(2,200):
		if not composite(i):
			string += str(i) + ", "
			for k in range(2, 35):
				if not composite(i+k):
					string += str(i+k) + ", "
					if not composite(i+2*k):
						string += str(i+2*k) + ", "
						if not composite(i+3*k):
							string += str(i+3*k) + ", "
							if not composite(i+4*k):
								string += str(i+4*k) + ", "
								if not composite(i+5*k):
									string += str(i+5*k) + ", "
				else:
					if len(string) > 0:
						print string
					string = ""

main()

