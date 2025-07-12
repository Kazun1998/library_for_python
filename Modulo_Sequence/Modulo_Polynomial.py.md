---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Polynomial/Division.test.py
    title: test_verify/yosupo_library_checker/Polynomial/Division.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Polynomial/Exp.test.py
    title: test_verify/yosupo_library_checker/Polynomial/Exp.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Polynomial/Inv.test.py
    title: test_verify/yosupo_library_checker/Polynomial/Inv.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Polynomial/Log.test.py
    title: test_verify/yosupo_library_checker/Polynomial/Log.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Polynomial/Power.test.py
    title: test_verify/yosupo_library_checker/Polynomial/Power.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Polynomial/Product_of_Polynomial_Sequence.test.py
    title: test_verify/yosupo_library_checker/Polynomial/Product_of_Polynomial_Sequence.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Polynomial/Taylor_Shift.test.py
    title: test_verify/yosupo_library_checker/Polynomial/Taylor_Shift.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - http://q.c.titech.ac.jp/docs/progs/polynomial_division.html
    - https://arxiv.org/abs/2008.08822
    - https://arxiv.org/pdf/1301.5804.pdf
    - https://arxiv.org/pdf/2008.08822.pdf
    - https://github.com/atcoder/ac-library/blob/master/atcoder/convolution.hpp
    - https://judge.yosupo.jp/submission/28304
    - https://judge.yosupo.jp/submission/42372
    - https://judge.yosupo.jp/submission/42413
    - https://judge.yosupo.jp/submission/72676
    - https://opt-cp.com/fps-fast-algorithms/
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Modulo_Polynomial:\n    __slots__= (\"poly\", \"max_degree\")\n\n \
    \   def __init__(self, poly: list[int] = None, max_degree: int = 2 * 10 ** 5):\n\
    \        \"\"\" \u591A\u9805\u5F0F\u3092\u5B9A\u7FA9\u3059\u308B (\u5404\u4FC2\
    \u6570\u306E\u6CD5 Mod \u306F\u30B0\u30ED\u30FC\u30D0\u30EB\u5909\u6570\u304B\u3089\
    \u6307\u5B9A\u3059\u308B).\n\n        Args:\n            poly (list[int], optional):\
    \ \u4FC2\u6570\u306E\u30EA\u30B9\u30C8. \u7B2C d \u8981\u7D20\u306F d \u6B21\u306E\
    \u4FC2\u6570\u3092\u8868\u3059. None \u306E\u3068\u304D\u306F [0] \u3068\u540C\
    \u7FA9. Defaults to None.\n            max_degree (int, optional): (mod X^n) \u3092\
    \u8003\u3048\u308B\u3068\u304D\u306E n. Defaults to 2*10**5.\n        \"\"\"\n\
    \n        if poly is None:\n            poly = [0]\n\n        self.poly: list[int]\
    \ = [a % Mod for a in poly[:max_degree]]\n        self.max_degree = max_degree\n\
    \n    def __str__(self) -> str:\n        return str(self.poly)\n\n    def __repr__(self)\
    \ -> str:\n        return f\"{self.__class__.__name__}({self.poly})\"\n\n    def\
    \ __iter__(self):\n        yield from self.poly\n\n    def __eq__(self, other:\
    \ \"Modulo_Polynomial\") -> bool:\n        from itertools import zip_longest\n\
    \        return all([a == b for a, b in zip_longest(self.poly, other.poly, fillvalue\
    \ = 0)])\n\n    #+,-\n    def __pos__(self) -> \"Modulo_Polynomial\":\n      \
    \  return self\n\n    def __neg__(self) -> \"Modulo_Polynomial\":\n        return\
    \ self.scale(-1)\n\n    #items\n    def __getitem__(self, index):\n        if\
    \ isinstance(index, slice):\n            return Modulo_Polynomial(self.poly[index],\
    \ self.max_degree)\n        else:\n            if index<0:\n                raise\
    \ IndexError(f\"index is negative (index: {index})\")\n            elif index>=len(self.poly):\n\
    \                return 0\n            else:\n                return self.poly[index]\n\
    \n    def __setitem__(self, index, value):\n        if index<0:\n            raise\
    \ IndexError(f\"index is negative (index: {index})\")\n        elif index>=self.max_degree:\n\
    \            return\n\n        if index>=len(self.poly):\n            self.poly+=[0]*(index-len(self.poly)+1)\n\
    \        self.poly[index]=value%Mod\n\n    #Boole\n    def __bool__(self) -> bool:\n\
    \        return any(self.poly)\n\n    #\u7C21\u7565\u5316\n    def reduce(self):\n\
    \        \"\"\" \u5148\u982D\u306E 0 \u3092\u524A\u9664\u3059\u308B.\n       \
    \ \"\"\"\n\n        poly = self.poly\n        while poly and (poly[-1] == 0):\n\
    \            poly.pop()\n\n\n    #\u30B7\u30D5\u30C8\n    def __lshift__(self,\
    \ depth: int) -> \"Modulo_Polynomial\":\n        if depth < 0:\n            return\
    \ self >> (-depth)\n\n        if depth > self.max_degree:\n            return\
    \ Modulo_Polynomial([0], self.max_degree)\n\n        return Modulo_Polynomial([0]\
    \ * depth + self.poly, self.max_degree)\n\n    def __rshift__(self, depth: int)\
    \ -> \"Modulo_Polynomial\":\n        if depth < 0:\n            return  self <<\
    \ (-depth)\n\n        return Modulo_Polynomial(self.poly[depth:], self.max_degree)\n\
    \n    #\u6B21\u6570\n    def degree(self) -> int:\n        \"\"\" \u3053\u306E\
    \u591A\u9805\u5F0F\u306E\u6B21\u6570\u3092\u6C42\u3081\u308B.\n\n        Returns:\n\
    \            int: \u6B21\u6570 (\u4FC2\u6570\u304C 0 \u3067\u306F\u306A\u3044\u6700\
    \u5927\u6B21\u6570)\n        \"\"\"\n\n        for d in range(len(self.poly) -\
    \ 1, -1, -1):\n            if self.poly[d]:\n                return d\n      \
    \  else:\n            return -float(\"inf\")\n\n    #\u52A0\u6CD5\n    def __add__(self,\
    \ other) -> \"Modulo_Polynomial\":\n        P=self; Q=other\n\n        if Q.__class__==Modulo_Polynomial:\n\
    \            N=min(P.max_degree,Q.max_degree)\n            A=P.poly; B=Q.poly\n\
    \        else:\n            N=P.max_degree\n            A=P.poly; B=Q\n      \
    \  return Modulo_Polynomial(Calc.add(A, B), N)\n\n    def __radd__(self, other)\
    \ -> \"Modulo_Polynomial\":\n        return self+other\n\n    #\u6E1B\u6CD5\n\
    \    def __sub__(self, other) -> \"Modulo_Polynomial\":\n        P=self; Q=other\n\
    \        if Q.__class__==Modulo_Polynomial:\n            N=min(P.max_degree,Q.max_degree)\n\
    \            A=P.poly; B=Q.poly\n        else:\n            N=P.max_degree\n \
    \           A=P.poly; B=Q\n        return Modulo_Polynomial(Calc.sub(A, B), N)\n\
    \n    def __rsub__(self, other) -> \"Modulo_Polynomial\":\n        return (-self)\
    \ + other\n\n    #\u4E57\u6CD5\n    def __mul__(self, other) -> \"Modulo_Polynomial\"\
    :\n        P=self\n        Q=other\n        if Q.__class__==Modulo_Polynomial:\n\
    \            a=b=0\n            for x in P.poly:\n                if x:\n    \
    \                a+=1\n            for y in Q.poly:\n                if y:\n \
    \                   b+=1\n\n            if a>b:\n                P,Q=Q,P\n\n \
    \           P.reduce();Q.reduce()\n            U,V=P.poly,Q.poly\n           \
    \ M=min(P.max_degree,Q.max_degree)\n            if a<2*P.max_degree.bit_length():\n\
    \                B=[0]*(len(U)+len(V)-1)\n                for i in range(len(U)):\n\
    \                    if U[i]:\n                        for j in range(len(V)):\n\
    \                            B[i+j]+=U[i]*V[j]\n                            if\
    \ B[i+j]>Mod:\n                                B[i+j]-=Mod\n            else:\n\
    \                B=Calc.convolution(U,V)[:M]\n            B=Modulo_Polynomial(B,M)\n\
    \            B.reduce()\n            return B\n        else:\n            return\
    \ self.scale(other)\n\n    def __rmul__(self, other) -> \"Modulo_Polynomial\"\
    :\n        return self.scale(other)\n\n    #\u9664\u6CD5\n    def __floordiv__(self,\
    \ other) -> \"Modulo_Polynomial\":\n        if not other:\n            raise ZeroDivisionError\n\
    \        if isinstance(other,int):\n            return self/other\n\n        self.reduce()\n\
    \        other.reduce()\n\n        return Modulo_Polynomial(Calc.flood_div(self.poly,\
    \ other.poly), max(self.max_degree, other.max_degree))\n\n    def __rfloordiv__(self,\
    \ other) -> \"Modulo_Polynomial\":\n        if not self:\n            raise ZeroDivisionError\n\
    \n        if isinstance(other,int):\n            return Modulo_Polynomial([],self.max_degree)\n\
    \n    #\u5270\u4F59\n    def __mod__(self, other) -> \"Modulo_Polynomial\":\n\
    \        if not other:\n            return ZeroDivisionError\n        self.reduce();\
    \ other.reduce()\n        r = Modulo_Polynomial(Calc.mod(self.poly, other.poly),\
    \ min(self.max_degree, other.max_degree))\n        r.reduce()\n        return\
    \ r\n\n    def __rmod__(self, other) -> \"Modulo_Polynomial\":\n        if not\
    \ self:\n            raise ZeroDivisionError\n        r=other-(other//self)*self\n\
    \        r.reduce()\n        return r\n\n    def __divmod__(self, other) -> tuple[\"\
    Modulo_Polynomial\", \"Modulo_Polynomial\"]:\n        q=self//other\n        r=self-q*other;\
    \ r.reduce()\n        return (q,r)\n\n    #\u7D2F\u4E57\n    def __pow__(self,\
    \ other) -> \"Modulo_Polynomial\":\n        if other.__class__==int:\n       \
    \     n=other\n            m=abs(n)\n\n            Q=self\n            A=Modulo_Polynomial([1],self.max_degree)\n\
    \            while m>0:\n                if m&1:\n                    A*=Q\n \
    \               m>>=1\n                Q*=Q\n\n            if n>=0:\n        \
    \        return A\n            else:\n                return A.inverse()\n   \
    \     else:\n            P=Log(self)\n            return Exp(P*other)\n\n    def\
    \ inverse(self, deg: int = None) -> \"Modulo_Polynomial\":\n        \"\"\" \u3053\
    \u306E\u591A\u9805\u5F0F\u306E (mod X^d) \u3067\u306E\u9006\u5143\u3092\u6C42\u3081\
    \u308B.\n\n        Args:\n            deg (int, optional): \u9006\u5143\u306E\u7CBE\
    \u5EA6 ((mod X^d) \u306E\u9006\u5143\u3092\u6C42\u3081\u308B\u969B\u306E d) \u3092\
    \u6307\u5B9A\u3059\u308B. None \u306E\u3068\u304D\u306F\u5143\u306E\u591A\u9805\
    \u5F0F\u306E\u7CBE\u5EA6\u3092\u305D\u306E\u307E\u307E\u63A1\u7528. Defaults to\
    \ None.\n\n        Returns:\n            Modulo_Polynomial: _description_\n  \
    \      \"\"\"\n        assert self.poly[0], \"\u5B9A\u6570\u9805\u304C0\"\n\n\
    \        if deg is None:\n            deg = self.max_degree\n\n        return\
    \ Modulo_Polynomial(Calc.inverse(self.poly, deg), self.max_degree)\n\n    #\u9664\
    \u6CD5\n    def __truediv__(self, other) -> \"Modulo_Polynomial\":\n        if\
    \ isinstance(other, Modulo_Polynomial):\n            if Calc.is_sparse(other.poly):\n\
    \                d,f=Calc.coefficients_list(other.poly)\n                K=len(d)\n\
    \                H=[0]*self.max_degree\n\n                alpha=pow(other[0],\
    \ -1, Mod)\n                H[0]=alpha*self[0]%Mod\n\n                for i in\
    \ range(1, self.max_degree):\n                    c=0\n                    for\
    \ j in range(1, K):\n                        if d[j]<=i:\n                   \
    \         c+=f[j]*H[i-d[j]]%Mod\n                        else:\n             \
    \               break\n                    c%=Mod\n                    H[i]=alpha*(self[i]-c)%Mod\n\
    \                H=Modulo_Polynomial(H, min(self.max_degree, other.max_degree))\n\
    \                return H\n            else:\n                return self*other.inverse()\n\
    \        else:\n            return pow(other, -1, Mod)*self\n\n    def __rtruediv__(self,\
    \ other: \"Modulo_Polynomial\") -> \"Modulo_Polynomial\":\n        return other*self.inverse()\n\
    \n    #\u30B9\u30AB\u30E9\u30FC\u500D\n    def scale(self, s: int) -> \"Modulo_Polynomial\"\
    :\n        \"\"\" \u591A\u9805\u5F0F\u306B s \u500D\u3092\u639B\u3051\u305F\u591A\
    \u9805\u5F0F\u3092\u6C42\u3081\u308B.\n\n        Args:\n            s (int): \u30B9\
    \u30AB\u30E9\u30FC\u500D\u306E\u4FC2\u6570\n\n        Returns:\n            Modulo_Polynomial:\
    \ s \u500D\u3057\u305F\u591A\u9805\u5F0F\n        \"\"\"\n\n        return Modulo_Polynomial(Calc.times(self.poly,s),\
    \ self.max_degree)\n\n    #\u6700\u9AD8\u6B21\u306E\u4FC2\u6570\n    def leading_coefficient(self)\
    \ -> int:\n        \"\"\" \u6700\u9AD8\u6B21\u306E\u4FC2\u6570\u3092\u6C42\u3081\
    \u308B\n\n        Returns:\n            int: \u6700\u9AD8\u6B21\u306E\u4FC2\u6570\
    \ (0 \u591A\u9805\u5F0F\u306E\u8FD4\u308A\u5024\u306F 0 \u3068\u3059\u308B)\n\
    \        \"\"\"\n\n        for a in self.poly[::-1]:\n            if a:\n    \
    \            return a\n        else:\n            return 0\n\n    def censor(self,\
    \ m: int = None):\n        \"\"\" m \u6B21\u4EE5\u964D\u306E\u4FC2\u6570\u3092\
    \u5207\u308A\u6368\u3066\u308B.\n\n        Args:\n            m (int, optional):\
    \ \u5207\u308A\u6368\u3066\u308B\u7CBE\u5EA6. Defaults to None.\n        \"\"\"\
    \n\n        if m is None:\n            m = self.max_degree\n\n        m = min(m,\
    \ self.max_degree)\n        del self.poly[m:]\n\n    def resize(self, m: int):\n\
    \        \"\"\" \u3053\u306E\u591A\u9805\u5F0F\u306E\u60C5\u5831\u3092\u6301\u3063\
    \u3066\u3044\u308B\u914D\u5217\u306E\u9577\u3055\u3092 m \u306B\u3059\u308B (\u77ED\
    \u3044\u5834\u5408\u306F\u672B\u5C3E\u306B 0 \u3092\u8FFD\u52A0\u3057, \u9577\u3044\
    \u5834\u5408\u306F m \u6B21\u4EE5\u4E0A\u3092\u5207\u308A\u6368\u3066\u308B).\n\
    \n        Args:\n            m (int): \u6B21\u6570\n        \"\"\"\n        m\
    \ = min(m, self.max_degree)\n        if len(self.poly) > m:\n            del self.poly[:m]\n\
    \        elif len(self.poly) < m:\n            self.poly.extend([0] * (m - len(self.poly)))\n\
    \n    #\u4EE3\u5165\n    def substitution(self, a: int) -> int:\n        \"\"\"\
    \ \u591A\u9805\u5F0F\u306E\u5909\u6570\u306B a \u3092\u5F62\u5F0F\u7684\u306B\u4EE3\
    \u5165\u3057\u305F\u5F0F\u306E\u5024\u3092\u6C42\u3081\u308B.\n\n        Args:\n\
    \            a (int): \u4EE3\u5165\u3059\u308B\u5024\n\n        Returns:\n   \
    \         int: \u5F0F\u306E\u5024\n        \"\"\"\n\n        y = 0\n        a_pow\
    \ = 1\n        for p in self.poly:\n            y += p * a_pow % Mod\n       \
    \     a_pow = (a_pow * a) % Mod\n        return y % Mod\n\n    def order(self,\
    \ default: int = None) -> int:\n        \"\"\" \u3053\u306E\u5F62\u5F0F\u7684\u30D9\
    \u30AD\u7D1A\u6570\u306E\u4F4D\u6570 (\u4FC2\u6570\u304C 0 \u3067\u306A\u3044\u6B21\
    \u6570\u306E\u3046\u3061\u306E\u6700\u4F4E\u6B21\u6570) \u3092\u6C42\u3081\u308B\
    .\n\n        Args:\n            default (int, optional): \u30BC\u30ED\u591A\u9805\
    \u5F0F\u306E\u8FD4\u308A\u5024. Defaults to None.\n\n        Returns:\n      \
    \      int: \u4F4D\u6570\n        \"\"\"\n\n        for d in range(len(self.poly)):\n\
    \            if self.poly[d]:\n                return d\n        else:\n     \
    \       return default\n\n#=================================================\n\
    class Calculator:\n    def __init__(self):\n        self.primitive = self.__primitive_root()\n\
    \        self.__build_up()\n\n    def __primitive_root(self) -> int:\n       \
    \ \"\"\" Mod \u306E\u539F\u59CB\u6839\u3092\u6C42\u3081\u308B.\n\n        Returns:\n\
    \            int: Mod \u306E\u539F\u59CB\u6839\n        \"\"\"\n\n        p =\
    \ Mod\n        if p == 2:\n            return 1\n        if p == 998244353:\n\
    \            return 3\n        if p == 10**9 + 7:\n            return 5\n    \
    \    if p == 163577857:\n            return 23\n        if p == 167772161:\n \
    \           return 3\n        if p == 469762049:\n            return 3\n\n   \
    \     fac=[]\n        q=2\n        v=p-1\n\n        while v>=q*q:\n          \
    \  e=0\n            while v%q==0:\n                e+=1\n                v//=q\n\
    \n            if e>0:\n                fac.append(q)\n            q+=1\n\n   \
    \     if v>1:\n            fac.append(v)\n\n        for g in range(2, p):\n  \
    \          if pow(g, p-1, p) != 1:\n                return None\n\n          \
    \  flag=True\n            for q in fac:\n                if pow(g, (p-1) // q,\
    \ p) == 1:\n                    flag = False\n                    break\n\n  \
    \          if flag:\n                return g\n\n    #\u53C2\u8003\u5143: https://judge.yosupo.jp/submission/72676\n\
    \    def __build_up(self):\n        rank2=(~(Mod-1) & ((Mod-1)-1)).bit_length()\n\
    \        root=[0]*(rank2+1); iroot=[0]*(rank2+1)\n        rate2=[0]*max(0, rank2-1);\
    \ irate2=[0]*max(0, rank2-1)\n        rate3=[0]*max(0, rank2-2); irate3=[0]*max(0,\
    \ rank2-2)\n\n        root[-1]=pow(self.primitive, (Mod-1)>>rank2, Mod)\n    \
    \    iroot[-1]=pow(root[-1], -1, Mod)\n\n        for i in range(rank2)[::-1]:\n\
    \            root[i]=root[i+1]*root[i+1]%Mod\n            iroot[i]=iroot[i+1]*iroot[i+1]%Mod\n\
    \n        prod=iprod=1\n        for i in range(rank2-1):\n            rate2[i]=root[i+2]*prod%Mod\n\
    \            irate2[i]=iroot[i+2]*prod%Mod\n            prod*=iroot[i+2]; prod%=Mod\n\
    \            iprod*=root[i+2]; iprod%=Mod\n\n        prod=iprod = 1\n        for\
    \ i in range(rank2-2):\n            rate3[i]=root[i + 3]*prod%Mod\n          \
    \  irate3[i]=iroot[i + 3]*iprod%Mod\n            prod*=iroot[i + 3]; prod%=Mod\n\
    \            iprod*=root[i + 3]; iprod%=Mod\n\n        self.root=root; self.iroot=iroot\n\
    \        self.rate2=rate2; self.irate2=irate2\n        self.rate3=rate3; self.irate3=irate3\n\
    \n    def add(self, A: list[int] | int, B: list[int] | int) -> list[int]:\n  \
    \      \"\"\" \u5FC5\u8981\u306A\u3089\u3070\u672B\u5C3E\u306B\u5143\u3092\u8FFD\
    \u52A0\u3057\u3066, [A[i] + B[i]] \u3092\u6C42\u3081\u308B.\n\n        \"\"\"\n\
    \n        if type(A) == list:\n            pass\n        elif type(A) == int:\n\
    \            A = [A]\n        else:\n            raise NotImplementedError\n\n\
    \        if type(B) == list:\n            pass\n        elif type(B) == int:\n\
    \            B = [B]\n        else:\n            raise NotImplementedError\n\n\
    \        m = min(len(A), len(B))\n        C = [(A[i] + B[i]) %Mod for i in range(m)]\n\
    \        C.extend(A[m:])\n        C.extend(B[m:])\n        return C\n\n    def\
    \ sub(self, A: list[int] | int, B: list[int] | int) -> list[int]:\n        \"\"\
    \" \u5FC5\u8981\u306A\u3089\u3070\u672B\u5C3E\u306B\u5143\u3092\u8FFD\u52A0\u3057\
    \u3066, [A[i] - B[i]] \u3092\u6C42\u3081\u308B.\n\n        \"\"\"\n\n        if\
    \ type(A) == list:\n            pass\n        elif type(A) == int:\n         \
    \   A = [A]\n        else:\n            raise NotImplementedError\n\n        if\
    \ type(B) == list:\n            pass\n        elif type(B) == int:\n         \
    \   B = [B]\n        else:\n            raise NotImplementedError\n\n        m\
    \ = min(len(A), len(B))\n        C = [(A[i] - B[i]) % Mod for i in range(m)]\n\
    \        C.extend(A[m:])\n        C.extend([-b % Mod for b in B[m:]])\n      \
    \  return C\n\n    def times(self, A: list[int], k: int) -> list[int]:\n     \
    \   \"\"\" [k * A[i]] \u3092\u6C42\u3081\u308B.\n\n        \"\"\"\n        return\
    \ [k * a % Mod for a in A]\n\n    #\u53C2\u8003\u5143 https://judge.yosupo.jp/submission/72676\n\
    \    def ntt(self, A: list[int]):\n        \"\"\" A \u306B Mod \u3092\u6CD5\u3068\
    \u3059\u308B\u6570\u8AD6\u5909\u63DB\u3092\u65BD\u3059\n\n        \u203B Mod \u306F\
    \u30B0\u30ED\u30FC\u30D0\u30EB\u5909\u6570\u304B\u3089\u6307\u5B9A\n\n       \
    \ References:\n        https://github.com/atcoder/ac-library/blob/master/atcoder/convolution.hpp\n\
    \        https://judge.yosupo.jp/submission/72676\n        \"\"\"\n\n        N=len(A)\n\
    \        H=(N-1).bit_length()\n        l=0\n\n        I=self.root[2]\n       \
    \ rate2=self.rate2; rate3=self.rate3\n\n        while l<H:\n            if H-l==1:\n\
    \                p=1<<(H-l-1)\n                rot=1\n                for s in\
    \ range(1<<l):\n                    offset=s<<(H-l)\n                    for i\
    \ in range(p):\n                        x=A[i+offset]; y=A[i+offset+p]*rot%Mod\n\
    \                        A[i+offset]=(x+y)%Mod\n                        A[i+offset+p]=(x-y)%Mod\n\
    \n                    if s+1!=1<<l:\n                        rot*=rate2[(~s&-~s).bit_length()-1]\n\
    \                        rot%=Mod\n                l+=1\n            else:\n \
    \               p=1<<(H-l-2)\n                rot=1\n                for s in\
    \ range(1<<l):\n                    rot2=rot*rot%Mod\n                    rot3=rot2*rot%Mod\n\
    \                    offset=s<<(H-l)\n                    for i in range(p):\n\
    \                        a0=A[i+offset]\n                        a1=A[i+offset+p]*rot\n\
    \                        a2=A[i+offset+2*p]*rot2\n                        a3=A[i+offset+3*p]*rot3\n\
    \n                        alpha=(a1-a3)%Mod*I\n\n                        A[i+offset]=(a0+a2+a1+a3)%Mod\n\
    \                        A[i+offset+p]=(a0+a2-a1-a3)%Mod\n                   \
    \     A[i+offset+2*p]=(a0-a2+alpha)%Mod\n                        A[i+offset+3*p]=(a0-a2-alpha)%Mod\n\
    \n                    if s+1!=1<<l:\n                        rot*=rate3[(~s&-~s).bit_length()-1]\n\
    \                        rot%=Mod\n                l+=2\n\n    #\u53C2\u8003\u5143\
    \ https://judge.yosupo.jp/submission/72676\n    def inverse_ntt(self, A):\n  \
    \      \"\"\" A \u3092 Mod \u3092\u6CD5\u3068\u3059\u308B\u9006\u6570\u8AD6\u5909\
    \u63DB\u3092\u65BD\u3059\n\n        \u203B Mod \u306F\u30B0\u30ED\u30FC\u30D0\u30EB\
    \u5909\u6570\u304B\u3089\u6307\u5B9A\n\n        References:\n        https://github.com/atcoder/ac-library/blob/master/atcoder/convolution.hpp\n\
    \        https://judge.yosupo.jp/submission/72676\n        \"\"\"\n        N=len(A)\n\
    \        H=(N-1).bit_length()\n        l=H\n\n        J=self.iroot[2]\n      \
    \  irate2=self.rate2; irate3=self.irate3\n\n        while l:\n            if l==1:\n\
    \                p=1<<(H-l)\n                irot=1\n                for s in\
    \ range(1<<(l-1)):\n                    offset=s<<(H-l+1)\n                  \
    \  for i in range(p):\n                        x=A[i+offset]; y=A[i+offset+p]\n\
    \                        A[i+offset]=(x+y)%Mod\n                        A[i+offset+p]=(x-y)*irot%Mod\n\
    \n                    if s+1!=1<<(l-1):\n                        irot*=irate2[(~s&-~s).bit_length()-1]\n\
    \                        irot%=Mod\n                l-=1\n            else:\n\
    \                p=1<<(H-l)\n                irot=1\n                for s in\
    \ range(1<<(l-2)):\n                    irot2=irot*irot%Mod\n                \
    \    irot3=irot2*irot%Mod\n                    offset=s<<(H-l+2)\n           \
    \         for i in range(p):\n                        a0=A[i+offset]\n       \
    \                 a1=A[i+offset+p]\n                        a2=A[i+offset+2*p]\n\
    \                        a3=A[i+offset+3*p]\n\n                        beta=(a2-a3)*J%Mod\n\
    \n                        A[i+offset]=(a0+a1+a2+a3)%Mod\n                    \
    \    A[i+offset+p]=(a0-a1+beta)*irot%Mod\n                        A[i+offset+2*p]=(a0+a1-a2-a3)*irot2%Mod\n\
    \                        A[i+offset+3*p]=(a0-a1-beta)*irot3%Mod\n\n          \
    \          if s+1!=1<<(l-2):\n                        irot*=irate3[(~s&-~s).bit_length()-1]\n\
    \                        irot%=Mod\n                l-=2\n        N_inv=pow(N,\
    \ -1, Mod)\n        for i in range(N):\n            A[i]=N_inv*A[i]%Mod\n\n  \
    \  def non_zero_count(self, A: list[int]) -> int:\n        \"\"\" A \u306B\u3042\
    \u308B\u975E\u96F6\u8981\u7D20\u306E\u500B\u6570\u3092\u6C42\u3081\u308B.\n\n\
    \        Args:\n            A (list[int]):\n\n        Returns:\n            int:\
    \ \u975E\u96F6\u8981\u7D20\u306E\u500B\u6570\n        \"\"\"\n        return len(A)\
    \ - A.count(0)\n\n    def is_sparse(self, A: list[int], threshold: int = 25) ->\
    \ bool:\n        \"\"\"A \u304C\u758E\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\
    \u3059\u308B.\n\n        Args:\n            A (list[int]):\n            threshold\
    \ (int, optional): \u975E\u96F6\u8981\u7D20\u306E\u500B\u6570\u304C threshold\
    \ \u4EE5\u4E0B\u306A\u3089\u3070\u758E\u3068\u5224\u5B9A\u3059\u308B. Defaults\
    \ to 25.\n\n        Returns:\n            bool: \u758E?\n        \"\"\"\n\n  \
    \      return self.non_zero_count(A) <= threshold\n\n    def coefficients_list(self,\
    \ A: list[int]) -> tuple[list[int], list[int]]:\n        \"\"\" A \u306B\u3042\
    \u308B\u975E\u96F6\u8981\u7D20\u306E\u30EA\u30B9\u30C8\u3092\u6C42\u3081\u308B\
    .\n\n        Args:\n            A (list[int]):\n\n        Returns:\n         \
    \   tuple[list[int], list[int]]: ([d[0], ..., d[k-1]], [f[0], ..., f[k-1]]) \u306E\
    \u5F62\u306E\u30EA\u30B9\u30C8.\n                j = 0, 1, ..., k - 1 \u306B\u5BFE\
    \u3057\u3066, a[d[j]] = f[j] \u3067\u3042\u308B\u3053\u3068\u3092\u610F\u5473\u3059\
    \u308B.\n        \"\"\"\n\n        f = []; d = []\n        for i in range(len(A)):\n\
    \            if A[i] == 0:\n                continue\n\n            d.append(i)\n\
    \            f.append(A[i])\n        return d, f\n\n    def convoluton_greedy(self,\
    \ A: list[int], B: list[int]) -> list[int]:\n        \"\"\" \u7573\u307F\u8FBC\
    \u307F\u7A4D A * B \u3092\u611A\u76F4\u306A\u65B9\u6CD5\u3067\u6C42\u3081\u308B\
    .\n\n        Args:\n            A (list[int]):\n            B (list[int]):\n\n\
    \        Returns:\n            list[int]: \u7573\u307F\u8FBC\u307F\u7A4D A * B\n\
    \        \"\"\"\n\n        if len(A) < len(B):\n            A, B = B, A\n\n  \
    \      n = len(A)\n        m = len(B)\n        C = [0] * (n + m - 1)\n       \
    \ for i in range(n):\n            for j in range(m):\n                C[i + j]\
    \ += A[i] * B[j] % Mod\n\n        for k in range(n + m - 1):\n            C[k]\
    \ %= Mod\n\n        return C\n\n    def convolution(self, A: list[int], B: list[int])\
    \ -> list[int]:\n        \"\"\" \u7573\u307F\u8FBC\u307F\u7A4D A * B \u3092\u6C42\
    \u3081\u308B.\n\n        Args:\n            A (list[int]):\n            B (list[int]):\n\
    \n        Returns:\n            list[int]: \u7573\u307F\u8FBC\u307F\u7A4D A *\
    \ B\n        \"\"\"\n\n        if (not A) or (not B):\n            return []\n\
    \n        N=len(A)\n        M=len(B)\n        L=M+N-1\n\n        if min(N,M)<=50:\n\
    \            return self.convoluton_greedy(A, B)\n\n        H=L.bit_length()\n\
    \        K=1<<H\n\n        A=A+[0]*(K-N)\n        B=B+[0]*(K-M)\n\n        self.ntt(A)\n\
    \        self.ntt(B)\n\n        for i in range(K):\n            A[i]=A[i]*B[i]%Mod\n\
    \n        self.inverse_ntt(A)\n\n        return A[:L]\n\n    def autocorrelation(self,\
    \ A: list[int]) -> list[int]:\n        \"\"\" \u81EA\u5206\u81EA\u8EAB\u3068\u306E\
    \u7573\u307F\u8FBC\u307F\u7A4D\u3092\u6C42\u3081\u308B.\n\n        Args:\n   \
    \         A (list[int]):\n\n        Returns:\n            list[int]: \u7573\u307F\
    \u8FBC\u307F\u7A4D A * A\n        \"\"\"\n\n        N=len(A)\n        L=2*N-1\n\
    \n        if N<=50:\n            C=[0]*L\n            for i in range(N):\n   \
    \             for j in range(N):\n                    C[i+j]+=A[i]*A[j]\n    \
    \                C[i+j]%=Mod\n            return C\n\n        H=L.bit_length()\n\
    \        K=1<<H\n\n        A=A+[0]*(K-N)\n\n        self.ntt(A)\n\n        for\
    \ i in range(K):\n            A[i]=A[i]*A[i]%Mod\n        self.inverse_ntt(A)\n\
    \n        return A[:L]\n\n    def multiple_convolution(self, *A: list[int]) ->\
    \ list[int]:\n        \"\"\" A = (A[0], A[1], ..., A[k - 1]) \u306B\u5BFE\u3057\
    \u3066, \u3053\u306E k \u500B\u306E\u7573\u307F\u8FBC\u307F\u7A4D A[0] * A[1]\
    \ * ... * A[k - 1] \u3092\u6C42\u3081\u308B.\n\n        Args:\n            A (list[list[int]]):\
    \ \u7573\u307F\u8FBC\u3080 k \u500B\u306E\u6574\u6570\u306E\u30EA\u30B9\u30C8\n\
    \n        Returns:\n            list[int]: k \u500B\u306E\u7573\u307F\u8FBC\u307F\
    \u7A4D A[0] * A[1] * ... * A[k - 1]\n        \"\"\"\n\n        from collections\
    \ import deque\n\n        if not A:\n            return [1]\n\n        Q=deque(list(range(len(A))))\n\
    \        A=list(A)\n\n        while len(Q)>=2:\n            i=Q.popleft(); j=Q.popleft()\n\
    \            A[i]=self.convolution(A[i], A[j])\n            A[j]=None\n      \
    \      Q.append(i)\n\n        i=Q.popleft()\n        return A[i]\n\n    def inverse(self,\
    \ F: list[int], length: int = None) -> list[int]:\n        \"\"\" F * G = [1,\
    \ 0, 0, ..., 0] (0 \u304C (length - 1) \u500B) \u3092\u6E80\u305F\u3059\u9577\u3055\
    \ length \u306E\u30EA\u30B9\u30C8 G \u3092\u6C42\u3081\u308B.\n\n        Args:\n\
    \            F (list[int]):\n            length (int, optional): \u6C42\u3081\u308B\
    \ G \u306E\u9577\u3055. None \u306E\u3068\u304D\u306F length = len(F) \u3068\u3059\
    \u308B. Defaults to None.\n\n        Returns:\n            list[int]: _description_\n\
    \        \"\"\"\n\n        M = len(F) if length is None else length\n\n      \
    \  if M <= 0:\n            return []\n\n        if self.is_sparse(F):\n      \
    \      # \u611A\u76F4\u306B\u6F38\u5316\u5F0F\u3092\u7528\u3044\u3066\u6C42\u3081\
    \u308B.\n            # \u8A08\u7B97\u91CF: F \u306B\u3042\u308B\u4FC2\u6570\u304C\
    \u975E\u96F6\u306E\u9805\u306E\u500B\u6570\u3092 K, \u6C42\u3081\u308B\u6700\u5927\
    \u6B21\u6570\u3092 N \u3068\u3057\u3066, O(NK) \u6642\u9593\n\n            d,f=self.coefficients_list(F)\n\
    \n            G=[0]*M\n            alpha=pow(F[0], -1, Mod)\n            G[0]=alpha\n\
    \n            for i in range(1, M):\n                for j in range(1, len(d)):\n\
    \                    if d[j]<=i:\n                        G[i]+=f[j]*G[i-d[j]]%Mod\n\
    \                    else:\n                        break\n\n                G[i]%=Mod\n\
    \                G[i]=(-alpha*G[i])%Mod\n            del G[M:]\n        else:\n\
    \            # FFT\u306E\u7406\u8AD6\u3092\u5FDC\u7528\u3057\u3066\u6C42\u3081\
    \u308B.\n            # \u8A08\u7B97\u91CF: \u6C42\u3081\u305F\u3044\u9805\u306E\
    \u500B\u6570\u3092N\u3068\u3057\u3066, O(N log N)\n            # Reference: https://judge.yosupo.jp/submission/42413\n\
    \n            N=len(F)\n            r=pow(F[0], -1, Mod)\n\n            m=1\n\
    \            G=[r]\n            while m<M:\n                A=F[:min(N, 2*m)];\
    \ A+=[0]*(2*m-len(A))\n                B=G.copy(); B+=[0]*(2*m-len(B))\n\n   \
    \             Calc.ntt(A); Calc.ntt(B)\n                for i in range(2*m):\n\
    \                    A[i]=A[i]*B[i]%Mod\n\n                Calc.inverse_ntt(A)\n\
    \                A=A[m:]+[0]*m\n                Calc.ntt(A)\n                for\
    \ i in range(2*m):\n                    A[i]=-A[i]*B[i]%Mod\n                Calc.inverse_ntt(A)\n\
    \n                G.extend(A[:m])\n                m<<=1\n            G=G[:M]\n\
    \        return G\n\n    def flood_div(self, F: list[int], G: list[int]) -> list[int]:\n\
    \        assert F[-1]\n        assert G[-1]\n\n        F_deg=len(F)-1\n      \
    \  G_deg=len(G)-1\n\n        if F_deg<G_deg:\n            return []\n\n      \
    \  m=F_deg-G_deg+1\n        return self.convolution(F[::-1], Calc.inverse(G[::-1],m))[m-1::-1]\n\
    \n    def mod(self, F: list[int], G: list[int]) -> list[int]:\n        while F\
    \ and F[-1] == 0:\n            F.pop()\n\n        while G and G[-1] == 0:\n  \
    \          G.pop()\n\n        if not F:\n            return []\n\n        return\
    \ Calc.sub(F, Calc.convolution(Calc.flood_div(F, G), G))\n\n# \u4EE5\u4E0B \u53C2\
    \u8003\u5143: https://judge.yosupo.jp/submission/28304\ndef Differentiate(P: Modulo_Polynomial)\
    \ -> Modulo_Polynomial:\n    \"\"\" \u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\
    \ P \u306E\u5F62\u5F0F\u7684\u5FAE\u5206 P' \u3092\u6C42\u3081\u308B.\n\n    Args:\n\
    \        P (Modulo_Polynomial): \u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\n\n\
    \    Returns:\n        Modulo_Polynomial: \u5F62\u5F0F\u7684\u5FAE\u5206 P'\n\
    \    \"\"\"\n\n    poly = P.poly\n    diff_poly = [(k * poly[k]) % Mod for k in\
    \ range(1, len(poly))]\n    return Modulo_Polynomial(diff_poly, P.max_degree)\n\
    \ndef Integrate(P: Modulo_Polynomial, constant: int = 0) -> Modulo_Polynomial:\n\
    \    \"\"\" \u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570 P \u306E\u5F62\u5F0F\u7684\
    \u306A\u4E0D\u5B9A\u7A4D\u5206 Int(P) \u3092\u6C42\u3081\u308B. \u305F\u3060\u3057\
    , \u5B9A\u6570\u9805\u306F constant \u3068\u3059\u308B.\n\n    Args:\n       \
    \ P (Modulo_Polynomial): \u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\n        constant\
    \ (int, optional): \u5B9A\u6570\u9805. Defaults to 0.\n\n    Returns:\n      \
    \  Modulo_Polynomial: P \u306E\u5F62\u5F0F\u7684\u306A\u4E0D\u5B9A\u7A4D\u5206\
    \n    \"\"\"\n\n    if not P.poly:\n        return Modulo_Polynomial([constant],\
    \ P.max_degree)\n\n    n = len(P.poly)\n    inv = [0] * (n + 1)\n    inv[1] =\
    \ 1\n    for x in range(2, n + 1):\n        q, r = divmod(Mod, x)\n        inv[x]\
    \ = (-q * inv[r]) % Mod\n\n    integrate_poly = [0] + [(inv[k] * a) % Mod for\
    \ k, a in enumerate(P.poly,1)]\n    return Modulo_Polynomial(integrate_poly, P.max_degree\
    \ + 1)\n\n# \u7D2F\u4E57,\u6307\u6570,\u5BFE\u6570\ndef Log(P: Modulo_Polynomial)\
    \ -> Modulo_Polynomial:\n    \"\"\" \u5B9A\u6570\u9805\u304C 1 \u3067\u3042\u308B\
    \u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570 P \u306E\u5BFE\u6570 Log(P) \u3092\u6C42\
    \u3081\u308B.\n\n    Args:\n        P (Modulo_Polynomial): \u5B9A\u6570\u9805\u304C\
    \ 1 \u3067\u3042\u308B\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\n\n    Raises:\n\
    \        ValueError: \u5B9A\u6570\u9805\u304C 1 \u3067\u306A\u3044\u3068\u304D\
    \u306B\u767A\u751F\n\n    Returns:\n        Modulo_Polynomial: Log(P)\n    \"\"\
    \"\n\n    if P[0] != 1:\n        raise ValueError(\"\u5B9A\u6570\u9805\u304C 1\
    \ \u3067\u306F\u3042\u308A\u307E\u305B\u3093\")\n\n    Q = Integrate(Differentiate(P)\
    \ / P)\n    Q.censor(P.max_degree)\n    return Q\n\ndef Exp(P: Modulo_Polynomial)\
    \ -> Modulo_Polynomial:\n    \"\"\" \u5B9A\u6570\u9805\u304C 0 \u3067\u3042\u308B\
    \u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570 P \u306B\u5BFE\u3059\u308B Exp(P) \u3092\
    \u6C42\u3081\u308B.\n\n    Args:\n        P (Modulo_Polynomial): \u5B9A\u6570\u9805\
    \u304C 0 \u3067\u3042\u308B\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\n\n    Raises:\n\
    \        ValueError: \u5B9A\u6570\u9805\u304C 0 \u3067\u306F\u306A\u3044\u5834\
    \u5408\u306B\u767A\u751F\n\n    Returns:\n        Modulo_Polynomial: Exp(P)\n\n\
    \    References:\n        (1) https://arxiv.org/pdf/1301.5804.pdf\n        (2)\
    \ https://opt-cp.com/fps-fast-algorithms/\n    \"\"\"\n\n    from itertools import\
    \ zip_longest\n\n    if P[0] != 0:\n        raise ValueError(\"\u5B9A\u6570\u9805\
    \u304C 0 \u3067\u306F\u3042\u308A\u307E\u305B\u3093\")\n\n    n = P.max_degree\n\
    \    inv = [0] * (2 * n + 1)\n    inv[1] = 1\n    for x in range(2, 2 * n + 1):\n\
    \        q, r = divmod(Mod, x)\n        inv[x] = (-q * inv[r]) % Mod\n\n    H\
    \ = P.poly\n    H.extend([0] * (n - len(H)))\n\n    # \u758E\u306E\u5834\u5408\
    \u306B\u306F\u305D\u308C\u5C02\u7528\u306E\u51E6\u7406\u3092\u884C\u3046.\n  \
    \  if Calc.is_sparse(H):\n        F = [0] * n\n        F[0] = 1\n\n        d,\
    \ f = Calc.coefficients_list(H)\n        K = len(d)\n\n        for t in range(K):\n\
    \            f[t] = (d[t] * f[t]) %Mod\n            d[t] -= 1\n\n        for i\
    \ in range(1, n):\n            a = 0\n            for j in range(K):\n       \
    \         if d[j] > i - 1:\n                    break\n\n                a +=\
    \ f[j] * F[(i - 1) - d[j]] % Mod\n\n            a %= Mod\n            F[i] = a\
    \ * inv[i] % Mod\n\n        return Modulo_Polynomial(F[:n], P.max_degree)\n\n\
    \    dH = [(k * a) % Mod for k, a in enumerate(H[1:], 1)]\n    F, G, m = [1],\
    \ [1], 1\n\n    while m <= n:\n        #2.a'\n        if m > 1:\n            E\
    \ = Calc.convolution(F, Calc.autocorrelation(G)[:m])[:m]\n            G = [(2\
    \ * a - b) % Mod for a, b in zip_longest(G, E, fillvalue = 0)]\n\n        #2.b',\
    \ 2.c'\n        C = Calc.convolution(F, dH[:m - 1])\n        R = [0] * m\n   \
    \     for i, a in enumerate(C):\n            R[i % m] += a\n        R = [a % Mod\
    \ for a in R]\n\n        #2.d'\n        dF = [(k * a) % Mod for k, a in enumerate(F[1:],\
    \ 1)]\n        D = [0] + [(a - b) % Mod for a, b in zip_longest(dF, R, fillvalue\
    \ = 0)]\n        S = [0] * m\n        for i, a in enumerate(D):\n            S[i\
    \ % m] += a\n        S = [a % Mod for a in S]\n\n        #2.e'\n        T = Calc.convolution(G,\
    \ S)[:m]\n\n        #2.f'\n        E = [0] * (m - 1) + T\n        E = [0] + [(inv[k]\
    \ * a) % Mod for k, a in enumerate(E, 1)]\n        U = [(a - b) % Mod for a, b\
    \ in zip_longest(H[:2 * m], E, fillvalue = 0)][m:]\n\n        #2.g'\n        V\
    \ = Calc.convolution(F, U)[:m]\n\n        #2.h'\n        F.extend(V)\n\n     \
    \   #2.i'\n        m <<= 1\n\n    return Modulo_Polynomial(F[:n], P.max_degree)\n\
    \ndef Root(P: Modulo_Polynomial, k: int) -> Modulo_Polynomial:\n    \"\"\" \u5B9A\
    \u6570\u9805\u304C 1 \u3067\u3042\u308B\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\
    \ P \u306E k \u4E57\u6839\u3092\u6C42\u3081\u308B\n\n    Args:\n        P (Modulo_Polynomial):\
    \ \u5B9A\u6570\u9805\u304C 1 \u3067\u3042\u308B\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\
    \u6570\n        k (int): Mod \u306E\u500D\u6570\u3067\u306F\u306A\u3044\u6574\u6570\
    \n\n    Raises:\n        ValueError: \u5B9A\u6570\u9805\u304C 0 \u3067\u306A\u3044\
    \u5834\u5408\u306B\u767A\u751F\n        ValueError: k \u304C Mod \u306E\u500D\u6570\
    \u3067\u3042\u308B\u5834\u5408\u306B\u767A\u751F\n\n    Returns:\n        Modulo_Polynomial:\
    \ Q^k = P, [X^0]Q = 1 \u3092\u6E80\u305F\u3059\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\
    \u6570 Q\n    \"\"\"\n\n    if P[0] != 1:\n        raise ValueError(\"\u5B9A\u6570\
    \u9805\u304C 1 \u3067\u306F\u3042\u308A\u307E\u305B\u3093\")\n\n    k %= Mod\n\
    \    if k == 0:\n        raise ValueError(\"k \u304C\u7279\u7570\u3067\u3059\"\
    )\n\n    return Power(P, pow(k, -1, Mod))\n\n\n# \u4E09\u89D2\u95A2\u6570\n# \u6B63\
    \u5F26\ndef Sin(P: Modulo_Polynomial) -> Modulo_Polynomial:\n    \"\"\" \u5B9A\
    \u6570\u9805\u304C 0 \u3067\u3042\u308B\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\
    \ P \u306B\u5BFE\u3057\u3066, Sin(P) \u3092\u6C42\u3081\u308B.\n\n    Args:\n\
    \        P (Modulo_Polynomial): \u5B9A\u6570\u9805\u304C 0 \u3067\u3042\u308B\u5F62\
    \u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\n\n    Raises:\n        ValueError: \u5B9A\
    \u6570\u9805\u304C 0 \u3067\u306A\u3044\u5834\u5408\u306B\u767A\u751F\n\n    Returns:\n\
    \        Modulo_Polynomial: Sin(P)\n    \"\"\"\n\n    if P[0] != 0:\n        raise\
    \ ValueError(\"\u5B9A\u6570\u9805\u304C 0 \u3067\u306F\u3042\u308A\u307E\u305B\
    \u3093\")\n\n    I = Tonelli_Shanks(-1)\n    B = I * P\n    B_exp = Exp(B)\n \
    \   C = B_exp - (1 / B_exp)\n    return C * pow(2 * I, -1, Mod)\n\n#\u4F59\u5F26\
    \ndef Cos(P: Modulo_Polynomial) -> Modulo_Polynomial:\n    \"\"\" \u5B9A\u6570\
    \u9805\u304C 0 \u3067\u3042\u308B\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570 P\
    \ \u306B\u5BFE\u3057\u3066, Cos(P) \u3092\u6C42\u3081\u308B.\n\n    Args:\n  \
    \      P (Modulo_Polynomial): \u5B9A\u6570\u9805\u304C 0 \u3067\u3042\u308B\u5F62\
    \u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\n\n    Raises:\n        ValueError: \u5B9A\
    \u6570\u9805\u304C 0 \u3067\u306A\u3044\u5834\u5408\u306B\u767A\u751F\n\n    Returns:\n\
    \        Modulo_Polynomial: Cos(P)\n    \"\"\"\n    if P[0] != 0:\n        raise\
    \ ValueError(\"\u5B9A\u6570\u9805\u304C 0 \u3067\u306F\u3042\u308A\u307E\u305B\
    \u3093\")\n\n    I = Tonelli_Shanks(-1)\n    B = I * P\n    B_exp = Exp(B)\n \
    \   C = B_exp + (1 / B_exp)\n    return C * pow(2, -1, Mod)\n\n#\u6B63\u63A5\n\
    def Tan(P: Modulo_Polynomial) -> Modulo_Polynomial:\n    \"\"\" \u5B9A\u6570\u9805\
    \u304C 0 \u3067\u3042\u308B\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570 P \u306B\
    \u5BFE\u3057\u3066, Tan(P) \u3092\u6C42\u3081\u308B.\n\n    Args:\n        P (Modulo_Polynomial):\
    \ \u5B9A\u6570\u9805\u304C 0 \u3067\u3042\u308B\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\
    \u6570\n\n    Raises:\n        ValueError: \u5B9A\u6570\u9805\u304C 0 \u3067\u306A\
    \u3044\u5834\u5408\u306B\u767A\u751F\n\n    Returns:\n        Modulo_Polynomial:\
    \ Tan(P)\n    \"\"\"\n\n    if P[0] != 0:\n        raise ValueError(\"\u5B9A\u6570\
    \u9805\u304C 0 \u3067\u306F\u3042\u308A\u307E\u305B\u3093\")\n\n    I = Tonelli_Shanks(-1)\n\
    \    B = I * P\n    B_exp = Exp(B)\n    B_sin = (B_exp - 1 / B_exp) * pow(2 *\
    \ I, -1, Mod)\n    B_cos = (B_exp + 1 / B_exp) * pow(2, -1, Mod)\n    return B_sin\
    \ / B_cos\n\n#\u9006\u6B63\u5F26\ndef ArcSin(P: Modulo_Polynomial) -> Modulo_Polynomial:\n\
    \    \"\"\" \u5B9A\u6570\u9805\u304C 0 \u3067\u3042\u308B\u5F62\u5F0F\u7684\u30D9\
    \u30AD\u7D1A\u6570\u306B\u5BFE\u3057\u3066, ArcSin(P) \u3092\u6C42\u3081\u308B\
    .\n\n    Args:\n        P (Modulo_Polynomial): \u5B9A\u6570\u9805\u304C 0 \u3067\
    \u3042\u308B\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\n\n    Raises:\n      \
    \  ValueError: \u5B9A\u6570\u9805\u304C 0 \u3067\u306A\u3044\u5834\u5408\u306B\
    \u767A\u751F\n\n    Returns:\n        Modulo_Polynomial: ArcSin(P)\n    \"\"\"\
    \n\n    if P[0] != 0:\n        raise ValueError(\"\u5B9A\u6570\u9805\u304C 0 \u3067\
    \u306F\u3042\u308A\u307E\u305B\u3093\")\n\n    return Integrate(Differentiate(P)\
    \ / Sqrt(1 - P * P))\n\n#\u9006\u4F59\u5F26\ndef ArcCos(P: Modulo_Polynomial)\
    \ -> Modulo_Polynomial:\n    \"\"\" \u5B9A\u6570\u9805\u304C 0 \u3067\u3042\u308B\
    \u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\u306B\u5BFE\u3057\u3066, ArcCos(P)\
    \ \u3092\u6C42\u3081\u308B. \u203B \u5B9F\u969B\u306B\u306F, ArcCos(0) = pi /\
    \ 2 \u3067\u3042\u308B\u305F\u3081, \u6CE8\u610F\u304C\u5FC5\u8981\u3067\u3042\
    \u308B.\n\n    Args:\n        P (Modulo_Polynomial): \u5B9A\u6570\u9805\u304C\
    \ 0 \u3067\u3042\u308B\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\n\n    Raises:\n\
    \        ValueError: \u5B9A\u6570\u9805\u304C 0 \u3067\u306A\u3044\u5834\u5408\
    \u306B\u767A\u751F\n\n    Returns:\n        Modulo_Polynomial: ArcCos(P) \u306E\
    \ 1 \u6B21\u4EE5\u964D\u306E\u4FC2\u6570\n    \"\"\"\n\n    if P[0] != 0:\n  \
    \      raise ValueError(\"\u5B9A\u6570\u9805\u304C 0 \u3067\u306F\u3042\u308A\u307E\
    \u305B\u3093\")\n\n    return -ArcSin(P)\n\n#\u9006\u6B63\u63A5\ndef ArcTan(P:\
    \ Modulo_Polynomial) -> Modulo_Polynomial:\n    \"\"\" \u5B9A\u6570\u9805\u304C\
    \ 0 \u3067\u3042\u308B\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\u306B\u5BFE\u3057\
    \u3066, ArcTan(P) \u3092\u6C42\u3081\u308B.\n    Args:\n        P (Modulo_Polynomial):\
    \ \u5B9A\u6570\u9805\u304C 0 \u3067\u3042\u308B\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\
    \u6570\n\n    Raises:\n        ValueError: \u5B9A\u6570\u9805\u304C 0 \u3067\u306A\
    \u3044\u5834\u5408\u306B\u767A\u751F\n\n    Returns:\n        Modulo_Polynomial:\
    \ ArcCos(P) \u306E 1 \u6B21\u4EE5\u964D\u306E\u4FC2\u6570\n    \"\"\"\n\n    if\
    \ P[0] != 0:\n        raise ValueError(\"\u5B9A\u6570\u9805\u304C 0 \u3067\u306F\
    \u3042\u308A\u307E\u305B\u3093\")\n\n    return Integrate(Differentiate(P) / (1\
    \ + P * P))\n\ndef Power(P: Modulo_Polynomial, M: int) -> Modulo_Polynomial:\n\
    \    \"\"\" \u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570 P \u306E M \u4E57\u3092\
    \u6C42\u3081\u308B.\n\n    Args:\n        P (Modulo_Polynomial): \u5F62\u5F0F\u7684\
    \u30D9\u30AD\u7D1A\u6570\n        M (int): \u975E\u8CA0\u6574\u6570\n\n    Raises:\n\
    \        ValueError: M \u304C\u8CA0\u306E\u3068\u304D\u306B\u767A\u751F\n\n  \
    \  Returns:\n        Modulo_Polynomial: P \u306E M \u4E57\n    \"\"\"\n\n    if\
    \ M < 0:\n        raise ValueError(\"M \u306F\u975E\u8CA0\u3067\u306A\u304F\u3066\
    \u306F\u306A\u308A\u307E\u305B\u3093\")\n    elif M == 0:\n        # M = 0\u3000\
    \u306E\u3068\u304D\u306F P^0 = 1 \u78BA\u5B9A.\n        return Modulo_Polynomial([1],\
    \ P.max_degree)\n\n    n = P.max_degree\n    F = P.poly\n    F.extend([0] *((n\
    \ + 1) - len(F)))\n\n    # \u4FC2\u6570\u304C 0 \u3067\u306F\u306A\u3044\u6700\
    \u4F4E\u6B21\u306E\u6B21\u6570\u3068\u305D\u306E\u4FC2\u6570\u3092\u6C42\u3081\
    \u308B.\n    if (ord := P.order(-1)) == -1:\n        return Modulo_Polynomial([0],\
    \ P.max_degree)\n\n    if ord * M > n:\n        # M \u4E57\n        return Modulo_Polynomial([0],\
    \ P.max_degree)\n\n    lowest = F[ord]\n    lowest_inv = pow(lowest, -1, Mod)\n\
    \    M_mod = M % Mod\n\n    if Calc.is_sparse(F):\n        # P \u304C\u758E\u306A\
    \u5834\u5408\n        H = [(lowest_inv * a) % Mod for a in F[ord:]] + [0]\n  \
    \      Nh = len(H) - 1\n        d, _ = Calc.coefficients_list(H)\n        K =\
    \ len(d)\n\n        inv = [0] * (Nh + 1)\n        inv[1] = 1\n        for x in\
    \ range(2, Nh+1):\n            q, r = divmod(Mod, x)\n            inv[x] = (-q\
    \ * inv[r]) % Mod\n\n        G = [0] * Nh; G[0] = 1\n        for i in range(Nh\
    \ - 1):\n            g = (M_mod * (i + 1) % Mod) * H[i + 1] % Mod\n          \
    \  for j in range(K):\n                if not (1 <= d[j] <= i):\n            \
    \        continue\n\n                alpha = (d[j] * M_mod - (i - d[j] + 1)) %\
    \ Mod\n                beta = G[i + 1 - d[j]] * H[d[j]] % Mod\n              \
    \  g += alpha * beta % Mod\n            g %= Mod\n\n            G[i + 1] = g *\
    \ inv[i + 1] % Mod\n    else:\n        # P \u304C\u5BC6\u306A\u5834\u5408\n  \
    \      # P^M = Exp(M Log(P)) \u3092\u5229\u7528\u3059\u308B\n\n        Q = Modulo_Polynomial([(lowest_inv\
    \ * a) % Mod for a in F[ord:]], P.max_degree)\n        G = Exp(M_mod*Log(Q)).poly\n\
    \n    lowest_k = pow(lowest, M, Mod)\n    G = [0] * (ord * M) + [(lowest_k * a)\
    \ % Mod for a in G]\n    return Modulo_Polynomial(G, P.max_degree)\n\n#\u6839\u53F7\
    \ndef Tonelli_Shanks(X: int, default: int = -1) -> int:\n    \"\"\" X=a (mod Mod)\
    \ \u306E\u3068\u304D, r*r=a (mod Mod) \u3092\u6E80\u305F\u3059 r \u3092\u8FD4\u3059\
    .\n\n    \u203B\u6CD5p\u304C\u7D20\u6570\u306E\u3068\u304D\u306E\u307F\u6709\u52B9\
    \n    \u203B\u5B58\u5728\u3057\u306A\u3044\u3068\u304D\u306F default \u304C\u8FD4\
    \u308A\u5024\n    \"\"\"\n\n    #\u30EB\u30B8\u30E3\u30F3\u30C9\u30EB\u8A18\u53F7\
    \n    def Legendre(X):\n        \"\"\"\u30EB\u30B8\u30E3\u30F3\u30C9\u30EB\u8A18\
    \u53F7 (a/Mod) \u3092\u8FD4\u3059.\n\n        \u203B\u6CD5\u304C\u7D20\u6570\u306E\
    \u3068\u304D\u306E\u307F\u6210\u7ACB\u3059\u308B.\n        \"\"\"\n\n        if\
    \ X % Mod == 0:\n            return 0\n        elif pow(X, (Mod - 1) // 2, Mod)\
    \ == 1:\n            return 1\n        else:\n            return -1\n\n    X %=\
    \ Mod\n    if Legendre(X) == -1:\n        return default\n\n    from random import\
    \ randint as ri\n    if X == 0:\n        return X\n    elif Mod == 2:\n      \
    \  return X\n    elif Mod % 4 == 3:\n        return pow(X, (Mod + 1) // 4,Mod)\n\
    \n    u = 2\n    s = 1\n    while (Mod - 1) % (2 * u) == 0:\n        u *= 2\n\
    \        s += 1\n\n    q = (Mod - 1) // u\n    z = 0\n    while pow(z, (Mod -\
    \ 1) // 2, Mod) != Mod - 1:\n        z = ri(1, Mod - 1)\n\n    m, c, t, r = s,\
    \ pow(z, q, Mod), pow(X, q, Mod), pow(X, (q + 1) // 2, Mod)\n    while m > 1:\n\
    \        if pow(t, pow(2, m - 2), Mod) == 1:\n            c = (c * c) % Mod\n\
    \            m = m - 1\n        else:\n            c, t, r, m = (c * c) % Mod,\
    \ (c * c * t) % Mod, (c * r) % Mod, m - 1\n    return r\n\n#\u591A\u9805\u5F0F\
    \u306E\u6839\u53F7\ndef __sqrt(F, N):\n    F+=[0]*(N-len(F))\n    s=Tonelli_Shanks(F[0])\n\
    \    if s==-1:\n        return None\n\n    two_inv=pow(2, -1, Mod)\n\n    if not\
    \ Calc.is_sparse(F):\n        # P \u304C\u758E\u306A\u5834\u5408\n        F.append(0)\n\
    \        d,f=Calc.coefficients_list(F); K=len(d)\n\n        Inv=[0]*(N+1); Inv[1]=1\n\
    \        for i in range(2, N+1):\n            q,r=divmod(Mod, i)\n           \
    \ Inv[i]=(-q*Inv[r])%Mod\n\n        G=[0]*N; G[0]=1\n        for i in range(N):\n\
    \            g=(two_inv*(i+1)%Mod)*F[i+1]%Mod\n            for j in range(K):\n\
    \                if 1<=d[j]<=i:\n                    alpha=(d[j]*two_inv-(i-d[j]+1))%Mod\n\
    \                    beta=G[i+1-d[j]]*F[d[j]]%Mod\n                    g+=alpha*beta\n\
    \            g%=Mod\n            G[i+1]=g*Inv[i+1]%Mod\n    else:\n        m=1\n\
    \        G=[min(s,Mod-s)]\n\n        while m<N:\n            G+=[0]*m\n      \
    \      m<<=1\n            H=Calc.convolution(F[:m], Calc.inverse(G))\n       \
    \     G=[two_inv*(a+b)%Mod for a,b in zip(G,H)]\n    return G[:N]\n\ndef Sqrt(P:\
    \ Modulo_Polynomial) -> Modulo_Polynomial:\n    \"\"\" Q^2 = P \u3092\u6E80\u305F\
    \u3059\u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570 Q \u3092\u6C42\u3081\u308B\n\n\
    \    Args:\n        P (Modulo_Polynomial):\n\n    Returns:\n        Modulo_Polynomial:\
    \ Q^2 = P \u3092\u6E80\u305F\u3059 Q\n    \"\"\"\n\n    N = P.max_degree\n   \
    \ F = P.poly\n\n    for d, p in enumerate(F):\n        if p:\n            break\n\
    \    else:\n        return Modulo_Polynomial([0], P.max_degree)\n\n    if d %\
    \ 2 == 1:\n        return None\n\n    E = __sqrt(F[d:], N - d // 2)\n    if E\
    \ is None:\n        return\n\n    E = [0] * (d // 2) + E\n    return Modulo_Polynomial(E,\
    \ P.max_degree)\n\n\n# \u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\u6570\u306B\u5BFE\u3059\
    \u308B\u7279\u5225\u306A\u64CD\u4F5C\ndef Composition(P: Modulo_Polynomial, Q:\
    \ Modulo_Polynomial) -> Modulo_Polynomial:\n    \"\"\" \u5F62\u5F0F\u7684\u30D9\
    \u30AD\u7D1A\u6570 P \u3068\u5B9A\u6570\u9805\u304C 0 \u3067\u3042\u308B\u5F62\
    \u5F0F\u7684\u30D9\u30AD\u7D1A\u6570 0 \u306B\u5BFE\u3057\u3066, P o Q = P(Q)\
    \ \u3092\u6C42\u3081\u308B (\u203B \u9806\u756A\u6CE8\u610F).\n\n    Args:\n \
    \       P (Modulo_Polynomial): \u5916\u5074\n        Q (Modulo_Polynomial): \u5185\
    \u5074\n\n    Raises:\n        Modulo_Polynomial: Q \u306E\u5B9A\u6570\u9805\u304C\
    \ 0 \u3067\u306A\u3044\u6642\u306B\u767A\u751F\n\n    Returns:\n        Modulo_Polynomial:\
    \ \u5408\u6210 P o Q\n\n    Reference:\n        https://judge.yosupo.jp/submission/42372\n\
    \    \"\"\"\n\n    if Q[0] != 0:\n        raise Modulo_Polynomial\n\n    deg =\
    \ min(P.max_degree, Q.max_degree)\n    k = int(deg ** 0.5 + 1)\n    d = (deg +\
    \ k) // k\n\n    X = [[1]]\n    for i in range(k):\n        X.append(Calc.convolution(X[-1],\
    \ Q.poly)[:deg + 1])\n\n    Y = [[0] * len(X[k]) for _ in range(k)]\n    for i,\
    \ y in enumerate(Y):\n        for j, x in enumerate(X[:d]):\n            if i\
    \ * d + j > deg:\n                break\n\n            for t in range(deg + 1):\n\
    \                if t >= len(x):\n                    break\n\n              \
    \  if t < len(y):\n                    y[t] += x[t] * P[i * d + j] % Mod\n\n \
    \   F = [0] * (deg + 1)\n    Z = [1]\n    x = X[d]\n    for i in range(k):\n \
    \       Y[i] = Calc.convolution(Y[i], Z)[:deg + 1]\n        for j in range(len(Y[i])):\n\
    \            F[j] += Y[i][j]\n        Z = Calc.convolution(Z, x)[:deg + 1]\n \
    \   return Modulo_Polynomial(F, deg)\n\ndef Taylor_Shift(P: Modulo_Polynomial,\
    \ a: int) -> Modulo_Polynomial:\n    \"\"\" \u5F62\u5F0F\u7684\u30D9\u30AD\u7D1A\
    \u6570 P \u3068\u6574\u6570 a \u306B\u5BFE\u3057\u3066, P(X + a) \u3092\u6C42\u3081\
    \u308B.\n\n    Args:\n        P (Modulo_Polynomial): \u5F62\u5F0F\u7684\u30D9\u30AD\
    \u7D1A\u6570\n        a (int): \u5B9A\u6570\n\n    Returns:\n        Modulo_Polynomial:\
    \ P(X + a)\n    \"\"\"\n\n    n = len(P.poly) - 1\n\n    fact = [0] * (n + 1)\n\
    \    fact[0] = 1\n    for i in range(1, n + 1):\n        fact[i] = (fact[i-1]\
    \ * i) % Mod\n\n    fact_inv = [0] * (n + 1)\n    fact_inv[-1] = pow(fact[-1],\
    \ -1, Mod)\n    for i in range(n - 1, -1, -1):\n        fact_inv[i] = (fact_inv[i\
    \ + 1] * (i + 1)) % Mod\n\n    f = P.poly.copy()\n    for i in range(n+1):\n \
    \       f[i] = (f[i] * fact[i]) % Mod\n\n    g = [0] * (n + 1)\n    c = 1\n  \
    \  for i in range(n+1):\n        g[i] = (c * fact_inv[i]) % Mod\n        c = (c\
    \ * a) % Mod\n    g.reverse()\n\n    h = Calc.convolution(f, g)[n:]\n    for i\
    \ in range(len(h)):\n        h[i] = (h[i] * fact_inv[i]) % Mod\n\n    return Modulo_Polynomial(h,\
    \ P.max_degree)\n\ndef Polynominal_Coefficient(P: Modulo_Polynomial, Q: Modulo_Polynomial,\
    \ N: int) -> int:\n    \"\"\" [X^N] P/Q \u3092\u6C42\u3081\u308B.\n\n    Args:\n\
    \        P (Modulo_Polynomial): \u5206\u5B50\n        Q (Modulo_Polynomial): \u5206\
    \u6BCD\n        N (int): \u6B21\u6570\n\n    Returns:\n        int: [X^N] P/Q\n\
    \n    References:\n        http://q.c.titech.ac.jp/docs/progs/polynomial_division.html\n\
    \        https://arxiv.org/abs/2008.08822\n        https://arxiv.org/pdf/2008.08822.pdf\n\
    \    \"\"\"\n\n    p = P.poly.copy()\n    q = Q.poly.copy()\n    m = 1 << ((len(q)-1).bit_length())\n\
    \    p.extend([0] * (2 * m - len(p)))\n    q.extend([0] * (2 * m - len(q)))\n\n\
    \    while N:\n        r = [q[i] if i & 1 == 0 else -q[i] for i in range(2 * m)]\n\
    \n        Calc.ntt(p)\n        Calc.ntt(q)\n        Calc.ntt(r)\n        for i\
    \ in range(2*m):\n            p[i] *= r[i]; p[i] %= Mod\n            q[i] *= r[i];\
    \ q[i] %= Mod\n\n        Calc.inverse_ntt(p)\n        Calc.inverse_ntt(q)\n  \
    \      if N & 1 == 0:\n            for i in range(m):\n                p[i] =\
    \ p[2 * i]\n        else:\n            for i in range(m):\n                p[i]\
    \ = p[2 * i + 1]\n\n        for i in range(m):\n            q[i] = q[2 * i]\n\n\
    \        for i in range(m, 2 * m):\n            p[i] = q[i] = 0\n\n        N >>=\
    \ 1\n\n    if q[0] == 1:\n        return p[0]\n    else:\n        return p[0]\
    \ * pow(q[0], -1, Mod) % Mod\n\ndef Multipoint_Evaluation(P: Modulo_Polynomial,\
    \ X: list[int]) -> list[int]:\n    \"\"\" \u591A\u9805\u5F0F P \u306B\u5BFE\u3057\
    \u3066, X = [x[0], ..., x[n - 1]] \u3068\u3057\u305F\u3068\u304D, [P(x[0]), ...,\
    \ P(x[n - 1])] \u3092\u6C42\u3081\u308B.\n\n    Args:\n        P (Modulo_Polynomial):\
    \ \u591A\u9805\u5F0F\n        X (list[int]): \u5F15\u6570\u306E\u30EA\u30B9\u30C8\
    \n\n    Returns:\n        int: \u9577\u3055 n \u306E\u30EA\u30B9\u30C8. \u7B2C\
    \ j \u8981\u7D20\u306F P(x[j]) \u3067\u3042\u308B.\n    \"\"\"\n\n    n = len(X)\n\
    \    size = 1 << (n - 1).bit_length()\n\n    G = [[1] for _ in range(2*size)]\n\
    \n    for i in range(n):\n        G[i + size] = [-X[i], 1]\n\n    for i in range(size\
    \ - 1, 0, -1):\n        G[i] = Calc.convolution(G[2*i], G[2*i+1])\n\n    for i\
    \ in range(1, 2*size):\n        A = P.poly if i == 1 else G[i>>1]\n        m =\
    \ len(A) - len(G[i]) + 1\n        v = Calc.convolution(A[::-1][:m], Calc.inverse(G[i][::-1],m))[m\
    \ - 1::-1]\n        w = Calc.convolution(v, G[i])\n\n        G[i] = A.copy()\n\
    \        g = G[i]\n\n        for j in range(len(w)):\n            g[j] -= w[j]\n\
    \            g[j] %= Mod\n\n        while len(g) > 1 and g[-1] == 0:\n       \
    \     g.pop()\n\n    return [G[i + size][0] for i in range(n)]\n\ndef Polynominal_Interpolation(X:\
    \ list[int], Y: list[int]) -> Modulo_Polynomial:\n    \"\"\" n = |X| = |Y| \u3068\
    \u3059\u308B. P(x_i) = y_i (0 <= i < n) \u3092\u6E80\u305F\u3059\u9AD8\u3005 (n-1)\
    \ \u6B21\u306E\u591A\u9805\u5F0F P \u3092\u6C42\u3081\u308B.\n\n    Args:\n  \
    \      X (list[int]): X\n        Y (list[int]): Y\n\n    Raises:\n        ValueError:\
    \ |X| != |Y| \u306E\u3068\u304D\u306B\u767A\u751F\n\n    Returns:\n        Modulo_Polynomial:\
    \ P(x_i) = y_i (0 <= i < n) \u3092\u6E80\u305F\u3059\u9AD8\u3005 (n-1) \u6B21\u306E\
    \u591A\u9805\u5F0F P\n    \"\"\"\n\n    if len(X) != len(Y):\n        raise ValueError(\"\
    X, Y \u306E\u9577\u3055\u304C\u7B49\u3057\u304F\u306A\u3051\u308C\u3070\u306A\u308A\
    \u307E\u305B\u3093\")\n\n    n = len(X)\n    size = 1 << (n - 1).bit_length()\n\
    \n    T = [[1] for _ in range(2 * size)]\n\n    for i in range(n):\n        T[i\
    \ + size] = [-X[i], 1]\n\n    for i in range(size - 1, 0, -1):\n        T[i] =\
    \ Calc.convolution(T[2 * i], T[2 * i + 1])\n\n    U = [[] for _ in range(2 * size)]\n\
    \    U[1] = [k * a for k, a in enumerate(T[1][1:], 1)]\n\n    for i in range(2,\
    \ n + size):\n        m = len(U[i//2]) - len(T[i]) + 1\n        v = Calc.convolution(U[i\
    \ // 2][::-1][:m], Calc.inverse(T[i][::-1], m))[m - 1::-1]\n        w = Calc.convolution(v,\
    \ T[i])\n\n        U[i] = U[i//2].copy()\n        u = U[i]\n        for j in range(len(w)):\n\
    \            u[j] -= w[j]\n            u[j] %= Mod\n\n        while len(u) > 1\
    \ and u[-1] == 0:\n            u.pop()\n\n    for i in range(n):\n        U[i\
    \ + size] = [(Y[i] * pow(U[i + size][0], -1, Mod)) % Mod]\n\n    for i in range(size\
    \ - 1, 0, -1):\n        A = Calc.convolution(U[2 * i], T[2 * i + 1])\n       \
    \ B = Calc.convolution(T[2 * i], U[2 * i + 1])\n\n        m = min(len(A), len(B))\n\
    \n        u = [0] * m\n        for j in range(m):\n            u[j] = (A[j] +\
    \ B[j]) % Mod\n        u.extend(A[m:])\n        u.extend(B[m:])\n        U[i]\
    \ = u\n\n    return Modulo_Polynomial(U[1], n)\n\ndef Slide_Convolution(A: list[int],\
    \ B: list[int], cyclic: bool = False) -> list[int]:\n    \"\"\" A = (a_i), B =\
    \ (b_j) \u306B\u5BFE\u3057\u3066, c_k = sum_{i - j = k} a_i b_j \u3068\u306A\u308B\
    \ C = (c_k)_{k >= 0} \u3092\u6C42\u3081\u308B.\n\n    Args:\n        A (list[int]):\n\
    \        B (list[int]):\n        cyclic (bool, optional): True \u306B\u3059\u308B\
    \u3068, c_k \u306E\u7DCF\u548C\u306E\u7BC4\u56F2 i - j = k \u304C i - j \u2261\
    \ 0 (mod |A|) \u306B\u306A\u308B. Defaults to False.\n\n    Raises:\n        ValueError:\
    \ |A| < |B| \u306E\u5834\u5408\u306B\u767A\u751F\n\n    Returns:\n        list[int]:\
    \ C\n    \"\"\"\n\n    if len(A) < len(B):\n        raise ValueError(\"len(A)\
    \ >= len(B) \u3067\u306A\u304F\u3066\u306F\u306A\u308A\u307E\u305B\u3093\")\n\n\
    \    n, m = len(A) - 1, len(B) - 1\n\n    if cyclic:\n        A = A + A[:m]\n\
    \        return Calc.convolution(A, B[::-1])[m: n + m + 1]\n    else:\n      \
    \  return Calc.convolution(A, B[::-1])[m: n + 1]\n\n#=================================================\n\
    Mod = 998244353\nCalc = Calculator()\n"
  dependsOn: []
  isVerificationFile: false
  path: Modulo_Sequence/Modulo_Polynomial.py
  requiredBy: []
  timestamp: '2025-05-04 10:58:23+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Polynomial/Division.test.py
  - test_verify/yosupo_library_checker/Polynomial/Log.test.py
  - test_verify/yosupo_library_checker/Polynomial/Product_of_Polynomial_Sequence.test.py
  - test_verify/yosupo_library_checker/Polynomial/Exp.test.py
  - test_verify/yosupo_library_checker/Polynomial/Taylor_Shift.test.py
  - test_verify/yosupo_library_checker/Polynomial/Power.test.py
  - test_verify/yosupo_library_checker/Polynomial/Inv.test.py
documentation_of: Modulo_Sequence/Modulo_Polynomial.py
layout: document
title: Modulo Polynomial
---

## Outline

多項式, 形式的ベキ級数に関する計算を行う.

## Theory

### 解析

$f \in \mathbb{F}_p[\\![X]\\!]$ に対する形式的積分 $\displaystyle \int f(X)~dX$ , 形式的微分 $f'(X)$ をそれぞれ

- $\displaystyle f'(X)=\sum_{n=0}^{\infty} (n+1) f_{n+1} X^n$
- $\displaystyle \int f(X) dX=\sum_{n=0}^{\infty} \dfrac{f_n}{n+1} X^{n+1}$

と定義する.

### Newton 法

線形部分空間 $D \subset \mathbb{F}_p[\\![X]\\!]$ に対して, $T: D \to \mathbb{F}_p[\\![X]\\!]$ が与えられているとする. このとき, $f \in \mathbb{F}_p$ に対して, $T(g)=f$ となる $g \in D$ を求めたい.

$T(\beta)=f_0$ となる $\beta \in F_p$ を何かしらの方法で求め, $g^{(1)}=\beta$ とする.

$T(g^{(N)}) \equiv f \pmod{X^N}$ となる多項式 $g^{(N)}$ が求まっているとする. Taylor 展開から

$$f=T(g)=T(g^{(N)})+T'(g^{(N)})(g-g^{(N)})+O((g-g^{(N)})^2)$$

となる. $\pmod{X^{2N}}$ での剰余を考えることによって,

$$f \equiv T(g^{(N)})+T'(g^{(N)})(g-g^{(N)}) \pmod{X^{2N}}$$

となる. これを整理することによって,

$$g \equiv g^{(N)}+\dfrac{f-T(g^{(N)})}{T'(g^{(N)})} \pmod{X^{2N}}$$

となる. よって, $g^{(2N)}:=g^{(N)}+\dfrac{f-T(g^{(N)})}{T'(g^{(N)})} \pmod{X^{2N}}$ とすればよい.

### 逆元

$f \in \mathbb{F}_p[\\![X]\\!]$ に対して, $f_0 \neq 0$ ならば, $fg=1$ となる $g \in \mathbb{F}_p[\\![X]\\!]$ が存在する.

$D$ を $f_0 \neq 0$ となる $f \in \mathbb{F}_p[\\![X]\\!]$ 全体の集合とする. $T: D \to \mathbb{F}_p[\\![X]\\!]$ を $T(g):=g^{-1}$ と定める.

Newton 法で求める. $g^{(0)}=f_0^{-1}$ である. また, $T'(g)=-\dfrac{1}{g^2}$ であるから,

$$g^{(2N)}=g^{(N)}+\dfrac{f-(1/g^{(N)})}{-(1/{g^{(N)}}^2)}=g^{(N)}(2-fg^{(N)})$$

となる.

### 対数関数

$f \in F_p[\\![X]\\!]$ に対して, $\displaystyle \log f:=\int \dfrac{f(X)}{f'(X)}~dX$ と定義する.

### 指数関数

$f_0=0$ となる $f \in \mathbb{F}\_p[\\![X]\\!]$ に対して, $\displaystyle \exp f:=\sum\_{n=0}^{\infty} \dfrac{f_n}{n!} X^n$ と定義する.

このとき, $\exp (\log f)=\log(\exp f)=f$ が成り立つ. よって, $g=\exp f \iff f=\log g$ である.

Newton 法において, $T(g):=\log g$ とすると, $T'(g)=\dfrac{1}{g}$ であるから, $g^{(1)}=1$ 及び,

$$g^{(N)}+\dfrac{f-\log g^{(N)}}{\log'g^{(N)}}=g^{(N)}(1+f-\log g^{(N)})$$

となるから, $g^{(2N)}=g^{(N)}(1+f-\log g^{(N)}) \pmod{X^{2N}}$ である.

### 累乗

$f \in \mathbb{F}_p[\\![X]\\!]$ に対して, $f \neq 0$ ならば, $f=\alpha X^d g, g_0=1$ となる $\alpha \in F_p^\times, d \geq 0, g \in \mathbb{F}_p[\\![X]\\!]$ が唯一存在する. ここで, $g=\exp(\log g)$ であるから, $g^M=\exp(M \log g)$ である. これを利用することによって, $f^M=\alpha^M X^{Md} \exp(M \log g)$ となる.

### 平方根

$f \in \mathbb{F}_p[\\![X]\\!]$ に対して, $h^2=f$ となる $\mathbb{F}_p[\\![X]\\!]$ となる $h$ が存在することと, 以下の2条件のうち, どちらか一方が成り立つことは同値である.

- $f=0$
- $f=\alpha X^d g, g_0=1$ となる $\alpha \in F_p$, 非負整数 $d$, $g_0 \in \mathbb{F}_p[\\![X]\\!]$ は唯一存在するが, $\alpha$ が平方剰余で, $d$ が偶数.

$g_0=1$ とする. このとき, $T(h):=h^2$ として, $T(h)=g$ となる $h$ を Newton 法で求めることにする.

まず, $h^{(1)}=1$ である. また, $T'(h)=2hh'$ であるから,

$$g^{(N)}+\dfrac{f-{g^{(N)}}^2}{2g^{(N)}}=\dfrac{1}{2}\left(g^{(N)}+\dfrac{f}{g^{(N)}} \right)$$

より, $g^{(2N)}=\dfrac{1}{2}\left(g^{(N)}+\dfrac{f}{g^{(N)}} \right) \pmod{X^{2N}}$ である.

### 多項式の商と剰余

$f,g \in \mathbb{F}_p[X]$ は多項式で, $g \neq 0$ であるとする. このとき, $f=q g+r, \deg r < \deg g$ となる多項式の組 $(q,r)$ が唯一存在する. このとき, $q,r$ をそれぞれ多項式 $f$ を多項式 $g$ で割った商, 余りという.

多項式 $h$ が高々 $K$ 次になるとき, $\widetilde{h}(X):=h(X^{-1}) X^K$ は多項式になる. なお, $h(X)=\alpha_0+\alpha_1 X+\dots+\alpha_K X^K$ のとき, $h(X)=\alpha_K+\dots+\alpha_1 X^{K-1}+\alpha_0 X^K$ である.

$\deg f=N, \deg g=M$ とすると, $\deg q=N-M, \deg r<M$ となる. $f=q g+r$ の両辺に $X^N$ を掛けると,

$$\widetilde{f}=\widetilde{g} \widetilde{q}+\widetilde{r} X^{N-(M-1)} \equiv \widetilde{g} \widetilde{q} \pmod{X^{N-M+1}}$$

である. $g \neq 0$ から, $\left(\widetilde{g} \right)_0 \neq 0$ なので,

$$\widetilde{q}=\dfrac{\widetilde{f}}{\widetilde{g}} \pmod{X^{N-M+1}}$$

であり, $q=\widetilde{\widetilde{q}}$ によって $q$ を求めることが出来る. これにより, $r=f-pg$ で $r$ も求められる.

### 除算における $N$ 次の係数

$P$ は高々 $(d-1)$ 次未満の多項式, $Q$ は $d$ 次の多項式であるとする. このとき,

$$\left[X^N \right] \dfrac{P(X)}{Q(X)}$$

を求めたい.

$\left[X^0 \right] Q \in \mathbb{F}_p^\times$ とする.

分子と分母の両方に $Q(-X)$ を掛けると, $Q(X)Q(-X)$ が偶多項式になるので, $V(X^2)=Q(X)Q(-X)$ となる多項式 $V$ が存在する.

また, 多項式 $P(X)Q(-X)$ を $P(X)Q(-X)=S_{{\rm even}}(X^2)+XS_{{\rm odd}}(X^2)$ と分解する.

このとき, 分母が偶多項式であるから, $N$ が偶数のときは

$$\left[X^N \right] \dfrac{P(X)}{Q(X)}=\left[X^N \right] \dfrac{S_{{\rm even}}(X^2)}{V(X^2)}=\left[X^{N/2} \right] \dfrac{S_{{\rm even}}(X)}{V(X)}$$

が成り立つ. $N$ が奇数のときも同様にして,

$$\left[X^N \right] \dfrac{P(X)}{Q(X)}=\left[X^N \right] \dfrac{XS_{{\rm odd}}(X^2)}{V(X^2)}=\left[X^{(N-1)/2} \right] \dfrac{S_{{\rm odd}}(X)}{V(X)}$$

が成り立つ.

これにより, 1回関係式を利用することにより, 求める指数をが $1/2$ に落とすことが出来る.

また, 自明な場合として,

$$\left[X^0 \right] \dfrac{P(X)}{Q(X)}=\dfrac{\left[X^0 \right] P}{\left[X^0 \right] Q}$$

が成り立つ.

よって, $d$ 次の多項式の積を $O(\log N)$ 回求めることによって, $\displaystyle \left[X^N \right] \dfrac{P(X)}{Q(X)}$ を求めることができる.

この多項式の積を求めるパートがボトルネックになるから, 計算量は $O(d \log d \log N)$ Time である.

### 多点評価

$N$ 次の多項式 $P \in \mathbb{F}_p[X]$ と $M$ 個の整数 $\alpha_1, \dots, \alpha_M$ に対して, $P(\alpha_1), \dots, P(\alpha_M)$ を求める.

次の2つの定理を利用して求めることにする.

> 剰余の定理
>
> $R$ を可換環とする. 多項式 $P \in R[X]$ と $\alpha$ に対して,
> $$P(\alpha)=P(X) \pmod {(X-\alpha)}$$
> が成り立つ.

> 中国剰余定理
>
> $R$ を環, $I_1, \dots, I_k \subset R$ は $R$ のイデアルで, どの2つも互いに素であるとする. このとき,
> $$\displaystyle \prod_{i=1}^k R/I_i \simeq R/(I_1 \cap \dots \cap I_k)$$
> である.
>
> なお, $R$ が可換環の場合は
> $$I_1 \cap \dots \cap I_k=I_1 \dots I_k$$
> である.

これらの定理から,
$$P(X) \pmod{(X-\alpha_1) \dots (X-\alpha_M)}$$
を求め,

$$(F \pmod{GH}) \pmod{H}=F \pmod{H}$$

を利用して除式の次数を半分にしながら最終的に $P(X) \pmod{(X-\alpha_j)}$ を求める.
