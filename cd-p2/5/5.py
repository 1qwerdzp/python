f=open("example.txt","r")
da=f.readlines()
for line in da:
    print(line, end='')
f.close()