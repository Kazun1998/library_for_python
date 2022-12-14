class Monoided_Functional_Graph:
    def __init__(self, N, K, calc, unit):
        """ 有向辺にモノイドの重みを乗せた Functional Graph を生成する.

        Args:
            N : 頂点数 (0,1,2,...,N-1 を生成する)
            K : 計算に必要な最大の指数
            calc : モノイドの演算 calc(new, old)
            unit : 単位元
        """

        self.N=N
        self.K=K
        self.calc=calc
        self.unit=unit

        self.out=[list(range(N))]
        self.value=[[unit]*N]

    def set_arc(self, source, target, x):
        self.out[0][source]=target
        self.value[0][source]=x

    def build(self):
        K=self.K>>1
        N=self.N
        calc=self.calc
        while K:
            A=self.out[-1]; X=[0]*N
            B=self.value[-1]; Y=[0]*N

            for i in range(N):
                p=A[i]; x=B[i]
                q=A[p]; y=B[p]
                X[i]=q; Y[i]=calc(y,x)

            self.out.append(X)
            self.value.append(Y)
            K>>=1

    def calculate(self, v, k):
        x=self.unit
        calc=self.calc
        out=self.out
        value=self.value
        d=0
        while k:
            if k&1:
                x=calc(value[d][v], x)
                v=out[d][v]
            k>>=1; d+=1
        return x

