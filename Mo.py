class Mo:
    def __init__(self, N: int):
        """ 範囲が 0 以上 N "未満" の Mo's Algorithm の準備をする.

        Args:
            N (int): 範囲の上限 (N は含まない)
        """

        self.__N = N
        self.__query_count = 0
        self.left: list[int] = []
        self.right: list[int] = []

    @property
    def N(self) -> int:
        return self.__N

    @property
    def query_count(self) -> int:
        """ 現在登録されているクエリの数を出力する.

        Returns:
            int: 現在登録されているクエリの数
        """

        return self.__query_count

    def add_query(self, l: int, r: int):
        """ 閉区間 [l,r] に対するクエリを追加する.

        Args:
            l (int): 左端
            r (int): 右端
        """

        self.left.append(l)
        self.right.append(r + 1)
        self.__query_count += 1

    def calculate(self, add, delete, rem):
        """ クエリを処理する.

        Args:
            add (Callable[[int]]): add(k): 区間に k を追加する場合の処理
            delete (Callable[[int]]): delete(k): 区画から k を削除する場合の処理
            rem (Callable[[int]]): query(q): 第 q クエリ (add_query に追加した順) の処理
        """

        bucket_size = self.N // (min(self.N, int(self.query_count ** 0.5 + 0.5)))
        bucket_count = (self.N + bucket_size - 1) // bucket_size
        buckets = [[] for _ in range(bucket_count)]

        left = self.left
        right = self.right

        for q in range(self.query_count):
            buckets[left[q] // bucket_size].append(q)

        for i in range(bucket_count):
            buckets[i].sort(key = lambda q: right[q], reverse = i % 2)

        x = y = 0
        for bucket in buckets:
            for q in bucket:
                l = left[q]
                r = right[q]

                for i in range(x, l):
                    delete(i)

                for i in range(x - 1, l - 1 , -1):
                    add(i)

                for j in range(y, r):
                    add(j)

                for j in range(y - 1, r - 1, -1):
                    delete(j)

                x = l
                y = r
                rem(q)

    def calculate_noncommutative(self, add_left, add_right, delete_left, delete_right, rem):
        bucket_size = self.N // (min(self.N, int(self.query_count ** 0.5 + 0.5)))
        bucket_count = (self.N + bucket_size - 1) // bucket_size
        buckets = [[] for _ in range(bucket_count)]

        left = self.left
        right = self.right

        for q in range(self.query_count):
            buckets[left[q] // bucket_size].append(q)

        for i in range(bucket_count):
            buckets[i].sort(key=lambda q: right[q], reverse=i%2)

        x = y = 0
        for bucket in buckets:
            for q in bucket:
                l = left[q]
                r = right[q]

                for i in range(x, l):
                    delete_left(i)

                for i in range(x-1, l-1, -1):
                    add_left(i)

                for j in range(y, r):
                    add_right(j)

                for j in range(y-1, r-1, -1):
                    delete_right(j)

                x = l
                y = r
                rem(q)
