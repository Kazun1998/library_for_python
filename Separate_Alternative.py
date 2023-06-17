class Separate_Alternative:
    def __init__(self, N):
        self.N=N

        self.same_edge=[[] for _ in range(N)]
        self.diff_edge=[[] for _ in range(N)]

    def same(self, x, y):
        self.same_edge[x].append(y)
        self.same_edge[y].append(x)

    def difference(self, x, y):
        self.diff_edge[x].append(y)
        self.diff_edge[y].append(x)

    def is_reasonable(self):
        T=[0]*self.N
        for x in range(self.N):
            if T[x]!=0:
                continue

            T[x]=1
            S=[x]
            while S:
                y=S.pop()
                for z in self.same_edge[y]:
                    if T[z]==0:
                        T[z]=T[y]
                        S.append(z)
                    elif T[z]!=T[y]:
                        return False

                for z in self.diff_edge[y]:
                    if T[z]==0:
                        T[z]=-T[y]
                        S.append(z)
                    elif T[z]==T[y]:
                        return False
        return True

    def separate(self):
        Sep=[]
        seen=[0]*self.N

        for x in range(self.N):
            if seen[x]!=0:
                continue

            seen[x]=1
            U=[x]; V=[]
            S=[x]
            while S:
                y=S.pop()
                for z in self.same_edge[y]:
                    if seen[z]==0:
                        seen[z]=seen[y]
                        S.append(z)

                        if seen[z]==1:
                            U.append(z)
                        else:
                            V.append(z)

                    elif seen[z]!=seen[y]:
                        return None

                for z in self.diff_edge[y]:
                    if seen[z]==0:
                        seen[z]=-seen[y]
                        S.append(z)

                        if seen[z]==1:
                            U.append(z)
                        else:
                            V.append(z)

                    elif seen[z]==seen[y]:
                        return None

            Sep.append((U,V))
        return Sep
