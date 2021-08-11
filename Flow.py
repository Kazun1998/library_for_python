#Thansk for  aaaaaaaaaa2230
#URL:https://atcoder.jp/contests/practice2/submissions/17017319
from collections import deque
import sys
class MaxFlow:
    class Edge:
        def __init__(self,target,cap,base,direct):
            self.target = target
            self.cap = cap
            self.flow=0
            self.base=base
            self.direct=direct
            self.rev = None

        def __str__(self):
            return "target:{}, flow/cap:{}/{}".format(self.target,self.flow,self.direct*self.base)

        __repr__=__str__

    def __init__(self,N):
        self.N = N
        self.graph = [[] for _ in range(N)]
        self.old_flow=0

    def add_edge(self,u,v, cap):
        """容量が cap である有向辺 u→v を加える.
        """
        graph = self.graph
        edge = self.Edge(v,cap,cap,1)
        edge2 = self.Edge(u,0,cap,-1)
        edge.rev = edge2
        edge2.rev = edge
        graph[u].append(edge)
        graph[v].append(edge2)

    def __bfs(self, s, t):
        level = self.level = [self.N]*self.N
        q = deque([s])
        level[s] = 0
        while q:
            now = q.popleft()
            lw = level[now]+1
            for e in self.graph[now]:
                if e.cap and level[e.target]> lw:
                    level[e.target] = lw
                    if e.target == t:
                        return True
                    q.append(e.target)
        return False

    def __dfs(self, s, t, up):
        graph = self.graph
        it = self.it
        level = self.level

        st = deque([t])
        while st:
            v = st[-1]
            if v == s:
                st.pop()
                flow = up
                for w in st:
                    e = graph[w][it[w]].rev
                    flow = min(flow, e.cap)
                for w in st:
                    e = graph[w][it[w]]
                    e.cap += flow
                    e.flow-=flow
                    e.rev.cap -= flow
                    e.rev.flow+=flow
                return flow
            lv = level[v]-1
            while it[v] < len(graph[v]):
                e = graph[v][it[v]]
                re = e.rev
                if re.cap == 0 or lv != level[e.target]:
                    it[v] += 1
                    continue
                st.append(e.target)
                break
            if it[v] == len(graph[v]):
                st.pop()
                level[v] = self.N

        return 0

    def max_flow(self,source,target,flow_limit=float("inf")):
        Flow=0
        while Flow < flow_limit and self.__bfs(source,target):
            self.it=[0]*self.N
            while Flow<flow_limit:
                F=self.__dfs(source,target,flow_limit-Flow)
                if F==0:break
                Flow+=F
        self.old_flow+=Flow
        return self.old_flow

    def flow(self):
        X=[{} for _ in range(N)]
        for i in range(self.N):
            x=X[i]
            for e in self.graph[i]:
                if e.direct==-1: continue
                if e.target not in x: x[e.target]=0
                x[e.target]+=e.flow
        return X

    def min_cut(self,s):
        """sにおける最小カットを求める.

        s:sorce
        """
        visited = [0]*self.N
        q = deque([s])
        while q:
            v = q.pop()
            visited[v] = 1
            for e in self.graph[v]:
                if e.cap and not visited[e.target]:
                    q.append(e.target)
        return visited

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
        """

        self.F.add_edge(a,self.M+b,1)

    def max_matching_size(self):
        return self.F.max_flow(self.Size,self.Size+1)

    def max_matching(self):
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
        return A,B

S=[
    [0,0,1,1,0,0,0,0],
    [0,1,1,1,0,0,0,0],
    [1,1,1,1,1,0,1,1],
    [1,1,1,1,1,0,1,1],
    [1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1],
    [0,0,0,1,1,1,1,1],
    [0,0,0,0,1,1,1,0]]

A=[
    [0,0,1,1,2,2,3,3],
    [4,4,5,5,6,6,7,7],
    [8,8,9,9,10,10,11,11],
    [12,12,13,13,14,14,15,15],
    [16,16,17,17,18,18,19,19],
    [20,20,21,21,22,22,23,23],
    [24,24,25,25,26,26,27,27],
    [28,28,29,29,30,30,31,31]]

def p(x,y):
    return A[x][y]

H=W=8
M=Bipartite_Matching(32,32)

E=[set() for _ in range(32)]
for x in range(8):
    for y in range(8):
        if (x+y)%2==1: continue
        if S[x][y]==0: continue

        i=p(x,y)
        if 0<y and S[x][y-1]==1: E[i].add(p(x,y-1))
        if y<7 and S[x][y+1]==1: E[i].add(p(x,y+1))
        if 0<x and S[x-1][y]==1: E[i].add(p(x-1,y))
        if x<7 and S[x+1][y]==1: E[i].add(p(x+1,y))
