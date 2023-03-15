def f(n):
    if n>0:
        if n%2==0:
            print(n,end=' ')
        f(n-1)
n=10
f(n)