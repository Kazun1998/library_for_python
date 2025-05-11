"""
変数 X_i の否定は ~i で宣言する.
例えば, ~0=-1 なので, X_{-1} は not X_0 を意味する.
"""

class Two_SAT:
    def __init__(self, N: int = 0):
        """ N 変数の 2-SAT を定義する.

        Args:
            N (int, optional): 変数の数. Defaults to 0.
        """

        self.N = N
        self.var_num = N

        self.arc: list[int] = [[] for _ in range(2 * N)]
        self.rev: list[int] = [[] for _ in range(2 * N)]

    def __var_to_index(self, v: int) -> int:
        """ 反転の情報を含んだ変数番号から, arc, rev におけるインデックスを求める.

        Args:
            v (int): 反転の情報を含んだ変数番号

        Returns:
            int: インデックス
        """

        return 2 * v if v >= 0 else 2 * (-v - 1) + 1

    def add_variable(self, k: int = 1) -> list[int]:
        """ 新たに k 個の変数を追加する

        Args:
            k (int, optional): 追加する変数の数. Defaults to 1.

        Returns:
            list[int]: 追加された変数の頂点番号のリスト
        """

        m = self.var_num
        self.var_num += k

        self.arc.extend([[] for _ in range(2*k)])
        self.rev.extend([[] for _ in range(2*k)])

        return list(range(m, m + k))

    def __add_clause(self,i,j):
        self.arc[self.__var_to_index(i)].append(self.__var_to_index(j))
        self.rev[self.__var_to_index(j)].append(self.__var_to_index(i))

    def add_imply(self, i: int, j: int):
        """ X_i -> X_j を追加する.

        Args:
            i (int): 変数番号
            j (int): 変数番号
        """

        self.__add_clause(i, j)
        self.__add_clause(~j, ~i)

    def add_or(self, i: int, j: int):
        """ X_i or X_j を追加する.

        Args:
            i (int): 変数番号
            j (int): 変数番号
        """

        self.add_imply(~i, j)

    def add_nand(self, i: int, j: int):
        """ not(X_i and X_j) を追加する

        Args:
            i (int): 変数番号
            j (int): 変数番号
        """

        self.add_imply(i, ~j)

    def add_equal(self, i: int, j: int):
        """ X_i = X_j を追加する.

        Args:
            i (int): 変数番号
            j (int): 変数番号
        """

        self.add_imply(i, j)
        self.add_imply(~i, ~j)

    def add_not_equal(self, i: int, j: int):
        """ X_i != X_j を追加する.

        Args:
            i (int): 変数番号
            j (int): 変数番号
        """

        self.add_equal(i, ~j)

    def add_equivalent(self, *I: int):
        """ I = [i_0, ..., i_{k-1}] に対して, X_{i_0} = ... = X_{i_{k-1}} を追加する.

        Args:
            I (int): 変数番号たち
        """

        if len(I) <= 1:
            return

        for j in range(len(I) - 1):
            self.add_imply(I[j], I[j + 1])

        self.add_imply(I[-1],I[0])

    def set_true(self, i: int):
        """ 変数 X_i を True にする.

        Args:
            i (int): 変数番号
        """

        self.__add_clause(~i, i)

    def set_false(self, i: int):
        """ 変数 X_i を False にする.

        Args:
            i (int): 変数番号
        """

        self.__add_clause(i, ~i)

    def at_most_one(self, *I: int):
        """X_i (i in I) を満たすような i は高々1つだけという条件を追加する.

        Args:
            I (int): 変数番号の配列
        """

        # k = 1 のときの条件は無意味
        if (k := len(I)) <= 1:
            return

        A = self.add_variable(k)

        self.add_imply(I[0], A[0])
        for i in range(1, k):
            self.add_imply(A[i - 1], A[i])
            self.add_imply(I[i], A[i])
            self.add_nand(A[i - 1],I[i])

    def calculate(self):
        n = self.var_num
        group = [0] * (2 * n)
        order = []

        for s in range(2 * n):
            if group[s]:
                continue

            stack = [s]
            group[s] = -1

            while stack:
                u = stack.pop()
                for v in self.arc[u]:
                    if group[v]:
                        continue

                    group[v] = -1

                    stack.append(u)
                    stack.append(v)
                    break
                else:
                    order.append(u)

        k = 0
        for s in reversed(order):
            if group[s] != -1:
                continue

            stack = [s]
            group[s] = k

            while stack:
                u = stack.pop()
                for v in self.rev[u]:
                    if group[v] != -1:
                        continue

                    group[v] = k
                    stack.append(v)
            k += 1

        ans = [None] * n
        for i in range(n):
            if group[2 * i] > group[2 * i + 1]:
                ans[i] = True
            elif group[2 * i] < group[2 * i + 1]:
                ans[i] = False
            else:
                self.__satisfiability = False
                self.__ans = None
                self.__self_contradiction = []
                return
        else:
            self.__satisfiability = True
            self.__ans = ans
            self.__self_contradiction = [i for i in range(self.var_num) if group[2 * i] == group[2 * i + 1]]

    @property
    def is_satisfiable(self):
        return self.__satisfiability

    @property
    def ans(self):
        return self.__ans

    @property
    def self_contradiction(self):
        return self.__self_contradiction
