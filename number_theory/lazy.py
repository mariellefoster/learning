pq = 73*101
i = 90
while i < 100000:
	if (i**2 + 1)% pq == 0:
		print i
	i += 1

def main():
	empireState = Building("height", "width", "color", "xpos")
	empireState.setHeight(500)
	empireState.draw()

class Building():

	self.height =