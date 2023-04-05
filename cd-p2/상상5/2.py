f=open("anna.txt","r")
t=f.readline()
tx=t.split(' ')
for i in range(len(tx)):
    if 'b' in tx[i]:
        print(tx[i])
f.close()