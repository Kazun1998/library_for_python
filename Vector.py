class VectorException(Exception):
    pass

class Vector():
    def __init__(self,*V):
        self.ele=list(V)
        self.dim=len(V)

    def __str__(self):
        if self.dim!=1:
            return str(tuple(self.ele))
        else:
            return "({})".format(self.ele[0])

    #+,-
    def __pos__(self):
        return self

    def __neg__(self):
        return Vector(*[-x for x in self.ele])

    #加法
    def __add__(self,other):
        if other.__class__==Vector:
            assert self.dim==other.dim,"2つのベクトルの次元が異なる"
            U=[self.ele[i]+other.ele[i] for i in range(self.dim)]
        else:
            U=[x+other for x in self.ele]
        return Vector(*U)
        
    #減法
    def __sub__(self,other):
        if other.__class__==Vector:
            assert self.dim==other.dim,"2つのベクトルの次元が異なる"
            U=[self.ele[i]-other.ele[i] for i in range(self.dim)]
        else:
            U=[x-other for x in self.ele]
        return Vector(*U)

    #乗法
    def __mul__(self,other):
        if other.__class__==Vector:
            return self.inner(other)
        else:
            return self.scale(k)

    def __rmul__(self,k):
        return self.scale(k)

    #スカラー倍
    def scale(self,k):
        U=[x*k for x in self.ele]
        return Vector(*U)

    #内積
    def inner(self,other):
        if self.dim!=other.dim:
            raise VectorException("ベクトルの次元が異なります({},{}).".format(self.dim,other.dim))
        S=0
        for i in range(self.dim):
            S+=self.ele[i]*other.ele[i]
        return S
