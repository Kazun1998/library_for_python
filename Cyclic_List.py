class Cyclic_List:
    def __init__(self, A: list):
        """ N 個の要素全てが default であるリストを生成する.

        Args:
            N (int): 要素数
            default : 埋める値
        """

        self.__list = A
        self.__offset = 0

    @property
    def offset(self):
        return self.__offset

    def push(self, k: int = 1):
        """ k 要素だけ進める (第 i 要素が第 (i+k) 要素に移動する)

        Args:
            k (int, optional): 移動量. Defaults to 1.
        """

        self.__offset += k
        self.__offset %= len(self)

    def pull(self, k = 1):
        """ k 要素だけ戻す (第 i 要素が第 (i-k) 要素に移動する)

        Args:
            k (int, optional): 移動量. Defaults to 1.
        """

        self.__offset -= k
        self.__offset %= len(self)

    def __setitem__(self, index, value):
        self.__list[(index - self.offset) % len(self)] = value

    def __getitem__(self, index):
        return self.__list[(index - self.offset) % len(self)]

    def __len__(self):
        return len(self.__list)

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __str__(self):
        return f"[{', '.join(map(str, self))}]"

    def __repr__(self):
        return f"{self.__class__.__name__}({list(self)})"
