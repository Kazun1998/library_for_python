class Binary_Indexed_Tree_2D():
    def __init__(self, M, op, zero, neg):
        """ op を演算とする N 項の Binary Indexed Tree (0-indexed) を作成
        op: 演算 (2変数関数, 可換群)
        zero: 群 op の単位元 (x+e=e+x=xを満たすe)
        neg : 群 op の逆元 (1変数関数, x+neg(x)=neg(x)+x=e をみたす neg(x))
        """

        self.op=op
        self.zero=zero
        self.neg=neg

        self.H=H=len(M)
        self.W=W=len(M[0]) if self.H else 0

        X=[[zero]*(W+1) for _ in range(H+1)]

        for i in range(H):
            Mi=M[i]
            for j in range(W):
                alpha=Mi[j]

                a=i+1
                while a<=H:
                    Xa=X[a]
                    b=j+1
                    while b<=W:
                        Xa[b]=op(Xa[b], alpha)
                        b+=b&(-b)
                    a+=a&(-a)
        self.data=X

    def get(self, i, j):
        """ 第 (i,j) 要素の値を出力する.
        (i,j)   : 数列の要素
        """
        return self.sum(i,j,i,j)

    def add(self, i, j, x):
        """ 第 (i,j) 要素に x を加え, 更新を行う.
        (i,j): 数列の要素
        x    : 加える値
        """
        H=self.H; W=self.W
        if (i<0) or (i>=H) or (j<0) or (j>=W):
            return

        X=self.data; op=self.op
        a=i+1
        while a<=H:
            Xa=X[a]
            b=j+1
            while b<=W:
                Xa[b]=op(Xa[b], x)
                b+=b&(-b)
            a+=a&(-a)

    def update(self, i, j, x):
        """ 第 (i,j) 要素を x に変え, 更新を行う.
        (i,j): 数列の要素
        x: 更新後の値
        """

        a=self.get(i,j)
        y=self.op(self.neg(a),x)
        self.add(i,j,y)

    def sum(self, i0, j0, i1, j1):
        """ sum_{i0<=x<=i1, j0<=y<=j1} B[x][y] を求める.
        """

        if (i0>i1) or (j0>j1):
            return self.zero

        op=self.op; neg=self.neg; box=self.__box

        a=op(box(i1,j1), box(i0-1, j0-1))
        b=op(box(i1,j0-1), box(i0-1, j1))
        return op(a,neg(b))

    def __box(self, i, j):
        """ sum_{0<=x<=i, 0<=y<=j} B[x][y] を求める."""

        if (i<0) or (j<0):
            return self.zero

        H=self.H; W=self.W
        X=self.data; op=self.op

        i=min(i,H-1); j=min(j, W-1)

        total=self.zero

        a=i+1
        while a>0:
            Xa=X[a]
            b=j+1
            while b>0:
                total=op(total, Xa[b])
                b-=b&(-b)
            a-=a&(-a)
        return total

    def all_sum(self):
        return self.sum(0, 0, self.H-1, self.W-1)

    def __getitem__(self,index):
        if isinstance(index,int):
            return [self.get(index, j) for j in range(self.W)]
        elif isinstance(index, tuple) and len(index)==2:
            i,j=index
            return self.get(i,j)

    def __setitem__(self, index, value):
        self.update(*index,value)
