class Permutation_Error(Exception):
    pass

class Permutation():
    def __init__(self, n, p=[]):
        if p==[]:
            self.p=[i for i in range(n)]
            self.ind=[i for i in range(n)]
        else:
            self.p=p
            self.ind=[0]*n

            for i in range(n):
                self.ind[p[i]]=i

        self.n=n

    def __getitem__(self, k):
        return self.p[k]

    def __str__(self):
        return str(self.p)

    __repr__=__str__

    def __eq__(self,other):
        return (self.n==other.n) and (self.p==other.p)

    def __mul__(self,other):
        assert self.n==other.n

        p=self.p; q=other.p
        return Permutation(self.n,  [p[q[i]] for i in range(self.n)])

    def __pow__(self, n):
        if n<0:
            return pow(self,-n).inverse()

        a=list(range(self.n))
        e=self.p[:]

        while n:
            if n&1:
                a=[a[e[i]] for i in range(self.n)]
            e=[e[e[i]] for i in range(self.n)]
            n>>=1

        return Permutation(self.n, a)
                
    def __truediv__(self,other):
        pass

    def sgn(self):
        if self.Minimum_Transposition()%2:
            return -1
        else:
            return 1

    def inverse(self):
        return Permutation(self.n, self.ind)

    def inversion(self):
        BIT=[0]*(self.n+1)
        Y=(self.n*(self.n-1))//2

        for a in self.p:
            s=a
            while 1<=s:
                Y-=BIT[s]
                s-=s&(-s)

            r=a+1
            while r<=self.n:
                BIT[r]+=1
                r+=r&(-r)
        return Y

    def transposition(self,u,v):
        """ u,v のある場所を交換する ※ u番目とv番目ではない"""

        
        a=self.ind[u]
        b=self.ind[v]

        self.p[a]=v
        self.p[b]=u

        self.ind[u]=b
        self.ind[v]=a

    def minimum_transposition(self):
        """ 互換の最小回数を求める. """

        X=self.cycle_division()

        T=0
        for d in X:
            T+=len(d)-1
        return T

    def Cycle_Multiplication(self,*C):
        X=[self.p.index(k) for k in C]

        N=len(C)
        for i in range(N):
            self.p[X[i]]=C[(i+1)%N]

    def cycle_division(self, mode=True):
        """ 置換を巡回置換の積に分解する.

        mode: 自己ループを入れるか否か"""

        p=self.p
        T=[False]*self.n
        A=[]

        for k in range(self.n):
            if not T[k]:
                a=[k]

                T[k]=True
                v=p[k]
                while v!=k:
                    T[v]=True
                    a.append(v)
                    v=p[v]

                if mode or len(a)>=2:
                    A.append(a)
        return A

    def operate_List(self, list):
        assert self.n==len(list),"置換の長さとリストの長さが違います."

        return [list[self.ind[i]] for i in range(self.n)]


    def order(self):
        from math import gcd

        x=1
        for m in self.cycle_division():
            g=gcd(x,len(m))
            x=(x//g)*len(m)
        return x

#=================================================
def Permutation_Inversion(P,Q):
    """ P から Q へ隣接項同士の入れ替えのみの最小回数を求める.
    """
    R=Q*(P.inverse())
    return R.inversion()

def List_Inversion(A,B):
    """長さが等しいリスト A,B に対して, 以下の操作の最小回数を求める.
    列 A[i] と A[i+1] を入れ替え, B と一致させる.
    """

    from collections import defaultdict

    if len(A)!=len(B):
        return -1

    N=len(A)
    D=defaultdict(list)

    for i in range(N):
        D[A[i]].append(i)

    for lis in D:
        D[lis].reverse()

    try:
        return Permutation(N,[D[B[i]].pop() for i in range(N)]).inversion()
    except:
        return -1
#=================================================
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
