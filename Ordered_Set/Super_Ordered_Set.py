class Super_Fenwick_Tree:
    def __init__(self, N):
        self.N=N
        self.data={}

    def add(self, i, x):
        i+=1
        data=self.data
        while i<=self.N:
            data[i-1]=data.get(i-1,0)+x
            i+=i&(-i)

    def sum(self, i):
        S=0
        data=self.data
        while i:
            S+=data.get(i-1,0)
            i-=i&(-i)
        return S

    def range_sum(self,l,r):
        return self.sum(r)-self.sum(l)

    def bisect_left(self, x, default=-1):
        i=0
        k=1<<self.N.bit_length()
        data=self.data

        while k:
            if i+k<=self.N and data.get(i+k-1,0)<x:
                x-=data.get(i+k-1,0)
                i+=k
            k>>=1
        return i if x else default

    def bisect_right(self, x, default=-1):
        i=0
        k=1<<self.N.bit_length()
        data=self.data

        while k:
            if i+k<=self.N and data.get(i+k-1,0)<=x:
                x-=data.get(i+k-1,0)
                i+=k
            k>>=1
        return i if i<self.N else default

class Super_Ordered_Set:
    def __init__(self, N, multiple=False):
        self.N=N
        self.multiple=bool(multiple)

        self.Fenwick=Super_Fenwick_Tree(N)
        self.__card=self.Fenwick.sum(N)

    def __contains__(self, x):
        return bool(self.count(x))

    def count(self, x):
        return self.Fenwick.range_sum(x,x+1)

    def __len__(self):
        return self.__card

    def __bool__(self):
        return bool(len(self))

    def add(self, x):
        if (not self.multiple) and (x in self):
            return

        self.Fenwick.add(x,1)
        self.__card+=1

    def discard(self, x):
        if x not in self:
            return

        self.Fenwick.add(x,-1)
        self.__card-=1

    def remove(self, x):
        if  x not in self:
            raise KeyError(x)

        self.Fenwick.add(x, -1)
        self.__card-=1

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
