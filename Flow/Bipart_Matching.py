from Flow import *

class Bipartite_Matching:
    def __init__(self,M,N):
        """ サイズが M,N からなる二部空グラフを作成する.
        """
        self.M=M
        self.N=N
        self.Size=M+N
        self.F=F=MaxFlow(M+N+2)

        for a in range(M):
            F.add_edge(M+N,a,1)

        for b in range(M,M+N):
            F.add_edge(b,M+N+1,1)

    def add_edge(self,a,b):
        """ 二部グラフに辺 X_a Y_b を加える.

        X_a, Y_b: 頂点 (0<=X_a<M, 0<=Y_b<N)
        """
        assert 0<=a<self.M and 0<=b<self.N
        self.F.add_edge(a,self.M+b,1)

    def max_matching_size(self):
        """ 二部グラフにおける最大マッチングのサイズを求める.
        """
        return self.F.max_flow(self.Size,self.Size+1)

    def max_matching(self,Mode=0):
        """ 二部グラフにおける最大マッチングの1つを求める.

        Mode:
        0: 最大マッチングの方法のみ
        1: 最大マッチングのサイズとその方法
        """

        size=self.max_matching_size()
        A=[-1]*self.M
        B=[-1]*self.N

        G=self.F.graph
        for a in range(self.M):
            for e in G[a]:
                if e.flow==1:
                    b=e.target-self.M
                    A[a]=b
                    B[b]=a
                    break

        if Mode==0:
            return A,B
        else:
            return size,(A,B)
