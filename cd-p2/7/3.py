class Car :
    def __init__(selp, mo, col):
        selp.model=mo
        selp.color=col

    def info(self):
        print("Mosel :", self.model, ", Coler :", self.color)
        
bmw= Car("BMW", "white")
bmw.info()