# [Note]
# 自然数全体の集合 N において, 加法と F_2 とのスカラー倍を
#   (和) x + y := x xor y
#   (スカラー倍) [0] x:=0, [1] x:=x
# と定めると, N は F_2 上のベクトル空間になる.
#
# ただし, 実用上は, ある非負整数 k を用いて 2^k 未満の自然数全体の集合を V_k として空間を扱う.
# この V_k は N の部分空間である.

class XOR_Vector_Space:
    def __init__(self, *vectors: int):
        """ vectors からなる XOR ベクトル空間を生成する.
        """

        self.basis: list[int] = []
        self.add_vector(*vectors)
        self.reduction()

    def __contains__(self, x: int) -> bool:
        for v in self.basis:
            x = min(x, x ^ v)
        return x == 0

    def __add__(self, other: "XOR_Vector_Space") -> "XOR_Vector_Space":
        """ ベクトル空間の和を求める.

        Args:
            other (XOR_Vector_Space): ベクトル空間

        Returns:
            XOR_Vector_Space: 和空間
        """

        return XOR_Vector_Space(*(self.basis + other.basis))

    def add_vector(self, *T: int):
        for x in T:
            if (y := self.projection(x)):
                self.basis.append(y)

    def dimension(self) -> int:
        """ 次元を求める.

        Returns:
            int: 次元
        """

        return len(self.basis)

    def reduction(self):
        S = self.basis
        for i in range(len(S)):
            vb = S[i] & (-S[i])
            for j in  range(len(S)):
                if (j != i) and (S[j] & vb):
                    S[j] ^= S[i]
        self.basis = [s for s in S if s]

    def projection(self, x: int) -> int:
        """ ベクトル空間への x の射影を求める.

        Args:
            x (int):

        Returns:
            int: 射影の結果
        """
        for v in self.basis:
            x = min(x, x ^ v)
        return x

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(map(str, self.basis))})"

    def is_subspace(self, V: "XOR_Vector_Space") -> bool:
        """ V の部分空間か?

        Args:
            V (XOR_Vector_Space): XOR ベクトル空間

        Returns:
            bool: 部分空間 ?
        """

        return all(u in V for u in self.basis)

    def __le__(self, other: "XOR_Vector_Space") -> bool:
        return self.is_subspace(other)

    def __ge__(self,other):
        return other<=self

    def __eq__(self,other):
        return (self <= other) and self.dimension() == other.dimension()
