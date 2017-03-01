#coding: utf-8

from sys import argv
script, user_name, user_sex = argv
prompt = '-> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few question."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of coumputer do you have?"
computer = raw_input(prompt)

print """
What! you are a %r?\n
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (user_sex, likes, lives, computer)
