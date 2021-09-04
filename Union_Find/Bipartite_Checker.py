from Union_Find import Union_Find

class Bipartite_Check():
    __slots__=["N","__Union"]
 
    def __init__(self,N):
        self.N=N
        self.__Union=Union_Find(2*N)
 
    def add_edge(self,u,v):
        self.__Union.union(u,v+self.N)
        self.__Union.union(u+self.N,v)
 
    def check(self):
        U=self.__Union
        for x in range(self.N):
            if U.same(x,x+self.N):
                return False
        return True
 
    def bipart(self, Mode=False):
        X=[-1]*self.N
        G=self.__Union.all_group_members()
        for x in range(self.N):
            if X[x]!=-1:
                continue
 
            z=self.__Union.find(x)
            for y in G[z]:
                if y<self.N:
                    if X[y]==1: return None,None
                    X[y]=0
                else:
                    if X[y-self.N]==0: return None,None
                    X[y-self.N]=1

        if Mode==0:
            return X
        else:
            U=[]; V=[]
            for x in range(self.N):
                if X[x]==0:
                    U.append(x)
                else:
                    V.append(x)
            return U,V

    def bipart_cases(self,Mod=None):
        """ 2部グラフへの分割の方法の場合の数を求める.

        """

        U,V=self.bipart(True)
        if U==None:
            return 0
        else:
            S=set()
            for u in U:
                S.add(self.__Union.find(u))
            return pow(2,len(S),Mod)
    
        
