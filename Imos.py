class Imos_1:
    def __init__(self,N):
        self.len=N
        self.list=[0]*(N+1)

    def add(self,F,T,C=1):
        """閉区間 [F,T] にCを加算する.
        """
        self.list[F]+=C
        self.list[T+1]-=C

    def cumulative_sum(self):
        """累積和を求める.
        """
        Y=[0]*(self.len)
        S=0
        for i in range(self.len):
            S+=self.list[i]
            Y[i]=S
        return Y

#=================================================
from collections import defaultdict
class Expanded_Imos_1:
    def __init__(self):
        self.dict=defaultdict(int)

    def add(self,F,T,C=1):
        """閉区間 [F,T] にCを加算する.
        """
        self.dict[F]+=C
        self.dict[T+1]-=C

    def cumulative_sum(self):
        """累積和を求める.
        """
        Y=defaultdict(int)
        S=0
        dic=self.dict
        for t in sorted(dic):
            if dic[t]!=0:
                Y[t]=S=S+dic[t]
        return Y

#=================================================
class Imos_2:
    def __init__(self,W,H):
        self.width=W
        self.height=H
        self.list=[[0]*(W+1) for _ in range(H+1)]

    def add(self,F,T,C=1):
        """F=(Fx,Fy), T=(Tx,Ty) に対して, 閉区間 [Fx,Tx] x [Fy,Ty] にCを加算する.
        """
        Fx,Fy=F
        Tx,Ty=T

        self.list[Fx][Fy]+=C
        self.list[Fx][Ty+1]-=C
        self.list[Tx+1][Fy]-=C
        self.list[Tx+1][Ty+1]+=C

    def cumulative_sum(self):
        Y=[[0]*(self.height+1) for _ in range(self.width+1)]

        for x in range(self.width+1):
            S=0
            for y in range(self.height+1):
                S+=self.list[x][y]
                Y[x][y]=S

        for y in range(self.height+1):
            S=0
            for x in range(self.width+1):
                S+=Y[x][y]
                Y[x][y]=S
        return Y
