a=0
for i in range(1,6):
    s='n'+str(i)+':'
    n=int(input(s))
    if n<0:
        n=n*-1
    a+=n
print(a)
