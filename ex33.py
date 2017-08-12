i = 0
numbers = []

def numlist(min, max):
	for i in range(min, max):
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	return numbers

numbers = numlist(0, 10)

for num in numbers:
	print num
