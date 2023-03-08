def ej(w,h) :
    return w+h

def Qo(w,h) :
    return w-h

def rhq(w,h) :
    return w*h

def sk(w,h):
    return w/h

n=input("공백없는 계산 식:")

if int(n.count("+"))!=1 and int(n.count("-"))!=1 and int(n.count("*"))!=1 and int(n.count("/"))!=1 :
    print("ERROR")

elif int(n.count("+")) == 1 :
    w = int(n[0:n.index('+')])
    h = int(n[n.index('+')+1:len(n)])
    area = ej(w,h)

elif int(n.count("-")) == 1 :
    w = int(n[0:n.index('-')])
    h = int(n[n.index('-')+1:len(n)])
    area = Qo(w,h)

elif int(n.count("*")) == 1 :
    w = int(n[0:n.index('*')])
    h = int(n[n.index('*')+1:len(n)])
    area = rhq(w,h)

elif int(n.count("/")) == 1 :
    w = int(n[0:n.index('/')])
    h = int(n[n.index('/')+1:len(n)])
    area = sk(w,h)

if int(n.count("+"))==1 or int(n.count("-"))==1 or int(n.count("*"))==1 or int(n.count("/"))==1 :
    print(area)
