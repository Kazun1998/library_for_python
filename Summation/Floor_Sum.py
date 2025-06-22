class Floor_Sum:
    @staticmethod
    def floor_sum(A: int, B: int, M: int, N: int) -> int:
        """ sum_{i=0}^{N-1} floor((A * i + B) / M) を求める

        Args:
            A (int)
            B (int)
            M (int)
            N (int)

        Returns:
            int
        """

        total = 0
        while True:
            total += ((N - 1) * N // 2) * (A // M)
            A %= M

            total += N * (B // M)
            B %= M

            y = (A * N + B) // M
            x = B - y * M

            if y == 0:
                return total

            total += (N + x // A) * y
            A, B, M, N = M, x % A, A, y

    @classmethod
    def floor_sum_interval(cls, A: int, B: int, M: int, L: int, R: int) -> int:
        """ sum_{i=L}^R floor((A * i + B) / M) を求める

        Args:
            A (int)
            B (int)
            M (int)
            L (int)
            R (int)

        Returns:
            int
        """

        return cls.floor_sum(A, A * L + B, M, R - L + 1)

def Min_of_Mod_of_Linear(A: int, B: int, M: int, N: int) -> int:
    """ min { (A x + B) mod M | 0 <= x < N } を求める.

    Args:
        A (int):
        B (int):
        M (int):
        N (int):

    Returns:
        int: min { (A x + B) mod M | 0 <= x < N }
    """

    L = 0
    R = M

    target = Floor_Sum.floor_sum(A, B, M, N)
    while R - L > 1:
        X = (L + R) // 2
        if target == Floor_Sum.floor_sum(A, B - X, M, N):
            L = X
        else:
            R = X
    return L
