from typing import TypeVar, Callable, Generic

T = TypeVar('T')
class Merge_Sort(Generic[T]):
    @staticmethod
    def sort_by_index(X: list[T], reverse: bool = False, key: Callable[[T, T], int] = None) -> list[int]:
        """ 安定マージソート (昇順) の結果をインデックスの配列で求める.

        Args:
            X (list[T]): ソート対象
            reverse (bool, optional): True ならば降順に並び替える.. Defaults to False.
            key (Callable[[T, T], int], optional): 比較方法の指定 (key(x, y) は x < y ならば負, x == y ならば 0, x > y ならば正となるようにする). Defaults to None.

        Returns:
            list[int]: 安定マージソート (昇順) の結果のインデックスの配列
        """

        if not X:
            return []

        if key is None:
            def key(x: T, y: T) -> int:
                if x < y:
                    return -1
                elif x == y:
                    return 0
                elif x > y:
                    return 1

        from collections import deque
        queue = deque([[k] for k in range(len(X))])

        def merge(A: list[int], B: list[int]) -> list[int]:
            i = j = 0
            C= [-1] * (len(A) + len(B))
            for t in range(len(A) + len(B)):
                if (i < len(A)) and (j < len(B)):
                    cmp = key(X[A[i]], X[B[j]])
                    if cmp == 0:
                        cmp = 1 if A[i] < B[j] else -1
                elif i == len(A):
                    cmp = 1
                elif j == len(B):
                    cmp = -1

                if cmp < 0:
                    C[t] = A[i]
                    i += 1
                else:
                    C[t] = B[j]
                    j += 1
            return C

        for _ in range(len(X) - 1):
            A = queue.popleft()
            B = queue.popleft()
            queue.append(merge(A, B))

        res = queue.pop()
        if reverse:
            res.reverse()
        return res

    @classmethod
    def sort(cls, X: list[T], reverse: bool = False, key: Callable[[T, T], int] = None) -> list[int]:
        return [X[k] for k in cls.sort_by_index(X, reverse = reverse, key = key)]
