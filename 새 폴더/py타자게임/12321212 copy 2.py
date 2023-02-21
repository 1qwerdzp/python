from random import *

a=[1,2,3,4,5,6,7,8,9,10]

b=choices(a, [1,1,1,1,1,1,9,1,1,1], k=3)

print(b)

print(b.count(7))
