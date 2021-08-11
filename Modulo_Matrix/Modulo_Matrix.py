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
        self.__is_calculatable(other)
        M=self.ele; N=other.ele

        L=[[0]*self.col for _ in range(self.row)]
        for i in range(self.row):
            Li,Mi,Ni=L[i],M[i],N[i]
            for j in range(self.col):
                Li[j]=Mi[j]+Ni[j]
        return Modulo_Matrix(L,self.Mod)

    def __iadd__(self,other):
        self.__is_calculatable(other)
        M=self.ele; N=other.ele

        for i in range(self.row):
            Mi,Ni=M[i],N[i]
            for j in range(self.col):
                Mi[j]+=Ni[j]
                Mi[j]%=self.Mod
        return self

    #減法
    def __sub__(self,other):
        self.__is_calculatable(other)
        M=self.ele; N=other.ele

        L=[[0]*self.col for _ in range(self.row)]
        for i in range(self.row):
            Li,Mi,Ni=L[i],M[i],N[i]
            for j in range(self.col):
                Li[j]=Mi[j]-Ni[j]
        return Modulo_Matrix(L,self.Mod)

    def __isub__(self,other):
        self.__is_calculatable(other)
        M=self.ele; N=other.ele

        for i in range(self.row):
            Mi,Ni=M[i],N[i]
            for j in range(self.col):
                Mi[j]-=Ni[j]
                Mi[j]%=self.Mod
        return self

    #乗法
    def __mul__(self,other):
        if isinstance(other,Modulo_Matrix):
            if self.col!=other.row:
                raise Modulo_Matrix_Error("左側の列と右側の行が一致しません.({},{})".format(self.size,other.size))

            M=self.ele; N=other.ele
            E=[[0]*other.col for _ in range(self.row)]

            for i in range(self.row):
                Ei,Mi=E[i],M[i]
                for k in range(self.col):
                    m_ik,Nk=Mi[k],N[k]
                    for j in range(other.col):
                        Ei[j]+=m_ik*Nk[j]
                        Ei[j]%=self.Mod
            return Modulo_Matrix(E,self.Mod)
        elif isinstance(other,int):
            return self.__scale__(other)

    def __rmul__(self,other):
        if isinstance(other,int):
            return self.__scale__(other)

    def Inverse(self):
        if  self.row!=self.col:
            raise Modulo_Matrix_Error("正方行列ではありません.")

        M=self
        N=M.row; Mod=M.Mod
        R=[[int(i==j) for j in range(N)] for i in range(N)]
        T=deepcopy(M.ele)

        for j in range(N):
            if T[j][j]==0:
                for i in range(j+1,N):
                    if T[i][j]:
                        break
                else:
                    raise Modulo_Matrix_Error("正則行列ではありません")
                T[j],T[i]=T[i],T[j]
                R[j],R[i]=R[i],R[j]
            Tj,Rj=T[j],R[j]
            inv=pow(Tj[j],Mod-2,Mod)
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
        return Modulo_Matrix(R,Mod)

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

def Determinant(M):
    if not Is_Square(M):
        raise Modulo_Matrix_Error("正方行列ではありません")

    N=M.row
    Mod=M.Mod
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
            det*=-1
        Tj=T[j]
        inv=pow(Tj[j],Mod-2,Mod)
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

