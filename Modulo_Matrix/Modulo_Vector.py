from Modulo_Matrix import *

class Modulo_Vector:
    def __init__(self, vector: list[int]):
        self.vec = [vi % Mod for vi in vector]

    @property
    def size(self) -> int:
        return len(self.vec)

    #出力
    def __str__(self):
        return str(self.vec)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.vec})"

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
    def inner(self, other: "Modulo_Vector") -> int:
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

    def is_zero(self) -> bool:
        return not any(self.vec)

#=================================================
def Zero_Vector(N: int) -> Modulo_Vector:
    """ N 次元のゼロベクトルを出力する.

    Args:
        N (int): 次元

    Returns:
        Modulo_Vector: N 次元ゼロベクトル
    """

    return Modulo_Vector([0]*N)

def Standard_Basis(N: int, k: int) -> Modulo_Vector:
    """ N 次元ベクトルの第 k 標準基底を出力する.

    Args:
        N (int): 次元
        k (int): 1 を立たせる成分

    Returns:
        Modulo_Vector: 第 k 成分のみ 1, それ以外はすべて 0 である N 次元ベクトル
    """

    return Modulo_Vector([1 if i == k else 0 for i in range(N)])

def Vectoric_Matrix(A: list[Modulo_Vector], column: bool = False) -> Modulo_Vector:
    """ ベクトルのリスト A から行列を生成する. A の各要素が行ベクトルになる.

    Args:
        A (list[Modulo_Vector]): ベクトルのリスト
        column (bool, optional): True にすると, A の各要素が列ベクトルになる行列を出力する. Defaults to False.

    Returns:
        Modulo_Vector: 行 (列) ベクトルとした行列
    """

    A = [a.vec for a in A]
    if column:
        A = [list(x) for x in zip(*A)]
    return Modulo_Matrix(A)

def Matrix_Action(A: Modulo_Matrix, v: Modulo_Vector) -> Modulo_Vector:
    """ 行列 A とベクトル v の積 Av を求める.

    Args:
        A (Modulo_Matrix): 行列
        v (Modulo_Vector): ベクトル

    Returns:
        Modulo_Vector: Av
    """

    if A.col != v.size:
        raise ValueError

    v = v.vec
    w = [0] * A.row
    for i in range(A.row):
        a = A.ele[i]
        w[i] = sum(a[j] * v[j] % Mod for j in range(A.col))
    return Modulo_Vector(w)

def Row_Vector(A: Modulo_Matrix) -> list[Modulo_Vector]:
    """ 行列 A の行ベクトルからなるリストを生成する.

    Args:
        A (Modulo_Matrix): 行列

    Returns:
        list[Modulo_Vector]: 行ベクトルからなるリスト
    """

    return [Modulo_Vector(v) for v in A.ele]

def Column_Vector(A: Modulo_Matrix) -> list[Modulo_Vector]:
    """ 行列 A の列ベクトルからなるリストを生成する.

    Args:
        A (Modulo_Matrix): 行列

    Returns:
        list[Modulo_Vector]: 列ベクトルからなるリスト
    """

    return [Modulo_Vector(v) for v in zip(*A.ele)]

def Tensor_Product(u: Modulo_Vector, v: Modulo_Vector) -> Modulo_Matrix:
    """ u,v のテンソル積 u (x) v を表すベクトルを求める.

    Args:
        u (Modulo_Vector):
        v (Modulo_Vector):

    Returns:
        Modulo_Matrix: テンソル積 u (x) v
    """

    M = [[0] * v.size for _ in range(u.size)]

    for i in range(u.size):
        M[i] = [u[i] * v[j] for j in range(v.size)]
    return Modulo_Matrix(M)
