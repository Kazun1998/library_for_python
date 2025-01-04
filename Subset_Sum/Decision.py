class Decision_Subset_Sum:
    @staticmethod
    def zero_one_dp(A: list[int], S: int) -> list[bool]:
        dp = [False] * (S + 1); dp[0] = 1

        for a in A:
            for y in range(S, a - 1, -1):
                dp[y] |= dp[y - a]
        return dp

    @classmethod
    def plus_minus_dp(cls, A: list[int], S: int) -> bool:
        B = list(map(abs, A))
        K = S + sum(A)
        return (K >= 0) and (K % 2 == 0) and cls.zero_one_dp(B, K // 2)[-1]
