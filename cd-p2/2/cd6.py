n=int(input('n:'))
def func():
    global n
    if n<0:
        n=n*-1
    print(n)
func()