class Permutation:
    def __init__(self, n: int, p: list[int] = None):
        """ N 要素の置換を生成する.

        Args:
            n (int): 要素数
            p (list[int], optional): 初期状態. None のときは恒等置換になる. Defaults to None.
        """

        if p is None:
            self.p = list(range(n))
            self.ind = list(range(n))
        else:
            self.p = p
            self.ind = [0] * n

            for i in range(n):
                self.ind[p[i]] = i

        self._n = n

    @property
    def N(self) -> int:
        return self._n

    def __getitem__(self, k: int) -> int:
        return self.p[k]

    def __str__(self) -> str:
        return str(self.p)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.N}, {self.p})"

    def __eq__(self, other: "Permutation") -> bool:
        return (self.N == other.N) and (self.p == other.p)

    def __iter__(self):
        return iter(self.p)

    def __len__(self) -> int:
        return self.N

    def index(self, x: int) -> int:
        return self.ind[x]

    def __mul__(self, other: "Permutation") -> "Permutation":
        assert self.N == other.N

        p = self.p
        q = other.p
        return Permutation(self.N,  [p[q[i]] for i in range(self.N)])

    def __pow__(self, k: int) -> "Permutation":
        if k < 0:
            return pow(self, -k).inverse()

        N = len(self)
        a = list(range(N))
        e = self.p[:]

        while k:
            if k & 1:
                a = [a[e[i]] for i in range(N)]
            e = [e[e[i]] for i in range(N)]
            k >>= 1

        return Permutation(N, a)

    def sgn(self):
        """ 置換の符号を求める (偶置換 → 1, 奇置換 → -1)

        """
        return -1 if self.minimum_transposition() % 2 else 1

    def inverse(self):
        return Permutation(len(self), self.ind)

    def inversion(self) -> int:
        """ 転倒数を求める.

        Returns:
            int: 転倒数
        """

        BIT = [0] * (len(self) + 1)
        y = (self.n * (self.n-1)) // 2

        for a in self.p:
            s = a
            while 1 <= s:
                y -= BIT[s]
                s -= s & (-s)

            r = a + 1
            while r <= self.n:
                BIT[r] += 1
                r += r & (-r)
        return y

    def swap(self, i: int, j: int):
        """ i 番目と j 番目を交換する (※ i と j を交換ではない)

        Args:
            i (int):
            j (int):
        """

        u=self.p[i]; v=self.p[j]

        self.p[i]=v; self.p[j]=u
        self.ind[v]=i; self.ind[u]=j

    def transposition(self, u: int, v: int):
        """ u と v を交換する (※ u 番目と v 番目ではない)

        Args:
            u (int):
            v (int):
        """

        a=self.ind[u]; b=self.ind[v]

        self.p[a]=v; self.p[b]=u
        self.ind[u]=b; self.ind[v]=a

    def minimum_transposition(self) -> int:
        """ 互換の最小回数を求める.

        Returns:
            int: 互換の最小回数
        """

        return len(self) - len(self.cycle_division())

    def cycle_division(self, self_loop = True) -> list[list[int]]:
        """ 置換を巡回置換の積に分解する.

        Args:
            self_loop (bool, optional): 長さ 1 の自己ループを入れるかどうか. Defaults to True.

        Returns:
            list[list[int]]: 各要素がサイクルになる.
        """

        N = len(self)
        p = self.p
        seen = [False] * N
        cycles: list[list[int]] = []

        for k in range(N):
            if seen[k]:
                continue

            cycle = [k]
            seen[k] = True
            v = k

            while (v := p[v]) != k:
                seen[v] = True
                cycle.append(v)

            if self_loop or len(cycle)>=2:
                cycles.append(cycle)

        return cycles

    def operate_list(self, list):
        assert self.n==len(list),"置換の長さとリストの長さが違います."

        return [list[self.ind[i]] for i in range(self.n)]


    def order(self, mod=None):
        """ 位数を求める (mod を指定すると, mod で割った余りになる).

        """

        from math import gcd

        if mod==None:
            x=1
            for m in self.cycle_division():
                g=gcd(x,len(m))
                x=(x//g)*len(m)
            return x
        else:
            def factor(n):
                e=(n&(-n)).bit_length()-1
                yield 2,e

                n>>=e

                p=3
                while p*p<=n:
                    if n%p==0:
                        e=0
                        while n%p==0:
                            n//=p
                            e+=1
                        yield p,e
                    p+=2

                if n>1:
                    yield n,1
                return

            T={}
            for m in self.cycle_division():
                for p,e in factor(len(m)):
                    T[p]=max(T.get(p,0), e)

            x=1
            for p in T:
                x*=pow(p, T[p], mod)
                x%=mod
            return x

    def conjugate(self) -> "Permutation":
        """ 共役の互換を求める.

        Returns:
            Permutation: 共役の互換
        """

        N = len(self)
        return Permutation(N, [N - 1 - x for x in self.p])

    def next(self):
        y=[]
        for i in range(self.n-1,0,-1):
            y.append(self.p[i])
            if self.p[i-1]<self.p[i]:
                y.append(self.p[i-1])
                a=self.p[i-1]
                break

        x=self.p[:i-1]
        y.sort()
        for j,b in enumerate(y):
            if a<b:
                x.append(b)
                del y[j]
                break
        return Permutation(self.n, x+y)

#=================================================
def Permutation_Inversion(P, Q):
    """ P から Q へ隣接項同士の入れ替えのみの最小回数を求める.
    """
    R=Q*(P.inverse())
    return R.inversion()

def List_Inversion(A, B, default=-1):
    """長さが等しいリスト A,B に対して, 以下の操作の最小回数を求める.
    列 A[i] と A[i+1] を入れ替え, B と一致させる.
    """

    from collections import defaultdict

    if len(A)!=len(B):
        return default

    N=len(A)
    D=defaultdict(list)

    for i in range(N):
        D[A[i]].append(i)

    for lis in D:
        D[lis].reverse()

    try:
        return Permutation(N,[D[B[i]].pop() for i in range(N)]).inversion()
    except:
        return default

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

def Generate_Permutation(P, Q):
    """ P を Q にする変換を表す置換を生成する.

    """
    assert len(P)==len(Q)
    N=len(P)
    X=[-1]*N
    for i in range(N):
        X[P[i]]=Q[i]
    return Permutation(N, X)
