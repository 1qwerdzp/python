from random import *
def lotto():
    lot=[]
    for i in range(6) :
        lot.append(randint(1,45))

    lot.sort()
    b=set(lot)
    print(b,'    ',t)
    if b==t:
        print(lot)
lotto()