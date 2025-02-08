from typing import TypeVar, Generic, Iterable, Iterator

M = TypeVar('M')
class Bucket_List:
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, A: Iterable[M] = []) -> None:
        A = list(A)
        N = self.size = len(A)

        bucket_number = int(pow(N / self.BUCKET_RATIO, 0.5) + 1)
        self.buckets = [A[N * i // bucket_number: N * (i + 1) // bucket_number] for i in range(bucket_number)]

    def __iter__(self) -> Iterator[M]:
        for bucket in self.buckets:
            yield from bucket

    def __reversed__(self) -> Iterator[M]:
        for bucket in reversed(self.buckets):
            for a in reversed(bucket):
                yield a

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return str(list(self))

    def __repr__(self) -> str:
        return f"[Bucket List] {str(self)}"

    def __contains__(self, x: M) -> bool:
        for y in self:
            if x == y:
                return True
        return False

    def reverse(self) -> None:
        self.buckets.reverse()
        for bucket in self.buckets:
            bucket.reverse()
