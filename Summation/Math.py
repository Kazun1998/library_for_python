class Sum:
    @staticmethod
    def linear(a: int, b: int, l: int, r: int) -> int:
        """ sum_{k=l}^r (a k + b) を求める

        Args:
            a (int): 1 次の項
            b (int): 定数項
            l (int):
            r (int):

        Returns:
            int: 総和
        """

        return (a * (l + r) + 2 * b) * (r - l + 1) // 2 if l <= r else 0

    @classmethod
    def max_linear(cls, a: int, b: int, c: int, d: int, l: int, r: int) -> int:
        """ sum_{k = l}^r max(a k + b, c k + d) を求める.

        Args:
            a (int):
            b (int):
            c (int):
            d (int):
            l (int):
            r (int):

        Returns:
            int:
        """

        if l > r:
            return 0

        if a == c:
            return cls.linear(a, max(b, d), l, r)

        if a < c:
            a, b, c, d = c, d, a, b

        if a * l + b > c * l + d:
            return cls.linear(a, b, l, r)
        elif a * r + b < c * r + d:
            return cls.linear(c, d, l, r)

        m = (d - b) // (a - c)
        return cls.linear(c, d, l, m) + cls.linear(a, b, m + 1, r)

    @classmethod
    def min_linear(cls, a: int, b: int, c: int, d: int, l: int, r: int):
        """ sum_{k = l}^r min(a k + b, c k + d) を求める.

        Args:
            a (int):
            b (int):
            c (int):
            d (int):
            l (int):
            r (int):

        Returns:
            int:
        """

        return -cls.max_linear(-a, -b, -c, -d, l, r)

    @classmethod
    def linear_lower_cut(cls, a: int, b: int, d: int, l: int, r: int) -> int:
        """ sum_{k=l}^r max(ak+b, d) を求める.

        Args:
            a (int):
            b (int):
            d (int):
            l (int):
            r (int):

        Returns:
            int:
        """

        return cls.max_linear(a, b, 0, d, l, r)

    @classmethod
    def linear_upper_cut(cls, a: int, b: int, u: int, l: int, r: int) -> int:
        """ sum_{k=l}^r min(ak+b, u) を求める.

        Args:
            a (int):
            b (int):
            d (int):
            l (int):
            r (int):

        Returns:
            int:
        """

        return cls.min_linear(a, b, 0, u, l, r)

    @classmethod
    def bound(cls, a: int, b: int, d: int, u: int, l: int, r: int) -> int:
        """ p[k]:=ak+b, q[k]:= u (u <= p[k]), d (d>=p[k]), p[k] (otherwise) としたとき, sum_{k = l}^r q[k] を求める.

        Args:
            a (int):
            b (int):
            d (int):
            u (int):
            l (int):
            r (int):

        Returns:
            int:
        """
        assert d <= u

        if l > r:
            return 0

        if a == 0:
            return max(d, min(b, u)) * (r - l + 1)

        X = 0
        if a > 0:
            s = (d - b + a -1) // a
            t = (u - b) // a

            if r < s:
                return d * (r - l + 1)
            elif t < l:
                return u * (r - l + 1)

            if l < s:
                X += d * (s - l)
                l = s
            if t < r:
                X += u * (r - t)
                r = t
        elif a < 0:
            a_abs = abs(a)
            s = (b - u + a_abs - 1) // a_abs
            t = (b - d) // a_abs

            if r < s:
                return u * (r - l + 1)
            elif t < l:
                return d * (r - l + 1)

            if l < s:
                X += u * (s - l)
                l = s
            if t < r:
                X += d * (r - t)
                r = t

        X += cls.linear(a, b, l, r)
        return X

#==================================================
#Sum_Count系
def Range_Sum_Inclusion(Range, S, Mod=None):
    """Range=[(A_0,B_0),...,(A_{N-1}, B_{N-1})] としとたき,
    A_i<=X_i<=B_i, X_0+...+X_{n-1}=S を満たす組の個数を包除原理で求める.

    0<=A_i<=B_i
    0<=S
    計算量: O(N2^N)
    """
    from itertools import product

    def nCr(n,r):
        if n<0: return 0
        if r<0 or n<r: return 0

        a=b=1
        r=min(r,n-r)

        while r:
            a*=n; b*=r

            if Mod!=None:
                a%=Mod; b%=Mod

            n-=1; r-=1

        if Mod!=None:
            return (a * pow(b, -1, Mod)) % Mod
        else:
            return a//b

    def nHr(n,r):
        if n==r==0:
            return 1
        else:
            return nCr(n+r-1,n-1)

    N=len(Range)
    X=0
    for p in product((0,1),repeat=N):
        T=S
        for i in range(N):
            a,b=Range[i]
            if p[i]:
                T-=b+1
            else:
                T-=a

        X+=pow(-1,sum(p))*nHr(N,T)

    if Mod==None:
        return X
    else:
        return X%Mod

#==================================================
#Find_Sum系
def Find_Range_Sum(Range, S):
    """Range=[(A_0,B_0),...,(A_{N-1}, B_{N-1})] としとたき,
    A_i<=X_i<=B_i, X_0+...+X_{n-1}=S を満たす組の例を1つ求める.

    A_i<=B_i
    """

    alpha=beta=0
    for a,b in Range:
        alpha+=a
        beta +=b

    if not (alpha<=S<=beta): return None

    N=len(Range)
    X=[a for a,_ in Range]
    remain=S-sum(X)
    for i in range(N):
        y=min(Range[i][1],X[i]+remain)
        remain-=y-X[i]
        X[i]=y
    return X
#==================================================
#幾何級数系

def Geometric_Sequence_Sum(r, n, Mod=None):
    """ sum_{i=0}^{n-1} r^i [(mod Mod)] """

    if Mod==None:
        if r==1: return n
        else: return (pow(r,n)-1)/(r-1)
    else:
        if r==1: return n%Mod
        else: return (pow(r,n,(r-1)*Mod)//(r-1))%Mod
