class Monoided_Functional_Graph:
    def __init__(self, N, K, calc, unit):
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

    def calculate(self, v, t):
        x=self.unit
        calc=self.calc
        out=self.out
        value=self.value
        d=0
        while t:
            if t&1:
                x=calc(value[d][v], x)
                v=out[d][v]
            t>>=1; d+=1
        return x

