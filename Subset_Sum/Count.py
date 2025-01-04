class Count_Sumset_Sum:
    @staticmethod
    def zero_one_dp(A: list, S: int, Mod: int = None) -> list[int]:
        """ A の多重部分集合のうち, 合計が 0,1,...,S になるものの数 (を Mod で割った余り) を求める (取り出す要素が異なれば別のものとみなす).

        Args:
            A (list): 多重集合
            S (int): 目標となる合計
            Mod (int, optional): 割る余り. Defaults to None.

        Returns:
            list[int]: 長さ (S+1) の配列. 第 k~(0 <= k <= S) 項には, 合計が k になる多重部分集合の数が格納されている.
        """

        dp = [0] * (S + 1); dp[0] = 1

        for a in A:
            for x in range(S, a - 1, -1):
                dp[x] += dp[x - a]

            if Mod is None:
                continue

            for x in range(a, S + 1):
                dp[x] %= Mod

        return dp

    @classmethod
    def plus_minus_dp(cls, A: list, S: int, Mod: int = None) -> list[int]:
        """ A の多重部分集合のうち, 合計が 0,1,...,S になるものの数 (を Mod で割った余り) を求める (取り出す要素が異なれば別のものとみなす).

        Args:
            A (list): 多重集合
            S (int): 目標となる合計
            Mod (int, optional): 割る余り. Defaults to None.

        Returns:
            list[int]: 長さ (S+1) の配列. 第 k~(0 <= k <= S) 項には, 合計が k になる多重部分集合の数が格納されている.
        """

        A = list(map(abs, A))
        K = S + sum(A)
        if (K < 0) or (K % 2 == 1):
            return 0

        return cls.zero_one_dp(A, K // 2, Mod)[-1]
