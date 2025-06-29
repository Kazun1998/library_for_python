class Binary_Trie:
    """ Reference
    https://judge.yosupo.jp/submission/35057
    https://judge.yosupo.jp/submission/53782
    """

    def __init__(self, max_value: int, allow_multiple: bool = False, query_number: int = None):
        self.bit = max_value.bit_length()
        self.upper = 1 << self.bit
        self.multi = allow_multiple

        if query_number is not None:
            self.arc = [-1] * 2 * (self.bit * query_number + 1)
            self.size = [0] * (self.bit*query_number + 1)
            self.terminal = [0] * (self.bit*query_number + 1)
            self.id=0
        else:
            self.arc = [-1, -1]
            self.size = [0]
            self.terminal = [0]

        self.query_number = query_number
        self.v_list = [0] * (self.bit + 1)
        self._lazy_xor = 0

    @property
    def lazy_xor(self) -> int:
        return self._lazy_xor

    def xor_all(self, x: int):
        assert 0 <= x < self.upper
        self._lazy_xor ^= x

    def __ixor__(self, x: int):
        self.xor_all(x)
        return self

    def insert(self, x: int) -> bool:
        """ x を追加する

        Args:
            x (int): 追加する要素

        Returns:
            bool: 差分が発生したら True
        """

        assert 0 <= x < self.upper

        x ^= self.lazy_xor
        v = 0
        for i in reversed(range(self.bit)):
            d = (x >> i) & 1
            if self.arc[2 * v + d] == -1:
                if self.query_number is not None:
                    self.id += 1
                    self.arc[2 * v + d] = self.id
                else:
                    self.arc[2 * v + d] = len(self.size)
                    self.arc.extend([-1, -1])
                    self.terminal.append(0)
                    self.size.append(0)

            v = self.arc[2 * v + d]
            self.v_list[i] = v

        if self.terminal[v] > 0 and (not self.multi):
            return False

        self.terminal[v] += 1
        for w in self.v_list:
            self.size[w] += 1

        return True

    def discard(self, x: int) -> bool:
        """ x が存在する場合, x を (1 個) 削除する

        Args:
            x (int): 削除する要素

        Returns:
            bool: 差分が発し得したら True
        """
        if not (0 <= x < self.upper):
            return

        x ^= self.lazy_xor
        v = 0
        for i in reversed(range(self.bit)):
            d = (x >> i) & 1
            if self.arc[2*v+d] == -1:
                return False

            v = self.arc[2 * v + d]
            self.v_list[i] = v

        if self.terminal[v] == 0:
            return False

        self.terminal[v] -= 1
        for w in self.v_list:
            self.size[w] -= 1

        return True

    def erase(self, x: int, k: int) -> int:
        """ x を高々 k 回削除する (ただし, k=-1 のときは無限回)

        Args:
            x (int): 削除する要素
            k (int): 削除する回数 (k = -1 のときは無限回)

        Returns:
            int: 実際に削除した回数
        """

        assert -1 <= k
        if not (0 <= x < self.upper):
            return 0

        x ^= self.lazy_xor
        v = 0
        for i in reversed(range(self.bit)):
            d = (x>>i) & 1
            if self.arc[2 * v + d] == -1:
                return 0

            v = self.arc[2 * v + d]
            self.v_list[i] = v

        if (k == -1) or (self.terminal[v] < k):
            k = self.terminal[v]

        self.terminal[v] -= k
        for w in self.v_list:
            self.size[w] -= k

        return k

    def count(self, x: int) -> int:
        """ x の個数を求める

        Args:
            x (int): 要素

        Returns:
            int: 個数
        """

        if not (0 <= x < self.upper):
            return 0

        x ^= self.lazy_xor
        v = 0
        for i in reversed(range(self.bit)):
            d = (x >> i) & 1
            if self.arc[2 * v + d] == -1:
                return 0

            v = self.arc[2 * v + d]
        return self.terminal[v]

    def __contains__(self, x: int) -> bool:
        return bool(self.count(x))

    def __len__(self) -> int:
        return self.size[0]

    def __bool__(self) -> bool:
        return bool(len(self))

    def less_count(self, x: int, equal: bool = False) -> int:
        """ x 未満の要素数を求める.

        Args:
            x (int): 閾値
            equal (bool, optional): True にすると, "未満" が "以下" になる. Defaults to False.

        Returns:
            int: x より大きい要素の数.
        """

        x ^= self.lazy_xor
        if equal:
            x += 1

        if x < 0:
            return 0

        if self.upper <= x:
            return len(self)

        v = 0
        res = 0
        for i in reversed(range(self.bit)):
            d = (x>>i) & 1
            lc = self.arc[2 * v]
            rc = self.arc[2 * v + 1]

            if (self.lazy_xor >> i) & 1:
                lc, rc = rc ,lc

            if d:
                if lc != -1:
                    res += self.size[lc]
                if rc == -1:
                    return res
                v = rc
            else:
                if lc == -1:
                    return res
                v = lc
        return res

    def more_count(self, x: int, equal: bool = False) -> int:
        """ x より大きい要素数を求める.

        Args:
            x (int): 閾値
            equal (bool, optional): True にすると, "より大きい" が "以上" になる. Defaults to False.

        Returns:
            int: x より大きい要素の数.
        """

        return len(self) - self.less_count(x, not equal)

    def low_value(self, x: int, equal = False, default = None):
        """ x 未満の整数のうち, 最大の整数を求める (存在しない場合は default).

        equal: True のとき, "未満" が "以下" になる.
        """

        x ^= self.lazy_xor
        if equal:
            x += 1

        alpha = self.less_count(x, False)

        return self.kth_element(alpha - 1) if alpha > 0 else default

    def high_value(self, x: int, equal: bool = False, default: int = None) -> int:
        """ x より大きい整数のうち, 最小の整数を求める.

        Args:
            x (int): 閾値
            equal (bool, optional): True にすると, "より大きい" が "以上" になる. Defaults to False.
            default (int, optional): x より大きい整数が存在しない場合の返り値. Defaults to None.

        Returns:
            int: _description_
        """
        x ^= self.lazy_xor
        if equal:
            x -= 1

        beta = self.more_count(x, False)
        if beta == 0:
            return default
        else:
            return self.kth_element(-beta, 0)

    def kth_element(self, k: int, default: int = None) -> int:
        """ 昇順 k 番目を求める.

        Args:
            k (int): 番号
            default (int, optional): k 番目が存在しない場合の返り値. Defaults to None.

        Returns:
            int: 昇順 k 番目の要素
        """
        if k < 0:
            k += len(self)

        if not (0 <= k < len(self)):
            return default

        v = 0
        res = 0
        for i in reversed(range(self.bit)):
            lc = self.arc[2 * v]
            rc = self.arc[2 * v + 1]

            if (self.lazy_xor >> i) & 1:
                lc, rc = rc, lc

            if lc == -1:
                v = rc
                res |= 1 << i
            elif self.size[lc] <= k:
                k -= self.size[lc]
                v = rc
                res |= 1 << i
            else:
                v = lc
        return res

    @property
    def min(self) -> int:
        return self.kth_element(0)

    @property
    def max(self) -> int:
        return self.kth_element(-1)

    def __getitem__(self, index: int) -> int:
        return self.kth_element(index)
