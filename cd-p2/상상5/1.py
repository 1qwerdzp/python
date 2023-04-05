f=open("example.txt","r")
tx=f.readlines()
for i in range(len(tx)):
    if len(tx[i])>=10:
        print(tx[i],end="")
f.close()