class Two_SAT:
    """2-SATを定義する.

    """

    #※ i:変数 i が Trueの頂点, i+N:変数 i がFalseの頂点

    #入力定義
    def __init__(self,N):
        """N変数の2-SATを考える.

        """
        self.N=N
        self.clause_number=0
        self.adjacent_out=[set() for k in range(2*N)] #出近傍(vが始点)
        self.adjacent_in=[set() for k in range(2*N)] #入近傍(vが終点)

    #節の追加
    def add_clause(self,X,F,Y,G):
        """(X=F) or (Y=G) という節を加える.

        X,Y:変数の名前
        F,G:真偽値(True or False)
        """

        assert 0<=X<self.N and 0<=Y<self.N

        F=bool(F);G=bool(G)
        (A,P)=(X,X+self.N) if F else (X+self.N,X)
        (B,Q)=(Y,Y+self.N) if G else (Y+self.N,Y)

        if not self.clause_exist(X,F,Y,G):
            self.clause_number+=1

        #(X,not F)→(Y,G)を追加
        self.adjacent_out[P].add(B)
        self.adjacent_in [B].add(P)

        #(Y,not G) → (X,F)を追加
        self.adjacent_out[Q].add(A)
        self.adjacent_in [A].add(Q)

    #節を除く
    def remove_edge(self,X,F,Y,G):
        """(X=F) or (Y=G) という節を加える.

        X,Y:変数の名前
        F,G:真偽値(True or False)
        """

        assert 0<=X<self.N and 0<=Y<self.N

        F=bool(F);G=bool(G)
        (A,P)=(X,X+self.N) if F else (X+self.N,X)
        (B,Q)=(Y,Y+self.N) if G else (Y+self.N,Y)

        if not self.clause_exist(X,F,Y,G):
            return

        self.clause_number-=1

        #(X,not F)→(Y,G)を追加
        self.adjacent_out[P].remove(B)
        self.adjacent_in [B].remove(P)

        #(Y,not G) → (X,F)を追加
        self.adjacent_out[Q].remove(A)
        self.adjacent_in [A].remove(Q)

    #グラフに節が存在するか否か
    def clause_exist(self,X,F,Y,G):
        """(X=F) or (Y=G) という節が存在するか?

        X,Y:変数の名前
        F,G:真偽値(True or False)
        """
        assert 0<=X<self.N and 0<=Y<self.N

        (A,P)=(X,X+self.N) if F else (X+self.N,X)
        (B,Q)=(Y,Y+self.N) if G else (Y+self.N,Y)

        return B in self.adjacent_out[P]

    #近傍
    def neighbohood(self,v):
        pass

    #出次数
    def out_degree(self,v):
        pass

    #入次数
    def in_degree(self,v):
        pass

    #次数
    def degree(self,v):
        pass

    #変数の数
    def variable_count(self):
        return self.N

    #節の数
    def clause_count(self):
        return self.clause_number

    #充足可能?
    def Is_Satisfy(self,Mode=0):
        """充足可能?

        Mode:
        0(Defalt)---充足可能?
        1        ---充足可能ならば,その変数の割当を変える.(不可能なときはNone)
        2        ---充足不能の原因である変数を全て挙げる.
        """
        N=self.N
        Group=[0]*(2*N)
        Order=[]

        for s in range(2*N):
            if Group[s]:continue

            S=[s]
            Group[s]=-1

            while S:
                u=S.pop()
                for v in self.adjacent_out[u]:
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
                for v in self.adjacent_in[u]:
                    if Group[v]!=-1:continue

                    Group[v]=K
                    S.append(v)
            K+=1

        if Mode==0:
            for i in range(N):
                if Group[i]==Group[i+N]:
                    return False
            return True
        elif Mode==1:
            T=[0]*N
            for i in range(N):
                if Group[i]>Group[i+N]:
                    T[i]=1
                elif Group[i]==Group[i+N]:
                    return None
            return T
        elif Mode==2:
            return [i for i in range(N) if Group[i]==Group[i+N]]
