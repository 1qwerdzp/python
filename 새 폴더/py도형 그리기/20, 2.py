s=input(' :')
m=int(s)
a1=0
for h in range(len(s)):
    a1+=m%10
    m=m//10
print(a1)