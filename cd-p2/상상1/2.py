def Login(id,code):
    a=0
    if id=='Cude':
        a+=1
        if code=='1234':
            a+=1
    elif code=='1234':
        a+=10
    return a
id=input("ID:")
code=input("PW:")
n=int(Login(id,code))
if n<10:
    if n==1:
        print('not code')
    if n==2:
        print('o')
    
else :
    print('All not')
