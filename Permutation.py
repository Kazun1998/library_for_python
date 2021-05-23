class Permutation_Error(Exception):
    pass

class Permutation():
    def __init__(self,n,p=[]):
        if p==[]:
            self.p=[i for i in range(n)]
            self.ind=[i for i in range(n)]
        else:
            self.p=p[:]
            self.ind=[0]*n

            for i in range(n):
                self.ind[p[i]]=i

        self.n=n

    def index(self,i):
        if self.n<=i: return i
        else: return self.ind[i]

    def __str__(self):
        return "["+", ".join(map(str,self.p))+"]"

    __repr__=__str__

    def __mul__(self,other):
        T=[]
        n=max(self.n,other.n)

        for i in range(n):
            T.append(self.Replace(other.Replace(i)))

        return Permutation(n,T)

    def __truediv__(self,other):
        pass

    def __sgn__(self):
        if self.Minimum_Transposition()%2:
            return -1
        else:
            return 1

    def Inverse(self):
        Q=list(range(self.n))
        for k in range(self.n):
            Q[self.p[k]]=k
        return Permutation(self.n,Q)

    def Inversion(self):
        X=["*"]+[0]*self.n

        A=0
        Y=(self.n*(self.n-1))//2

        for a in self.p:
            s=a
            while 1<=s:
                Y-=X[s]
                s-=s&(-s)

            r=a+1
            while r<=self.n:
                X[r]+=1
                r+=r&(-r)
        return Y


    def Transposition(self,u,v):
        a=self.p.index(u)
        b=self.p.index(v)

        self.p[a]=v
        self.p[b]=u

        self.ind[a]=v
        self.ind[b]=u

    def Minimum_Transposition(self):
        X=self.Cycle_Division()

        T=0
        for d in X:
            T+=len(d)-1
        return T

    def Cycle_Multiplication(self,*C):
        X=[self.p.index(k) for k in C]

        N=len(C)
        for i in range(N):
            self.p[X[i]]=C[(i+1)%N]

    def Cycle_Division(self):
        T=[False]*self.n
        k=0
        v=0

        A=[]
        for k in range(self.n):
            if (not T[k]) and self.p[k]!=k:
                v=k
                B=[k]
                while self.p[v]!=k:
                    v=self.p[v]
                    T[v]=True
                    B.append(v)
                A.append(B)
        return A

    def Replace(self,x):
        if x<self.n:
            return self.p[x]
        else:
            return x

    def Replace_List(self,List):
        assert self.n==len(List),"置換の長さとリストの長さが違います."

        A=[0]*self.n
        for i in range(self.n):
            A[self.p[i]]=List[i]
        return A

    def Order(self):
        L=self.Cycle_Division()
        C=[]
        for K in L:
            C.append(len(K))
        return LCM(*C)

#-------------------------------------------------
#ランダムに置換を生成する.
def Random_Permutation(N):
    from random import shuffle
    L=list(range(N))
    shuffle(L)
    return Permutation(N,L)

def Is_Identity(P):
    for k,a in enumerate(P.p):
        if k!=a:
            return False
    return True

#以下Orderを用いる時に必要
#最大公約数
def gcd(m,n):
    x,y=max(m,n),min(m,n)
    if x%y==0:
        return y
    else:
        while x%y!=0:
            z=x%y
            x,y=y,z
        else:
            return z

from functools import reduce
def GCD(*X):
    return reduce(gcd,X)

#最小公倍数
def lcm(m,n):
    return (m//gcd(m,n))*n

def LCM(*X):
    return reduce(lcm,X)
