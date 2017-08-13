from sys import exit

def dead(why):
	print why
	exit(0)

def dino_room():
	print "This room has a hungry dinosaur. Do you enter? Y/N"
	response = raw_input('> ')

	if response == 'Y':
		dead("You're dumb. The dinosaur bites off your head and you die immediately.")
	elif response == 'N':
		dead("Good choice. You survive to live another day.")
	else:
		dead("what does that even mean.")

dino_room()