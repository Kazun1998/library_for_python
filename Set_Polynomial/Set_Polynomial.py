from itertools import zip_longest

class Set_Polynomial:
    __slots__ = ('poly', )

    def __init__(self, poly = []):
        n = max(len(poly), 1)
        if n & (-n) == n: # n が 2 ベキ
            N = n.bit_length() - 1
        else:
            N = n.bit_length()

        self.poly = [a % Mod for a in poly] + [0] * ((1<<N) - n)

    def __len__(self):
        return len(self.poly)

    def cardinality(self):
        return len(self.poly).bit_length() - 1

    def __str__(self):
        return str(self.poly)

    __repr__ = __str__

    def __getitem__(self, index):
        if 0 <= index < len(self):
            return self.poly[index]
        else:
            return 0

    def __iter__(self):
        yield from self.poly

    def __eq__(self, other):
        return all(a == b for a,b in zip_longest(self, other, fillvalue = 0))

    def __add__(self, other):
        return Set_Polynomial([a + b for a,b in zip_longest(self, other, fillvalue = 0)])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return Set_Polynomial([a - b for a,b in zip_longest(self, other, fillvalue = 0)])

    def __rsub__(self, other):
        return (- self) + other

    def __mul__(self, other):
        if other.__class__ == Set_Polynomial:
            N = self.cardinality(); M = other.cardinality()
            L = max(N, M)

            a = Set_Polynomial.__zeta_transform(self.poly + [0] * ((1 << M) - (1 << N)) )
            b = Set_Polynomial.__zeta_transform(other.poly + [0] * ((1 << N) - (1 << M)) )

            c = [0] * ((L + 1)  << L)
            popcount = Set_Polynomial.__popcount
            for S in range(1 << L):
                S_pop = popcount(S)
                for i in range(S_pop + 1):
                    for j in range(min(S_pop, L - i) + 1):
                        alpha = a[S * (L + 1) + i] * b[S * (L + 1) + j]
                        c[S * (L + 1) + (i + j)] = (c[S * (L + 1) + (i + j)] + alpha) % Mod
            return Set_Polynomial(Set_Polynomial.__mobius_transform(c))
        else:
            return self.scale(other)

    def __rmul__(self, other):
        return self * other

    @staticmethod
    def __popcount(n):
        c = (n & 0x5555555555555555) + ((n >> 1 ) & 0x5555555555555555)
        c = (c & 0x3333333333333333) + ((c >> 2 ) & 0x3333333333333333)
        c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4 ) & 0x0f0f0f0f0f0f0f0f)
        c = (c & 0x00ff00ff00ff00ff) + ((c >> 8 ) & 0x00ff00ff00ff00ff)
        c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
        c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
        return c

    @staticmethod
    def __zeta_transform(p):
        N = len(p).bit_length() - 1
        q = [0] * ((N + 1) * (1 << N))
        popcount = Set_Polynomial.__popcount
        for S in range(len(p)):
            q[S * (N + 1) + popcount(S)] = p[S]

        L = 1 << N
        for i in range(N):
            bit = 1 << i
            S = 0
            for _ in range(L >> 1):
                S |= bit
                T = S ^ bit
                for k in range(N + 1):
                    q[S * (N + 1) + k] += q[T * (N + 1) + k]
                S += 1
        return [qS % Mod for qS in q]

    @staticmethod
    def __mobius_transform(q):
        N = 0
        while ((N + 1) << N) < len(q):
            N += 1
        assert ((N + 1) << N) == len(q)

        L = 1 << N
        for i in range(N):
            bit = 1 << i
            S = 0
            for _ in range(L >> 1):
                S |= bit
                T = S ^ bit
                for k in range(N + 1):
                    q[S * (N + 1) + k] -= q[T * (N + 1) + k]
                S += 1

        popcount = Set_Polynomial.__popcount
        return [q[S * (N + 1) + popcount(S)] % Mod for S in range(1 << N)]

    def scale(self, r):
        return Set_Polynomial([(r * a) % Mod for a in self])

#==================================================
Mod = 998244353
