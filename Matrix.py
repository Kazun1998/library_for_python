from copy import copy,deepcopy

class Matrix_Error(Exception):
    pass

class Matrix():
    #入力
    def __init__(self,M=[]):
        self.ele=M
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
            raise Matrix_Error("2つの行列のサイズが異なります.({},{})".format(A.size,B.size))
        M=A.ele
        N=B.ele

        L=[]
        for i in range(A.row):
            E=[]
            for j in range(A.col):
                E.append(M[i][j]+N[i][j])

            L.append(E)
        return Matrix(L)

    #減法
    def __sub__(self,other):
        return self+(-other)

    #乗法
    def __mul__(self,other):
        A=self
        B=other
        if isinstance(B,Matrix):
            R=A.row
            C=B.col

            if A.col!=B.row:
                raise Matrix_Error("左側の列と右側の行が一致しません.({},{})".format(A.size,B.size))
            G=A.col

            M=A.ele
            N=B.ele

            E=[]
            for i in range(R):
                F=[]
                for j in range(C):
                    S=0
                    for k in range(G):
                        S+=M[i][k]*N[k][j]
                    F.append(S)
                E.append(F)

            return Matrix(E)

        elif isinstance(B,int):
            return A.__scale__(B)

    def __rmul__(self,other):
        if isinstance(other,int):
            return self*other

    def Inverse(self):
        from copy import copy
        M=self
        if M.row!=M.col:
            raise Matrix_Error("正方行列ではありません.")

        R=M.row
        I=[[1*(i==j) for j in range(R)] for i in range(R)]
        G=M.Column_Union(Matrix(I))
        G=G.Row_Reduce()

        A,B=[],[]
        for i in range(R):
            A.append(copy(G.ele[i][:R]))
            B.append(copy(G.ele[i][R:]))

        if A==I:
            return Matrix(B)
        else:
            raise Matrix_Error("正則ではありません.")

    #スカラー倍
    def __scale__(self,r):
        M=self.ele
        L=[[r*M[i][j] for j in range(self.col)] for i in range(self.row)]
        return Matrix(L)

    #累乗
    def __pow__(self,n):
        A=self
        if A.row!=A.col:
            raise Matrix_Error("正方行列ではありません.")

        if n<0:
            return (A**(-n)).Inverse()

        R=Matrix([[1*(i==j) for j in range(A.row)] for i in range(A.row)])
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
                for j in range(C):
                    T[I][j]/=u

                for i in range(R):
                    if i!=I:
                        v=T[i][J]
                        for j in range(C):
                            T[i][j]-=v*T[I][j]
                I+=1
                if I==R:
                    break

        return Matrix(T)

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
                for i in range(R):
                    T[i][J]/=u

                for j in range(C):
                    if j!=J:
                        v=T[I][j]
                        for i in range(R):
                            T[i][j]-=v*T[i][J]
                J+=1
                if J==C:
                    break

        return Matrix(T)

    #行列の階数
    def Rank(self,ep=None):
        M=self.Row_Reduce()
        (R,C)=M.size
        T=M.ele

        S=0
        for i in range(R):
            f=False
            if ep==None:
                for j in range(C):
                    if T[i][j]!=0:
                        f=True
            else:
                for j in range(C):
                    if abs(T[i][j])>=ep:
                        f=True

            if f:
                S+=1
            else:
                break

        return S

    #行の結合
    def Row_Union(self,other):
        return Matrix(self.ele+other.ele)

    #列の結合
    def Column_Union(self,other):
        E=[]
        for i in range(self.row):
            E.append(self.ele[i]+other.ele[i])

        return Matrix(E)
#------------------------------------------------------------
#単位行列
def Identity_Matrix(n):
    return Matrix([[1*(i==j) for j in range(n)] for i in range(n)])

#零行列
def Zero_Matrix(r,c=None):
    if c==None:
        c=r
    return Matrix([[0]*c for i in range(r)])

#正方行列?
def Is_Square(M):
    return M.row==M.col

#対角行列
def Diagonal_Matrix(*A):
    N=len(A)
    return Matrix([[A[i]*(i==j) for j in range(N)] for i in range(N)])

#跡
def Trace(M):
    if not Is_Square(M):
        raise Matrix_Error("正方行列ではありません")

    T=0
    for i in range(M.col):
        T+=M.ele[i][i]

    return T

#行列式
def Det(M):
    if not Is_Square(M):
        raise Matrix_Error("正方行列ではありません")

    R=M.row
    T=deepcopy(M.ele)

    I=0
    D=1
    for J in range(R):
        if T[I][J]==0:
            for i in range(I+1,R):
                if T[i][J]!=0:
                    T[i],T[I]=T[I],T[i]
                    D*=-1
                    break

        if T[I][J]!=0:
            u=T[I][J]
            for j in range(R):
                T[I][j]/=u
            D*=u

            for i in range(I+1,R):
                v=T[i][J]
                for j in range(R):
                    T[i][j]-=v*T[I][j]
            I+=1
            if I==R:
                break

    for i in range(R):
        D*=T[i][i]

    return D

#要素毎に1変数関数を通す.
def Element_Map(M,f):
    T=deepcopy(M.ele)

    for i in range(M.row):
        for j in range(M.col):
            T[i][j]=f(T[i][j])

    return Matrix(T)
