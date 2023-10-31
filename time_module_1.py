import time 

def using_while():

    i = 0
    while i < 50000:
        i = i + 1
        print(i)

def using_for():

    for i in range(50000):
        print(i)        

init = time.time()

using_for()
t1 = time.time() - init

init = time.time()
using_while()

print(time.time() - init)
print(t1)