class Doubling():
    def __init__(self,A,Max_Level=1):
        """ N=len(A), X={0,1,...,N-1} とする. f:X→X を f(x):=A[x] としたとき, f^k(x)を求める.

        A:fを表すリスト, 任意の x in X に対して, f(x) in Xでなければならない.
        Max_Level:k=2^(Max_Level+1)-1 まで対応可能になる.
        """

        self.N=len(A)
        self.D=[[0]*self.N for _ in range(Max_Level+1)]
        self.Level=Max_Level

        E=self.D[0]
        for i in range(self.N):
            assert 0<=A[i]<self.N
            E[i]=A[i]

        for k in range(1,Max_Level+1):
            E=self.D[k];F=self.D[k-1]
            for i in range(self.N):
                E[i]=F[F[i]]

    def evaluate(self,x,k):
        """ f^k(x) を求める.

        """

        for i in range(self.Level+1):
            E=self.D[i]
            if k&1:
                x=E[x]
            k>>=1
            if k==0:
                break
        return x

    def evaluate_List(self,k):
        """ [f^k(0), f^k(1), ..., f^k(N-1)] を求める.

        """

        X=list(range(self.N))
        for i in range(self.Level+1):
            E=self.D[i]
            if k&1:
                for x in range(self.N):
                    X[x]=E[X[x]]
            k>>=1
            if k==0:
                break
        return X
