
print "solutions to n = 105 is 8"
for i in range(1, 105):
	if (i%3 != 0) and (i%5 != 0) and (i%7 != 0):
		if i*i%105 == 1:
			print i
print ""
print "solutions to n = 165 is 8"

for i in range(1, 165):
	if (i%3 != 0) and (i%5 != 0) and (i%11 != 0):
		if i*i%165 == 1:
			print i

print ""
print "solutions to n = 231 is 8"

for i in range(1, 231):
	if (i%3 != 0) and (i%7 != 0) and (i%11 != 0):
		if i*i%231 == 1:
			print i

print ""
print "solutions to n = 127361"

for i in range(1, 127361):
	if (i%97 != 0) and (i%101 != 0) and (i%13 != 0):
		if i*i%127361 == 1:
			print i

print ""
print "solutions to n = 1155"

for i in range(1, 1155):
	if (i%3 != 0) and (i%5 != 0) and (i%7 != 0) and (i%11 != 0):
		if i*i%1155 == 1:
			print i

