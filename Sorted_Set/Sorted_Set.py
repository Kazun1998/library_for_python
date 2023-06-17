" Reference: https://qiita.com/tatyam/items/492c70ac4c955c055602"
# ※ 計算量が O(sqrt(N)) per query なので, 過度な期待はしないこと.

from bisect import bisect_left, bisect_right
class Sorted_Set:
    BUCKET_RATIO=50
    REBUILD_RATIO=170

    def __init__(self, A=[]):
        A=list(A)
        if not all(A[i]<A[i+1] for i in range(len(A)-1)):
            A=sorted(set(A))
        self.__build(A)
        return

    def __build(self, A=None):
        if A is None:
            A=list(self)

        self.N=N=len(A)
        K=1
        while self.BUCKET_RATIO*K*K<N:
            K+=1

        self.list=[A[N*i//K: N*(i+1)//K] for i in range(K)]

    def __iter__(self):
        for A in self.list:
            for a in A:
                yield a

    def __reversed__(self):
        for A in reversed(self.list):
            for a in reversed(A):
                yield a

    def __len__(self):
        return self.N

    def __bool__(self):
        return bool(self.N)

    def __str__(self):
        string=str(list(self))
        return "{"+string[1:-1]+"}"

    def __repr__(self):
        return "Sorted Set: "+str(self)

    def __find_bucket(self, x):
        for A in self.list:
            if x<=A[-1]:
                return A
        else:
            return A

    def __contains__(self, x):
        if self.N==0:
            return False

        A=self.__find_bucket(x)
        i=bisect_left(A,x)
        return i!=len(A) and A[i]==x

    def add(self, x):
        if self.N==0:
            self.list=[[x]]
            self.N+=1
            return True

        A=self.__find_bucket(x)
        i=bisect_left(A, x)

        if i!=len(A) and A[i]==x:
            return False # x が既に存在するので...

        A.insert(i,x)
        self.N+=1

        if len(A)>len(self.list)*self.REBUILD_RATIO:
            self.__build()
        return True

    def discard(self, x):
        if self.N==0:
            return False

        A=self.__find_bucket(x)
        i=bisect_left(A, x)

        if not(i!=len(A) and A[i]==x):
            return False # x が存在しないので...

        A.pop(i)
        self.N-=1

        if len(A)==0:
            self.__build()

        return True

    def remove(self, x):
        if not self.discard(x):
            raise KeyError(x)

    #=== get, pop

    def __getitem__(self, index):
        if index<0:
            index+=self.N
            if index<0:
                raise IndexError("index out of range")

        for A in self.list:
            if index<len(A):
                return A[index]
            index-=len(A)
        else:
            raise IndexError("index out of range")

    def get_min(self):
        if self.N==0:
            raise ValueError("This is empty set.")

        return self.list[0][0]

    def pop_min(self):
        if self.N==0:
            raise ValueError("This is empty set.")

        A=self.list[0]
        value=A.pop(0)
        self.N-=1

        if len(A)==0:
            self.__build()

        return value

    def get_max(self):
        if self.N==0:
            return ValueError("This is empty set.")

        return self.list[-1][-1]

    def pop_max(self):
        if self.N==0:
            raise ValueError("This is empty set.")

        A=self.list[-1]
        value=A.pop(-1)
        self.N-=1

        if len(A)==0:
            self.__build()

        return value

    #=== k-th element
    def kth_min(self, k):
        """ k (0-indexed) 番目に小さい整数を求める.

        k: int (0<=k<|S|)
        """

        assert 0<=k<len(self)

        return self[k]

    def kth_max(self, k):
        """ k (0-indexed) 番目に大きい整数を求める.

        k: int (0<=k<|S|)
        """

        assert 0<=k<len(self)

        return self[len(self)-1-k]

    #=== previous, next

    def previous(self, value, mode=False):
        """ S にある value 未満で最大の要素を返す (存在しない場合は None)

        mode: True のときは "未満" が "以下" になる.
        """

        if self.N==0:
            return None

        if mode:
            for A in reversed(self.list):
                if A[0]<=value:
                    return A[bisect_right(A,value)-1]
        else:
            for A in reversed(self.list):
                if A[0]<value:
                    return A[bisect_left(A,value)-1]

    def next(self, value, mode=False):
        """ S にある value より大きい最小の要素を返す (存在しない場合は None)

        mode: True のときは "より大きい" が "以上" になる.
        """

        if self.N==0:
            return None

        if mode:
            for A in self.list:
                if A[-1]>=value:
                    return A[bisect_left(A,value)]
        else:
            for A in self.list:
                if A[-1]>value:
                    return A[bisect_right(A,value)]

    #=== count
    def less_count(self, value, equal=False):
        """ a < value となる S の元 a の個数を求める.

        equal=True ならば, a < value が a <= value になる.
        """

        count=0
        if equal:
            for A in self.list:
                if A[-1]>value:
                    return count+bisect_right(A, value)
                count+=len(A)
        else:
            for A in self.list:
                if A[-1]>=value:
                    return count+bisect_left(A, value)
                count+=len(A)
        return count

    def more_count(self, value, equal=False):
        """ a > value となる S の元 a の個数を求める.

        equal=True ならば, a > value が a >= value になる.
        """

        return self.N-self.less_count(value, not equal)

    #===
    def is_upper_bound(self, x, equal=True):
        if self.N:
            a=self.list[-1][-1]
            return (a<x) or (bool(equal) and a==x)
        else:
            return True

    def is_lower_bound(self, x, equal=True):
        if self.N:
            a=self.list[0][0]
            return (x<a) or (bool(equal) and a==x)
        else:
            return True

    #=== index
    def index(self, value):
        index=0
        for A in self.list:
            if A[-1]>value:
                i=bisect_left(A, value)
                if A[i]==value:
                    return index+i
                else:
                    raise ValueError("{} is not in Set".format(value))
            index+=len(A)
        raise ValueError("{} is not in Set".format(value))
