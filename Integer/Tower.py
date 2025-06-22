def Power_Tower(tower: list[int], m: int) -> int:
    def mod(a, m):
        return a if a < 2 * m else a % m + m

    def mul(a, b, m):
        return mod(a * b, m)

    def power(a, k, m):
        res = 1
        while k:
            if k & 1:
                res = mul(res, a, m)
            a = mul(a, a, m)
            k >>= 1
        return res

    def totient(x):
        if x == 1:
            return 1

        phi = 1
        def calc(p):
            nonlocal x, phi

            if not(x % p == 0 and p != 1):
                return

            e = 0
            while x % p == 0:
                e += 1
                x //= p

            phi *= (p - 1) * pow(p, e - 1)

        calc(2); calc(3)

        parity = 0; p = 5
        while p * p <= x:
            calc(p)
            p += 4 if parity else 2
            parity ^= 1
        calc(x)
        return phi

    nest_totients = [m]
    for _ in range(len(tower) - 1):
        nest_totients.append(totient(nest_totients[-1]))

    while len(tower) > 1:
        k = mod(tower.pop(), nest_totients.pop())
        tower[-1] = power(tower[-1], k, nest_totients[-1])

    return tower[0] % m

def Tetoration(a: int, k: int, m: int) -> int:
    """ a^(a^(a^(...^a))) (k 個の累乗タワー) を m で割った余りを求める

    Args:
        a (int): 底 (a >= 0)
        k (int): a を重ねる数 (k >= 0)
        m (int): 剰余 (m >= 1)

    Returns:
        int: テトレーションを m で割った余り
    """

    assert a >= 0
    assert k >= 0
    assert m >= 1

    # 例外ケースの処理
    if k == 0:
        return 1 % m
    elif a == 0:
        return 1 % m if k % 2 == 0 else 0

    k = min(k, (m - 1).bit_length() + 1)
    return Power_Tower([a] * k, m)
