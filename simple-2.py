
def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data


if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.txt'
    data = read_file(changes_file)


print data
