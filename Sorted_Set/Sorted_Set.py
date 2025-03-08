# Reference: https://qiita.com/tatyam/items/492c70ac4c955c055602
# ※ 計算量が O(sqrt(N)) per query なので, 過度な期待はしないこと.

from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar
T = TypeVar('T')

class Sorted_Set(Generic[T]):
    BUCKET_RATIO=50
    REBUILD_RATIO=170

    def __init__(self, A: Iterable[T] = None):
        if A is None:
            A = []

        A = list(A)

        # Sorted ?
        if not all(A[i] < A[i+1] for i in range(len(A) - 1)):
            A = sorted(set(A))

        # Unique ?
        if not all(A[i] == A[i + 1] for i in range(len(A) - 1)):
            A, A_cand = [], A
            for a in A_cand:
                if (not A) or (A[-1] != a):
                    A.append(a)

        self.__build(A)

    def __build(self, A: list = None):
        if A is None:
            A = list(self)

        self._N = N = len(A)
        K = 1
        while self.BUCKET_RATIO * K * K < N:
            K += 1

        self._buckets: list[list[T]] = [A[N * i // K: N * (i + 1) // K] for i in range(K)]
        self._last : list[T] = [bucket[-1] for bucket in self._buckets]

    @property
    def N(self) -> int:
        return self._N

    def __iter__(self) -> Iterator[T]:
        for A in self._buckets:
            yield from A

    def __reversed__(self) -> Iterator[T]:
        for A in reversed(self._buckets):
            yield from reversed(A)

    def __len__(self) -> int:
        return self.N

    def __bool__(self) -> bool:
        return self.N > 0

    def is_empty(self) -> bool:
        """ 空集合かどうかを判断する.

        Returns:
            bool: 空集合ならば True
        """
        return self.N == 0

    def __str__(self) -> str:
        return str(set(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self)})"

    def __find_bucket(self, x):
        for bucket in self._buckets:
            if x <= bucket[-1]:
                return bucket
        else:
            return bucket

    def __contains__(self, x: T) -> bool:
        if self.is_empty():
            return False

        A=self.__find_bucket(x)
        i=bisect_left(A,x)
        return i!=len(A) and A[i]==x

    def add(self, x: T) -> bool:
        """ 集合に要素 x を追加する.

        Args:
            x (T): 追加する要素

        Returns:
            bool: 追加による差分が発生すれば True
        """

        if self.is_empty():
            self._buckets=[[x]]
            self._N += 1
            return True

        A=self.__find_bucket(x)
        i=bisect_left(A, x)

        if i!=len(A) and A[i]==x:
            return False # x が既に存在するので...

        A.insert(i,x)
        self._N += 1

        if len(A)>len(self._buckets)*self.REBUILD_RATIO:
            self.__build()
        return True

    def discard(self, x: T) -> bool:
        """ 集合から要素 x を削除する.

        Args:
            x (T): 削除する要素

        Returns:
            bool: 削除による差分が発生すれば True
        """

        if self.is_empty():
            return False

        A=self.__find_bucket(x)
        i=bisect_left(A, x)

        if not(i!=len(A) and A[i]==x):
            return False # x が存在しないので...

        A.pop(i)
        self._N -= 1

        if len(A)==0:
            self.__build()

        return True

    def remove(self, x: T):
        """ 集合から x を削除する.

        Args:
            x (T): 削除する要素

        Raises:
            KeyError: x が存在しないときに発生.
        """
        if not self.discard(x):
            raise KeyError(x)

    #=== get, pop

    def __getitem__(self, index):
        if index<0:
            index+=self.N
            if index<0:
                raise IndexError("index out of range")

        for A in self._buckets:
            if index<len(A):
                return A[index]
            index-=len(A)
        else:
            raise IndexError("index out of range")

    def get_min(self) -> T:
        """ 最小値を取得する.

        Raises:
            ValueError: 空集合であってはならない.

        Returns:
            T: 最小値
        """

        if self.is_empty():
            raise ValueError("This is empty set.")

        return self._buckets[0][0]

    def pop_min(self) -> T:
        """ 最小値を削除し, その最小値を返り値とする.

        Raises:
            ValueError: 空集合であってはならない.

        Returns:
            T: 最小値
        """

        if self.is_empty():
            raise ValueError("This is empty set.")

        A=self._buckets[0]
        value=A.pop(0)
        self._N -= 1

        if len(A)==0:
            self.__build()

        return value

    def get_max(self) -> T:
        """ 最大値を取得する.

        Raises:
            ValueError: 空集合であってはならない.

        Returns:
            T: 最大値
        """

        if self.is_empty():
            return ValueError("This is empty set.")

        return self._buckets[-1][-1]

    def pop_max(self) -> T:
        """ 最大値を削除し, その最大値を返り値とする.

        Raises:
            ValueError: 空集合であってはならない.

        Returns:
            T: 最大値
        """

        if self.is_empty():
            raise ValueError("This is empty set.")

        A=self._buckets[-1]
        value=A.pop(-1)
        self._N -= 1

        if len(A)==0:
            self.__build()

        return value

    #=== k-th element
    def kth_min(self, k: int) -> T:
        """ k (0-indexed) 番目に小さい値を求める.

        Args:
            k (int): 要素番号

        Returns:
            T: k 番目に小さい値
        """

        if not(0 <= k < len(self)):
            raise IndexError

        return self[k]

    def kth_max(self, k: int) -> T:
        """ k (0-indexed) 番目に大きい値を求める.

        Args:
            k (int): 要素番号

        Returns:
            T: k 番目に大きい値
        """

        if not(0 <= k < len(self)):
            raise IndexError

        return self[len(self) - 1 - k]

    #=== previous, next

    def previous(self, value: T, equal: bool = False) -> T | None:
        """ value 未満の最大値を求める.

        Args:
            value (T): 閾値
            equal (bool, optional): True にすると, "未満" が "以下"になる. Defaults to False.

        Returns:
            T | None: value 未満の最大値 (存在しない場合は None)
        """

        if self.is_empty():
            return None

        if equal:
            for bucket in reversed(self._buckets):
                if bucket[0] <= value:
                    return bucket[bisect_right(bucket,value) - 1]
        else:
            for bucket in reversed(self._buckets):
                if bucket[0] <value:
                    return bucket[bisect_left(bucket, value) - 1]

    def next(self, value: T, equal: bool = False) -> T | None:
        """ value より大きい最小値を求める.

        Args:
            value (T): 閾値
            mode (bool, optional): True にすると, "より大きい" が "以上"になる. Defaults to False.

        Returns:
            T | None: value より大きい最小値 (存在しない場合は None)
        """

        if self.is_empty():
            return None

        if equal:
            for bucket in self._buckets:
                if bucket[-1] >= value:
                    return bucket[bisect_left(bucket, value)]
        else:
            for bucket in self._buckets:
                if bucket[-1] > value:
                    return bucket[bisect_right(bucket, value)]

    #=== count
    def less_count(self, value: T, equal: bool = False) -> int:
        """ value 未満の元の個数を求める.

        Args:
            value (T): 閾値
            equal (bool, optional): True にすると, "未満" が "以下" になる. Defaults to False.

        Returns:
            int: value 未満の元の個数
        """

        if self.is_empty():
            return 0

        count=0
        if equal:
            for A in self._buckets:
                if A[-1]>value:
                    return count+bisect_right(A, value)
                count+=len(A)
        else:
            for A in self._buckets:
                if A[-1]>=value:
                    return count+bisect_left(A, value)
                count+=len(A)
        return count

    def more_count(self, value: T, equal: bool = False) -> int:
        """ value より大きいの元の個数を求める.

        Args:
            value (T): 閾値
            equal (bool, optional): True にすると, "より大きい" が "以上" になる. Defaults to False.

        Returns:
            int: value より大きい元の個数
        """

        return self.N - self.less_count(value, not equal)

    #===
    def is_upper_bound(self, x: T, equal: bool = True) -> bool:
        """ x はこの集合の上界 (任意の元 a に対して, a <= x) か ?

        Args:
            x (T): 値
            equal (bool, optional): False にすると, 真の上界か? になる. Defaults to True.

        Returns:
            bool: 上界 ?
        """

        if self.is_empty():
            return True

        a=self._buckets[-1][-1]
        return (a<x) or (bool(equal) and a==x)

    def is_lower_bound(self, x: T, equal: bool = True) -> bool:
        """ x はこの集合の下界 (任意の元 a に対して, x <= a) か ?

        Args:
            x (T): 値
            equal (bool, optional): False にすると, 真の下界か? になる. Defaults to True.

        Returns:
            bool: 下界 ?
        """

        if self.is_empty():
            return True

        a=self._buckets[0][0]
        return (x<a) or (bool(equal) and a==x)


    #=== index
    def index(self, value: T) -> int:
        """ 要素 x の要素番号を求める.

        Args:
            value (T): 要素

        Raises:
            ValueError: 存在しない場合に発生

        Returns:
            int: 要素番号
        """

        index=0
        for A in self._buckets:
            if A[-1]>value:
                i=bisect_left(A, value)
                if A[i]==value:
                    return index+i
                else:
                    raise ValueError("{} is not in Set".format(value))
            index+=len(A)
        raise ValueError("{} is not in Set".format(value))
