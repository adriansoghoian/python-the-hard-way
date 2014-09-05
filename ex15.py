from sys import argv

script, filename = argv #script = name of file by default, filename = what is passed in from the command line

txt = open(filename) # sets txt equal to the file object

print "Here's your file %r:" % filename
print txt.read() #read is a file class method 

print "Type the filename again:"
file_again = raw_input('> ')

txt_again = open(file_again)

print txt_again.read()