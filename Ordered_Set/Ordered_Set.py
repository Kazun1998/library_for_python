class Fenwick_Tree:
    def __init__(self, N, A=None):
        self.N=N
        if A==None:
            self.data=[0]*N
        else:
            assert len(A)==N
            self.data=A
            self.__build()

    def __build(self):
        data=self.data
        for i in range(1, self.N+1):
            if i+(i&(-i))<=self.N:
                data[i+(i&(-i))-1]+=data[i-1]

    def add(self, i, x):
        i+=1
        data=self.data
        while i<=self.N:
            data[i-1]+=x
            i+=i&(-i)

    def sum(self, i):
        S=0
        data=self.data
        while i:
            S+=data[i-1]
            i-=i&(-i)
        return S

    def range_sum(self,l,r):
        return self.sum(r)-self.sum(l)

    def bisect_left(self, x, default=-1):
        i=0
        k=1<<self.N.bit_length()
        data=self.data

        while k:
            if i+k<=self.N and data[i+k-1]<x:
                x-=self.data[i+k-1]
                i+=k
            k>>=1
        return i if x else default

    def bisect_right(self, x, default=-1):
        i=0
        k=1<<self.N.bit_length()
        data=self.data

        while k:
            if i+k<=self.N and data[i+k-1]<=x:
                x-=self.data[i+k-1]
                i+=k
            k>>=1
        return i if i<self.N else default

class Ordered_Set:
    def __init__(self, N, multiple=False, S=None):
        self.N=N
        self.multiple=bool(multiple)

        if (not multiple) and S:
            S=[1 if S[i] else 0 for i in range(N)]

        self.Fenwick=Fenwick_Tree(N,S)
        self.__card=self.Fenwick.sum(N)

    def __contains__(self, x):
        return bool(self.count(x))

    def count(self, x):
        return self.Fenwick.range_sum(x,x+1)

    def __len__(self):
        return self.__card

    def __bool__(self):
        return bool(len(self))

    def add(self, x, k=1):
        """ x を k 個 (多重集合のとき) 加える.

        """

        if (not self.multiple) and (x in self):
            return

        if not self.multiple:
            k=1

        self.Fenwick.add(x,k)
        self.__card+=k

    def discard(self, x, k=1):
        """ x を k 個 (多重集合のとき) 削除する.

        x: int
        k: k=-1 とすると, x を全て削除する.
        """

        if x not in self:
            return

        if k==-1:
            k=self.count(x)
        elif not self.multiple:
            k=1

        self.Fenwick.add(x,-k)
        self.__card-=k

    def remove(self, x):
        """ x を k 個 (多重集合のとき) 削除する.

        x: int
        k: k=-1 とすると, x を全て削除する.
        """

        if  x not in self:
            raise KeyError(x)

        if k==-1:
            k=self.count(x)
        elif not self.multiple:
            k=1

        self.Fenwick.add(x, -k)
        self.__card-=k

    def get(self, index, default=-1):
        size=len(self)
        if size<=index or size+index<0:
            return default

        if index<0:
            index+=size

        return self.Fenwick.bisect_left(index+1)

    def __getitem__(self, index):
        size=len(self)
        if size<=index or size+index<0:
            raise IndexError

        if index<0:
            index+=size

        return self.Fenwick.bisect_left(index+1)

    def get_min(self, default=-1):
        return self.get(0, default)

    def pop_min(self):
        y=self.get_min()
        if y==-1:
            raise IndexError
        self.remove(y)
        return y

    def get_max(self, default=-1):
        return self.get(-1, default)

    def pop_max(self):
        y=self.get_max()
        if y==-1:
            raise IndexError
        self.remove(y)
        return y

    def index(self, x, mode=False, default=-1):
        """ S[k]=x を満たす k を求める.

        x: int
        mode: False のときは k の最小値, True の時は k の最大値 (多重集合のとき有用)
        """

        if x not in self:
            return default

        if mode:
            return self.Fenwick.sum(x+1)-1
        else:
            return self.Fenwick.sum(x)

    def previous(self, x, mode=True, default=-1):
        """ S に含まれる x 以下の要素のうち, 最大値を求める.

        x: int
        mode: False のときは "以下" が "未満" になる.
        """

        if mode:
            x+=1

        if x>=0:
            return self.Fenwick.bisect_left(self.Fenwick.sum(x), default)
        else:
            return default

    def next(self, x, mode=True, default=-1):
        """ S に含まれる x 以上の要素のうち, 最大値を求める.

        x: int
        mode: False のときは "以上" が "より大きい" になる.
        """

        if not mode:
            x+=1
        return self.Fenwick.bisect_right(self.Fenwick.sum(x), default)

    def less_count(self, x, mode=False):
        """ x 未満の元の個数を求める.

        x: int
        mode: mode=True ならば, "未満" が "以下" になる.
        """

        if mode:
            x+=1
        return self.Fenwick.sum(x)

    def more_count(self, x, mode=False):
        """ x より大きい元の個数を求める.

        x: int
        mode: mode=True ならば, "より大きい" が "以上" になる.
        """

        return len(self)-self.less_count(x, not mode)

    def kth_min(self, k, default=-1):
        """ k 番目に小さい元を求める.

        """

        if 1<=k<=len(self):
            return self[k-1]
        else:
            return default

    def kth_max(self, k, default=-1):
        """ k 番目に大きい元を求める.

        """

        if 1<=k<=len(self):
            return self[~(k-1)]
        else:
            return default

class Ordered_Set_with_Negative:
    def __init__(self, N, multiple=False):
        """ -N < x < N の範囲での順序付き集合を生成する.

        """
        self.N=N
        self.multiple=bool(multiple)
        self.positive=Ordered_Set(N, multiple)
        self.negative=Ordered_Set(N, multiple)

    def __contains__(self, x):
        return bool(self.count(x))

    def count(self, x):
        if x>=0:
            return self.positive.count(x)
        else:
            return self.negative.count(-x)

    def __len__(self):
        return len(self.positive)+len(self.negative)

    def __bool__(self):
        return bool(len(self))

    def add(self, x):
        if (not self.multiple) and (x in self):
            return

        if x>=0:
            self.positive.add(x)
        else:
            self.negative.add(-x)

    def discard(self, x):
        if x>=0:
            self.positive.discard(x)
        else:
            self.negative.discard(-x)

    def remove(self, x):
        if x>=0:
            self.positive.remove(x)
        else:
            self.negative.remove(-x)

    def get(self, index, default=None):
        size=len(self)
        if size<=index or size+index<0:
            return default

        if index<0:
            index+=size

        if index<len(self.negative):
            return -self.negative.get(~index)
        else:
            return self.positive.get(index-len(self.negative))

    def __getitem__(self, index):
        size=len(self)
        if size<=index or size+index<0:
            raise IndexError

        if index<0:
            index+=size

        if index<len(self.negative):
            return -self.negative.get(~index)
        else:
            return self.positive.get(index-len(self.negative))

    def get_min(self, default=None):
        if self.negative:
            return -self.negative.get_max()
        else:
            return self.positive.get_min(default=default)

    def pop_min(self):
        y=self.get_min()
        if y==None:
            raise IndexError
        self.remove(y)
        return y

    def get_max(self, default=None):
        if self.positive:
            return self.positive.get_max()
        elif self.negative:
            return -self.negative.get_min()
        else:
            return default

    def pop_max(self):
        y=self.get_max()
        if y==None:
            raise IndexError
        self.remove(y)
        return y

    def index(self, x, mode=False, default=None):
        """ S[k]=x を満たす k を求める.

        x: int
        mode: False のときは k の最小値, True の時は k の最大値 (多重集合のとき有用)
        """

        if x not in self:
            return default

        if mode:
            return self.Fenwick.sum(x+1)-1
        else:
            return self.Fenwick.sum(x)

    def previous(self, x, mode=True, default=None):
        """ S に含まれる x 以下の要素のうち, 最大値を求める.

        x: int
        mode: False のときは "以下" が "未満" になる.
        """


        if x<=0:
            y=self.negative.next(-x, mode, None)
            if y==None:
                return default
            else:
                return -y
        else:
            y=self.positive.previous(x, mode, None)
            if y==None:
                return self.previous(-1, True, default)
            else:
                return y

    def next(self, x, mode=True, default=None):
        """ S に含まれる x 以上の要素のうち, 最大値を求める.

        x: int
        mode: False のときは "以上" が "より大きい" になる.
        """

        if x>=0:
            y=self.positive.next(x, mode, None)
            if y==None:
                return default
            else:
                return y
        else:
            y=self.negative.previous(-x, mode, None)
            if y==None:
                return self.next(0, True, default)
            else:
                return -y
