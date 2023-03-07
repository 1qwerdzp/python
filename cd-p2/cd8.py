def get_max(n1) :
    s1=0
    s=0
    for i in range(n1):
        s1 = int(input())
        if s < s1:
            s=s1
    return(s)

n=int(input("Enter integer n :"))
print('max value:',get_max(n))