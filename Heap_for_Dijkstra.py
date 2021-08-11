class Dijkstra_Heap:
    inf=float("inf")

    def __init__(self,N):
        self.N=m=N
        self.remain=m

        self.value=[self.inf]*m
        self.dist=[-1]*m
        self.index=list(range(m))
        self.inverse=list(range(m))

    def pop(self):
        x=self.index[0]
        d=self.value[0]

        self.remain-=1

        y=self.index[self.remain]

        V=self.value
        self.dist[x]=d
        V[0],V[self.remain]=V[self.remain],self.inf
        self.index[0],self.index[self.remain]=y,x
        self.inverse[x],self.inverse[y]=self.remain,0

        k=0
        while True:
            if 2*k+1>=self.N:
                break

            if self.N==2*k+2:
                u=V[2*k+1]

                if V[k]<=u:
                    break

                b=2*k+1
            else:
                u=V[2*k+1]; v=V[2*k+2]

                if V[k]<=u and V[k]<=v:
                    break

                if u<=v:
                    b=2*k+1
                else:
                    b=2*k+2

            V[k],V[b]=V[b],V[k]

            s,t=self.index[k],self.index[b]
            self.index[k],self.index[b]=t,s
            self.inverse[s],self.inverse[t]=b,k

            k=b

        return (x,d)

    def __setitem__(self,index,value):
        if self.dist[index]!=-1:
            return

        V=self.value
        k=self.inverse[index]
        V[k]=min(V[k],value)

        while k>0 and V[(k-1)>>1]>V[k]:
            s=(k-1)>>1
            V[k],V[s]=V[s],V[k]

            a=self.index[k]
            b=self.index[s]

            self.index[k],self.index[s]=b,a
            self.inverse[a],self.inverse[b]=s,k

            k=s

    def __getitem__(self,index):
        return self.dist[index] if self.dist[index]>=0 else self.value[index]
