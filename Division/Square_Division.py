class Square_Division:
    def __init__(self, L, op, unit):
        self.op = op
        self.unit = unit

        self.N = N = len(L)
        self.bucket_size = int(pow(N, 0.5) + 1)
        self.bucket_number = (N - 1) // self.bucket_size + 1

        self.upper = [unit] * self.bucket_number
        self.lower = [unit] * self.bucket_number * self.bucket_size

        for i in range(N):
            self.lower[i] = L[i]

            t = i // self.bucket_size
            self.upper[t] = op(self.upper[t], self.lower[i])

    def update(self, k, x):
        """ 第 k 要素を x に変更する.

        Args:
            k (int): index
            x : value
        """

        self.lower[k] = x

        l = self.bucket_size * (k // self.bucket_size)
        r = l + self.bucket_size
        y = self.unit
        for i in range(l, r):
            y = self.op(y, self.lower[i])

        self.upper[k // self.bucket_size] = y

    def product(self, l, r, left_close = True, right_close = True):
        """ 第 l 項から第 r 項までの積を求める.

        Args:
            l (int): 左端
            r (int): 右端
        """

        if not left_close:
            l += 1

        if not right_close:
            r -= 1

        b = self.bucket_size
        op = self.op
        lower = self.lower
        upper = self.upper
        prod = self.unit

        if l // b == r // b:
            for i in range(l, r + 1):
                prod = op(prod, lower[i])
            return prod

        while l % b != 0:
            prod = op(prod, lower[l])
            l += 1

        while l + (b - 1) <= r:
            prod = op(prod, upper[l // b])
            l += b

        while l <= r:
            prod = op(prod, lower[l])
            l += 1

        return prod

    def __getitem__(self, k):
        return self.lower[k]
