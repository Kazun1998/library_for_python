from Modulo_Matrix import *
from Modulo_Vector import *

class Modulo_Vector_Space:
    def __init__(self, n: int):
        """ n 次元の F 係数数ベクトル空間を生成する. 最初はゼロ空間.

        Args:
            n (int): 次元
        """

        self.__n = n
        self.basis: list[Modulo_Vector] = []
        self.__ind = []

    @property
    def n(self):
        return self.__n

    def __contains__(self, v: Modulo_Vector) -> bool:
        return self.projection(v).is_zero()

    def add_vectors(self, *S: Modulo_Vector):
        for v in S:
            if (v := self.projection(v)).is_zero():
                continue

            for j in range(self.n):
                if v[j]:
                    self.__ind.append(j)
                    break

            v = pow(v[j], -1, Mod) * v
            self.basis.append(v)

            for k in range(len(self.basis)-1):
                self.basis[k] -= self.basis[k][j] * v

    def dimension(self) -> int:
        return len(self.basis)

    def __le__(self, other: "Modulo_Vector_Space") -> bool:
        return all(u in other for u in self.basis)

    def __ge__(self, other: "Modulo_Vector_Space") -> bool:
        return other <= self

    def __eq__(self, other):
        return (self <= other) and (other <= self)

    def refresh(self):
        I = sorted(range(self.dimension()), key = lambda i: self.__ind[i])

        self.basis = [self.basis[i] for i in I]
        self.__ind = [self.__ind[i] for i in I]

    def projection(self, v: Modulo_Vector) -> Modulo_Vector:
        for i, u in zip(self.__ind, self.basis):
            v -= v[i] * u
        return v

#====================
def Overall(n: int) -> Modulo_Vector_Space:
    """ n 次元の数ベクトル空間 F^n を生成する.

    Args:
        n (int): 次元

    Returns:
        Modulo_Vector: F^n
    """

    V = Modulo_Vector_Space(n)
    V.add_vectors(*[Standard_Basis(n, k) for k in range(n)])
    return V

def Kernel_Space(A: Modulo_Matrix) -> Modulo_Vector_Space:
    """ 行列 A の核空間 Ker A (Ax=0 となる x の空間) を求める.

    Args:
        A (Modulo_Matrix): 行列

    Returns:
        Modulo_Vector_Space: Ker A
    """

    row,col=A.size
    T=deepcopy(A.ele)

    p=[]; q=[]
    rnk=0
    for j in range(col):
        for i in range(rnk,row):
            if T[i][j]!=0:
                break
        else:
            q.append(j)
            continue

        p.append(j)
        T[rnk],T[i]=T[i],T[rnk]

        inv=pow(T[rnk][j], -1, Mod)
        for k in range(col):
            T[rnk][k]=(inv*T[rnk][k])%Mod

        for s in range(row):
            if s==rnk:
                continue
            c=-T[s][j]
            for t in range(col):
                T[s][t]=(T[s][t]+c*T[rnk][t])%Mod
        rnk+=1

    x=[0]*col
    for i in range(rnk):
        x[p[i]]=T[i][-1]

    ker_dim=col-rnk
    ker=[[0]*col for _ in range(ker_dim)]

    for i in range(ker_dim):
        ker[i][q[i]]=1

    for i in range(ker_dim):
        for j in range(rnk):
            ker[i][p[j]]=-T[j][q[i]]%Mod

    Ker=Modulo_Vector_Space(col)
    Ker.add_vectors(*[Modulo_Vector(v) for v in ker])
    return Ker

def Image_Space(A: Modulo_Matrix) -> Modulo_Vector_Space:
    """ A の像空間 Im A を求める.

    Args:
        A (Modulo_Matrix): 行列

    Returns:
        Modulo_Vector_Space: Im A
    """

    V = Modulo_Vector_Space(A.row)
    V.add_vectors(*Column_Vector(A))
    return V

def Linear_System_Equations(A: Modulo_Matrix, b: Modulo_Vector) -> tuple[Modulo_Vector, Modulo_Vector_Space] | None:
    """ A x = b を満たす x の解空間を求める.

    Args:
        A (Modulo_Matrix): 行列
        b (Modulo_Vector): ベクトル

    Returns:
        tuple[Modulo_Vector, Modulo_Vector_Space] | None:
            解が存在しない場合は None
            解が存在する場合, 解空間はあるベクトル c を用いて, c + Ker A となるため, (c, Ker A) を返す.
    """

    row, col = A.size
    T = deepcopy(A.ele)

    if row != b.size:
        raise ValueError("A の行と b の次元が一致しません.")

    for i in range(row):
        T[i].append(b[i])

    p=[]; q=[]
    rnk=0
    for j in range(col+1):
        for i in range(rnk,row):
            if T[i][j]!=0:
                break
        else:
            q.append(j)
            continue
        if j==col:
            return None
        p.append(j)
        T[rnk],T[i]=T[i],T[rnk]

        inv=pow(T[rnk][j], -1, Mod)
        for k in range(col+1):
            T[rnk][k]=(inv*T[rnk][k])%Mod

        for s in range(row):
            if s==rnk:
                continue
            c=-T[s][j]
            for t in range(col+1):
                T[s][t]=(T[s][t]+c*T[rnk][t])%Mod
        rnk+=1

    x=[0]*col
    for i in range(rnk):
        x[p[i]]=T[i][-1]

    ker_dim=col-rnk
    ker=[[0]*col for _ in range(ker_dim)]

    for i in range(ker_dim):
        ker[i][q[i]]=1

    for i in range(ker_dim):
        for j in range(rnk):
            ker[i][p[j]]=-T[j][q[i]]%Mod
    return x,ker
