class Find_Subset_Sum:
    @staticmethod
    def zero_one_dp(A: list[int], S: int) -> list[int] | None:
        """ 動的計画法で求める: sum(T[i] * A[i]) = S となる 01 列 T が存在するならば, その例を求める.\n
        計算量 O(|A| S)

        Args:
            A (list[int]): 元となる数列
            S (int): 目標となる合計

        Returns:
            list[int] | None: 存在するならば, そのような 01 列の例, 存在しないならば, None
        """

        N = len(A)
        dp = [None for _ in range(N + 1)]
        dp[0] = [1] + [0] * S

        for i, a in enumerate(A, 1):
            dp_i = dp[i] = (dp_prev := dp[i - 1]).copy()

            for x in range(S, a - 1, -1):
                dp_i[x] = dp_prev[x] | dp_prev[x - a]
            for x in range(a - 1, -1, -1):
                dp_i[x] = dp_prev[x]

        if not dp[N][S]:
            return None

        signs = []
        pointer = S
        for i, a in reversed(list(enumerate(A, 1))):
            dp_prev = dp[i - 1]
            if (pointer >= a) and dp_prev[pointer - a]:
                signs.append(1)
                pointer -= a
            else:
                signs.append(0)

        signs.reverse()
        return signs

    @classmethod
    def plus_minus_dp(cls, A: list[int], S: int) -> list[int] | None:
        """ 動的計画法で求める: sum(T[i] * A[i]) = S となる +- 列 T が存在するならば, その例を求める.\n
        計算量 O(|A| S)

        Args:
            A (list[int]): 元となる数列
            S (int): 目標となる合計

        Returns:
            list[int] | None: 存在するならば, そのような +- 列の例, 存在しないならば, None
        """

        p = [1 if a >= 0 else -1 for a in A]
        B = list(map(abs, A))

        K = S + sum(B)
        if (K < 0) or (K % 2 == 1):
            return None

        signs = cls.zero_one_dp(B, K // 2)
        if signs is not None:
            return [p[i] * (2 * s - 1) for i, s in enumerate(signs)]
        else:
            return None

    @staticmethod
    def zero_one_middle(A: list[int], S: int) -> list[int] | None:
        N = len(A)
        X = A[:N//2]; Y = A[N//2:]

        def bit(X, k):
            return (X >> k) & 1

        def enumerate_sum(B):
            N = len(B)
            E = {}
            for S in range(1 << N):
                S_copy = S
                res = 0
                for i in range(N):
                    res += B[i] if S & 1 else 0
                    S >>= 1
                E[res] = S_copy
            return E

        E = enumerate_sum(X)
        F = enumerate_sum(Y)
        for f, Q in F.items():
            if (e := S - f) not in E:
                continue

            P = E[e]
            return [bit(P, k) for k in range(len(X))] + [bit(Q, l) for l in range(len(Y))]

        return None

    @classmethod
    def plus_minus_middle(cls, A: list[int], S: int) -> list[int] | None:
        K = S + sum(A)
        if K % 2 == 1:
            return None

        if (P := cls.zero_one_middle(A, K // 2)) is None:
            return None

        return [1 if p else -1 for p in P]
