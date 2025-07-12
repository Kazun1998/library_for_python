---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Math/Discrete_Log.test.py
    title: test_verify/yosupo_library_checker/Math/Discrete_Log.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Math/Sqrt_Mod.test.py
    title: test_verify/yosupo_library_checker/Math/Sqrt_Mod.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Modulo:\n    __slots__ = (\"_a\", \"_n\")\n\n    @property\n    def\
    \ a(self) -> int:\n        return self._a\n\n    @property\n    def n(self) ->\
    \ int:\n        return self._n\n\n    def __init__(self, a: int, n: int, mode:\
    \ bool = True):\n        if mode:\n            a %= n\n\n        self._a = a\n\
    \        self._n = n\n\n    def __str__(self) -> str:\n        return f\"{self.a}\
    \ (mod {self.n})\"\n\n    def __repr__(self) -> str:\n        return f\"{self.__class__.__name__}({self.a},\
    \ {self.n})\"\n\n    #+,-\n    def __pos__(self) -> \"Modulo\":\n        return\
    \ self\n\n    def __neg__(self) -> \"Modulo\":\n        return Modulo(self.n -\
    \ self.a, self.n, False) if self.a else Modulo(0, self.n, False)\n\n    #\u7B49\
    \u53F7,\u4E0D\u7B49\u53F7\n    def __eq__(self, other: \"Modulo\") -> bool:\n\
    \        if isinstance(other, Modulo):\n            return (self.a == other.a)\
    \ and (self.n == other.n)\n        elif isinstance(other, int):\n            return\
    \ (self.a - other) % self.n == 0\n\n    def __neq__(self, other: \"Modulo\") ->\
    \ bool:\n        return not(self == other)\n\n    def __le__(self, other: \"Modulo\"\
    ) -> bool:\n        a, p = self.a, self.n\n        b, q = other.a, other.n\n \
    \       return (a - b) % q == 0 and p % q == 0\n\n    def __ge__(self, other:\
    \ \"Modulo\") -> bool:\n        return other <= self\n\n    def __lt__(self, other:\
    \ \"Modulo\") -> bool:\n        return (self <= other) and (self != other)\n\n\
    \    def __gt__(self, other: \"Modulo\") -> bool:\n        return (self >= other)\
    \ and (self != other)\n\n    def __contains__(self, val) -> bool:\n        return\
    \ val % self.n == self.a\n\n    #\u52A0\u6CD5\n    def __add__(self, other: \"\
    Modulo\") -> \"Modulo\":\n        if isinstance(other,Modulo):\n            assert\
    \ self.n==other.n, \"\u7570\u306A\u308B\u6CD5\u540C\u58EB\u306E\u6F14\u7B97\u3067\
    \u3059.\"\n            y=other.a\n        elif isinstance(other,int):\n      \
    \      y=other%self.n\n\n        b=self.a+y\n        if self.n<=b:\n         \
    \   b-=self.n\n        return Modulo(b,self.n, False)\n\n    def __radd__(self,\
    \ other: \"Modulo\") -> \"Modulo\":\n        if isinstance(other,int):\n     \
    \       b=self.a+(other%self.n)\n            if b>=self.n:\n                b-=self.n\n\
    \            return Modulo(b,self.n, False)\n\n    def __iadd__(self, other: \"\
    Modulo\") -> \"Modulo\":\n        if isinstance(other,Modulo):\n            assert\
    \ self.n==other.n, \"\u7570\u306A\u308B\u6CD5\u540C\u58EB\u306E\u6F14\u7B97\u3067\
    \u3059.\"\n            y=other.a\n        elif isinstance(other,int):\n      \
    \      y=other%self.n\n\n        self.a+=y\n        if self.a>=self.n:\n     \
    \       self.a-=self.n\n        return self\n\n    #\u6E1B\u6CD5\n    def __sub__(self,\
    \ other: \"Modulo\") -> \"Modulo\":\n        if isinstance(other,Modulo):\n  \
    \          assert self.n==other.n, \"\u7570\u306A\u308B\u6CD5\u540C\u58EB\u306E\
    \u6F14\u7B97\u3067\u3059.\"\n            y=other.a\n        elif isinstance(other,int):\n\
    \            y=other%self.n\n\n        b=self.a-y\n        if b<0:\n         \
    \   b+=self.n\n        return Modulo(b,self.n, False)\n\n    def __rsub__(self,\
    \ other: \"Modulo\") -> \"Modulo\":\n        if isinstance(other,int):\n     \
    \       b=other%self.n-self.a\n            if b<0:\n                b+=self.n\n\
    \            return Modulo(b,self.n, False)\n\n    def __isub__(self, other: \"\
    Modulo\") -> \"Modulo\":\n        if isinstance(other,Modulo):\n            assert\
    \ self.n==other.n, \"\u7570\u306A\u308B\u6CD5\u540C\u58EB\u306E\u6F14\u7B97\u3067\
    \u3059.\"\n            y=other.a\n        elif isinstance(other,int):\n      \
    \      y=other%self.n\n\n        self.a-=y\n        if self.a<0:\n           \
    \ self.a+=self.n\n        return self\n\n    #\u4E57\u6CD5\n    def __mul__(self,\
    \ other: \"Modulo\") -> \"Modulo\":\n        if isinstance(other,Modulo):\n  \
    \          assert self.n==other.n, \"\u7570\u306A\u308B\u6CD5\u540C\u58EB\u306E\
    \u6F14\u7B97\u3067\u3059.\"\n            y=other.a\n        elif isinstance(other,int):\n\
    \            y=other%self.n\n\n        return Modulo((self.a*y)%self.n, self.n,\
    \ False)\n\n    def __rmul__(self, other: \"Modulo\") -> \"Modulo\":\n       \
    \ if isinstance(other,int):\n            return Modulo((self.a*other)%self.n,\
    \ self.n, False)\n\n    def __imul__(self, other: \"Modulo\") -> \"Modulo\":\n\
    \        if isinstance(other,Modulo):\n            assert self.n==other.n, \"\u7570\
    \u306A\u308B\u6CD5\u540C\u58EB\u306E\u6F14\u7B97\u3067\u3059.\"\n            y=other.a\n\
    \        elif isinstance(other,int):\n            y=other%self.n\n\n        self.a*=y\n\
    \        self.a%=self.n\n        return self\n\n    #Modulo\u9006\u6570\n    def\
    \ inverse(self) -> \"Modulo\":\n        return self.modulo_inverse()\n\n    def\
    \ modulo_inverse(self) -> \"Modulo\":\n        try:\n            return Modulo(pow(self.a,\
    \ -1, self.n), self.n, False)\n        except ValueError:\n            raise ValueError(f\"\
    {self} \u306E\u9006\u6570\u304C\u5B58\u5728\u3057\u307E\u305B\u3093\") from None\n\
    \n    #\u9664\u6CD5\n    def __truediv__(self,other) -> \"Modulo\":\n        return\
    \ self*(other.modulo_inverse())\n\n    def __rtruediv__(self,other) -> \"Modulo\"\
    :\n        return other*(self.modulo_inverse())\n\n    #\u7D2F\u4E57\n    def\
    \ __pow__(self, other: int) -> \"Modulo\":\n        if isinstance(other, int):\n\
    \            return Modulo(pow(self.a, other, self.n), self.n, False)\n      \
    \  else:\n            b,n=other.a,other.n\n            assert pow(self.a,n,self.n)==1,\
    \ \"\u77DB\u76FE\u306A\u304F\u5B9A\u7FA9\u3067\u304D\u307E\u305B\u3093.\"\n  \
    \          return self**b\n\n\"\"\"\n\u521D\u7B49\u7684\n\"\"\"\ndef Modulo_Inverse_List(M:int,K:int):\n\
    \    \"\"\"\n    1^(-1), 2^(-1), ... , K^(-1) (mod N) \u306E\u30EA\u30B9\u30C8\
    \u3092\u51FA\u529B\u3059\u308B.\n\n    [\u5165\u529B]\n    M,K:\u6574\u6570\n\
    \    M>0, K>=1\n    K=min(M-1,K) \u306B\u5909\u63DB\u3055\u308C\u308B.\n\n   \
    \ [\u51FA\u529B]\n    \u9577\u3055 K+1 \u306E\u30EA\u30B9\u30C8 F\n    k=1,2,...,K\
    \ \u306B\u5BFE\u3057\u3066, F[k]=k^(-1) mod M\n    \u307E\u305F, k^(-1) mod M\
    \ \u304C\u5B58\u5728\u3057\u306A\u3044\u5834\u5408, F[k]=None\n    \"\"\"\n\n\
    \    assert M>0 and K>=1\n\n    if K==None:\n        K=M-1\n    K=min(K,M-1)\n\
    \n    F=[None,Modulo(1,M)]\n    for k in range(2,K+1):\n        q,r=divmod(M,k)\n\
    \        if F[r]!=None:\n            F.append(-q*F[r])\n        else:\n      \
    \      F.append(None)\n    return F\n\n#\u7D30\u5206\u5316\ndef Subdivision(X:Modulo,M:int):\n\
    \    \"\"\" X \u3092x (mod M) \u306E\u5F62\u306B\u7D30\u5206\u5316\u3059\u308B\
    .\n\n    X.n | M\u3067\u306A\u304F\u3066\u306F\u306A\u3089\u306A\u3044.\n    \"\
    \"\"\n\n    assert M%X.n==0,\"X.n | M \u3067\u306F\u3042\u308A\u307E\u305B\u3093\
    .\"\n\n    k=M//X.n\n    return [Modulo(X.n*i+X.a,M) for i in range(k)]\n\n#\u9000\
    \u5316\ndef Degenerate(X:Modulo, M:int):\n    \"\"\" X \u306E\u60C5\u5831\u3092\
    \u9000\u5316\u3055\u305B\u308B. X=x (mod N) \u3067\u3042\u308B\u3068\u304D, mod\
    \ M \u3067\u306E\u60C5\u5831\u306B\u9000\u5316\u3055\u305B\u308B.\n\n    M | X.n\
    \ \u3067\u306A\u304F\u3066\u306F\u306A\u3089\u306A\u3044.\n    \"\"\"\n\n    assert\
    \ X.n%M==0,\"M | X.n \u3067\u306F\u3042\u308A\u307E\u305B\u3093.\"\n    return\
    \ Modulo(X.a%M,M)\n\ndef Chinese_Remainder(X: Modulo):\n    \"\"\" \u4E2D\u56FD\
    \u5270\u4F59\u5B9A\u7406\u306B\u3088\u308A, X\u3092\u5206\u89E3\u3059\u308B.\n\
    \n    \"\"\"\n\n    Y=[]\n\n    a,N=X.a,X.n\n    e=(N&(-N)).bit_length()-1\n \
    \   if e>0:\n        N>>=e\n        Y.append(Modulo(a,1<<e))\n\n    e=0\n    while\
    \ N%3==0:\n        e+=1\n        N//=3\n\n    if e>0:\n        Y.append(Modulo(a,pow(3,e)))\n\
    \n    flag=0\n    p=5\n    while p*p<=N:\n        if N%p==0:\n            e=0\n\
    \            while N%p==0:\n                e+=1\n                N//=p\n\n  \
    \          Y.append(Modulo(a,pow(p,e)))\n\n        p+=2+2*flag\n        flag^=1\n\
    \n    if N>1:\n        Y.append(Modulo(a,N))\n\n    return Y\n\n\"\"\"\n\u7DDA\
    \u5F62\u5408\u540C\u65B9\u7A0B\u5F0F\u95A2\u9023\n\"\"\"\ndef Modulo_Composite(*X:\
    \ Modulo) -> Modulo:\n    \"\"\" N \u500B\u306E Modulo \u306E\u5171\u901A\u90E8\
    \u5206\u3092\u6C42\u3081\u308B.\n\n    Returns:\n        Modulo: \u5171\u901A\u90E8\
    \u5206\n    \"\"\"\n\n    def composite(p: Modulo, q: Modulo) -> Modulo | None:\n\
    \        \"\"\" 2\u3064\u306E\u7B49\u5F0F x \u2261 p.a (mod p.n), x \u2261 q.a\
    \ (mod q.n) \u3092\u3068\u3082\u306B\u6E80\u305F\u3059 x \u3092\u5168\u3066\u6C42\
    \u3081\u308B.\n\n        Args:\n            p (Modulo):\n            q (Modulo):\n\
    \n        Returns:\n            Modulo | None: \u6761\u4EF6\u3092\u6E80\u305F\u3059\
    \u3053\u3068\u304C\u5FC5\u8981\u5341\u5206\u306B\u306A\u308B Modulo. \u5B58\u5728\
    \u3057\u306A\u3044\u5834\u5408\u306F None\n        \"\"\"\n        from math import\
    \ gcd\n\n        a, n = p.a, p.n\n        b, m = q.a, q.n\n\n        d = b - a\n\
    \        g = gcd(n, m)\n\n        if d % g:\n            return None\n\n     \
    \   n //= g\n        m //= g\n        d //= g\n\n        s = pow(n, -1, m)\n\n\
    \        return Modulo(a + (n * g) * d * s, n * m *g)\n\n    res = Modulo(0, 1)\n\
    \    for a in X:\n        if (res := composite(res, a)) is None:\n           \
    \ break\n\n    return res\n\ndef Is_Included(X: Modulo, Y: Modulo):\n    \"\"\"\
    \ X \u3092\u5168\u3066\u6E80\u305F\u3059\u6574\u6570\u306F Y \u3092\u5168\u3066\
    \u6E80\u305F\u3059\u304B?\n\n    X,Y: Modulo\n    \"\"\"\n    a,p=X.a,X.n\n  \
    \  b,q=Y.a,Y.n\n    return (a-b)%q==0 and p%q==0\n\n#\u62E1\u5F35Euclid\u306E\u4E92\
    \u9664\u6CD5\ndef Extended_Euclid(a: int, b: int) -> tuple[int, int, int]:\n \
    \   \"\"\" a x + b y = gcd(a, b) \u3092\u6E80\u305F\u3059\u6574\u6570\u306E\u7D44\
    \ (x, y) \u3092\u6C42\u3081\u308B.\n\n    Args:\n        a (int): \u6574\u6570\
    \n        b (int): \u6574\u6570\n\n    Returns:\n        tuple[int, int, int]:\
    \ (x, y, g) \u306F a x + b y = g \u3092\u6E80\u305F\u3059.\n    \"\"\"\n\n   \
    \ from math import gcd\n    g = gcd(a, b)\n    if g == 0:\n        return (0,\
    \ 0, 0)\n\n    x = pow(a//g, -1, b//g)\n    y = - (a*x-g) // b\n    return (x,\
    \ y, g)\n\n#1\u6B21\u5408\u540C\u65B9\u7A0B\u5F0F\u3092\u89E3\u304F\ndef First_Order_Congruent_Equation(a:\
    \ int, b: int, m: int) -> Modulo:\n    \"\"\" 1\u6B21\u5408\u540C\u65B9\u7A0B\u5F0F\
    \ a x \u2261 b (mod m) \u3092\u6C42\u3081\u308B.\n\n    Args:\n        a (int):\n\
    \        b (int):\n        m (int): m != 0\n\n    Returns:\n        Modulo: \u6761\
    \u4EF6\u3092\u6E80\u305F\u3059 X \u304C\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\
    \u306F None.\n    \"\"\"\n    from math import gcd\n\n    if m == 0:\n       \
    \ raise ValueError\n\n    g = gcd(a, m)\n\n    # \u5B58\u5728\u78BA\u8A8D\n  \
    \  if b % g:\n        return None\n\n    a, b, m = a // g, b // g, m // g\n  \
    \  c = pow(a, -1, m)\n    return Modulo(b * c, m)\n\n#1\u6B21\u9023\u7ACB\u5408\
    \u540C\u65B9\u7A0B\u5F0F\u3092\u89E3\u304F\ndef First_Order_Simultaneous_Congruent_Equation(*X:\
    \ tuple[int, int, int]) -> Modulo:\n    \"\"\" 1 \u6B21\u5408\u540C\u65B9\u7A0B\
    \u5F0F a_i x \u2261 b_i (mod m_i) \u3092\u6C42\u3081\u308B.\n\n    Args:\n   \
    \     X (list[tuple[int, int, int]]): (a, b, m) \u306E\u5F62\u306E\u30BF\u30D7\
    \u30EB. (a, b, m) \u306F ax \u2261 b (mod m) \u3092\u610F\u5473\u3059\u308B.\n\
    \n    Returns:\n        Modulo: \u89E3\n    \"\"\"\n\n    equations = []\n   \
    \ for (a, b, m) in X:\n        t = First_Order_Congruent_Equation(a, b, m)\n \
    \       if t is None:\n            break\n\n        equations.append(t)\n\n  \
    \  return Modulo_Composite(*equations)\n\n\"\"\"\n\u7DCF\u548C\n\"\"\"\n\ndef\
    \ Geometric_Sum(X, L, R):\n    \"\"\" sum_{i=L}^R X^i \u3092\u6C42\u3081\u308B\
    .\n\n    X: modulo\n    0<=L<=R\n    \"\"\"\n    assert 0<=L\n    if L>R:\n  \
    \      return 0\n\n    a=X.a; m=X.n\n    def calc(K):\n        \"\"\" sum_{i=0}^{K-1}\
    \ a^i\n        \"\"\"\n\n        if K==0:\n            return 0\n        elif\
    \ K%2==0:\n            return (1+pow(a, K//2, m))*calc(K//2)%m\n        else:\n\
    \            return (1+a*calc(K-1))%m\n\n    return Modulo(calc(R+1)-calc(L),\
    \ m)\n\n\"\"\"\n\u6709\u9650\u4F53\u306E\u64CD\u4F5C\u95A2\u9023\n\"\"\"\n#\u30EB\
    \u30B8\u30E3\u30F3\u30C9\u30EB\u8A18\u53F7\ndef Legendre(X: Modulo) -> int:\n\
    \    \"\"\" \u30EB\u30B8\u30E3\u30F3\u30C9\u30EB\u8A18\u53F7 (a/p) \u3092\u8FD4\
    \u3059. \u203B \u6CD5\u304C\u7D20\u6570\u306E\u3068\u304D\u306E\u307F\u6210\u7ACB\
    \u3059\u308B.\n\n    Args:\n        X (Modulo):\n\n    Returns:\n        int:\n\
    \            X = 0 \u306E\u3068\u304D\u306F 0\n            X \u304C\u5E73\u65B9\
    \u5270\u4F59\u306E\u3068\u304D\u306F 1\n            X \u304C\u5E73\u65B9\u975E\
    \u5270\u4F59\u306E\u3068\u304D\u306F -1\n    \"\"\"\n    if 0 in X:\n        return\
    \ 0\n\n    return 1 if pow(X, (X.n - 1) // 2) == 1 else -1\n\n#\u6839\u53F7\n\
    def Sqrt(X: Modulo) -> Modulo:\n    \"\"\" r * r = a (mod p) \u3092\u6E80\u305F\
    \u3059 r \u3092 (\u5B58\u5728\u3059\u308C\u3070) \u6C42\u3081\u308B.\n\n    Args:\n\
    \        X (Modulo):\n\n    Returns:\n        Modulo: \u5B58\u5728\u3057\u306A\
    \u3044\u5834\u5408\u306F None, \u5B58\u5728\u3059\u308B\u5834\u5408\u306F r *\
    \ r = a \u3092\u6E80\u305F\u3059 r (\u306E\u3046\u3061\u306E 1 \u3064)\n    \"\
    \"\"\n\n    if Legendre(X) == -1:\n        return None\n\n    p = X.n\n    if\
    \ X == 0:\n        return X\n    elif p == 2:\n        return X\n    elif p %\
    \ 4 == 3:\n        return pow(X, (p + 1) // 4)\n    elif p % 8 == 5:\n       \
    \ if pow(X, (p - 1) // 4) == 1:\n            return pow(X, (p + 3) // 8)\n   \
    \     else:\n            return pow(2, (p - 1) // 4, p) * pow(X, (p + 3) // 8)\n\
    \n    from random import randint as ri\n    u = 2\n    s = 1\n    while (p - 1)\
    \ % (2 * u) == 0:\n        u *= 2\n        s += 1\n    q = (p - 1) // u\n\n  \
    \  while True:\n        z = Modulo(ri(1, p - 1), p)\n        if pow(z, (p - 1)\
    \ // 2) == -1:\n            break\n\n    m, c, t, r = s, pow(z, q), pow(X, q),\
    \ pow(X, (q + 1) // 2)\n    while m > 1:\n        if pow(t, pow(2, m - 2)) ==\
    \ 1:\n            c = c * c\n            m = m - 1\n        else:\n          \
    \  c, t, r, m = c * c, c * c * t, c * r, m - 1\n\n    return r\n\n#\u96E2\u6563\
    \u5BFE\u6570\ndef Discrete_Log(A: Modulo, B: Modulo | int, default: int = -1)\
    \ -> int | None:\n    \"\"\" A^x \u2261 B \u3092\u6E80\u305F\u3059\u6700\u5C0F\
    \u306E\u975E\u8CA0\u6574\u6570 x \u3092\u6C42\u3081\u308B.\n\n    Args:\n    \
    \    A (Modulo): \u5E95\n        B (Modulo | int): \u771F\u6570\n        default\
    \ (int, optional): \u5B58\u5728\u3057\u306A\u3044\u3068\u304D\u306E\u8FD4\u308A\
    \u5024. Defaults to -1.\n\n    Raises:\n        ValueError: A, B \u5171\u306B\
    \ Modulo \u306E\u3068\u304D\u306F\u6CD5\u3092\u4E00\u81F4\u3055\u305B\u306A\u3051\
    \u308C\u3070\u306A\u3089\u306A\u3044.\n\n    Returns:\n        int | None: A^x\
    \ \u2261 B \u3092\u6E80\u305F\u3059\u6700\u5C0F\u306E\u975E\u8CA0\u6574\u6570\
    \ x (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F default).\n    \"\"\"\n\n\
    \    A, M = A.a, A.n\n\n    if isinstance(B, int):\n        B %= M\n    elif isinstance(B,\
    \ Modulo):\n        if M != B.n:\n            raise ValueError\n        B = B.a\
    \ % M\n    else:\n        raise NotImplementedError\n\n    m = 0\n    while m\
    \ * m < M:\n        m += 1\n\n    E = set()\n    y = B\n    for _ in range(m):\n\
    \        y *= A; y %= M\n        E.add(y)\n\n    step = pow(A, m, M)\n    head\
    \ = 1 % M\n    count = 0\n    for k in range(1, m + 1):\n        tail = head\n\
    \        head = step * head % M\n\n        if head not in E:\n            continue\n\
    \n        body = tail\n        for n in range((k - 1) * m, k * m):\n         \
    \   if body == B:\n                return n\n\n            body = (A * body) %\
    \ M\n\n        count += 1\n        if count == 2:\n            break\n\n    return\
    \ default\n\ndef Order(X: Modulo, defalut: int = -1) -> int:\n    \"\"\" X^k =\
    \ 1 \u3092\u6E80\u305F\u3059\u6700\u5C0F\u306E\u6B63\u306E\u6574\u6570 k \u3092\
    \u6C42\u3081\u308B (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F -1)\n\n \
    \   Args:\n        X (Modulo): \u5E95\n        defalut (int, optional): \u5B58\
    \u5728\u3057\u306A\u3044\u5834\u5408\u306E\u5024. Defaults to -1.\n\n    Returns:\n\
    \        int: X^k \u3092\u6E80\u305F\u3059\u6700\u5C0F\u306E k\n    \"\"\"\n\n\
    \    phi=1\n    N=X.n\n\n    e=(N&(-N)).bit_length()-1\n    if e>0:\n        phi=1<<(e-1)\n\
    \        N>>=e\n    else:\n        phi=1\n\n    e=0\n    while N%3==0:\n     \
    \   e+=1\n        N//=3\n\n    if e>0:\n        phi*=pow(3,e-1)*2\n\n    flag=0\n\
    \    p=5\n    while p*p<=N:\n        if N%p==0:\n            e=0\n           \
    \ while N%p==0:\n                e+=1\n                N//=p\n\n            phi*=pow(p,e-1)*(p-1)\n\
    \n        p+=2+2*flag\n        flag^=1\n\n    if N>1:\n        phi*=N-1\n\n  \
    \  a=float(\"inf\")\n    k=1\n    while k*k<=phi:\n        if phi%k==0:\n    \
    \        if k<a and pow(X,k)==1:\n                a=k\n                break\n\
    \n            if phi//k<a and pow(X,phi//k)==1:\n                a=phi//k\n  \
    \      k+=1\n\n    return a if a < float(\"inf\") else defalut\n\ndef Primitive_Root(p):\n\
    \    \"\"\" Z/pZ \u4E0A\u306E\u539F\u59CB\u6839\u3092\u898B\u3064\u3051\u308B\n\
    \n    p: \u7D20\u6570\n    \"\"\"\n    if p==2:\n        return 1\n    if p==998244353:\n\
    \        return 3\n    if p==10**9+7:\n        return 5\n    if p==163577857:\n\
    \        return 23\n    if p==167772161:\n        return 3\n    if p==469762049:\n\
    \        return 3\n\n    fac=[]\n    q=2\n    v=p-1\n\n    while v>=q*q:\n   \
    \     e=0\n        while v%q==0:\n            e+=1\n            v//=q\n\n    \
    \    if e>0:\n            fac.append(q)\n        q+=1\n\n    if v>1:\n       \
    \ fac.append(v)\n\n    g=2\n    while g<p:\n        if pow(g,p-1,p)!=1:\n    \
    \        return None\n\n        flag=True\n        for q in fac:\n           \
    \ if pow(g,(p-1)//q,p)==1:\n                flag=False\n                break\n\
    \n        if flag:\n            return g\n\n        g+=1\n\n\"\"\"\n\u6570\u3048\
    \u4E0A\u3052\u95A2\u9023\n\"\"\"\ndef Factor_Modulo(N, Mod, Mode=0):\n    \"\"\
    \"\n    Mode=0: N! (mod Mod) \u3092\u6C42\u3081\u308B.\n    Mode=1: k! (mod Mod)\
    \ (k=0,1,...,N) \u306E\u30EA\u30B9\u30C8\u3082\u51FA\u529B\u3059\u308B.\n\n  \
    \  [\u8A08\u7B97\u91CF]\n    O(N)\n    \"\"\"\n\n    if Mode==0:\n        X=1\n\
    \        for k in range(1,N+1):\n            X*=k; X%=Mod\n        return Modulo(X,Mod)\n\
    \    else:\n        L=[Modulo(1,Mod)]*(N+1)\n        for k in range(1,N+1):\n\
    \            L[k]=k*L[k-1]\n        return L\n\ndef Factor_Modulo_with_Inverse(N,\
    \ Mod):\n    \"\"\" k=0,1,...,N \u306B\u5BFE\u3059\u308B k! (mod Mod) \u3068 (k!)^(-1)\
    \ (mod Mod) \u306E\u30EA\u30B9\u30C8\u3092\u51FA\u529B\u3059\u308B.\n\n    [\u5165\
    \u529B]\n    N, Mod: \u6574\u6570\n    Mod >0\n    [\u51FA\u529B]\n    \u9577\u3055\
    \ N+1 \u306E\u30EA\u30B9\u30C8\u306E\u30BF\u30D7\u30EB (F,G): F[k]=k! (mod M),\
    \ G[k]=(k!)^(-1) (mod M)\n    [\u8A08\u7B97\u91CF]\n    O(N+log Mod)\n    \"\"\
    \"\n\n    assert Mod>0\n\n    F=Factor_Modulo(N,Mod,Mode=1)\n    G=[0]*(N+1)\n\
    \n    G[-1]=F[-1].inverse()\n    for k in range(N,0,-1):\n        G[k-1]=k*G[k]\n\
    \    return F,G\n\ndef Binomial_Coefficient_Modulo(n: int, r: int, Mod:int):\n\
    \    \"\"\" nCr (mod Mod) \u3092\u611A\u76F4\u306A\u65B9\u6CD5\u3067\u6C42\u3081\
    \u308B.\n\n    [\u5165\u529B]\n    n, r, Mod: \u6574\u6570\n    Mod>0\n    [\u51FA\
    \u529B]\n    nCr (mod Mod)\n    [\u8A08\u7B97\u91CF]\n    O(r)\n    \"\"\"\n \
    \   assert Mod>0\n    if r<0 or n<r:\n        return Modulo(0,Mod)\n\n    X=Y=1\n\
    \n    r=min(r,n-r)\n    for i in range(r):\n        X*=n-i; X%=Mod\n        Y*=r-i;\
    \ Y%=Mod\n    return Modulo(X,Mod)/Modulo(Y,Mod)\n\ndef Binomial_Coefficient_Modulo_List(n:int,\
    \ Mod:int):\n    \"\"\" n \u3092\u56FA\u5B9A\u3057, r=0,1,...,n \u3068\u3057\u305F\
    \u3068\u304D\u306E nCr (mod Mod) \u306E\u30EA\u30B9\u30C8\u3092\u51FA\u529B\u3059\
    \u308B.\n\n    [\u5165\u529B]\n    n,Mod: \u6574\u6570\n    Mod>0\n    [\u51FA\
    \u529B]\n    [nC0 (mod Mod), nC1 (mod Mod),..., nCn (mod Mod)]\n    [\u8A08\u7B97\
    \u91CF]\n    O(n)\n    \"\"\"\n\n    assert Mod>0\n    L=[Modulo(1,Mod) for _\
    \ in range(n+1)]\n\n    I=Modulo_Inverse_List(Mod,n)\n    for r in range(1,n+1):\n\
    \        L[r]=(n+1-r)*I[r]*L[r-1]\n    return L\n\ndef Pascal_Triangle(N,M):\n\
    \    \"\"\"\n    0<=n<=N, 0<=r<=n \u306E\u5168\u3066\u306B\u5BFE\u3057\u3066 nCr\
    \ (mod M) \u306E\u30EA\u30B9\u30C8\u3092\u51FA\u529B\u3059\u308B.\n\n    [\u5165\
    \u529B]\n    N,M:\u6574\u6570\n    M>0\n    [\u51FA\u529B] (mod M) \u3092\u7701\
    \u7565.\n    [[0C0], [1C0, 1C1], ... , [nC0, ... , nCn], ..., [NC0, ..., NCN]]\n\
    \    [\u8A08\u7B97\u91CF]\n    O(N^2)\n    \"\"\"\n\n    X=[Modulo(1,M)]\n   \
    \ L=[[Modulo(1,M)]]\n    for n in range(N):\n        Y=[Modulo(1,M)]\n       \
    \ for k in range(1,n+1):\n            Y.append(X[k]+X[k-1])\n        Y.append(Modulo(1,M))\n\
    \        X=Y\n        L.append(Y)\n    return L\n"
  dependsOn: []
  isVerificationFile: false
  path: Modulo.py
  requiredBy: []
  timestamp: '2025-05-11 20:45:40+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Math/Sqrt_Mod.test.py
  - test_verify/yosupo_library_checker/Math/Discrete_Log.test.py
documentation_of: Modulo.py
layout: document
title: Modulo
---

## Theory

### 定義

$\mathbb{Z}$ を整数環とし, $m$ を正の整数とする. このとき, $m \mathbb{Z}$ は $\mathbb{Z}$ のイデアルであるから, 剰余環 $\mathbb{Z}/m \mathbb{Z}$ を考えることができる.

$x \in \mathbb{Z}$ の属する類を $[x], [x]\_m$ と書くことにする. このとき, $x,y \in \mathbb{Z}$ に対して, 以下は同値になる.

* $[x]=[y]$
* $(x-y)$ は $m$ の倍数
* $x \equiv y \pmod{m}$

よって, 各整数の余りを考えることにより,

$$\mathbb{Z}/m\mathbb{Z}=\{[0], [1], \dots, [m-1] \}$$

となることがわかる.

この剰余環は次の和と積によって可換環になる.

* $[x]+[y]:=[x+y]$
* $[x] [y]:=[xy]$

$[x] \in \mathbb{Z}/m \mathbb{Z}$ が可逆元になることの必要十分条件は $x,m$ が互いに素になることである.

よって, $\mathbb{Z}/m\mathbb{Z}$ が体になることの必要十分条件は $m$ が素数であることである.

### 中国剰余定理

$m$ の素因数分解を $m=p_1^{e_1} \dots p_k^{e_k}$ とする. このとき, 中国剰余定理から

$$\displaystyle \mathbb{Z}/m\mathbb{Z} \simeq \prod_{i=1}^k (\mathbb{Z}/p_i^{e_i} \mathbb{Z})$$

である. このとき, 同型写像 $\varphi$ として

$$\varphi([x]):=([x \bmod{p_1^{e_1}}]_{p_1^{e_1}}, \dots, [x \bmod{p_k^{e_k}}]_{p_k^{e_k}})$$

が挙げられる.

### 剰余の合成

$x \in \mathbb{Z}$ としたとき,

$$x \equiv a \pmod{m} \cdots (\spadesuit), \quad x \equiv b \pmod{n} \cdots (\heartsuit)$$

を共にみたすような整数 $x$ の特徴づけをする (中国剰余定理の節における $\varphi$ の逆関数の構成).

$(\spadesuit), (\heartsuit)$ を書き換えると,

* $x=a+mp$ となる整数 $p$ が存在する.
* $x=b+nq$ となる整数 $q$ が存在する.

となることから, 合わせると

* $a+mp=b+nq$ となる整数 $p,q$ が存在する.

ということになる. 式変形をし, $d:=b-a$ とおくと,

* $mp-nq=d \cdots (\diamondsuit)$ となる整数 $p,q$ が存在する.

となる. このような整数 $p,q$ が存在することの必要十分条件は $d$ が $g:=\gcd(m,n)$ の倍数であることである.

以降, $d$ が $\gcd(m,n)$ の倍数であるとし, 整数 $m',n',d'$ をそれぞれ

$$m=gm', \quad n=gn', \quad d=gd'$$

とすると, $(\diamondsuit)$ は $mp \equiv d \pmod{n}$ と同値である.

$m,n,d$ は全て $g$ の倍数であるから, $m'p \equiv d' \pmod{n'}$ と同値になる.

$m', n'$ は互いに素であるので, $m' k \equiv 1 \pmod{n'}$ となる整数 $k$ が存在する. これを両辺にかけることにより,

$$p \equiv dk \pmod{n'}$$

を得る.

これを $x=a+mp$ に代入することによって, $mn'=\dfrac{mn}{\gcd(m,n)}=\operatorname{lcm}(m,n)$ であるから,

$$x \equiv a+mdk \pmod{\operatorname{lcm}(m,n)}$$

を得る. 逆に, これを満たす整数 $x$ は全て $(\spadesuit), (\heartsuit)$ を満たす.

### 線形方程式

$ax \equiv b \pmod{m}$ を満たす整数 $x$ の特徴づけを行う.

まず, $b$ が $g:=\gcd(a,m)$ の倍数でない場合はこのような整数 $x$ は存在しない. 整数 $a', b', m'$ は $a=ga', b=gb', m=gm'$ を満たすようにとる.

このとき, $a', m'$ は互いに素なので, $a'k \equiv 1 \pmod{m'}$ なる整数 $k$ が存在する. よって,

$$ax \equiv b \pmod{m} \iff x \equiv bk \pmod{m'}$$

となる.

### ルジャンドル記号

$p$ を素数とする. 整数 $a \in \mathbb{Z}$ におけるルジャンドル記号 $\displaystyle \left( \dfrac{a}{p} \right)$ を

$$\left( \dfrac{a}{p} \right) \equiv a^{(p-1)/2} \pmod{p}, \quad \left( \dfrac{a}{p} \right) \in \{-1,0,1\}$$

をみたす (唯一の) 整数と定義する (well-defindness はフェルマーの小定理より従う).

このとき,

* $\left( \dfrac{a}{p} \right)=1 \iff a \not \equiv 0 \pmod{p}$ かつ $\exists b \in \mathbb{Z} {\rm ~s.t.~} b^2=a$ (平方剰余)
* $\left( \dfrac{a}{p} \right)=-1 \iff a \not \equiv 0 \pmod{p}$ かつ $\exists b \in \mathbb{Z} {\rm ~s.t.~} b^2=a$ (平方非剰余)
* $\left( \dfrac{a}{p} \right)=0 \iff a \equiv 0 \pmod{p}$

よって, $a$ が $p$ を法にして平方剰余であることと, $\left( \dfrac{a}{p} \right) \neq -1$ であることは同値になる.

### 位数

$[a] \in \mathbb{Z}/m \mathbb{Z}$ に対して, $[a]^n=[1]$ となる 正の整数 $n$ が存在するか? 存在するならばその $n$ の最小値 $\operatorname{ord} [a]$を求める.

まず, 存在性については $[a]^n=[1]$ が存在することと, $[a]$ が可逆である. つまり, $a,m$ が互いに素になることが同値になる.

実際, $[a]^n=[1]$ となる正の整数 $n$ が存在するならば, $[a]^{-1}=[a]^{n-1}$ であるから, $[a]$ は可逆である. 一方で, $[a]$ が可逆であるとき, $[a]^0, [a]^1, \dots, [a]^m$ には鳩ノ巣原理から, $0 \leq i<j \leq m$ で $[a]^i=[a]^j$ となるようなものが存在する. $[a]$ は可逆と仮定しているので, $[a]^{j-i}=[1]$ である.

可逆元 $[a]$ に対して, 積に関して生成される $\left \langle [a] \right \rangle$ は $(\mathbb{Z}/m\mathbb{Z})^\times$ の部分群である. このとき, ラグランジュの定理から次のことが従う.

* $\\# \left \langle [a] \right \rangle$ は $\\# (\mathbb{Z}/m\mathbb{Z})^\times$ の約数である.

また, この2つの群の位数について,

* $\operatorname{ord} [a]=\left \langle [a] \right \rangle$
* $\\# (\mathbb{Z}/m\mathbb{Z})^\times=\varphi(m)$ (Euler's totient function)

が成り立つ.

以上のことから,

$$\operatorname{ord} [a]=\min \{d \mid 1 \leq d \leq m, d~|~\varphi(m), [a]^d=1 \}$$

となる.

### 原始根

次のような定理がある.

> 原始根の存在定理
>
> $p$ を素数とする. このとき, $\mathbb{Z}/p \mathbb{Z}$ には位数 $(p-1)$ の元が存在する.
>
> このような元のことを原始根という.

$p$ を素数とすると, 任意の $p$ の倍数ではない整数 $a$ に対して, $[x]^{p-1}=[1]$ である.

$[g] \in (\mathbb{Z}/p \mathbb{Z})^\times$ が原始根であることの必要十分条件は任意の $(p-1)$ の素因数 $q$ に対して, $[a]^{(p-1)/q} \neq [1]$ となることである.

[参考ページ](https://37zigen.com/primitive-root/)
