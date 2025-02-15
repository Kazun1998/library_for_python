# Reference: https://github.com/tatyam-prime/SortedSet/blob/main/BucketList.py
from typing import TypeVar, Generic, Iterable, Iterator

T = TypeVar('T')
class Bucket_List(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, A: Iterable[T] = []) -> None:
        A = list(A)
        N = self.size = len(A)

        bucket_number = int(pow(N / self.BUCKET_RATIO, 0.5) + 1)
        self.buckets = [A[N * i // bucket_number: N * (i + 1) // bucket_number] for i in range(bucket_number)]

    def __iter__(self) -> Iterator[T]:
        for bucket in self.buckets:
            yield from bucket

    def __reversed__(self) -> Iterator[T]:
        for bucket in reversed(self.buckets):
            yield from reversed(bucket)

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return str(list(self))

    def __repr__(self) -> str:
        return f"[Bucket List] {str(self)}"

    def __eq__(self, other):
        if len(self) != len(other):
            return False

        for x, y in zip(self, other):
            if x != y:
                return False
        return True

    def __contains__(self, x: T) -> bool:
        for y in self:
            if x == y:
                return True
        return False

    def __insert(self, bucket: list[T], bucket_index: int, index: int, x: T) -> None:
        bucket.insert(index, x)
        self.size += 1
        if len(bucket) > len(self.buckets) * self.SPLIT_RATIO:
            mid = len(bucket) >> 1
            self.buckets[bucket_index: bucket_index + 1] = [bucket[:mid], bucket[mid:]]

    def insert(self, i: int, x: T) -> None:
        if len(self) == 0:
            if not(i == 0 or i == -1):
                raise IndexError

            self.buckets = [[x]]
            self.size = 1
            return

        if i < 0:
            for reversed_bucket_index, bucket in enumerate(reversed(self.buckets)):
                i += len(bucket)
                if i >= 0:
                    return self.__insert(bucket, len(self.buckets) + (~reversed_bucket_index), i, x)
        else:
            for bucket_index, bucket in enumerate(self.buckets):
                if i <= len(bucket):
                    return self.__insert(bucket, bucket_index, i, x)
                i -= len(bucket)

    def append(self, x: T) -> None:
        bucket = self.buckets[-1]
        return self.__insert(bucket, len(self.buckets) - 1, len(bucket), x)

    def extend(self, X: list[T]) -> None:
        for x in X:
            self.append(x)

    def __getitem__(self, i: int) -> T:
        if i >= 0:
            for bucket in self.buckets:
                if i < len(bucket):
                    return bucket[i]
                i -= len(bucket)
        else:
            for bucket in reversed(self.buckets):
                i += len(bucket)
                if i >= 0:
                    return bucket[i]
        raise IndexError

    def __pop(self, bucket: list[T], bucket_index: int, i: int) -> T:
        res = bucket.pop(i)
        self.size -= 1
        if not bucket:
            del self.buckets[bucket_index]
        return res

    def pop(self, i: int = -1):
        if i >= 0:
            for bucket_index, bucket in enumerate(self.buckets):
                if i < len(bucket):
                    return self.__pop(bucket, bucket_index, i)
                i -= len(bucket)
        else:
            for reversed_bucket_index, bucket in enumerate(self.buckets):
                i += len(bucket)
                if i < len(bucket):
                    return self.__pop(bucket, ~reversed_bucket_index, i)
        raise IndexError

    def count(self, x: T) -> int:
        return sum(bucket.count(x) for bucket in self.buckets)

    def index(self, x: T) -> int:
        for i, y in self:
            if x == y:
                return i
        raise ValueError

    def remove(self, x: T) -> None:
        self.pop(self.index(x))

    def clear(self) -> None:
        self.buckets = []
        self.size = 0

    def reverse(self) -> None:
        self.buckets.reverse()
        for bucket in self.buckets:
            bucket.reverse()
