def readf(filen,mode):
    f=open(filen,mode)
    print(f.read())
def writef(filen,mode):
    f=open(filen,mode)
    print("Input(Enter 'q' to exit input :")
    while True:
        t=input()
        if t=='q':
            break
        f.write(t+"\n")
        t=''


t=''
filen=input("File name : ")
mode=input("File mode(r/w/a) : ")

if mode == 'r':
    readf(filen,mode)
else :
    writef(filen,mode)
