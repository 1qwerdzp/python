class Cha :
    def __init__(selp, na, we):
        selp.na=na
        selp.we=we

    def intro(self):
        print("Name :", self.na)
        print("Weapon :", self.we)

class Ac(Cha) :
    st = 0

    def mofo(selp,n):
        selp.st += n
        print("current location is %d." % selp.st)
    def moba(selp,n):
        selp.st -= n
        print("current location is %d." % selp.st)
    def turi(selp):
        print("Turn right")
    def tule(selp):
        print("Turn left")
lugo= Ac("Lugo", "Weapon")
lugo.intro()
lugo.mofo(int(input()))
lugo.moba(int(input()))
lugo.turi()
lugo.tule()