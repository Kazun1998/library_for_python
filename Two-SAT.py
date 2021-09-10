"""
変数 X_i の否定は ~i で宣言する.
例えば, ~0=-1 なので, X_{-1} は not X_0 を意味する.
"""

class Two_SAT:
    def __init__(self,N):
        """ N 変数の 2-SAT を定義する.

        N: int
        """

        self.N=N
        self.var_num=N
        self.__cost=2*N

        self.arc=[[] for _ in range(2*N)]
        self.rev=[[] for _ in range(2*N)]

    def cost(self):
        return self.__cost

    def var_to_index(self,v):
        if v>=0:
            return 2*v
        else:
            return 2*(-v-1)+1

    def index_to_var(self,i):
        if i%2:
            return -(i+1)//2
        else:
            return i//2

    def add_variable(self,k):
        """ 新たに変数 k 個を加える.
        """

        m=self.var_num
        self.var_num+=k
        self.__cost+=2*k

        self.arc+=[[] for _ in range(2*k)]
        self.rev+=[[] for _ in range(2*k)]

        return list(range(m,m+k))

    def __add_clause(self,i,j):
        self.__cost+=1
        self.arc[self.var_to_index(i)].append(self.var_to_index(j))
        self.rev[self.var_to_index(j)].append(self.var_to_index(i))

    def add_imply(self,i,j):
        """ X_i -> X_j を加える.
        """
        self.__add_clause(i,j)
        self.__add_clause(~j,~i)

    def add_or(self,i,j):
        """ X_i or X_j を加える.
        """

        self.add_imply(~i,j)

    def add_nand(self,i,j):
        """ not (X_i and X_j) を加える.
        """

        self.add_imply(i,~j)

    def add_equivalent(self,*I):
        """ I=[i_0, ..., i_{k-1}] に対して, X_{i_0}=...=X_{i_{k-1}} を追加する.
        """

        k=len(I)

        if k<=1:
            return

        for j in range(k-1):
            self.add_imply(I[j],I[j+1])
        self.add_imply(I[-1],I[0])

    def add_not_equal(self,i,j):
        """ X_i != X_j を追加する.
        """
        self.add_equal(i,~j)

    def set_true(self,i):
        """ 変数 X_i を True にする.
        """

        self.__add_clause(~i,i)

    def set_false(self,i):
        """ 変数 X_i を False にする.
        """

        self.__add_clause(i,~i)

    def at_most_one(self,*I):
        """ X_i (i in I) を満たすような i は高々1つだけという条件を追加する.
        """

        k=len(I)

        if k<=1:
            return

        A=self.add_variable(k)

        self.add_imply(I[0],A[0])
        for i in range(1,k):
            self.add_imply(A[i-1],A[i])
            self.add_imply(I[i],A[i])
            self.add_nand(A[i-1],I[i])

    def is_satisfy(self,Mode=0):
        """ Two-SAT は充足可能?

        Mode:
        0 (Defalt): 充足可能?
        1: 充足可能ならば,その変数の割当を与える (不可能なときはNone).
        2: 充足不能の原因である変数を全て挙げる.
        """
        N=self.var_num
        Group=[0]*(2*N)
        Order=[]

        for s in range(2*N):
            if Group[s]:continue

            S=[s]
            Group[s]=-1

            while S:
                u=S.pop()
                for v in self.arc[u]:
                    if Group[v]:continue
                    Group[v]=-1
                    S.append(u);S.append(v)
                    break
                else:
                    Order.append(u)

        K=0
        for s in Order[::-1]:
            if Group[s]!=-1:continue

            S=[s]
            Group[s]=K

            while S:
                u=S.pop()
                for v in self.rev[u]:
                    if Group[v]!=-1:continue

                    Group[v]=K
                    S.append(v)
            K+=1

        if Mode==0:
            for i in range(N):
                if Group[2*i]==Group[2*i+1]:
                    return False
            return True
        elif Mode==1:
            T=[0]*N
            for i in range(N):
                if Group[2*i]>Group[2*i+1]:
                    T[i]=1
                elif Group[2*i]==Group[2*i+1]:
                    return None
            return T[:self.N]
        elif Mode==2:
            return [i for i in range(self.N) if Group[2*i]==Group[2*i+1]]
