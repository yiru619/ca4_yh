
def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip().split(' ')[0],
                'time': details[2].strip().split(' ')[1],
                'number_of_lines': details[3].strip().split(' ')[0]
            }
            # add details to the list of commits.
            
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits

def get_stat_keyword(commits,key):
    stat_keyword = {}
    max =0
    top_keyword=""
    
    for cmt in commits:
        keyword = cmt.get(key)
        stat_keyword[keyword] = stat_keyword.get(keyword,0) +1
        if stat_keyword[keyword] > max:
            max = stat_keyword[keyword]
            top_keyword=keyword
    return stat_keyword
#{top_keyword:max}

def get_commit_lines(commits, key):
    sum_line=0

    for cmt in commits:
        sum_line = sum_line + int(cmt.get(key))

    return sum_line


def get_commit_time_range(commits, time_breakpoint):
    stat_time = {}
    morning = 0
    afternoon = 0

    for cmt in commits:
        if cmt.get('time') < time_breakpoint:
            morning = morning + 1
        else:
            afternoon = afternoon + 1
    return [morning, afternoon]


if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.txt'
    data = read_file(changes_file)
    commits = get_commits(data)

#read file
#print data

#print the number of lines read
#print(len(data))

#print first commit
#print(commits[0])

#print last commit
#print(commits[-1])


#print last commit author
#print(commits[-1]['author'])

#print(commits[0]['author'])

#print the number of commits
#print(len(commits))

#print(commits[4])
#print(len(commits))
# commits[0]['author']
#print commits[0].get('author')


#####################################################
####### to statistics the highest committed author

stat_author = get_stat_keyword(commits, 'author')
print "staticstics by author, the top author committed", stat_author


#####################################################
####### to statistics the highest committed date

stat_date = get_stat_keyword(commits, 'date')
#print "staticstics by date, the top date committed", stat_date

#####################################################
####### to statistics the populor commit time

stat_time = get_stat_keyword(commits, 'time')
#print "staticstics by time, the top time committed", stat_time

stat_lines = get_stat_keyword(commits, 'number_of_lines')
print "staticstics by number of lines, the top time committed", stat_lines

#####################################################
####### to statistics the total lines of commits
sum_line=get_commit_lines(commits,'number_of_lines')
print "staticstics by number of lines and it committed", sum_line


#####################################################
####### to statistics the committed in morning and afternoon

commit_range = get_commit_time_range(commits,'12:00:00')

print "In the morning, committed ", commit_range[0]
print "In the afternoon, committed ", commit_range[1]








