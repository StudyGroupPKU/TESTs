import time

def tail(infile):
    f = open(infile)
#    f.seek(0,2)
    f.seek(0,0)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def print_matches(matchtext):
    print("Looking for", matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(line)

matchers = [
    print_matches("end"),
    print_matches("test")
]

#next() to call everything to be ready
for m in matchers: m.__next__()

log = tail("foo.txt")
for line in log:
    for m in matchers:
        m.send(line)

