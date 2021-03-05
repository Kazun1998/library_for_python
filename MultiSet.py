class MultiSet():
    def __init__(self):
        self.num={}
        self.set=set()

    def __bool__(self):
        return bool(self.set)

    #要素の添加
    def add(self,x,k=1):
        """要素xをk個加える.

        x:要素
        k=1:個数
        """

        if k==0:
            return
        elif k<0:
            self.discard(x,-k)
            return

        self.set.add(x)
        if x in self.num:
            self.num[x]+=k
        else:
            self.num[x]=k

    #要素の削除
    def discard(self,x,k=1):
        """要素xからk個除く.

        x:要素
        k=1:個数
        ただし, 多重集合に要素xがk個ないときは全て取り除く.
        """
        if k==0:
            return
        elif k<0:
            self.add(x,-k)
            return

        if x not in self.set:
            return

        self.num[x]=max(0,self.num[x]-k)
        if self.num[x]==0:
            self.set.remove(x)

    def remove(self,x,k=1):
        """要素xからk個除く.

        x:要素
        k=1:個数
        ただし, 多重集合に要素xがk個ないときはValue Error.
        """

        if x not in self.set:
            raise KeyError(x)

        if self.num[x]<k:
            raise ValueError(x,k)

        self.num[x]-=k
        if self.num[x]==0:
            self.set.remove(x)

    def pop(self):
        """多重集合から適当に1個の要素を削除し, その要素を出力する.
        """

        a=self.set.pop()
        self.num[a]-=1
        if self.num[a]:
            self.set.add(a)
        return a

    def clear(self):
        """多重集合から全ての要素を削除する.
        """

        self.set=set()
        self.num={}

    #集合の演算
    #共通部分
    def __and__(self,other):
        A=MultiSet()
        for x in self.set:
            if x in other:
                A.set.add(x)
                A.num[x]=min(self.num[x],other.num[x])
        return A

    def intersection(self,other):
        return self&other

    #和集合
    def __or__(self,other):
        A=MultiSet()
        A.set=self.set.copy()
        A.num=self.num.copy()

        for x in other.set:
            if x in A.set:
                A.num[x]=max(A.num[x],other.num[x])
            else:
                A.num[x]=other.num[x]
        return A

    def union(self,other):
        return self|other

    #差集合
    def __sub__(self,other):
        A=MultiSet()

        for x in self.set:
            t=self.count(x)-other.count(x)
            if t>0:
                A.set.add(x)
                A.num[x]=t
        return A

    def difference(self,other):
        return self-other

    #対称差
    def __xor__(self,other):
        A=MultiSet()
        A.set=self.set.copy()
        A.num=self.num.copy()

        for y in other.set:
            if y in self:
                t=abs(self.count(y)-other.count(y))
                A.num[y]=t

                if t==0:
                    A.set.discard(y)
            else:
                A.set.add(y)
                A.num[y]=other.num[y]
        return A

    def symmetric_difference(self,other):
        return self^other

    #部分集合?
    def __le__(self,other):
        for x in self.set:
            if not self.count(x)<=other.count(x):
                return False
        return True

    def issubset(self,other):
        return self<=other

    def __ge__(self,other):
        for x in self.set:
            if not self.count(x)>=other.count(x):
                return False
        return True

    def issuperset(self,other):
        return self>=other

    def __eq__(self,other):
        return (self<=other) and (other<=self)

    #互いに素?
    def isdisjoint(self,other):
        return not(self & other)

    #要素の存在
    def __contains__(self,x):
        return x in self.set

    #集合の比較
    def count(self,x):
        """要素xの個数を返す.

        x:要素
        """

        if x not in self.set:
            return 0
        return self.num[x]

    def refresh(self):
        L=[]
        for x in self.num:
            if x not in self.set:
                L.append(x)

        for x in L:
            del self.num[x]

def mex(S,start=0):
    x=start
    while x in S:
        x+=1
    return x

S=MultiSet()
S.add(1,3);S.add(2,5);S.add(3,8);S.add(4,3);S.add("x",2)

T=MultiSet()
T.add(1,2);T.add(2,8);T.add(4,1);T.add("x",2)

U=MultiSet()
U.add(1,3);U.add(2,19);U.add(4,3);U.add("x",2)

V=MultiSet()
V.add("y",4);V.discard(1,-3)
