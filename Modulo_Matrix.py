from copy import copy,deepcopy

class Modulo_Matrix_Error(Exception):
    pass

class Modulo_Matrix():
    #入力
    def __init__(self,M,Mod):
        self.ele=[[x%Mod for x in X] for X in M]
        self.Mod=Mod
        R=len(M)
        if R!=0:
            C=len(M[0])
        else:
            C=0
        self.row=R
        self.col=C
        self.size=(R,C)

    #出力
    def __str__(self):
        T=""
        (r,c)=self.size
        for i in range(r):
            U="["
            for j in range(c):
                U+=str(self.ele[i][j])+" "
            T+=U[:-1]+"]\n"

        return "["+T[:-1]+"]"

    def __repr__(self):
        return str(self)

    #+,-
    def __pos__(self):
        return self

    def __neg__(self):
        return self.__scale__(-1)

    #加法
    def __add__(self,other):
        A=self
        B=other
        if A.size!=B.size:
            raise Modulo_Matrix_Error("2つの行列のサイズが異なります.({},{})".format(A.size,B.size))
        M=A.ele
        N=B.ele

        L=[0]*self.row
        for i in range(A.row):
            E,F=M[i],N[i]
            L[i]=[(E[j]+F[j])%self.Mod for j in range(self.col)]
        return Modulo_Matrix(L,self.Mod)

    #減法
    def __sub__(self,other):
        return self+(-other)

    #乗法
    def __mul__(self,other):
        A=self
        B=other
        if isinstance(B,Modulo_Matrix):
            R=A.row
            C=B.col

            if A.col!=B.row:
                raise Modulo_Matrix_Error("左側の列と右側の行が一致しません.({},{})".format(A.size,B.size))
            G=A.col

            M=A.ele
            N=B.ele

            E=[[0]*other.col for _ in range(self.row)]
            for i in range(R):
                F=M[i]
                for k in range(G):
                    for j in range(C):
                        E[i][j]+=F[k]*N[k][j]
                        E[i][j]%=self.Mod

            return Modulo_Matrix(E,self.Mod)

        elif isinstance(B,int):
            return A.__scale__(B)

    def __rmul__(self,other):
        if isinstance(other,int):
            return self*other

    def Inverse(self):
        M=self
        if  M.row!=M.col:
            raise Modulo_Matrix_Error("正方行列ではありません.")

        R=M.row
        I=[[1*(i==j) for j in range(R)] for i in range(R)]
        G=M.Column_Union(Modulo_Matrix(I,self.Mod))
        G=G.Row_Reduce()

        A,B=[None]*R,[None]*R
        for i in range(R):
            A[i]=G.ele[i][:R]
            B[i]=G.ele[i][R:]

        if A==I:
            return Modulo_Matrix(B,self.Mod)
        else:
            raise Modulo_Matrix_Error("正則ではありません.")

    #スカラー倍
    def __scale__(self,r):
        M=self.ele
        L=[[(r*M[i][j])%self.Mod for j in range(self.col)] for i in range(self.row)]
        return Modulo_Matrix(L,self.Mod)

    #累乗
    def __pow__(self,n):
        A=self
        if A.row!=A.col:
            raise Modulo_Matrix_Error("正方行列ではありません.")

        if n<0:
            return (A**(-n)).Inverse()

        R=Modulo_Matrix([[1*(i==j) for j in range(A.row)] for i in range(A.row)],self.Mod)
        D=A

        while n>0:
            if n%2==1:
                R*=D
            D*=D
            n=n>>1

        return R

    #等号
    def __eq__(self,other):
        A=self
        B=other
        if A.size!=B.size:
            return False

        for i in range(A.row):
            for j in range(A.col):
                if A.ele[i][j]!=B.ele[i][j]:
                    return False

        return True

    #不等号
    def __neq__(self,other):
        return not(self==other)

    #転置
    def Transpose(self):
        self.col,self.row=self.row,self.col
        self.ele=list(map(list,zip(*self.ele)))

    #行基本変形
    def Row_Reduce(self):
        M=self
        (R,C)=M.size
        T=[]

        for i in range(R):
            U=[]
            for j in range(C):
                U.append(M.ele[i][j])
            T.append(U)

        I=0
        for J in range(C):
            if T[I][J]==0:
                for i in range(I+1,R):
                    if T[i][J]!=0:
                        T[i],T[I]=T[I],T[i]
                        break

            if T[I][J]!=0:
                u=T[I][J]
                u_inv=pow(u,self.Mod-2,self.Mod)
                for j in range(C):
                    T[I][j]*=u_inv
                    T[I][j]%=self.Mod

                for i in range(R):
                    if i!=I:
                        v=T[i][J]
                        for j in range(C):
                            T[i][j]-=v*T[I][j]
                            T[i][j]%=self.Mod
                I+=1
                if I==R:
                    break

        return Modulo_Matrix(T,self.Mod)

    #列基本変形
    def Column_Reduce(self):
        M=self
        (R,C)=M.size

        T=[]
        for i in range(R):
            U=[]
            for j in range(C):
                U.append(M.ele[i][j])
            T.append(U)

        J=0
        for I in range(R):
            if T[I][J]==0:
                for j in range(J+1,C):
                    if T[I][j]!=0:
                        for k in range(R):
                            T[k][j],T[k][J]=T[k][J],T[k][j]
                        break

            if T[I][J]!=0:
                u=T[I][J]
                u_inv=pow(u,self.Mod-2,self.Mod)
                for i in range(R):
                    T[i][J]*=u_inv
                    T[i][J]%=self.Mod

                for j in range(C):
                    if j!=J:
                        v=T[I][j]
                        for i in range(R):
                            T[i][j]-=v*T[i][J]
                            T[i][j]%=self.Mod
                J+=1
                if J==C:
                    break

        return Modulo_Matrix(T,self.Mod)

    #行列の階数
    def Rank(self):
        M=self.Row_Reduce()
        (R,C)=M.size
        T=M.ele

        S=0
        for i in range(R):
            f=False
            for j in range(C):
                if T[i][j]!=0:
                    f=True
                    break

            if f:
                S+=1
            else:
                break

        return S

    #行の結合
    def Row_Union(self,other):
        return Modulo_Matrix(self.ele+other.ele,self.Mod)

    #列の結合
    def Column_Union(self,other):
        E=[]
        for i in range(self.row):
            E.append(self.ele[i]+other.ele[i])

        return Modulo_Matrix(E,self.Mod)

    def __getitem__(self,index):
        assert isinstance(index,tuple) and len(index)==2
        return self.ele[index[0]][index[1]]

    def __setitem__(self,index,val):
        assert isinstance(index,tuple) and len(index)==2
        self.ele[index[0]][index[1]]=val
#=================================================
#単位行列
def Identity_Matrix(n,Mod):
    return Modulo_Matrix([[1*(i==j) for j in range(n)] for i in range(n)],Mod)

#零行列
def Zero_Matrix(r,c,Mod):
    return Modulo_Matrix([[0]*c for i in range(r)],Mod)

#正方行列?
def Is_Square(M):
    return M.row==M.col

#対角行列
def Diagonal_Matrix(A,Mod):
    """Aの第i要素が(i,i)成分である対角行列を生成する.

    A:リスト
    M:整数
    """
    N=len(A)
    T=[[0]*N for _ in range(N)]
    for i in range(N):
        T[i][i]=A[i]
    return Modulo_Matrix(T,Mod)

#跡
def Trace(M):
    if not Is_Square(M):
        raise Modulo_Matrix_Error("正方行列ではありません")

    T=0
    for i in range(len(M)):
        T+=M.ele[i][i]
        T%=M.Mod
    return T

#行列式
def Det(M):
    if not Is_Square(M):
        raise Modulo_Matrix_Error("正方行列ではありません")

    N=M.row
    Mod=M.Mod
    A=deepcopy(M.ele)
    D=1

    for I in range(N):
        if A[I][I]==0:
            D*=-1
            for i in range(I+1,N):
                if A[i][I]:
                    A[I],A[i]=A[i],A[I]
                    break
            else:
                return 0

        u_inv=pow(A[I][I],Mod-2,Mod)
        for i in range(I+1,N):
            k=(u_inv*A[i][I])%Mod
            for j in range(I+1,N):
                A[i][j]-=k*A[I][j]
                A[i][j]%=Mod

    for I in range(N):
        D*=A[I][I]
        D%=Mod
    return D%M.Mod

def Linear_System_Equations(A,b,Mod):
    assert len(A)==len(b)

    X=[]
    for i in range(len(A)):
        X.append(A[i]+[b[i]])

    Y=Modulo_Matrix(X,Mod)
    Y=Y.Row_Reduce()

    T=[]
    M=len(A[0])

    B=[[0]*M for _ in range(M)]
    v=[0]*M

    Flag=[0]*M
    C=[]
    for i in range(len(A)):
        E=Y.ele[i]
        j=0
        while j<M and E[j]==0:
            j+=1
        if j==M:
            if E[-1]!=0:
                return None
            continue

        Flag[j]=1
        v[j]=E[-1]
        C.append(i)
        for k in range(j+1,M):
            if E[k]%Mod!=0:
                B[k][j]=(-E[k])%Mod
                Flag[k]=-1

    for i in range(M):
        if Flag[i]!=1:
            B[i][i]=1
    B=[B[i] for i in range(M) if Flag[i]!=1]
    return v,B

#漸化式と行列
def Linear_Recurrence_Sequence_Value(p,x,N,Mod):
    """線形漸化式の第N項を求める.

    p:漸化式 (d=|p| とする.)
    x:第0項から第(d-1)項までの値
    N:第N項
    Mod:法

    線形漸化式は x[n+d]=p[0]x[0]+p[1]x[1]+...+p[d-1] x[d-1] とする.
    """

    assert len(p)==len(x)
    d=len(p)

    if N<d:
        return x[N]

    A=[p[::-1]]
    for i in range(d-1):
        A.append([1 if j==i else 0 for j in range(d)])
    A=Modulo_Matrix(A,Mod)
    v=Modulo_Matrix([[y] for y in x],Mod)

    X=0
    aa=pow(A,N-d+1).ele[0][::-1]

    for i in range(d):
        X+=aa[i]*x[i]

    return X%Mod

def Linear_Recurrence_Sequence_Matrix(p,Mod):
    """線形漸化式から行列を作る.

    p:漸化式 (d=|p|)
    Mod:法

    線形漸化式は x[n+d]=p[0]x[0]+p[1]x[1]+...+p[d-1] x[d-1] とする.
    """

    A=[p[::-1]]
    d=len(p)
    for i in range(d-1):
        A.append([1 if j==i else 0 for j in range(d)])
    return Modulo_Matrix(A,Mod)
#=================================================
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
