n=int(input())
def f():
    for re1 in range(1,n+1):
        for re in range(1,n+1):
            d=' '
            if re*re1>9:
                d=''
            print(re*re1,end=' '+d) #끝에 공백을 추가하고 다음줄로 이동하지 않음
        print(end='\n') #\n은 다음줄로 이동
f()

