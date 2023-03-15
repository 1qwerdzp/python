n1=int(input())

def f(n):
    global n1
    if n<n1+1 :
        global a
        a+=n
        f(n+1)
    else :
        print(a)
a=0
n=1
f(n)