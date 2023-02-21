#for문-1
lest=['a','b','c']
for s in lest:
    print(s)
#1
Lest=[1,2,3,4,5]
s=0
for n in Lest:
    s += n
print('avg:%d' %(s//5))
#3
a=[1,2,3]
b= [10, 100, 1000]
for a1 in a :
    for b1 in b :
        print(a1*b1,end=' ')
    print()