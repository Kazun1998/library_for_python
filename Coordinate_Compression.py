class Coordinate_compression_1:
    def __init__(self,X,Mode=False):
        """1次元の座標圧縮を行う.
        X:分割する値.
        Mode:X=[x_0,x_1, ... , x_k] (重複なし, 昇順) のとき,
        Mode=False -> [-inf, x_0), [x_0, x_1), ..., [x_{k-1}, x_k), [x_k, inf]
        Mode=True -> [-inf, x_0], (x_0, x_1], ..., (x_{k-1}, x_k], (x_k, inf]
        """
        self.X=list(set(X))
        self.X.sort()
        self.Mode=Mode

    def __str__(self):
        X=self.X
        Mode=self.Mode
        S=[""]*(len(self)-1)
        for k in range(len(self)-1):
            if not Mode:
                S[k]="[{},{})".format(X[k],X[k+1])
            else:
                S[k]="({},{}]".format(X[k],X[k+1])

        if not Mode:
            return "X: [-inf, {}) ".format(X[0])+" ".join(S)+" [{}, inf]".format(X[-1])
        else:
            return "X: [-inf, {}] ".format(X[0])+" ".join(S)+" ({}, inf]".format(X[-1])

    def __repr__(self):
        return str(self)

    def at(self,x):
        X=self.X
        Mode=self.Mode

        if x<X[0] or (Mode and x==X[0]):
            return 0

        L,R=0,len(self)
        while R-L>1:
            C=L+(R-L)//2
            xc=X[C]
            if x>xc or (not Mode and x==xc):
                L=C
            else:
                R=C
        return L+1

    def __len__(self):
        return len(self.X)

class Coordinate_compression_2(Coordinate_compression_1):
    def __init__(self,X,Y,Mode=False):
        """2次元の座標圧縮を行う.
        X,Y:分割する値.
        Mode:(1次元の時と同様, False ならば右半開区間, True ならば半開区間)
        """
        self.X=Coordinate_compression_1(X,Mode)
        self.Y=Coordinate_compression_1(Y,Mode)
        self.Mode=Mode

    def __str__(self):
        return str(self.X)+"\nY:"+str(self.Y)[2:]

    def __repr__(self):
        return str(self)

    def at(self,x,y):
        return (self.X.at(x),self.Y.at(y))
        
    def __len__(self):
        pass

class Coordinate_compression_N(Coordinate_compression_1):
    def __init__(self,XX,Mode=False):
        """N次元の座標圧縮を行う.
        XX:分割する値のリスト.
        Mode:(1次元の時と同様, False ならば右半開区間, True ならば半開区間)
        """
        self.XX=[Coordinate_compression_1(X,Mode) for X in XX]
        self.Mode=Mode

    def __str__(self):
        T=["X{}: {}".format(i,str(x)[3:]) for i,x in enumerate(self.XX,1)]
        return "\n".join(T)

    def __repr__(self):
        return str(self)

    def at(self,*r):
        assert len(self.XX)==len(r)
        return tuple([self.XX[i].at(r[i]) for i in range(len(r))])
        
    def __len__(self):
        pass
