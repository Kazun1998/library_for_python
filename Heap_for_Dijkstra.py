class Dijkstra_Heap:
    inf=float("inf")

    def __init__(self,N):
        """ ダイクストラ専用のヒープを生成する.
        """

        self.N=N
        self.remain=N

        self.value=[Dijkstra_Heap.inf]*N
        self.dist=[-1]*N
        self.tree=list(range(N))
        self.inverse=list(range(N))

    def __bool__(self):
        return bool(self.remain)

    def __swap(self, i, j):
        """ ヒープ木の第 i 要素と第 j 要素を交換する. """

        self.value[i],self.value[j]=self.value[j],self.value[i]

        p=self.tree[i]; q=self.tree[j]

        self.tree[i],self.tree[j]=q,p
        self.inverse[p],self.inverse[q]=j,i

    def pop(self):
        assert bool(self.remain)

        p=self.tree[0]
        d=self.value[0]

        self.dist[p]=d
        self.remain-=1

        self.__swap(0,self.remain)
        self.value[self.remain]=Dijkstra_Heap.inf

        V=self.value
        k=0
        while True:
            if 2*k+1>=self.N:
                break

            if 2*k+2==self.N:
                if V[k]<=V[2*k+1]:
                    break
                j=2*k+1
            else:
                u=V[2*k+1]; v=V[2*k+2]

                if V[k]<=u and V[k]<=v:
                    break

                if u<=v:
                    j=2*k+1
                else:
                    j=2*k+2
            self.__swap(k,j)
            k=j

        return (p,d)

    def __setitem__(self,index,value):
        if self.dist[index]!=-1:
            return

        V=self.value
        i=self.inverse[index]

        if V[i]<=value:
            return

        V[i]=value
        while i>0 and V[(i-1)>>1]>V[i]:
            j=(i-1)>>1
            self.__swap(i,j)
            i=j

    def __getitem__(self,index):
        return self.dist[index] if self.dist[index]>=0 else self.value[self.inverse[index]]
