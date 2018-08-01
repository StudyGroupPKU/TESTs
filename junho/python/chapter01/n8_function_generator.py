
count = 0
def global_var():
    global count 
    count = 3

def countdown(n):   ### generate multiple numbers via 'yield!!'
    print("counting down!")
    while n>0:
        yield n ## !!! generator
        n -= 1

global_var()
print(count)

## countdown(count).__next__()
for i in countdown(count):
    print(i)
