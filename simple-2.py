
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
print(commits[0])

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
#####################################################
stat_author = {}
max_commit =0
top_author="nobody"
keys = stat_author.keys()
value = stat_author.values()

for cmt in commits:
    author = cmt.get('author')
    stat_author[author] = stat_author.get(author,0) +1
    if stat_author[author] > max_commit:
        max_commit = stat_author[author]
        top_author=author

print "The top author :", top_author, "committed " , max_commit

print "The overall author committed as : "
print stat_author
# stat_author.keys()
#print stat_author.values()


#####################################################
####### to statistics the highest committed date
#####################################################
stat_date = {}
top_date=''
max_date=0

for cmt in commits:
    cmt_date=cmt.get('date')
    stat_date[cmt_date] = stat_date.get(cmt_date,0) + 1
    if stat_date[cmt_date] > max_date:
        max_date = stat_date[cmt_date]
        top_date = cmt_date

print "The top date :", top_date, "committed " , max_date

print "The overall date committed as : "
print stat_date



#####################################################
####### to statistics the total lines of commits
#####################################################
sum_line=0

for cmt in commits:
    sum_line = sum_line + int(cmt.get('number_of_lines'))

print "There are ",sum_line, "lines committed"


#####################################################
####### to statistics the populor commit time
#####################################################
stat_time = {}
top_time=''
max_time=0

for cmt in commits:
    cmt_time=cmt.get('time')
    stat_time[cmt_time] = stat_time.get(cmt_time,0) + 1
    if stat_time[cmt_time] > max_time:
        max_time = stat_time[cmt_time]
        top_time = cmt_time

print "The popullar time :", top_time, "committed " , max_time

print "The overall time committed as : "
print stat_time


#####################################################
####### to statistics the committed in morning, afternoon and night
#####################################################
stat_time = {}
morning = 0
afternoon = 0
others = 0


for cmt in commits:
    if cmt.get('time') > '06:00:00' and cmt.get('time') < '12:00:00':
        morning = morning + 1
    elif cmt.get('time') > '12:00:01' and cmt.get('time') < '18:00:00':
        afternoon = afternoon + 1
else:
        others = others + 1


print "In the morning, committed ", morning
print "In the afternoon, committed ", afternoon
print "at night, committed ", others







