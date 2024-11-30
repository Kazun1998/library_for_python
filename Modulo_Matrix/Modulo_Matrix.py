from copy import deepcopy

class SingularMatrixError(Exception):
    def __str__(self):
        return "非正則行列の逆行列を求めようとしました."

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

    # 零行列, 単位行列
    @classmethod
    def Zero_Matrix(cls, row, col):
        return Modulo_Matrix([[0] * col for _ in range(row)])

    @classmethod
    def Identity_Matrix(cls, N):
        return Modulo_Matrix([[1 if i==j else 0 for j in range(N)] for i in range(N)])

    #+,-
    def __pos__(self):
        return self

    def __neg__(self):
        return self.__scale__(-1)

    #加法
    def __add__(self, other):
        C = [None] * self.row
        for i, (Ai, Bi) in enumerate(zip(self.ele, other.ele)):
            C[i] = [Ai[j] + Bi[j] for j in range(self.col)]

        return Modulo_Matrix(C)

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
        C = [None] * self.row
        for i, (Ai, Bi) in enumerate(zip(self.ele, other.ele)):
            C[i] = [Ai[j] - Bi[j] for j in range(self.col)]

        return Modulo_Matrix(C)

    def __isub__(self,other):
        M=self.ele; N=other.ele

        for i in range(self.row):
            Mi,Ni=M[i],N[i]
            for j in range(self.col):
                Mi[j]-=Ni[j]
                Mi[j]%=Mod
        return self

    #乗法
    def __mul__(self, other):
        if isinstance(other, int):
            return self.__scale__(other)

        if not isinstance(other, Modulo_Matrix):
            raise TypeError

        assert self.col == other.row, f"左側の列と右側の行が一致しません (left: {self.col}, right:{other.row})."

        A = self.ele; B = other.ele
        C = [[0] * other.col for _ in range(self.row)]

        for i, Ci in enumerate(C):
            for k, a_ik in enumerate(A[i]):
                for j, b_kj in enumerate(B[k]):
                    Ci[j] = (Ci[j] + a_ik * b_kj) % Mod

        return Modulo_Matrix(C)

    def __rmul__(self,other):
        if isinstance(other,int):
            return self.__scale__(other)

    def inverse(self):
        inverse, _ = self.inverse_with_determinant()
        if self is None:
            raise SingularMatrixError()

        return inverse

    def inverse_with_determinant(self):
        assert self.row == self.col,"正方行列ではありません."

        M = self
        N = M.row
        R = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
        T = deepcopy(M.ele)
        det = 1

        for j in range(N):
            if T[j][j] == 0:
                for i in range(j+1,N):
                    if T[i][j]:
                        break
                else:
                    return None, 0

                T[j], T[i] = T[i], T[j]
                R[j], R[i] = R[i], R[j]
                det = -det % Mod

            Tj, Rj = T[j] ,R[j]
            inv = pow(Tj[j], -1, Mod)
            det = (Tj[j] * det) % Mod

            for k in range(N):
                Tj[k] *=inv; Tj[k] %= Mod
                Rj[k] *=inv; Rj[k] %= Mod

            for i in range(N):
                if i == j:
                    continue

                c = T[i][j]
                Ti, Ri = T[i], R[i]
                for k in range(N):
                    Ti[k] -= Tj[k] * c; Ti[k] %= Mod
                    Ri[k] -= Rj[k] * c; Ri[k] %= Mod

        for i in range(N):
            det = (T[i][i] * det) % Mod

        return Modulo_Matrix(R), det

    #スカラー倍
    def __scale__(self, r):
        r %= Mod
        return Modulo_Matrix([[r * m_ij for m_ij in Mi] for Mi in self.ele])

    #累乗
    def __pow__(self, n):
        assert self.row==self.col, "正方行列ではありません."

        sgn = 1 if n >= 0 else -1
        n = abs(n)

        C = Modulo_Matrix.Identity_Matrix(self.row)
        tmp = self
        while n:
            if n & 1:
                C = C * tmp
            tmp = tmp * tmp
            n >>= 1

        return C if sgn == 1 else C.inverse()

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
        (row, col) = self.size

        T = deepcopy(self.ele)

        I = 0
        for J in range(col):
            if T[I][J] == 0:
                for i in range(I + 1, row):
                    if T[i][J] != 0:
                        T[i], T[I] = T[I], T[i]
                        break
                else:
                    continue

            u = T[I][J]
            u_inv = pow(u, -1, Mod)
            for j in range(col):
                T[I][j] *= u_inv
                T[I][j] %= Mod

            for i in range(row):
                if i == I:
                    continue

                v = T[i][J]
                for j in range(col):
                    T[i][j] -= v * T[I][j]
                    T[i][j] %= Mod
            I += 1
            if I == row:
                break

        return Modulo_Matrix(T)

    #列基本変形
    def column_reduce(self):
        (row, col) = self.size

        T = deepcopy(self.ele)

        J = 0
        for I in range(row):
            if T[I][J] ==0 :
                for j in range(J + 1, col):
                    if T[I][j] != 0:
                        for k in range(row):
                            T[k][j], T[k][J] = T[k][J], T[k][j]
                        break
                else:
                    continue

            u = T[I][J]
            u_inv = pow(u, -1, Mod)
            for i in range(row):
                T[i][J] *= u_inv
                T[i][J] %= Mod

            for j in range(col):
                if j != J:
                    v = T[I][j]
                    for i in range(row):
                        T[i][j] -= v * T[i][J]
                        T[i][j] %= Mod
            J += 1
            if J == col:
                break

        return Modulo_Matrix(T)

    #行列の階数
    def rank(self):
        row_reduced = self.row_reduce()
        (row, col) = row_reduced.size

        rnk = 0
        for i in range(row):
            Ti = row_reduced.ele[i]
            if any(Ti[j] for j in range(col)):
                rnk += 1

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
        A=Kronecker_Product(A, Modulo_Matrix.Identity_Matrix(B.row))+Kronecker_Product(Modulo_Matrix.Identity_Matrix(A.row),B)
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

def Adjugate_Matrix(A):
    """ A の余因子行列 adj A := ((-1)^(i+j) det A_{i,j}) を求める.

    Args:
        A (Matrix): 正方行列
    """

    from random import randint

    N = A.row
    A_ext = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            A_ext[i][j] = A[i][j]

    for i in range(N):
        A_ext[i][N] = A_ext[N][i] = randint(0, Mod - 1)

    A_ext_inv, det = Modulo_Matrix(A_ext).inverse_with_determinant()

    if A_ext_inv is None:
        return Modulo_Matrix.Zero_Matrix(N, N)

    adj = [[det * ((A_ext_inv[N][N] * A_ext_inv[i][j] - A_ext_inv[i][N] * A_ext_inv[N][j]) % Mod) for j in range(N)] for i in range(N)]
    return Modulo_Matrix(adj)

#===
Mod=998244353
