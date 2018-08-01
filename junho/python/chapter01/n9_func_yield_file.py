import time

def tail(filename):  ## ON-line monitoring the changes of file appending, like UNIX's "tail -f" (cntr-c to terminate)
    f = open(filename)
    f.seek(0, 2) # from file ending point
#    f.seek(0,0)  # from file starting point
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def grep(lines, search_text):
    for line in lines:
        if search_text in line:
            yield line


#infile = "/Users/leejunho/Desktop/git/python3Env/group_study/TWITTER_SENTI/ALL_ORDERED_NY.txt"
infile = "foo.txt"
#for i in tail(infile):
#    print(i)

log_file = tail(infile)
pylines = grep(log_file,"test")
for line in pylines:
    print("a_{}".format(line),end="")

