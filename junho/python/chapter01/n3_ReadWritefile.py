'''
# 1. while
f = open("foo.txt")
line = f.readline()
while line:
    print(line,end='')
    line = f.readline()
f.close()
'''
'''
# 2. for
for line in open("foo.txt"):
    print(line,end='')
'''

#3 write with 'while'
principal = 1000
rate = 0.05
numyears = 5
year = 1
f = open("foo_write.txt","w")
while year <= numyears:
    principal = principal * (1 + rate)
    #print("{0:3d} {1:0.2f}".format(year,principal), file=f)
    f.write("{0:3d} {1:0.2f}\n".format(year,principal))
    year += 1
