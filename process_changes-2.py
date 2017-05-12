
# open the file - and read all of the lines.
changes_file = 'changes_python.txt'

# use strip to strip out spaces and trim the line.
data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

