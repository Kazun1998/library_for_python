from copy import deepcopy

class Modulo_Matrix():
    __slots__=("ele","row","col","size")

    #入力
    def __init__(self,M):
        """ 行列 M の定義

        M: 行列
        ※ Mod: 法はグローバル変数から指定
        """

        self.ele=[[x%Mod for x in X] for X in M]
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
        return "["+"\n".join(map(str,self.ele))+"]"

    def __repr__(self):
        return str(self)

    #+,-
    def __pos__(self):
        return self

    def __neg__(self):
        return self.__scale__(-1)

    #加法
    def __add__(self,other):
        M=self.ele; N=other.ele

        L=[[0]*self.col for _ in range(self.row)]
        for i in range(self.row):
            Li,Mi,Ni=L[i],M[i],N[i]
            for j in range(self.col):
                Li[j]=Mi[j]+Ni[j]
        return Modulo_Matrix(L)

    def __iadd__(self,other):
        M=self.ele; N=other.ele

        for i in range(self.row):
            Mi,Ni=M[i],N[i]
            for j in range(self.col):
                Mi[j]+=Ni[j]
                Mi[j]%=Mod
        return self

    #減法
    def __sub__(self,other):
        M=self.ele; N=other.ele

        L=[[0]*self.col for _ in range(self.row)]
        for i in range(self.row):
            Li,Mi,Ni=L[i],M[i],N[i]
            for j in range(self.col):
                Li[j]=Mi[j]-Ni[j]
        return Modulo_Matrix(L)

    def __isub__(self,other):
        M=self.ele; N=other.ele

        for i in range(self.row):
            Mi,Ni=M[i],N[i]
            for j in range(self.col):
                Mi[j]-=Ni[j]
                Mi[j]%=Mod
        return self

    #乗法
    def __mul__(self,other):
        if isinstance(other,Modulo_Matrix):
            assert self.col==other.row, "左側の列と右側の行が一致しません.({},{})".format(self.size,other.size)

            M=self.ele; N=other.ele
            E=[[0]*other.col for _ in range(self.row)]

            for i in range(self.row):
                Ei,Mi=E[i],M[i]
                for k in range(self.col):
                    m_ik,Nk=Mi[k],N[k]
                    for j in range(other.col):
                        Ei[j]+=m_ik*Nk[j]
                        Ei[j]%=Mod
            return Modulo_Matrix(E)
        elif isinstance(other,int):
            return self.__scale__(other)

    def __rmul__(self,other):
        if isinstance(other,int):
            return self.__scale__(other)

    def inverse(self):
        assert self.row==self.col,"正方行列ではありません."

        M=self
        N=M.row
        R=[[1 if i==j else 0 for j in range(N)] for i in range(N)]
        T=deepcopy(M.ele)

        for j in range(N):
            if T[j][j]==0:
                for i in range(j+1,N):
                    if T[i][j]:
                        break
                else:
                    assert 0, "正則行列ではありません"

                T[j],T[i]=T[i],T[j]
                R[j],R[i]=R[i],R[j]
            Tj,Rj=T[j],R[j]
            inv=pow(Tj[j], -1, Mod)
            for k in range(N):
                Tj[k]*=inv; Tj[k]%=Mod
                Rj[k]*=inv; Rj[k]%=Mod
            for i in range(N):
                if i==j: continue
                c=T[i][j]
                Ti,Ri=T[i],R[i]
                for k in range(N):
                    Ti[k]-=Tj[k]*c; Ti[k]%=Mod
                    Ri[k]-=Rj[k]*c; Ri[k]%=Mod
        return Modulo_Matrix(R)

    #スカラー倍
    def __scale__(self,r):
        M=self.ele
        r%=Mod
        L=[[(r*M[i][j])%Mod for j in range(self.col)] for i in range(self.row)]
        return Modulo_Matrix(L)

    #累乗
    def __pow__(self,n):
        assert self.row==self.col, "正方行列ではありません."

        r=self.col

        def __mat_mul(A,B):
            E=[[0]*r for _ in range(r)]
            for i in range(r):
                a=A[i]; e=E[i]
                for k in range(r):
                    b=B[k]
                    for j in range(r):
                        e[j]+=a[k]*b[j]
                        e[j]%=Mod
            return E

        X=deepcopy(self.ele)
        E=[[1 if i==j else 0 for j in range(r)] for i in range(r)]

        sgn=1 if n>=0 else -1
        n=abs(n)

        while True:
            if n&1:
                E=__mat_mul(E,X)
            n>>=1
            if n:
                X=__mat_mul(X,X)
            else:
                break

        if sgn==1:
            return Modulo_Matrix(E)
        else:
            return Modulo_Matrix(E).inverse()

    #等号
    def __eq__(self,other):
        return self.ele==other.ele

    #不等号
    def __neq__(self,other):
        return not(self==other)

    #転置
    def transpose(self):
        return Modulo_Matrix(list(map(list,zip(*self.ele))))

    #行基本変形
    def row_reduce(self):
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
                u_inv=pow(u, -1, Mod)
                for j in range(C):
                    T[I][j]*=u_inv
                    T[I][j]%=Mod

                for i in range(R):
                    if i!=I:
                        v=T[i][J]
                        for j in range(C):
                            T[i][j]-=v*T[I][j]
                            T[i][j]%=Mod
                I+=1
                if I==R:
                    break

        return Modulo_Matrix(T)

    #列基本変形
    def column_reduce(self):
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
                u_inv=pow(u, -1, Mod)
                for i in range(R):
                    T[i][J]*=u_inv
                    T[i][J]%=Mod

                for j in range(C):
                    if j!=J:
                        v=T[I][j]
                        for i in range(R):
                            T[i][j]-=v*T[i][J]
                            T[i][j]%=Mod
                J+=1
                if J==C:
                    break

        return Modulo_Matrix(T)

    #行列の階数
    def rank(self):
        M=self.row_reduce()
        (R,C)=M.size
        T=M.ele

        rnk=0
        for i in range(R):
            f=False
            for j in range(C):
                if T[i][j]!=0:
                    f=True
                    break

            if f:
                rnk+=1
            else:
                break

        return rnk

    # 単射 ?
    def is_injection(self):
        return self.rank() == self.col

    # 全射 ?
    def is_surjective(self):
        return self.rank() == self.row

    # 全単射 ?
    def is_bijection(self):
        return self.col == self.row == self.rank()

    #行の結合
    def row_union(self,other):
        return Modulo_Matrix(self.ele+other.ele)

    #列の結合
    def column_union(self,other):
        E=[]
        for i in range(self.row):
            E.append(self.ele[i]+other.ele[i])

        return Modulo_Matrix(E)

    def __getitem__(self,index):
        if isinstance(index, int):
            return self.ele[index]
        else:
            return self.ele[index[0]][index[1]]

    def __setitem__(self,index,val):
        assert isinstance(index,tuple) and len(index)==2
        self.ele[index[0]][index[1]]=val

#=================================================
#単位行列
def Identity_Matrix(N):
    """ N 次単位行列を作成する. """

    return Modulo_Matrix([[1 if i==j else 0 for j in range(N)] for i in range(N)])

#零行列
def Zero_Matrix(row, col):
    """ row 行 col 列のゼロ行列を作成する. """

    return Modulo_Matrix([[0]*col for i in range(row)])

#正方行列?
def Is_Square(M):
    return M.row==M.col

#対角行列
def Diagonal_Matrix(D):
    """ D の第 i 要素が (i,i) 成分である対角行列を生成する.

    D: リスト
    """

    N=len(D)
    return Modulo_Matrix([[D[i] if i==j else 0 for j in range(N)] for i in range(N)])

#行列の直和
def Direct_Sum(*A):
    """ A=[A_0, A_1, ..., A_{N-1}] に対する直和行列を求める.

    """

    r=c=0
    for a in A:
        r+=a.row
        c+=a.col

    M=[[0]*c for _ in range(r)]
    x=y=0
    for p in range(len(A)):
        a=A[p]
        for i in range(a.row):
            b=A[p].ele[i]
            m=M[x+i]
            for j in range(a.col):
                m[y+j]=b[j]
        x+=a.row; y+=a.col
    return Modulo_Matrix(M)

#クロネッカー積
def Kronecker_Product(*X):
    A=[[1]]
    for B in X:
        A=[[A[i//B.row][j//B.col]*B[i%B.row][j%B.col]%Mod for j in range(len(A[0])*B.col)] for i in range(len(A)*B.row)]
    return Modulo_Matrix(A)

#クロネッカー和
def Kronecker_Sum(*X):
    A=Modulo_Matrix([[0]])
    for B in X:
        A=Kronecker_Product(A, Identity_Matrix(B.row))+Kronecker_Product(Identity_Matrix(A.row),B)
    return A

#跡
def Trace(M):
    """ 正方行列 M の跡 (=対角成分の和) を求める. """

    assert Is_Square(M)

    T=0
    for i in range(M.row):
        T+=M.ele[i][i]
        T%=Mod
    return T

def Determinant(M):
    """ 正方行列 M の行列式 (素数 mod) を求める."""

    assert Is_Square(M)

    N=M.row
    T=deepcopy(M.ele)
    det=1

    for j in range(N):
        if T[j][j]==0:
            for i in range(j+1,N):
                if T[i][j]:
                    break
            else:
                return 0
            T[j],T[i]=T[i],T[j]
            det=-det
        Tj=T[j]
        inv=pow(Tj[j], -1, Mod)
        for i in range(j+1,N):
            Ti=T[i]
            c=-inv*Ti[j]%Mod
            for k in range(N):
                Ti[k]+=c*Tj[k]
                Ti[k]%=Mod

    for i in range(N):
        det*=T[i][i]
        det%=Mod
    return det

def Determinant_Arbitrary_Mod(A):
    """ 正方行列 M の行列式 (任意 mod) を求める."""

    N=A.row
    A=deepcopy(A.ele)
    det=1

    for i in range(N):
        Ai=A[i]
        for j in range(i+1, N):
            Aj=A[j]
            while Aj[i]:
                alpha=Ai[i]//Aj[i]
                if alpha:
                    for k in range(i, N):
                        Ai[k]-=alpha*Aj[k]
                        Ai[k]%=Mod
                A[i], A[j]=A[j], A[i]
                Ai=A[i]; Aj=A[j]
                det*=-1
        det*=Ai[i]
        det%=Mod
        if det==0:
            break
    return det

def Characteristic_Polynomial(M):
    """ M の固有多項式を sum(P[i] X^i) としたとき, P を求める.

    M: Modulo Matrix
    """

    T=deepcopy(M.ele)
    N=M.row

    for j in range(N-2):
        for i in range(j+1, N):
            if T[i][j]:
                break
        else:
            continue

        T[j+1],T[i]=T[i],T[j+1]
        for k in range(N):
            T[k][j+1],T[k][i]=T[k][i],T[k][j+1]

        if T[j+1][j]:
            Tjj=T[j+1]
            inv=pow(Tjj[j], -1, Mod)
            for i in range(j+2, N):
                Ti=T[i]
                c=inv*Ti[j]%Mod
                for k in range(j,N):
                    Ti[k]-=c*Tjj[k]
                    Ti[k]%=Mod

                for k in range(N):
                    T[k][j+1]+=c*T[k][i]
                    T[k][j+1]%=Mod

    dp=[[0]*(i+1) for i in range(N+1)]; dp[0][0]=1
    for i in range(N):
        P=dp[i+1]
        for k in range(i+1):
            P[k+1]=dp[i][k]
        for k in range(i+1):
            P[k]+=T[i][i]*dp[i][k]
            P[k]%=Mod

        p=1
        for j in range(i-1,-1,-1):
            p*=-T[j+1][j]; p%=Mod
            c=p*T[j][i]%Mod
            for k in range(j+1):
                P[k]+=c*dp[j][k]
                P[k]%=Mod
    P=dp[-1]
    for i in range(N+1):
        if i%2:
            P[~i]*=-1; P[~i]%=Mod
    return P

#===
Mod=998244353
