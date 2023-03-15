def get_sum(a,b) :
    i=0
    for n in range(a,b+1):
        i+=n
    return(i)

a=int(input())
b=int(input())
m=get_sum(a,b)
print(a,'부터 ',b,'까지의 합은 ',m,'입니다')