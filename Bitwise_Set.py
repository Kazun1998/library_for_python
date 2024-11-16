class Bitwise_Set:
    @staticmethod
    def emptyset(n):
        """ {0, 1, ..., n} の部分集合で空集合を表す整数を求める (要するに 0).
        """

        return 0

    @staticmethod
    def universal_set(n):
        """ {0, 1, ..., n} を表す整数を求める.
        """

        return (1 << n) - 1

    @classmethod
    def subset_yield(cls, S, _):
        """ S の部分集合のジェネレータを作成する.
        """

        T = S
        while True:
            yield T
            if T == 0:
                break

            T = (T - 1) & S

    @classmethod
    def betweenset_yield(cls, S, T):
        """ S subset U subset T を満たす集合 U のジェネレータを作成する.
        """

        if S | T != T:
            return

        for V in cls.subset_yield(T ^ S, 0):
            yield S | V

    @classmethod
    def superset_yield(cls, S, n):
        """ S の上位集合のジェネレータを作成する.
        """

        yield from cls.betweenset_yield(S, cls.universal_set(n))

    @classmethod
    def build(cls, E):
        """ 集合 E を表す整数を返す.
        """

        return sum(1 << k for k in E)

    @classmethod
    def bit(cls, A, k):
        return (A >> k) & 1

    @classmethod
    def add(cls, A, k):
        return A | (1 << k)

    @classmethod
    def remove(cls, A, k):
        return A & (~ (1 << k))

    @classmethod
    def switch(cls, A, k):
        return A ^ (1 << k)

    @classmethod
    def popcount(cls, A: int):
        return A.bit_count()

    @classmethod
    def get_min(self, A: int):
        return (A & (-A)).bit_length() - 1
