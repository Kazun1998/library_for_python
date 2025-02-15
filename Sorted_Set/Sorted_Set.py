# Reference: https://qiita.com/tatyam/items/492c70ac4c955c055602
# ※ 計算量が O(sqrt(N)) per query なので, 過度な期待はしないこと.

from typing import Generic, Iterable, Iterator, TypeVar
from bisect import bisect_left, bisect_right

T = TypeVar('T')
class Sorted_Set:
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, A: Iterable[T] = []) -> None:
        A = list(A)
        N = len(A)

        # sort if necessary.
        if any(A[i] > A[i + 1] for i in range(N - 1)):
            A.sort()

        # unique if nexesarry.
        if any(A[i] >= A[i + 1] for i in range(N - 1)):
            A, B = [], A
            for b in B:
                if (not A) or (A[-1] != b):
                    A.append(b)

        N = self.size = len(A)
        bucket_number = int(pow(N / self.BUCKET_RATIO, 0.5) + 1)
        self.buckets = [ A[N * j // bucket_number: N * (j + 1) // bucket_number] for j in range(bucket_number)]

    # Iterator

    def __iter__(self) -> Iterator[T]:
        for bucket in self.buckets:
            yield from bucket

    def __reversed__(self) -> Iterator[T]:
        for bucket in reversed(self.buckets):
            yield from reversed(bucket)

    # 長さ, bool

    def __len__(self) -> int:
        return self.size

    def __bool__(self) -> bool:
        return self.size > 0

    def is_empty(self) -> bool:
        return self.size == 0

    # 文字列
    def __str__(self):
        return "{" + str(list(self)) + "}"

    def __repr__(self):
        return f"Sorted Set: {str(self)}"

    # 場所
    def __position(self, x: T) -> tuple[list[T], int, int]:
        for index, bucket in enumerate(self.buckets):
            if x <= bucket[-1]:
                break
        return (bucket, index, bisect_left(bucket, x))

    def __contains__(self, x: T) -> bool:
        if self.is_empty():
            return False

        bucket, _, i = self.__position(x)
        return (i != len(bucket)) and (bucket[i] == x)

    # 追加
    def add(self, x: T) -> bool:
        """ 要素 x を追加する.

        Args:
            x (T): 要素

        Returns:
            bool: 実際に追加されたならば True.
        """

        # 空集合のときのみ別処理
        if self.is_empty():
            self.buckets = [[x]]
            self.size = 1
            return True

        bucket, p, i = self.__position(x)

        # x はすでに存在するか?
        if (i != len(bucket)) and (bucket[i] == x):
            return False

        bucket.insert(i, x)
        self.size += 1
        if len(bucket) > len(self.buckets) * self.SPLIT_RATIO:
            mid = len(bucket) >> 1
            self.buckets[p: p + 1] = [bucket[:mid], bucket[mid:]]
        return True

    # 削除
    def __pop(self, bucket: list[T], p: int, i: int) -> T:
        res = bucket.pop(i)
        self.size -= 1
        if not bucket:
            del self.buckets[p]
        return res

    def pop(self, i: int = -1) -> T:
        if i < 0:
            for p, bucket in enumerate(reversed(self.buckets)):
                i += len(bucket)
                if i >= 0:
                    return self.__pop(bucket, p, i)
        else:
            for p, bucket in enumerate(self.buckets):
                if i < len(bucket):
                    return self.__pop(bucket, p, i)
                i -= len(bucket)
        raise IndexError

    def discard(self, x: T) -> bool:
        """ x を削除する (存在しない場合は何もしない).

        Args:
            x (T): 要素

        Returns:
            bool: 元の集合に存在するならば True
        """
        if self.is_empty():
            return False

        bucket, p, i = self.__position(x)
        if not((i != len(bucket)) and (bucket[i] == x)):
            return False

        self.__pop(bucket, p, i)
        return True

    def remove(self, x: T) -> None:
        """ 要素 x を削除する (存在しないならば KeyError)

        Args:
            x (T): _description_

        Raises:
            KeyError: 存在しない場合に発動
        """
        if not self.discard(x):
            raise KeyError(x)

    # get
    def __getitem__(self, index: int) -> T:
        if index < 0:
            for bucket in reversed(self.buckets):
                index += len(bucket)
                if index >= 0:
                    return bucket[index]
        else:
            for bucket in self.buckets:
                if index < len(bucket):
                    return bucket[index]

        raise IndexError

    def get_min(self) -> T:
        if self.N == 0:
            raise ValueError("This is empty set.")
        return self.buckets[0][0]

    def pop_min(self) -> T:
        if self.N == 0:
            raise ValueError("This is empty set.")
        return self.pop(0)

    def get_max(self) -> T:
        if self.N == 0:
            return ValueError("This is empty set.")
        return self.buckets[-1][-1]

    def pop_max(self) -> T:
        if self.N==0:
            raise ValueError("This is empty set.")
        return self.pop(-1)

    #=== k-th element
    def kth_min(self, k: int) -> T:
        """ k 番目に小さい要素を求める.

        Args:
            k (int): index (0-indexed)

        Returns:
            T: k 番目に小さい要素
        """
        if 0 <= k < len(self):
            raise IndexError

        return self[k]

    def kth_max(self, k: int) -> T:
        """ k 番目に大きい要素を求める.

        Args:
            k (int): index (0-indexed)

        Returns:
            T: k 番目に大きい要素
        """
        if 0 <= k < len(self):
            raise IndexError

        return self[-(k + 1)]

    #=== previous, next

    def previous(self, value: T, default: T = None, equal: bool = False) -> T | None:
        """ value 未満で最大の要素を出力する.

        Args:
            value (T) : 閾値
            default (T, optional): 全ての要素が value 以上である時の返り値. Defaults to None.
            equal (bool, optional): equal を True にすると, "未満" が "以下" になる. Defaults to False.

        Returns:
            T | None: value 未満 (以下) の要素が存在するならばその最大値, 存在しないならば default.
        """

        if self.is_empty():
            return default

        if equal:
            for bucket in reversed(self.buckets):
                if bucket[0] <= value:
                    return bucket[bisect_right(bucket, value) - 1]
        else:
            for bucket in reversed(self.buckets):
                if bucket[0] < value:
                    return bucket[bisect_left(bucket, value) - 1]

        return default

    def next(self, value: T, default: T = None, equal: bool = False) -> T | None:
        """ value より大きい最小の要素を出力する.

        Args:
            value (T) : 閾値
            default (T, optional): 全ての要素が value 以下である時の返り値. Defaults to None.
            equal (bool, optional): equal を True にすると, "より大きい" が "以上" になる. Defaults to False.

        Returns:
            T | None: value より大きい (以上) の要素が存在するならばその最小値, 存在しないならば default.
        """

        if not self.N:
            return default

        if equal:
            for bucket in self.buckets:
                if bucket[-1] >= value:
                    return bucket[bisect_left(bucket, value)]
        else:
            for bucket in self.buckets:
                if bucket[-1] > value:
                    return bucket[bisect_right(bucket, value)]

        return default

    #=== count
    def less_count(self, value: T, equal: bool = False) -> int:
        """ value 未満である要素の数を求める.

        Args:
            value (T): 要素
            equal (bool, optional): True にすると, "未満" が "以下" になる. Defaults to False.

        Returns:
            int: value 未満 (以下) の要素数
        """

        if self.is_empty():
            return 0

        count = 0
        if equal:
            for bucket in self.buckets:
                if value < bucket[-1]:
                    return count + bisect_right(bucket, value)
                count += len(bucket)
        else:
            for bucket in self.buckets:
                if value <= bucket[-1]:
                    return count + bisect_left(bucket, value)
                count += len(bucket)
        return count

    def more_count(self, value: T, equal: bool = False) -> int:
        """ value より大きい要素の数を求める.

        Args:
            value (T): 要素
            equal (bool, optional): True にすると, "より大きい" が "以上" になる. Defaults to False.

        Returns:
            int: value 未満 (以下) の要素数
        """

        return len(self) - self.less_count(value, not equal)

    # bound
    def is_upper_bound(self, x: T, equal = True) -> bool:
        """ x はこの集合の上界 (全ての要素 a に対して, a <= x) か?

        Args:
            x (T): 要素
            equal (bool, optional): False にした場合, 判定条件が a < x になる. Defaults to True.

        Returns:
            bool: 上界 ?
        """

        if self.is_empty():
            return True

        a = self.get_max()
        return (a < x) or (equal and a == x)

    def is_lower_bound(self, x, equal=True):
        """ x はこの集合の下界 (全ての要素 a に対して, x <= a) か?

        Args:
            x (T): 要素
            equal (bool, optional): False にした場合, 判定条件が x < a になる. Defaults to True.

        Returns:
            bool: 下界 ?
        """

        if self.is_empty():
            return True

        a = self.get_min()
        return (x < a) or (equal and a == x)

    #=== index
    def index(self, value: T) -> int:
        offset = 0
        for bucket in self.buckets:
            if value < bucket[-1]:
                k = bisect_left(bucket, value)
                if bucket[k] == value:
                    return offset + k
                else:
                    raise ValueError(f"{value} is not in Set.")

            offset += len(bucket)
        else:
            raise ValueError(f"{value} is not in Set.")
