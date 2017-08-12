the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit

# mixed lists
for i in change:
	print "I got %r" % i

# empty list
elements = []

# use range function
for i in range(0, 6):
	print "Adding %d to the list." % i
	elements.append(i)

for i in elements:
	print "Elements was: %d" % i
	