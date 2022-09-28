class Imos_1:
    def __init__(self, N):
        """ 区間 0<=t<N に対する Imos 法を準備する.
        """
        self.__N=N
        self.list=[0]*(N+1)

    def __len__(self):
        return len(self.list)-1

    def add(self, l, r, x=1):
        """閉区間 [l, r] に x を加算する."""

        assert 0<=l<self.__N
        assert 0<=r<self.__N

        if l<=r:
            self.list[l]+=x
            self.list[r+1]-=x

    def cumulative_sum(self):
        """累積和を求める.
        """
        X=self.list.copy()[:-1]
        for i in range(1,len(self)):
            X[i]+=X[i-1]
        return X

#=================================================
from collections import defaultdict
class Sparse_Imos_1:
    def __init__(self):
        self.dict=defaultdict(int)

    def add(self, l, r, x=1):
        """閉区間 [l,r] に x を加算する.
        """

        if l<=r:
            self.dict[l]+=x
            self.dict[r+1]-=x

    def cumulative_sum(self, since, until):
        """累積和を求める.

        [Output]
        (y, l, r) という形のリスト. ただし, (y, l, r) は l<=x<=y の範囲では y であるということを意味する.
        """
        Y=[]
        S=0
        t_old=since
        dic=self.dict
        for t in sorted(dic):
            if t>until:
                break
            if dic[t]==0:
                continue

            if t_old<=t-1:
                Y.append((S, t_old,t-1))

            S+=dic[t]
            t_old=t

        if t_old<=until:
            Y.append((S, t_old,until))
        return Y

#=================================================
class Linear_Imos_1:
    def __init__(self, N):
        """ 区間 0<=t<N に対する Imos 法を準備する.
        """
        self.__N=N
        self.list=[0]*(N+2)

    def __len__(self):
        return len(self.list)-2

    def add(self, l, r, x=1):
        """閉区間 [l, r] に x を加算する."""

        assert 0<=l<self.__N
        assert 0<=r<self.__N

        self.add_linear(l,r,x,0)

    def add_linear(self, l, r, a, b):
        """ 閉区間 [l,r] に次のようにして加算する.
        I[l]+=a, I[l+1]+=a+b, I[l+2]+=a+2b, ..., I[t]+=a+(t-r)b, ...,  I[r]+=a+(r-l)b
        """

        assert 0<=l<self.__N
        assert 0<=r<self.__N

        if l<=r:
            self.list[l]+=a
            self.list[l+1]+=-a+b
            self.list[r+1]+=-a-(r-l+1)*b
            self.list[r+2]+=a+(r-l)*b

    def cumulative_sum(self):
        """累積和を求める.
        """
        X=self.list.copy()[:len(self)]
        for _ in range(2):
            for i in range(1,len(self)):
                X[i]+=X[i-1]
        return X

#=================================================
class Imos_2:
    def __init__(self,W,H):
        self.width=W
        self.height=H
        self.list=[[0]*(W+1) for _ in range(H+1)]

    def add(self, i0, j0, i1, j1, x=1):
        """ 閉区間 [i0, j0] x [i1,j1] に x を加算する.
        """

        self.list[i0][j0]+=x
        self.list[i0][j1+1]-=x
        self.list[i1+1][j0]-=x
        self.list[i1+1][j1+1]+=x

    def add_row(self, i, x):
        """ 第 i 行 (i, *) に x を加える."""
        self.add(i, 0, i, self.width-1, x)

    def add_column(self, j, x):
        """ 第 j 列 (*, j) に x を加える."""
        self.add(0, j, self.height-1, j, x)

    def cumulative_sum(self):
        Y=[self.list[i].copy()[:-1] for i in range(self.height)]

        for _ in range(2):
            for i in range(len(Y)):
                y=Y[i]
                for j in range(1,len(y)):
                    y[j]+=y[j-1]
            Y=[list(y) for y in zip(*Y)]
        return Y
