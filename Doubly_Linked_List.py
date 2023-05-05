class Doubly_Linked_List:
    def __init__(self, N):
        self.__N=N
        self.__front=[-1]*N
        self.__back=[-1]*N

    def __len__(self):
        return self.__N

    def __str__(self):
        res=[]
        used=[0]*self.__N

        for x in range(self.__N):
            if used[x]:
                continue

            a=self.enumerate(x)
            for y in a:
                used[y]=1
            res.append(a)
        return str(res)

    def __repr__(self):
        return "[Doubly Linked List]: "+str(self)

    def previous(self, x, default=-1):
        return self.__front[x] if self.__front[x]!=-1 else default

    def next(self, x, default=-1):
        return self.__back[x] if self.__back[x]!=-1 else default

    def disconnect_front(self, x):
        """ x から前に伸びるリンクを削除する.

        """

        front=self.__front; back=self.__back

        y=front[x]
        if y>=0:
            front[x]=-1
            back[y]=-1

    def disconnect_back(self, x):
        """ x から後ろに伸びるリンクを削除する.

        """

        front=self.__front; back=self.__back

        y=back[x]
        if y>=0:
            back[x]=-1
            front[y]=-1

    def extract(self, x):
        """ x に接続するリンクを削除し, x の前後が存在するならば, それらをつなぐ.
        """

        a=self.__front[x]
        b=self.__back[x]

        self.disconnect_front(x)
        self.disconnect_back(x)

        if a!=-1 and b!=-1:
            self.connect(a,b)

    def connect(self, x, y):
        """ x から y へのリンクを生成する (すでにある x からのリンクと y へのリンクは削除される).

        """

        self.disconnect_back(x)
        self.disconnect_front(y)
        self.__back[x]=y
        self.__front[y]=x

    def insert_front(self, x, y):
        """ x の前に y を挿入する.

        """

        z=self.__front[x]
        self.connect(y,x)
        if z!=-1:
            self.connect(z,y)

    def insert_back(self, x, y):
        """ x の後に y を挿入する.

        """

        z=self.__back[x]
        self.connect(x,y)
        if z!=-1:
            self.connect(y,z)

    def head(self, x):
        """ x が属する弱連結成分の先頭を求める.
        """

        while self.__front[x]!=-1:
            x=self.__front[x]
        return x

    def tail(self, x):
        """ x が属する弱連結成分の末尾を求める.
        """

        while self.__back[x]!=-1:
            x=self.__back[x]
        return x

    def enumerate(self, x):
        """ x が属している弱連結成分を先頭から順に出力する.

        """

        x=self.head(x)
        res=[x]
        while self.__back[x]>=0:
            x=self.__back[x]
            res.append(x)
        return res

    def depth(self, x):
        dep=0
        while self.__front[x]!=-1:
            x=self.__front[x]
            dep+=1
        return dep
