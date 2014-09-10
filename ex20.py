from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file: \n"

# print_all(current_file)

print "Now let's rewind, kind of like a tape."

def print_current(f):
	print f.readline()

print "the test"

print_current(current_file)
rewind(current_file)
print_current(current_file)

# print "the end of the test"

# print "Let's print three lines:"

# current_line = 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file) 