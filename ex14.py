from sys import argv

script, user_name, my_name = argv
reply = '> '

print "Hi %s, I'm the %s script named %s." % (user_name, script, my_name)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(reply)

print "Where do you live %s?" % user_name
lives = raw_input(reply)

print "What kind of computer do you have?"
computer = raw_input(reply)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)