class Doubling:
    def __init__(self, F: list[int], max_level: int):
        """ n = len(F), X = {0, 1, ..., n - 1} とする. f: X → X を f(x) := F[x] としたとき, f^k(x) を求める.

        Args:
            F (list[int]): [f(0), f(1), ..., f(n - 1)]
            max_level (int): k = 2^max_level - 1 まで対応になる
        """

        n = len(F)
        self.tower = [[0]* n for _ in range(max_level + 1)]
        self.__max_level = max_level

        bottom = self.tower[0]
        for x in range(n):
            assert 0 <= F[x] < n
            bottom[x] = F[x]

        for lv in range(1, max_level + 1):
            current = self.tower[lv]
            prev = self.tower[lv - 1]
            for x in range(n):
                current[x] = prev[prev[x]]

    @property
    def max_level(self) -> int:
        return self.__max_level

    def __len__(self) -> int:
        return len(self.tower[0])

    def evaluate(self, x: int, k: int) -> int:
        """ f^k(x) を求める.

        Args:
            x (int): 初期状態
            k (int): 遷移回数

        Returns:
            int: f^k(x)
        """

        for layer in self.tower:
            if k & 1:
                x = layer[x]

            k >>= 1

        return x

    def evaluate_list(self, k: int) -> list[int]:
        """ [f^k(0), f^k(1), ..., f^k(n - 1)] を求める.

        Args:
            k (int): 遷移回数

        Returns:
            list[int]: [f^k(0), f^k(1), ..., f^k(N - 1)]
        """

        y = list(range(len(self)))
        for layer in self.tower:
            if k & 1:
                y = [layer[b] for b in y]

            k >>= 1
        return y
