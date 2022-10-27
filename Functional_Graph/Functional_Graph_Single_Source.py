class Functional_Graph_Single_Source:
    def __init__(self, N, start):
        self.N=N
        self.start=start
        self.f=list(range(N))

    def set_arc(self, source, target):
        self.f[source]=target

    def build(self):
        self.first=[]
        used=[0]*self.N

        x=self.start
        while not used[x]:
            self.first.append(x)
            used[x]=1

            x=self.f[x]

        self.second=[x]
        y=self.f[x]
        while y!=x:
            self.second.append(y)
            y=self.f[y]

    def calculate(self, K):
        if K<len(self.first):
            return self.first[K]
        else:
            K-=len(self.first)
            return self.second[K%len(self.second)]
