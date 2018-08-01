import sys
# Execution ::  python n5_list.py foo1.txt  
# 'foo1.txt' would be 'sys.argv[1]'; 'n5_list.py' is 'sys.argv[0]'

'''
a = [1,2,3]
b = [4,5]
c= b + a
print(c)
'''

param = sys.argv[1]
print(param)
if len(sys.argv) != 2:
    print("please supply a filename")
    raise SystemExit(1)

f = open(sys.argv[1])
lines = f.readlines()
f.close()
fvalue = [float(line) for line in lines]
print("Max : {}".format(max(fvalue)))
print("Min : {}".format(min(fvalue)))

