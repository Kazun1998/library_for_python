from Modulo_Matrix import *

class Modulo_Vector:
    def __init__(self, vector):
        self.vec = [vi % Mod for vi in vector]
        self.size = len(vector)

        #出力
    def __str__(self):
        return str(self.vec)

    def __repr__(self):
        return str(self)

    def __bool__(self):
        return any(self.vec)

    def __iter__(self):
        yield from self.vec

    #+,-
    def __pos__(self):
        return self

    def __neg__(self):
        return self.__scale__(-1)

    #加法
    def __add__(self, other):
        assert self.size == other.size, f"2つのベクトルのサイズが異なります. ({self.size}, {other.size})"
        return Modulo_Vector([vi + wi for vi, wi in zip(self, other)])

    #減法
    def __sub__(self, other):
        return self+(-other)

    def __rsub__(self, other):
        return (-self)+other

    #乗法
    def __mul__(self,other):
        pass

    def __rmul__(self,other):
        return self.__scale__(other)

    #スカラー倍
    def __scale__(self, r):
        return Modulo_Vector([r * vi for vi in self])

    #内積
    def inner(self,other):
        assert self.size == other.size, f"2つのベクトルのサイズが異なります. ({self.size}, {other.size})"
        return sum(vi * wi % Mod for vi, wi in zip(self, other)) % Mod

    #累乗
    def __pow__(self,n):
        pass

    #等号
    def __eq__(self, other):
        return self.vec == other.vec

    def __len__(self):
        return self.size

    #不等号
    def __neq__(self, other):
        return not (self == other)

    def __getitem__(self,index):
        assert isinstance(index,int)
        return self.vec[index]

    def __setitem__(self,index,val):
        assert isinstance(index,int)
        self.vec[index]=val

#=================================================
def Zero_Vector(N):
    """N 次元のゼロベクトルを出力する.

    """
    return Modulo_Vector([0]*N)

def Standard_Basis(N, k):
    """N 次元ベクトルの第 k 標準基底を出力する.

    """
    return Modulo_Vector([1 if i==k else 0 for i in range(N)])

def Vectoric_Matrix(V, Mode=True):
    """

    V: ベクトルのリスト
    Mode: True → 行ベクトル, False → 列ベクトル
    """

    M=[v.vec for v in V]
    if Mode==True:
        M=[list(c) for c in zip(*M)]
    return Modulo_Matrix(M)

def Matrix_Action(A,v):
    """ 行列 Aとベクトル v の積 Av を求める.

    A: Matrix
    v: Vector
    """

    assert A.col==v.size

    v=v.vec
    w=[0]*A.row
    for i in range(A.row):
        a=A.ele[i]
        for j in range(A.col):
            w[i]+=a[j]*v[j]
            w[i]%=Mod
    return Modulo_Vector(w)

def Row_Vector(A):
    """ 行列 A の行ベクトルを生成する.

    A: Modulo_Matrix
    """

    return [Modulo_Vector(v) for v in A.ele]

def Column_Vector(A):
    """ 行列 A の列ベクトルを生成する.

    A: Modulo_Matrix
    """

    return [Modulo_Vector(v) for v in zip(*A.ele)]

def Tensor_Product(u,v):
    """ u,v のテンソル積 u (x) v を表すベクトルを求める.

    u,v: vector
    """

    M=[[0]*len(v) for _ in range(len(u))]

    for i in range(len(u)):
        Mi=M[i]
        for j in range(len(v)):
            Mi[j]=u[i]*v[j]
    return Modulo_Matrix(M)

