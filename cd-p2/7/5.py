class Action(Character) :
    step = 0
    def __init__(selp, na, we):
        selp.na=na
        selp.we=we

    def intro(self):
        print("Name :", self.na)
        print("Weapon :", self.we)
lugo= Car("Lugo", "Weapon")
lugo.intro()