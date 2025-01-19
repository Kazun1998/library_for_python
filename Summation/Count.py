class Sum_Count:
    @staticmethod
    def box_sum(p: int, q: int, r: int, s: int, k: int) -> int:
        """ p <= x <= q, r <= y <= s, x + y = k を満たす整数の組 (x, y) の数を求める.

        Args:
            p (int):
            q (int):
            r (int):
            s (int):
            k (int):

        Returns:
            int: 組の数
        """

        a = max(0, k - (p     + r    ) + 1)
        b = max(0, k - (q + 1 + r    ) + 1)
        c = max(0, k - (p     + s + 1) + 1)
        d = max(0, k - (q + 1 + s + 1) + 1)
        return a - b - c + d

    @staticmethod
    def interval_sum(l: int, r: int, a: int, b: int) -> int:
        """ l <= x <= y, l <= x <= r, a <= x + y <= b を満たす整数の組 (x, y) の数を求める.

        Args:
            l (int):
            r (int):
            a (int):
            b (int):

        Returns:
            int: 組の数
        """
        if not(l <= r and a <= b):
            return 0

        a = max(a, 2 * l)
        b = min(b, 2 * r)

        if not(2 * l <= b and a <= 2 * r):
            return 0

        linear_sum = lambda a, b, l, r: (a * (l + r) + 2 *b) * (r - l + 1) // 2

        if a <= l + r < b:
            return linear_sum(1, - 2 * l + 1, a, l + r) + linear_sum(-1 ,2 * r + 1, l + r + 1, b)
        else:
            if b <= l + r:
                return linear_sum(1, - 2 * l + 1, a, b)
            else:
                return linear_sum(-1, 2 * r + 1, a, b)

    @staticmethod
    def range_sum_dp(ranges, S: int, Mod: int = None):
        """ ranges = [(a_0, b_0), (a_1, b_1), ..., (a_{N-1}, b_{N-1})] としたとき,
        a_i <= x_i <= b_i, x_0 + x_1 + ... + x_{N-1} = y を満たす整数の組の数を y = 0, 1, ..., S に対して求める.
        (Mod が None でないときは, 組の数を Mod で割った余り.)

        Args:
            ranges: (a, b) の形のタプル
            S (int): 上限
            Mod (int, optional): 法. Defaults to None.
        """

        dp = [0] * (S + 1); dp[0] = 1
        prev_cum = [0] * (S + 1)

        for a, b in ranges:
            # dp の累積和を取る
            prev_cum[0] = dp[0]
            for x in range(1, S + 1):
                prev_cum[x] = prev_cum[x - 1] + dp[x]

            if Mod is not None:
                for x in range(S):
                    prev_cum[x] %= Mod

            for x in range(S + 1):
                if x < a:
                    dp[x] = 0
                elif x <= b:
                    dp[x] = prev_cum[x - a]
                else:
                    dp[x] = prev_cum[x - a] - prev_cum[x - b - 1]

        if Mod is None:
            return dp
        else:
            return [y % Mod for y in dp]
