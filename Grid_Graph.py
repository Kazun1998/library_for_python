class Grid:
    def __init__(self,*F):
        self.F=tuple(F)
        self.dim=len(self.F)

        R=[1]
        for a in self.F[::-1]:
            R.append(R[-1]*a)

        self.volume,*self.partition=R[::-1]

    def number_to_position(self,N):
        assert 0<=N<self.volume

        pos=[0]*self.dim
        for i in range(self.dim):
            pos[i],N=divmod(N,self.partition[i])
        return pos

    def position_to_number(self,*pos):
        assert len(pos)==self.dim

        N=0
        for i in range(self.dim):
            assert 0<=pos[i]<self.F[i]
            N+=self.partition[i]*pos[i]
        return N

    def number_neighborhood_yielder(self,N):
        r=N
        for i in range(self.dim):
            q,r=divmod(r,self.partition[i])

            if 0<q:
                yield N-self.partition[i]

            if q<self.F[i]-1:
                yield N+self.partition[i]

    def position_neighborhood_yielder(self,*pos):
        assert self.dim==len(pos)
        pos=list(pos)

        for i in range(self.dim):
            if 0<pos[i]:
                pos[i]-=1
                yield pos
                pos[i]+=1

            if pos[i]<self.F[i]-1:
                pos[i]+=1
                yield pos
                pos[i]-=1
