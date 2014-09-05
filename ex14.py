from sys import argv

script, user_name = argv #argv automatically grabs the script title as the first argument
prompt = '> ' #this will be used in raw_input

print "Hi %s, I'm the %s script." % (user_name, script) #pulls in argv values
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt) # sets the command line inputs to variable likes

print "Where do you live %s?" % user_name #plugs in user_name again
lives = raw_input(prompt) # set the command line inputs to to the variable lives

print "What kind of computer do you have?"
computer = raw_input(prompt) # sets the command line input to computer 

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)