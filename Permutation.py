class Permutation:
    __slots__ = ('_n', '__p', '__ind')

    def __init__(self, p: list[int] = None):
        """ N 要素の置換を生成する.

        Args:
            p (list[int], optional): 初期状態. None のときは恒等置換になる. Defaults to None.
        """

        if p is None:
            p = list(range(n))

        n = len(p)
        ind = [0] * n

        for i in range(n):
            ind[p[i]] = i

        self.__p = p
        self.__ind = ind
        self._n = n

    @property
    def N(self) -> int:
        return self._n

    def __getitem__(self, k: int) -> int:
        return self.__p[k]

    def __str__(self) -> str:
        return str(self.__p)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.p})"

    def __eq__(self, other: "Permutation") -> bool:
        return (self.N == other.N) and (self.__p == other.__p)

    def __iter__(self):
        return iter(self.__p)

    def __len__(self) -> int:
        return self.N

    def index(self, x: int) -> int:
        return self.__ind[x]

    def __mul__(self, other: "Permutation") -> "Permutation":
        assert self.N == other.N

        p = self.__p
        q = other.__p
        return Permutation([p[q[i]] for i in range(self.N)])

    def __pow__(self, k: int) -> "Permutation":
        if k < 0:
            return pow(self, -k).inverse()

        N = len(self)
        a = list(range(N))
        e = self.__p[:]

        while k:
            if k & 1:
                a = [a[e[i]] for i in range(N)]
            e = [e[e[i]] for i in range(N)]
            k >>= 1

        return Permutation(a)

    def sgn(self) -> int:
        """ 置換の符号を求める

        Returns:
            int: 偶置換ならば +1, 奇置換ならば -1
        """

        return -1 if self.minimum_transposition() % 2 else 1

    def inverse(self) -> "Permutation":
        """ 逆置換を求める.

        Returns:
            Permutation: 逆置換
        """

        return Permutation(self.__ind)

    def inversion(self) -> int:
        """ 転倒数を求める.

        Returns:
            int: 転倒数
        """

        BIT = [0] * (len(self) + 1)
        y = (self.N * (self.N - 1)) // 2

        for a in self.__p:
            s = a
            while 1 <= s:
                y -= BIT[s]
                s -= s & (-s)

            r = a + 1
            while r <= self.N:
                BIT[r] += 1
                r += r & (-r)
        return y

    def swap(self, i: int, j: int):
        """ i 番目と j 番目を交換する (※ i と j を交換ではない)

        Args:
            i (int):
            j (int):
        """

        u=self.__p[i]; v=self.__p[j]

        self.__p[i]=v; self.__p[j]=u
        self.__ind[v]=i; self.__ind[u]=j

    def transposition(self, u: int, v: int):
        """ u と v を交換する (※ u 番目と v 番目ではない)

        Args:
            u (int):
            v (int):
        """

        a=self.__ind[u]; b=self.__ind[v]

        self.__p[a]=v; self.__p[b]=u
        self.__ind[u]=b; self.__ind[v]=a

    def minimum_transposition(self) -> int:
        """ 互換の最小回数を求める.

        Returns:
            int: 互換の最小回数
        """

        return len(self) - len(self.cycle_division())

    def cycle_division(self, self_loop = True) -> list[list[int]]:
        """ 置換を巡回置換の積に分解する.

        Args:
            self_loop (bool, optional): 長さ 1 の自己ループを入れるかどうか. Defaults to True.

        Returns:
            list[list[int]]: 各要素がサイクルになる.
        """

        N = len(self)
        p = self.__p
        seen = [False] * N
        cycles: list[list[int]] = []

        for k in range(N):
            if seen[k]:
                continue

            cycle = [k]
            seen[k] = True
            v = k

            while (v := p[v]) != k:
                seen[v] = True
                cycle.append(v)

            if self_loop or len(cycle)>=2:
                cycles.append(cycle)

        return cycles

    def operate_list(self, list):
        assert self.N==len(list),"置換の長さとリストの長さが違います."

        return [list[self.__ind[i]] for i in range(self.N)]


    def order(self, mod: int = None) -> int:
        """ 位数を求める (mod を指定すると, mod で割った余りになる).

        Args:
            mod (int, optional): 指定すると, 出力が mod で割った余りになる. Defaults to None.

        Returns:
            int: 位数
        """

        if mod is None:
            from math import lcm
            x = 1
            for cycle in self.cycle_division():
                x = lcm(x, len(cycle))
            return x

        def factor(n):
            e = (n & (-n)).bit_length() - 1
            yield 2, e

            n >>= e

            p = 3
            while p * p <= n:
                if n % p == 0:
                    e = 0
                    while n % p == 0:
                        n //= p
                        e += 1
                    yield p, e
                p += 2

            if n > 1:
                yield n, 1

        power = {}
        for cycle in self.cycle_division():
            for p, e in factor(len(cycle)):
                power[p] = max(power.get(p, 0), e)

        x=1
        for p, e in power.items():
            x *= pow(p, e, mod)
            x %= mod
        return x

    def conjugate(self) -> "Permutation":
        """ 共役の互換を求める.

        Returns:
            Permutation: 共役の互換
        """

        N = len(self)
        return Permutation([N - 1 - x for x in self.__p])

    def next(self):
        p = self.__p
        y = []
        for i in range(self.N - 1, 0, -1):
            y.append(p[i])
            if p[i - 1] < p[i]:
                y.append(p[i - 1])
                a = p[i - 1]
                break

        x=p[:i - 1]
        y.sort()
        for j, b in enumerate(y):
            if a < b:
                x.append(b)
                del y[j]
                break

        return Permutation(x + y)

    def is_identity(self) -> bool:
        """ 恒等置換 ?

        Returns:
            bool: 恒等置換 ?
        """

        return all(self.__p[i] == i for i in range(self.N))

#=================================================
def Permutation_Inversion(P: Permutation, Q: Permutation) -> int:
    """ P から Q へ隣接項同士の入れ替えのみの最小回数を求める.

    Args:
        P (Permutation): 起点となる置換
        Q (Permutation): 目標となる置換

    Returns:
        int: 隣接項同士の入れ替えのみの最小回数
    """

    return (Q*(P.inverse())).inversion()

def List_Inversion(A: list, B: list, default = None) -> int:
    """ 長さが等しいリスト A,B に対して, 以下の操作の最小回数を求める.
    列 A[i] と A[i+1] を入れ替え, B と一致させる.

    Args:
        A (list):
        B (list):
        default: 不可能な場合の返り値. Defaults to None.

    Raises:
        ValueError: A, B の長さが異なると発生

    Returns:
        int: 入れ替え回数の最小値. 不可能な場合は default
    """
    from collections import defaultdict

    if len(A) != len(B):
        raise ValueError(f'A, B の長さが異なります. (len(A) = {len(A)}, len(B) = {len(B)})')

    N = len(A)
    D = defaultdict(list)

    for i in range(N):
        D[A[i]].append(i)

    for key in D:
        D[key].reverse()

    try:
        return Permutation([D[B[i]].pop() for i in range(N)]).inversion()
    except:
        return default

#=================================================
def Random_Permutation(N: int) -> Permutation:
    """ 長さ N の置換をランダムに生成する.

    Args:
        N (int): 長さ

    Returns:
        Permutation: 長さ N の置換
    """

    from random import shuffle
    p = list(range(N))
    shuffle(p)
    return Permutation(p)

def Generate_Permutation(P: list[int], Q: list[int]) -> Permutation:
    """ P から Q に変換する置換を生成する.

    Args:
        P (list[int]):
        Q (list[int]):

    Raises:
        ValueError: P, Q の長さが異なる場合に発生

    Returns:
        Permutation: P から Q に変換する置換
    """

    if len(P) != len(Q):
        raise ValueError

    N = len(P)
    X = [-1]*N
    for i in range(N):
        X[P[i]] = Q[i]
    return Permutation(X)
