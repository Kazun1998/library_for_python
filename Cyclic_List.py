class Cyclic_List:
    def __init__(self, N, default):
        """ N 個の要素全てが default であるリストを生成する.

        Args:
            N (int): 要素数
            default : 埋める値
        """

        self.list = [default for _ in range(N)]
        self.N = N
        self.offset = 0

    def push(self, k = 1):
        """ k 要素だけ進める (第 i 要素が第 (i+k) 要素に移動する)

        Args:
            k (int, optional): 移動量. Defaults to 1.
        """

        self.offset += k
        self.offset %= self.N

    def pull(self, k = 1):
        """ k 要素だけ戻す (第 i 要素が第 (i-k) 要素に移動する)

        Args:
            k (int, optional): 移動量. Defaults to 1.
        """

        self.offset -= k
        self.offset %= self.N

    def __setitem__(self, index, value):
        self.list[(index - self.offset) % self.N] = value

    def __getitem__(self, index):
        return self.list[(index - self.offset) % self.N]

    def __len__(self):
        return self.N

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __str__(self):
        return f"[{', '.join(map(str, self))}]"

    __repr__ = __str__
