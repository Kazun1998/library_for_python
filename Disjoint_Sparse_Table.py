class Disjoint_Sparse_Table:
    """ 参考: https://ei1333.github.io/library/structure/others/disjoint-sparse-table.cpp.html"""

    def __init__(self, L, calc):
        self.b=0
        self.calc=calc
        self.size=N=len(L)
        while (1<<self.b)<=self.size:
            self.b+=1

        self.table=[[0]*self.size for _ in range(self.b)]

        tab=self.table[0]
        for i in range(self.size):
            tab[i]=L[i]

        shift=1
        for i in range(1,self.b):
            shift<<=1
            tab=self.table[i]
            for j in range(0,N,2*shift):
                t=min(j+shift,N)
                tab[t-1]=L[t-1]
                for k in range(t-2,j-1,-1):
                    tab[k]=calc(L[k],tab[k+1])
                if N<=t:
                    break

                tab[t]=L[t]
                r=min(t+shift,N)
                for k in range(t+1,r):
                    tab[k]=calc(tab[k-1],L[k])

    def product(self, l, r, left_close=True, right_close=True, default=None):
        if not left_close: l+=1
        if not right_close: r-=1

        if l==r:
            return self.table[0][l]
        elif l>r:
            return default

        p=(l^r).bit_length()-1
        return self.calc(self.table[p][l],self.table[p][r])

from operator import add
D=Disjoint_Sparse_Table("0123456789",add)
