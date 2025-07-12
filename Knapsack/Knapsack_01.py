class Knapsack_Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"value: {self.value}, weight: {self.weight}"

    __str__ = __repr__

class Knapsack_01:
    @classmethod
    def solve(cls, items, capacity):
        """ 01-Knapsack 問題を解く
        """

        from math import log2

        n = max(len(items), 1)
        cost_by_middle = n * log2(n)
        cost_by_weight = log2(n * max(capacity, 1))
        cost_by_value = log2(n * max(sum(item.value for item in items), 1))
        min_cost = min(cost_by_middle, cost_by_value, cost_by_weight)

        if min_cost == cost_by_middle:
            return cls.solve_small(items, capacity)
        elif min_cost == cost_by_weight:
            return cls.solve_weight(items, capacity)
        else:
            return cls.solve_value(items, capacity)

    @classmethod
    def solve_weight(_, items: list[Knapsack_Item], capacity: int):
        """ 各アイテムの重さが軽い場合の 01-Knapsack 問題を解く.

        Args:
            items (list[Knapsack_Item]): アイテムのリスト
            weight (int): ナップサックの容量
        """

        dp = [0] * (capacity + 1)
        for item in items:
            if item is None:
                continue

            for a in range(capacity, item.weight - 1, -1):
                dp[a] = max(dp[a], dp[a - item.weight] + item.value)

        packed_value = max(dp)
        packed_weight = dp.index(packed_value)
        knapsack = []
        for i, item in enumerate(items):
            if item is None:
                continue

            if (item.weight <= packed_weight) and (dp[packed_weight] == dp[packed_weight - item.weight] + item.value):
                knapsack.append(i)
                packed_weight -= item.weight

        return { 'value': packed_value, 'packed': knapsack }

    @classmethod
    def solve_value(_, items: list[Knapsack_Item], capacity: int):
        """ 各アイテムの価値が小さい 01-Knapsack 問題を解く.

        Args:
            items (list[Knapsack_Item]): アイテムのリスト
            weight (int): ナップサックの容量
        """

        value_sum = sum(item.value for item in items)
        dp = [capacity + 1] * (value_sum + 1)
        dp[0] = 0

        for item in items:
            if item is None:
                continue

            for a in range(value_sum, item.value - 1, -1):
                dp[a] = min(dp[a], dp[a - item.value] + item.weight)

        value = pointer = max(v for v in range(value_sum+ 1) if dp[v] <= capacity)
        knapsack = []
        for i, item in enumerate(items):
            if item is None:
                continue

            if dp[pointer] == dp[pointer - item.value] + item.weight:
                knapsack.append(i)
                pointer -= item.value

        return { 'value': value, 'packed': knapsack }

    @classmethod
    def __subset_sum(_, items: list[Knapsack_Item], capacity: int):
        def bit(x, k):
            return (x >> k) & 1

        memo = { }
        n = len(items)
        for E in range(1 << n):
            partial_value = 0
            partial_weight = 0

            for i in range(n):
                if bit(E, i) == 0:
                    continue

                partial_value += items[i].value
                partial_weight += items[i].weight

            if partial_weight > capacity:
                continue

            if partial_weight in memo:
                memoed_value, F = memo[partial_weight]
                if memoed_value <= partial_value:
                    memo[partial_weight] = (partial_value, F)
            else:
                memo[partial_weight] = (partial_value, E)

        champion_value = -1
        res = []
        for key in sorted(memo):
            value, E = memo[key]
            if value <= champion_value:
                continue

            res.append((value, key, E))
            champion_value = value
        return res

    @classmethod
    def __merge(cls, S, T, capacity):
        T.reverse()
        it = iter(T)
        v1, w1, F = next(it)

        t = 0
        E0 = 0
        F0 = 0

        for v, w, E in S:
            while w + w1 > capacity:
                v1, w1, F = next(it)

            if t < v + v1:
                t = v + v1
                E0 = E
                F0 = F

        return t, E0, F0

    @classmethod
    def solve_small(cls, items: list[Knapsack_Item], capacity: int):
        """ アイテムの個数が小さい 01-Knapsack 問題を解く.

        Args:
            items (list[Knapsack_Item]): アイテムのリスト
            capacity (int): ナップサックの容量

        Reference:
            https://tjkendev.github.io/procon-library/python/dp/knapsack-meet-in-the-middle.html
        """

        n = len(items)
        A = cls.__subset_sum(items[:n//2], capacity)
        B = cls.__subset_sum(items[n//2:], capacity)

        value, E, F  = cls.__merge(A, B, capacity)
        E_bit = [i for i in range(n // 2) if (E >> i) & 1 ]
        F_bit = [j for j in range(n // 2, n) if (F >> j) & 1]

        return { 'value': value, 'packed': E_bit + [f + n // 2 for f in F_bit] }
