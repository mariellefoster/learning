
bob_encrypted = [1384, 977, 2031, 1336, 2000, 2279, 977, 2031, 1875, 
	1646, 1336, 501, 2273, 624, 1646, 1336, 97, 501, 2031, 244, 2273, 1336, 
	1328, 244, 2279, 451, 2273, 896, 2273, 501, 421, 2000, 1336, 1831, 501, 
	2184, 1618, 261, 977, 500, 501, 624, 614, 1336, 451, 2273, 1974, 2000, 1875, 
	2273, 261, 261, 2273, 501, 1943, 1336, 2279, 261, 261, 1618, 2000, 1943, 
	2259, 2259, 1974, 1974, 1974, 220, 2000, 244, 2279, 451, 2273, 896, 2273, 
	501, 220, 244, 977, 614, 2259, 244, 501, 2184, 1618, 261, 977, 2298, 500, 
	501, 624, 614, 220, 2279, 261, 614, 1875]
e_bob = 17
n_bob = 2407

print "step -2"
ascii = []
for ch in bob_encrypted:
	i = 0
	while i < 128:
		if ch == (i**17)%2407:
			ascii.append(i)
		i+=1
string = ""
print "step -1"
for char in ascii:
	string += chr(char)
print string
print "step 0"

# trying stuff

sample = ["c", "C", "a", "t", "t", "T", "h", "j"]
encoded = []
sample_n = 6468857862473
sample_e = 104729

print "step 1"
for ch in sample:
	asc = (ord(ch)**104729)%6468857862473
	encoded.append(asc)

ascii = []
print "step 2"
for ch in encoded:
	i = 0
	while i < 128:		
		if ch == (i**104729)%6468857862473:
			ascii.append(i)
		i+=1
string = ""
print "step 3"
for char in ascii:
	string += chr(char)
print string


