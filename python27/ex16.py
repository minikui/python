#coding: utf-8

from sys import argv
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#str_concent = ("%s\n%s\n%s\n") % (line1, line2, line3)
target.write(("%s\n%s\n%s\n") % (line1, line2, line3))

print "And finally, we close it."
target.close()

# Study Drills
# w 以写模式打开文件，若文件不空，则覆盖掉。所以不需要提前清空
