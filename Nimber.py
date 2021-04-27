class Nimber():
    def __init__(self,x):
        assert x>=0
        self.x=x

    def __str__(self):
        return "Nimber({})".format(self.x)

    def __repr__(self):
        return "Nimber({})".format(self.x)

    #正, 負
    def __pos__(self):
        return self

    def __neg__(self):
        return self

    #加法
    def __add__(self,other):
        return Nimber(self.x^other.x)

    #減法
    def __sub__(self,other):
        return self+other

    #乗法
