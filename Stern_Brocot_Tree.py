class Stern_Brocot_Tree:
    @staticmethod
    def encode(a: int, b: int, left = 'L', right = 'R'):
        path = []
        q, r = divmod(a, b)
        if q > 0:
            path.append((right, q))

        a, b = b, r
        parity = True
        while b:
            q, r = divmod(a, b)
            path.append((left if parity else right, q))
            a, b = b, r
            parity ^= True

        direction, k = path.pop()
        if k > 1:
            path.append((direction, k - 1))
        return path

    @staticmethod
    def decode_interval(code, left = 'L', right = 'R'):
        p, q, r, s = 0, 1, 1, 0
        for direction, k in code:
            if direction == left:
                r += k * p
                s += k * q
            elif direction == right:
                p += k * r
                q += k * s
        return (p, q, r, s)


    @classmethod
    def decode(cls, code, left = 'L', right = 'R'):
        p, q, r, s = cls.decode_interval(code, left, right)
        return (p + r, q + s)

    @classmethod
    def lowest_common_ancestor(cls, a: int, b: int, c:int, d:int):
        if (a, b) == (1, 1) or (c, d) == (1, 1):
            return (1, 1)

        code_1 = cls.encode(a, b)
        code_2 = cls.encode(c, d)
        if code_1[0][0] != code_2[0][0]:
            return (1, 1)

        lca_code = []
        for ((t, k), (_, l)) in zip(code_1, code_2):
            lca_code.append((t, min(k, l)))
            if k != l:
                break
        return cls.decode(lca_code)

    @classmethod
    def depth(cls, a: int, b: int):
        code = cls.encode(a, b)
        return sum(k for _, k in code)

    @classmethod
    def ancestor(cls, a: int, b: int, k: int, default = None):
        code = []
        for direction, l in cls.encode(a, b):
            l = min(k, l)
            code.append((direction, l))
            k -= l
            if k == 0:
                return cls.decode(code)
        else:
            return default

    @classmethod
    def range(cls, a: int, b: int):
        return cls.decode_interval(cls.encode(a, b))

class Stern_Brocot_Tree_Node:
    def __init__(self):
        pass

print(Stern_Brocot_Tree.ancestor(1000000000, 1, 300))
