class Doubly_Linked_List:
    def __init__(self, N: int):
        self.__front = [None] * N
        self.__back = [None] * N

    def add(self, k: int) -> list[int]:
        """ k 個の要素を追加する.

        Args:
            k (int): 追加する要素の数

        Returns:
            list[int]: 追加した要素の番号
        """

        self.__front.extend([None] * k)
        self.__back.extend([None] * k)
        return list(range(len(self.__front) - k, len(self.__front)))

    def __len__(self) -> int:
        return len(self.__front)

    def __str__(self) -> str:
        res = []
        used = [0] * len(self)

        for x in range(len(self)):
            if used[x]:
                continue

            a = self.enumerate(x)
            for y in a:
                used[y] = 1
            res.append(a)

        return str(res)

    def previous(self, x: int, default: int = -1) -> int:
        """ x の直前の要素を求める. 存在しない場合は default

        Args:
            x (int): 要素
            default (int, optional): 直前の要素が存在しない場合の返り値. Defaults to -1.

        Returns:
            int: x の直前の要素
        """
        return self.__front[x] if self.__front[x] is not None else default

    def next(self, x: int, default: int = -1) -> int:
        """ x の直後の要素を求める. 存在しない場合は default

        Args:
            x (int): 要素
            default (int, optional): 直後の要素が存在しない場合の返り値. Defaults to -1.

        Returns:
            int: x の直後の要素
        """
        return self.__back[x] if self.__back[x] is not None else default

    def disconnect_front(self, x: int):
        """ x から前に伸びるリンクを削除する.

        Args:
            x (int): 要素
        """

        front = self.__front
        back = self.__back

        if (y := front[x]) is None:
            return

        front[x] = None
        back[y] = None

    def disconnect_back(self, x):
        """ x から後ろに伸びるリンクを削除する.

        Args:
            x (int): 要素
        """

        front = self.__front
        back = self.__back

        if (y := back[x]) is None:
            return

        back[x] = None
        front[y] = None

    def extract(self, x: int):
        """ x に接続するリンクを削除し, x の前後が存在するならば, それらをつなぐ.

        Args:
            x (int): 要素
        """

        a = self.__front[x]
        b = self.__back[x]

        self.disconnect_front(x)
        self.disconnect_back(x)

        if (a is not None) and (b is not None):
            self.connect(a, b)

    def connect(self, x: int, y: int):
        """ x から y へのリンクを生成する (すでにある x からのリンクと y へのリンクは削除される).

        Args:
            x (int): リンク元要素
            y (int): リンク先要素
        """

        self.disconnect_back(x)
        self.disconnect_front(y)
        self.__back[x] = y
        self.__front[y] = x

    def insert_front(self, x: int, y: int):
        """ x の前に y を挿入する.

        Args:
            x (int): 基準要素
            y (int): 挿入要素
        """

        z = self.__front[x]
        self.connect(y, x)
        if z is not None:
            self.connect(z, y)

    def insert_back(self, x: int, y: int):
        """ x の後に y を挿入する.

        Args:
            x (int): 基準要素
            y (int): 挿入要素
        """

        z = self.__back[x]
        self.connect(x, y)
        if z is not None:
            self.connect(y, z)

    def head(self, x: int) -> int:
        """ x が属する弱連結成分の先頭を求める.

        Args:
            x (int): 要素

        Returns:
            int: x が属する弱連結成分の先頭
        """

        while self.__front[x] is not None:
            x = self.__front[x]
        return x

    def tail(self, x: int) -> int:
        """ x が属する弱連結成分の末尾を求める.

        Args:
            x (int): 要素

        Returns:
            int: x が属する弱連結成分の先頭
        """

        while self.__back[x] is not None:
            x = self.__back[x]
        return x

    def enumerate(self, x: int) -> list[int]:
        """ x が属している弱連結成分を先頭から順に出力する.

        Args:
            x (int): 要素

        Returns:
            list[int]: x が属している弱連結成分
        """

        x = self.head(x)
        res = [x]
        while self.__back[x] is not None:
            x = self.__back[x]
            res.append(x)
        return res

    def depth(self, x: int) -> int:
        """ 要素 x の深さ (先頭の要素への移動回数) を求める.

        Args:
            x (int): 要素

        Returns:
            int: 深さ
        """
        dep = 0
        while self.__front[x] is not None:
            x = self.__front[x]
            dep += 1
        return dep
