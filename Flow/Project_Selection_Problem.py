""" Note: Project Selection Problem で対応できる条件の一覧

h(x)=0 ならば a 点得る → set_zero(x,a)
h(x)=1 ならば a 点得る → set_one(x,a)
h(x)=0 かつ h(y)=1 ならば a (<=0) 点を得る → set_not_equal(x,y,a)
h(x_0)=...=h(x_{k-1})=0 ならば a (>=0) 点を得る → set_all_zero(X,a)
h(x_0)=...=h(x_{k-1})=1 ならば a (>=0) 点を得る → set_all_one(X,a)

一般的なグラフでは対応できない条件の例
[1]
h(x)=h(y)=0 ならば a (<=0) 点を得る
h(x)=h(y)=1 ならば a (<=0) 点を得る
→ グラフが二部グラフ (部集合を X,Y とする) であり, x in X,y in Y ならば, 以下のようにして変換する.
h'(z)=h(x) (x in X), 1-h(y) (y in Y) として, h' での条件 「h'(x),h'(y) が・・・ ならば, a (<=0) 点を得る」に置き換える.

[2]
h(x) != h(y) ならば, a (>=0) 点を得る
→グラフが二部グラフ (部集合を X,Y とする) であり, x in X,y in Y ならば, 以下のようにして変換する.
無条件に a 点得て, 「h(x)=h(y) ならば -a (<=0) 点を得る」に置き換える.
※下駄を履かせることと, 下駄をA, 帰着問題の答えを X としたとき, 元問題の答えは A+X になることに注意!!
"""

from Flow import *

inf=float("inf")
class Project_Selection_Problem:
    def __init__(self,N=0):
        """ N 要素の Project Selection Problem を生成する.

        N: int
        """

        self.N=N
        self.ver_num=N+2
        self.base=0
        self.source=N
        self.target=N+1
        self.indivi=[[0,0] for _ in range(N+2)]
        self.mutual=[]

    def add_vertex(self):
        n=self.ver_num
        self.indivi.append([0,0])
        self.ver_num+=1
        return n

    def __add_vertex_inner(self):
        n=self.ver_num
        self.indivi.append([None,None])
        self.ver_num+=1
        return n

    def add_vertices(self, k):
        n=self.ver_num
        self.indivi.extend([[0,0] for _ in range(k)])
        self.ver_num+=k
        return list(range(n,n+k))

    def set_zero_one(self,x,y,a):
        """ h(x)=0,  h(y)=1 のとき, a (<=0) 点を得るという条件を追加する.

        0<=x,y<N
        a<=0
        """

        assert 0<=x<self.N
        assert 0<=y<self.N
        assert a<=0

        self.mutual.append((x,y,-a))

    def set_zero(self,x,a):
        """ h(x)=0 のとき, a 点を得るという条件を追加する.

        0<=x<N
        """

        assert 0<=x<self.N
        self.indivi[x][0]+=a

    def set_one(self,x,a):
        """ h(x)=1 のとき, a 点を得るという条件を追加する.

        0<=x<N
        """

        assert 0<=x<self.N
        self.indivi[x][1]+=a

    def set_all_zero(self,X,a):
        """ h(x)=0 (forall x in X) のとき, a (>=0) 点を得るという条件を追加する.

        0<=x<N
        a>=0
        """

        assert a>=0

        k=self.__add_vertex_inner()
        self.base+=a

        self.indivi[k][0]=-a
        for x in X:
            assert 0<=x<self.N
            self.mutual.append((k,x,inf))

    def set_all_one(self,X,a):
        """ h(x)=1 (forall x in X) のとき, a (>=0) 点を得るという条件を追加する.

        0<=x<N
        a>=0
        """

        assert a>=0

        k=self.__add_vertex_inner()
        self.base+=a

        self.indivi[k][1]=-a
        for x in X:
            assert 0<=x<self.N
            self.mutual.append((x,k,inf))

    def set_not_equal(self,x,y,a):
        """ h(x)!=h(y) ならば, a (<=0) 点を得るという条件を追加する.

        0<=x,y<N
        a<=0
        """

        assert 0<=x<self.N and 0<=y<self.N
        assert a<=0

        self.set_zero_one(x,y,a)
        self.set_zero_one(y,x,a)

    def set_equal(self,x,y,a):
        """ h(x)=h(y) ならば, a (>=0) 点を得るという条件を追加する.

        0<=x,y<N
        a>=0
        """

        assert 0<=x<self.N and 0<=y<self.N
        assert a>=0

        self.set_all_zero([x,y],a)
        self.set_all_one([x,y],a)

    def ban_zero(self,x):
        """ h(x)=0 となることを禁止する. (実行したら -inf 点になる)

        0<=x<N
        """

        assert 0<=x<self.N
        self.set_zero(x,-inf)

    def ban_one(self,x):
        """ h(x)=1 となることを禁止する. (実行したら -inf 点になる)

        0<=x<N
        """

        assert 0<=x<self.N
        self.set_one(x,-inf)

    def force_zero(self, x):
        """ h(x) = 0 という条件を追加する (つまり, ban_zero(x)).

        0 <= x < N
        """

        assert 0 <= x < self.N
        self.ban_one(x)

    def force_one(self, x):
        """ h(x) = 1 という条件を追加する (つまり, ban_one(x)).

        0 <= x < N
        """

        assert 0 <= x < self.N
        self.ban_zero(x)

    def increase(self, X):
        """ h(x[0]) <= h(x[1]) <= ... <= h(x[n-2]) (h(x[i]) = 1, h(x[i+1]) = 0 を禁止) という条件を追加する.

        """

        for i in range(len(X) - 1):
            self.set_zero_one(X[i + 1], X[i], -inf)

    def decrease(self, X):
        self.increase(X[::-1])

    def solve(self,Mode=0):
        """ Project Selection Problem を解く.

        Mode
        0: 最大値のみ
        1: 最大値とそれを達成する例
        """

        F=MaxFlow(self.ver_num)
        base=self.base
        for i in range(self.N):
            F.add_arc(self.source,i,0)
            F.add_arc(i,self.target,0)

            if self.indivi[i][0]>=0:
                base+=self.indivi[i][0]
                F.add_arc(self.source,i,self.indivi[i][0])
            else:
                F.add_arc(i,self.target,-self.indivi[i][0])

            if self.indivi[i][1]>=0:
                base+=self.indivi[i][1]
                F.add_arc(i,self.target,self.indivi[i][1])
            else:
                F.add_arc(self.source,i,-self.indivi[i][1])

        for i in range(self.target+1,self.ver_num):
            if self.indivi[i][0]!=None:
                F.add_arc(self.source,i,-self.indivi[i][0])
            if self.indivi[i][1]!=None:
                F.add_arc(i,self.target,-self.indivi[i][1])

        for x,y,c in self.mutual:
            F.add_arc(x,y,c)

        alpha=F.max_flow(self.source,self.target)
        if Mode==0:
            return base-alpha
        else:
            return base-alpha, F.min_cut(self.source), self.source, self.target
