from sys import exit
from random import randint

class NewGame(object):
	def __init__(self, start):
		self.response = ["You're dead. Nice going.", "Great job, you just got yourself killed.", "Whoop dee doo. You're dead.", "Yikes, bad move."]
		self.start = start

	def play(self):
		next = self.start

		while True:
			print "\n--------------------"
			room = getattr(self, next)
			next = room()

	def win(self):
		print "Cool beans. You won and you made it out alive. bye."
		exit(1)

	def death(self):
		print self.response[randint(0, len(self.response)-1)] # using a list you made in a function(method)
		exit(1)

	def door1(self):
		print "Welcome to door 1."
		print "Here awaits your fate - doom or glory, you pick."
		print "Do you want to go left or right?"

		direction = raw_input("> ")

		if direction == "left":
			print "Cool beans. You live to see another day."
			return 'door2' # calls the function 'door2'

		elif direction == "right":
			print "Oh boy. Bad choice."
			return 'death'

		else: 
			print "What? Let's try again."
			return 'door1'

	def door2(self):
		print "Hi there. I'm detective Alcatraz."
		print "There appears to be a dead body and you're the only one here. What do you want to do?"
		print "Hide it or leave it alone?"

		body_fate = raw_input("> ")

		if body_fate == "hide it":
			print "Dude, I'm right here. I saw that and now you're under arrest."
			return 'death'

		elif body_fate == "leave it alone":
			print "Um, ok, I guess you're free to go."
			return 'win'

		else:
			print "yeah ok that doesn't make any sense."
			return 'door2'

play_game = NewGame("door1")
play_game.play()
