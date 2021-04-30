class Topological_Sort:
    def __init__(self,N):
        self.N=N
        self.arc=[[] for _ in  range(N)]
        self.rev=[[] for _ in range(N)]

    def add_arc(self,source,target):
        self.arc[source].append(target)
        self.rev[target].append(source)

    def sort(self):
        in_deg=[len(self.rev[x]) for x in range(self.N)]
        Q=[x for x in range(self.N) if in_deg[x]==0]

        S=[]
        while Q:
            u=Q.pop()
            S.append(u)

            for v in self.arc[u]:
                in_deg[v]-=1
                if in_deg[v]==0:
                    Q.append(v)
        return S

    def is_DAG(self):
        return len(self.sort())==self.N
