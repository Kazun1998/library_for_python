from Modulo_Matrix import *

class Modulo_Vector_Error(Exception):
    pass

class Modulo_Vector:
    def __init__(self,v,Mod):
        self.vec=[x%Mod for x in v]
        self.Mod=Mod
        self.size=len(v)

        #出力
    def __str__(self):
        return str(self.vec)

    def __repr__(self):
        return str(self)

    #+,-
    def __pos__(self):
        return self

    def __neg__(self):
        return self.__scale__(-1)

    #加法
    def __add__(self,other):
        if self.size!=other.size:
            raise Modulo_Vector_Error("2つのベクトルのサイズが異なります.({},{})".format(self.size,other.size))

        if self.Mod!=other.Mod:
            raise Modulo_Vector_Error("2つのベクトルの剰余が異なります.({}, {})".format(self.Mod,other.Mod))
        v=self.vec
        w=other.vec
        u=[v[i]+w[i] for i in range(self.size)]
        return Modulo_Vector(u,self.Mod)

    #減法
    def __sub__(self,other):
        return self+(-other)

    #乗法
    def __mul__(self,other):
        pass

    def __rmul__(self,other):
        return self.__scale__(other)

    def Inverse(self):
        pass

    #スカラー倍
    def __scale__(self,r):
        v=self.vec
        v=[r*x for x in v]
        return Modulo_Vector(v,self.Mod)

    #内積
    def inner(self,other):
        if self.size!=other.size:
            raise Modulo_Vector_Error("2つのベクトルのサイズが異なります.({},{})".format(self.size,other.size))

        if self.Mod!=other.Mod:
            raise Modulo_Vector_Error("2つのベクトルの剰余が異なります.({}, {})".format(self.Mod,other.Mod))

        X=0
        v=self.vec
        w=other.vec

        for x,y in zip(v,w):
            X+=x*y
        return X%self.Mod
    #累乗
    def __pow__(self,n):
        pass

    #等号
    def __eq__(self,other):
        return (self.vec==other.vec) and (self.Mod==other.Mod)

    #不等号
    def __neq__(self,other):
        return not(self==other)

    def __getitem__(self,index):
        assert isinstance(index,int)
        return self.vec[index]

    def __setitem__(self,index,val):
        assert isinstance(index,int)
        self.vec[index]=val
#=================================================
def Zero_Vector(N,Mod):
    """N次元のゼロベクトルを出力する.

    """
    return Modulo_Vector([0]*N,Mod)

def Standard_Basis(N,k,Mod):
    """N次元ベクトルの第k標準基底を出力する.

    """
    return Modulo_Vector([1 if i==k else 0 for i in range(N)],Mod)

def Vectoric_Matrix(V,Mode=True):
    """

    V:ベクトルのリスト
    Mode:True->行ベクトル, False->列ベクトル
    """
    assert V

    m=V[0].Mod
    assert any([1 if v.Mod==m else 0 for v in V])

    M=[v.vec for v in V]
    if Mode==False:
        M=[list(c) for c in zip(*M)]
    return Modulo_Matrix(M,m)
