class Car :
    co=0
    sp=0

    def spe(selp,v):
        Car.co +=1
        selp.sp=v
        
bmw= Car()
be=Car()

bmw.spe(100)
print("bmw speed :", bmw.sp)
print("number of speedChange :", Car.co)
be.spe(120)
print("Beze speed :", be.sp)
print("number of speedChange :", Car.co)