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
