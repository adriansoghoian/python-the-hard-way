from sys import argv 

script, filename = argv #script is the default first name of the script, filename is the user input

print "We're going to erase %r." % filename #letting user know that their file is being deleted
print "If you don't want that, hit CTR-C (^C)." #would abort the script
print "If you do want that, hit RETURN." # this would let the script continue running

raw_input("?") 

print "Opening the file..."
target = open(filename, 'w') # opens the file with read access

print "Truncating the file. Goodbye!"
target.truncate() # truncate is a file class method that deletes the file

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ") #asks for the user input
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
# target.write("\n") # separates the inputs; seems that write by default squishes them on one line. 
target.write(line2)
# target.write("\n")
target.write(line3)
# target.write("\n")

print "And finally we close it."
target.close()