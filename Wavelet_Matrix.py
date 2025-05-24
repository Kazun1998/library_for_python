class Fully_Indexable_Dictionary:
    """
    references:
    https://judge.yosupo.jp/submission/33990
    """

    bucket_size = 32

    def __init__(self, n: int):
        """ 長さ n の完備辞書を生成する.

        Args:
            n (int): 長さ
        """

        self.__n = n
        self.__bucket_number = (n - 1) // self.bucket_size
        self.bit = [0] * self.bucket_number
        self.mask=[(1<<i)-1 for i in range(1<<5)]

    def __popcount(self, x: int):
        x = x - ((x >> 1) & 0x55555555)
        x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
        x = x + (x >> 4) & 0x0f0f0f0f
        x = x + (x >> 8)
        x = x + (x >> 16)
        return x & 0x0000007f

    def __len__(self) -> int:
        return self.__n

    @property
    def bucket_number(self) -> int:
        return self.__bucket_number

    def set(self, index: int, bit: int):
        """ 第 index 要素を bit に変更する.

        Args:
            index (int): 要素番号
            bit (int): 0 or 1
        """

        if index < 0:
            index += len(self)

        if bit:
            self.bit[index >> 5] |= 1 << (index & 31)
        else:
            self.bit[index >> 5] &= ~(1 << (index & 31))

    def build(self):
        """ データ構造を確定させる. ※ 以降, set の使用禁止

        """

        # self.total[k] := 0, 1, ..., k - 1 番目の k 個のバケットにおける bit の総和

        self.total = [0] * self.bucket_number
        for k in range(1, self.blocks):
            self.total[k] = self.total[k - 1] + self.__popcount(self.bit[k - 1])

    def access(self, index: int) -> int:
        """ 第 index 要素を出力する.

        Args:
            index (int): 要素番号

        Returns:
            int: 0 or 1
        """

        if index < 0:
            index += len(self)

        return (self.bit[index >> 5] >> (index & 31)) & 1

    __getitem__ = access

    def rank(self, index: int, bit: int) -> int:
        """ [0, index) にある bit の数を求める.

        Args:
            index (int): 左端
            bit (int): 求める bit

        Returns:
            int: [0, index) にある bit の数
        """
        if index <= 0:
            return 0

        index = min(index, self.N)

        if index < self.N:
            alpha = self.total[index >> 5] + self.__popcount(self.bit[index >> 5] & self.mask[index & 31])
        else:
            alpha = self.total[-1] + self.__popcount(self.bit[-1])

        return alpha if bit else index-alpha

    def select(self, k: int, bit: int, default: int = -1) -> int:
        """ 先頭から k (1-indexed) 番目の bit の位置を求める (存在しない場合は default).

        Args:
            k (int): 1-indexed における出現回数
            bit (int): 0 or 1
            default (int, optional): k 番目の bit が存在しない場合の返り値. Defaults to -1.

        Returns:
            int: k 番目の bit の位置
        """

        if (k < 1 or self.rank(len(self), bit) < k):
            return default

        l, r = 0, len(self)
        while r - l > 1:
            m = (l + r) // 2
            if self.rank(m, bit) >= k:
                r = m
            else:
                l = m
        return l

class Wavelet_Matrix:
    def __init__(self, X: list[int]):
        """ X についての Wavelet 行列を作成する.

        """

        self.__n = N = len(X)

        self.value_list = sorted(set(X))
        self.value_dict = { x: i for i,x in enumerate(self.value_list) }
        Y=[self.value_dict[x] for x in X]

        self.bit_size=len(self.value_dict).bit_length()
        self.max_value=(1<<self.bit_size)-1

        self.zero_count=[0]*self.bit_size
        self.dictionaries = [Fully_Indexable_Dictionary(N) for _ in range(self.bit_size)]

        for lv in range(self.bit_size - 1, -1, -1):
            dictionary = self.dictionaries[~lv]
            left = []
            right = []
            for i in range(N):
                if (Y[i] >> lv) & 1:
                    dictionary.set(i, 1)
                    right.append(Y[i])
                else:
                    left.append(Y[i])

            dictionary.build()
            self.zero_count[~lv] = len(left)

            Y = left + right

        self.begin = [0] * len(self.value_dict)
        for i in range(N - 1, -1, -1):
            self.begin[Y[i]] = i

    def access(self, index: int) -> int:
        """ 第 index 要素の値を求める.

        Args:
            index (int): 要素番号

        Returns:
            int: 第 index 要素
        """

        if index < 0:
            index += self.N

        p = 0
        for lv in range(self.bit_size):
            dictionary = self.dictionaries[lv]
            bit = dictionary.access(index)
            p = (p << 1) | bit

            if bit:
                index = self.zero_count[lv] + dictionary.rank(index, 1)
            else:
                index = dictionary.rank(index ,0)

        return self.value_list[p]

    __getitem__ = access

    def __len__(self) -> int:
        return self.__n

    def rank(self, i, value):
        """ [0,i) にある value の個数を求める.

        i: 右端 (第 i 要素を含まない)
        value: 値
        """
        return self.range_rank(0,i,value)

    def range_rank(self, l: int, r: int, v: int) -> int:
        """ [l, r) にある v の個数を求める.

        Args:
            l (int): 左端
            r (int): 右端 (第 r 項自身は含めない)
            value (int): 値

        Returns:
            int: [l, r) にある v の個数
        """

        if (value := self.value_dict.get(v, None)) is None:
            return 0

        for lv in range(self.bit_size):
            dictionary = self.dictionaries[lv]

            if (value >> (self.bit_size - lv - 1)) & 1:
                l = dictionary.rank(l, 1) + self.zero_count[lv]
                r = dictionary.rank(r, 1) + self.zero_count[lv]
            else:
                l = dictionary.rank(l, 0)
                r = dictionary.rank(r, 0)

        return r-l

    def select(self, v: int, k: int, default: int = -1) -> int:
        """ k (1-indexed) 番目に登場する v の位置を求める.

        Args:
            v (int): 値
            k (int): 1-indexed での出現回数
            default (int, optional): v が k 個以上存在しない場合の返り値. Defaults to -1.

        Returns:
            int: k (1-indexed) 番目に登場する v の位置
        """

        if (value := self.value_dict.get(v, None)) is None:
            return default

        p=self.begin[value]
        index=p+k-1

        for lv in range(self.bit_size):
            dictionary = self.dictionaries[~lv]
            if (value >> lv) & 1:
                index = dictionary.select(index - self.zero_count[~lv] + 1, 1, None)
            else:
                index = dictionary.select(index+1, 0, None)

            if index is None:
                return default
        return index

    def quantile(self, l: int, r: int, k: int) -> int:
        """ [l,r) における k (1-indexed) 番目に小さい値を求める.

        Args:
            l (int): 左端
            r (int): 右端 (第 r 項自身は含まない)
            k (int): 小さい方から k 番目

        Returns:
            int: [l,r) における k (1-indexed) 番目に小さい値
        """

        p=0
        for lv in range(self.bit_size):
            dictionary = self.dictionaries[lv]
            alpha = dictionary.rank(r, 0) - dictionary.rank(l, 0)
            p <<= 1
            if alpha < k:
                p |= 1
                k -= alpha
                l = dictionary.rank(l, 1) + self.zero_count[lv]
                r = dictionary.rank(r, 1) + self.zero_count[lv]
            else:
                l = dictionary.rank(l, 0)
                r = dictionary.rank(r, 0)
        return self.value_list[p]

    kth_min = quantile

    def kth_max(self, l: int, r: int, k: int) -> int:
        """ [l,r) における k (1-indexed) 番目に大きい値を求める.

        Args:
            l (int): 左端
            r (int): 右端 (第 r 項自身は含まない)
            k (int): 大きい方から k 番目

        Returns:
            int: [l,r) における k (1-indexed) 番目に大きい値
        """
        return self.quantile(l, r, r - l - k + 1)

    def top(self, l: int, r: int, k: int) -> list[tuple[int, int]]:
        """ [l,r) にある出現回数が多い順から k 個 (値, 個数) のタプルを出力する (個数同率は値が小さい方が優先).

        l: 左端
        r: 右端 (第 r 項を含まない)
        k: 採用する要素数
        """

        assert k >= 1

        from heapq import heappush, heappop
        X = []
        Q = [(-(r - l), 0, 0, l, r)]
        while k and Q:
            _, p, lv, l, r = heappop(Q)

            if lv==self.bit_size:
                X.append((self.value_list[p], r - l))
                k -= 1
                continue

            dictionary = self.dictionaries[lv]
            beta = dictionary.rank(l, 0)
            alpha = dictionary.rank(r, 0) - beta

            # 0
            if alpha > 0:
                heappush(Q, (-alpha, p << 1, lv + 1, beta, beta + alpha))

            # 1
            if (r - l) - alpha > 0:
                x = self.zero_count[lv] + (l - beta)
                y = x + (r - l - alpha)
                heappush(Q, (-((r - l) - alpha), (p << 1) | 1, lv + 1, x, y))
        return X

    def sum(self, l: int, r: int) -> int:
        """ [l, r) における総和を求める.

        Args:
            l (int): 左端
            r (int): 右端 (第 r 項自身は含まない)

        Returns:
            int: 総和
        """

        return sum(value * frequency for value, frequency in self.top(l, r, r - l))

    def range_all(self, l, r, value):
        """ [l,r) にある (value 未満の個数, value ちょうどの個数, value より大きい個数) を求める.

        l: 左端
        r: 右端 (第 r 項を含まない)
        value: 値
        """

        pass

    def range_freq(self, l, r, x, y):
        """ [l,r) にある x 以上 y 未満の個数を求める.

        l: 左端
        r: 右端 (第 r 項を含まない)
        value: 値
        """

        pass

    def range_less(self, l, r, value):
        """ [l,r) にある value 未満の個数を求める.

        l: 左端
        r: 右端 (第 r 項を含まない)
        value: 値
        """

        pass

    def range_more(self, l, r, value):
        """ [l,r) にある value より大きい個数を求める.

        l: 左端
        r: 右端 (第 r 項を含まない)
        value: 値
        """

        pass

    def range_list(self, l, r, a, b):
        """ [l,r) にある (value 未満の個数, value ちょうどの個数, value より大きい個数) を求める.

        l: 左端
        r: 右端 (第 r 項を含まない)
        value: 値
        """
        pass

    def range_max(self, l, r, k):
        pass

    def range_min(self, l, r, k):
        pass

    def prev_value(self, l, r, a, b):
        pass

    def next_value(self, l, r, a, b):
        pass

    def intersect(self, l1: int, r1: int, l2: int, r2: int) -> list[tuple[int, int, int]]:
        """ [l1, r1), [l2, r2) に共に存在する要素 v における (v, 1番目の区間にある v の個数, 2番目の区間にある v の個数) のリストを出力する.

        Args:
            l1 (int): 区間 1 の左端
            r1 (int): 区間 1 の右端 (第 r1 項自身は含まない)
            l2 (int): 区間 2 の左端
            r2 (int): 区間 2 の右端 (第 r2 項自身は含まない)

        Returns:
            list[tuple[int, int, int]]: (v, a, b) の形のリスト. 各項は以下を表す.
                v: 共通して現れる要素
                a: 区間 1 における v の個数
                b: 区間 2 における v の個数
        """

        X = [(l1, r1, l2, r2, 0)]
        for lv in range(self.bit_size):
            Y = X
            X = []
            dictionary = self.dictionaries[lv]
            for l1, r1, l2, r2, p in Y:
                beta1 = dictionary.rank(l1, 0)
                alpha1 = dictionary.rank(r1, 0) - beta1
                a1 = beta1
                b1 = beta1 + alpha1
                c1 = self.zero_count[lv] + (l1 - beta1)
                d1 = c1 + (r1 - l1- alpha1)

                beta2 = dictionary.rank(l2, 0)
                alpha2 = dictionary.rank(r2, 0) - beta2
                a2 = beta2
                b2 = beta2 + alpha2
                c2 = self.zero_count[lv] + (l2 - beta2)
                d2 = c2 + (r2 - l2 - alpha2)

                if a1 < b1 and a2 < b2:
                    X.append((a1, b1, a2, b2, p << 1))

                if c1<d1 and c2<d2:
                    X.append((c1, d1, c2, d2, (p << 1) | 1))

        return [(self.value_list[p], y1 - x1, y2 - x2) for x1, y1, x2, y2, p in X]
