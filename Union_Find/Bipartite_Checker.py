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

    def bipart_example(self):
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
        return X

    def bipart(self):
        Bip=[]
        seen=[0]*self.N
        G=self.__Union.all_group_members()

        for x in range(self.N):
            if seen[x]:
                continue

            g=self.__Union.find(x)
            U=[]; V=[]
            for y in G[g]:
                if seen[y%self.N]:
                    return None

                seen[y%self.N]=1
                if y<self.N:
                    U.append(y)
                else:
                    V.append(y-self.N)
            Bip.append((U,V))
        return Bip

    def bipart_cases(self, Mod=None):
        """ 2部グラフへの分割の方法の場合の数を求める.

        """

        Bip=self.bipart()
        if Bip is None:
            return 0
        else:
            return pow(2, len(Bip), Mod)

