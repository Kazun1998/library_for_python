from Modulo_Matrix import *
from Modulo_Vector import *

class Modulo_Vector_Space:
    def __init__(self, dim):
        """ 次元が dim のベクトル空間の部分空間を生成する.

        """

        self.dim=dim
        self.basis=[]
        self.__ind=[]

    def __contains__(self, v):
        for i,u in zip(self.__ind, self.basis):
            v-=v[i]*u
        return not bool(v)

    def add_vectors(self, *S):
        for v in S:
            assert len(v)==self.dim
            for i,u in zip(self.__ind, self.basis):
                v-=v[i]*u

            if bool(v):
                for j in range(self.dim):
                    if v[j]:
                        self.__ind.append(j)
                        break
                v=pow(v[j], Mod-2, Mod)*v
                self.basis.append(v)

                for k in range(len(self.basis)-1):
                    self.basis[k]-=self.basis[k][j]*v

    def dimension(self):
        return len(self.basis)

    def __le__(self, other):
        for u in self.basis:
            if u not in other:
                return False
        return True

    def __ge__(self, other):
        return other<=self

    def __eq__(self, other):
        return (self<=other) and (other<=self)

    def refresh(self):
        I=sorted(range(len(self.__ind)), key=lambda i:self.__ind[i])
        self.basis=[self.basis[i] for i in I]
        self.__ind=[self.__ind[i] for i in I]

    def projection(self, v):
        for i,u in zip(self.__ind, self.basis):
            v-=v[i]*u
        return v

#====================
def Overall(dim):
    V=Modulo_Vector_Space(dim)
    V.add_vectors(*[Standard_Basis(dim,k) for k in range(dim)])
    return V

def Kernel_Space(A):
    """ 行列 A の核空間 Ker A (Ax=0 となる x の空間) を求める.

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
        if j==col:
            return None
        p.append(j)
        T[rnk],T[i]=T[i],T[rnk]

        inv=pow(T[rnk][j], Mod-2, Mod)
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

def Image_Space(A):
    """ A の像空間 Im A を求める.

    """

    V=Modulo_Vector_Space(A.row)
    V.add_vectors(*Column_Vector(A))
    return V

def Linear_System_Equations(A,b):
    if type(A) is Modulo_Matrix:
        row,col=A.size
        T=deepcopy(A.ele)
    else:
        row,col=len(A),len(A[0])
        T=deepcopy(A)

    assert row==len(b), "A の行と b の次元が一致しません."

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

        inv=pow(T[rnk][j], Mod-2, Mod)
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
