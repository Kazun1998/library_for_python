class Cumulative_2D:
    def __init__(self, A):
        H=self.H=len(A)
        W=self.W=len(A[0]) if self.H else 0

        self.cum=cum=[[0]*(W+1) for _ in range(H+1)]

        for i in range(H):
            Ai=A[i]
            ci=cum[i+1]; cii=cum[i]
            for j in range(W):
                ci[j+1]=ci[j]+Ai[j]

            for j in range(W):
                ci[j+1]+=cii[j+1]

    def sum(self, i0, j0, i1, j1):
        """ sum_{i0<=x<=i1, j0<=y<=j1} A[x][y] を求める.

        """

        if (i0>i1) or (j0>j1) or (self.H<=i0) or (i1<0) or (self.W<=j0) or (j1<0):
            return 0

        i0=i0 if i0>=0 else 0
        j0=j0 if j0>=0 else 0
        i1=i1 if i1<self.H else self.H-1
        j1=j1 if j1<self.W else self.W-1

        i0+=1; j0+=1; i1+=1; j1+=1
        b=self.cum
        return b[i1][j1]-b[i0-1][j1]-b[i1][j0-1]+b[i0-1][j0-1]

    def sum_range(self, h, w):
        """ 0<=i<=H-h, 0<=j<=W-w それぞれに対して, sum_{i<=x<i+h, j<=y<j+w} A[x][y] を求める.

        """

        H=self.H; W=self.W
        b=self.cum

        T=[[0]*(W-w+1) for _ in range(H-h+1)]
        for i in range(H-h+1):
            Ti=T[i]
            bih=b[i+h]; bi=b[i]
            for j in range(W-w+1):
                Ti[j]=bih[j+w]-bi[j+w]-bih[j]+bi[j]
        return T
