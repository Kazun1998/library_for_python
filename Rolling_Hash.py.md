---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Rolling_Hash():\n    def __init__(self,S, base, mod, hash_function\
    \ = None):\n        \"\"\" \u6587\u5B57\u5217 S \u306B\u5BFE\u3059\u308B Rolling\
    \ Hash \u3092\u6C42\u3081\u308B.\n\n        \"\"\"\n\n        self.mod = mod\n\
    \        self.base = base\n        self.length = len(S)\n        self.power =\
    \ power = [1]*(len(S)+1)\n        self.hash_function = hash_function = hash_function\
    \ if hash_function is not None else lambda x: x\n\n        length = len(S)\n \
    \       self.hash = h = [0] * (length + 1)\n\n        for i in range(length):\n\
    \            h[i + 1] = (base * h[i] + hash_function(S[i])) % mod\n\n        for\
    \ i in range(length):\n            power[i + 1] = base * power[i] % mod\n\n  \
    \  def __hasher(self, X):\n        assert len(X)<=len(self)\n        h=0\n   \
    \     for i in range(len(X)):\n            h = (h * self.base + self.hash_function(X[i]))\
    \ % self.mod\n        return h\n\n    def get(self, l, r):\n        return (self.hash[r]-self.hash[l]*self.power[r-l])%self.mod\n\
    \n    def count(self, T, start=0):\n        alpha=self.__hasher(T)\n        return\
    \ len([i for i in range(start, len(self) - len(T) + 1) if self[i: i + len(T)]\
    \ == alpha])\n\n    def find(self, T, start=0):\n        alpha=self.__hasher(T)\n\
    \n        for i in range(start, len(self)-len(T)+1):\n            if alpha==self[i:\
    \ i+len(T)]:\n                return i\n        return -1\n\n    def rfind(self,\
    \ T, start=0):\n        alpha=self.__hasher(T)\n\n        for i in range(len(self)-len(T),\
    \ start-1, -1):\n            if alpha==self[i: i+len(T)]:\n                return\
    \ i\n        return -1\n\n    def index(self, T, start=0):\n        ind = self.find(T,\
    \ start)\n        if ind == -1:\n            raise ValueError(\"substring not\
    \ found\")\n        return ind\n\n    def __getitem__(self, index):\n        if\
    \ index.__class__==int:\n            if index<0:\n                index+=self.length\n\
    \            assert 0<=index<self.length\n            return self.get(index, index+1)\n\
    \        elif index.__class__==slice:\n            assert (index.step==None) or\
    \ (index.step==1)\n            L=index.start if index.start else 0\n         \
    \   R=index.stop if index.stop else len(self)\n            if L<0:\n         \
    \       L+=len(self)\n            if R<0:\n                R+=len(self)\n    \
    \        return self.get(L,R)\n\n    def __len__(self):\n        return self.length\n\
    \n    def docking(self, l0, r0, l1, r1):\n        \"\"\" [l0, r0) \u3068 [l1,\
    \ r1) \u306E\u90E8\u5206\u5217\u3092\u30C9\u30C3\u30AD\u30F3\u30B0\u3057\u305F\
    \u30CF\u30C3\u30B7\u30E5\u3092\u8FD4\u3059.\n        \"\"\"\n\n        h0=self.get(l0,r0);\
    \ h1=self.get(l1,r1)\n        return (h0*self.power[r1-l1]+h1)%self.mod\n\n#=================================================\n\
    class Double_Rolling_Hash():\n    def __init__(self, S, base, mod0, mod1, hash_function\
    \ = None):\n        self.__length=len(S)\n        self.__base=base\n        self.__mod0=mod0\n\
    \        self.__mod1=mod1\n        self.hash_function = hash_function\n\n    \
    \    self.rh0=Rolling_Hash(S, base, mod0, hash_function)\n        self.rh1=Rolling_Hash(S,\
    \ base, mod1, hash_function)\n\n    def encode(self, a0, a1):\n        return\
    \ a0*self.__mod1+a1\n\n    def get(self, l, r):\n        a0=self.rh0.get(l,r)\n\
    \        a1=self.rh1.get(l,r)\n        return self.encode(a0,a1)\n\n    def __hasher(self,\
    \ X):\n        assert len(X)<=len(self)\n        a0=0; a1=0\n        for x in\
    \ X:\n            a0 = (a0 * self.__base + self.hash_function(x)) % self.__mod0\n\
    \            a1 = (a1 * self.__base + self.hash_function(x)) % self.__mod1\n \
    \       return self.encode(a0, a1)\n\n    def __getitem__(self, index):\n    \
    \    if index.__class__==int:\n            if index<0:\n                index+=self.__length\n\
    \            assert 0<=index<self.__length\n            return self.encode(self.rh0[index],\
    \ self.rh1[index])\n        elif index.__class__==slice:\n            assert (index.step==None)\
    \ or (index.step==1)\n            L=index.start if index.start else 0\n      \
    \      R=index.stop if index.stop else len(self)\n            if L<0:\n      \
    \          L+=len(self)\n            if R<0:\n                R+=len(self)\n \
    \           return self.encode(self.rh0[L: R], self.rh1[L: R])\n\n    def count(self,\
    \ T, start=0):\n        alpha=self.__hasher(T)\n        return len([i for i in\
    \ range(start, len(self) - len(T) + 1) if self[i: i + len(T)] == alpha])\n\n \
    \   def find(self, T, start=0):\n        alpha=self.__hasher(T)\n\n        for\
    \ i in range(start, len(self)-len(T)+1):\n            if alpha==self[i: i+len(T)]:\n\
    \                return i\n        return -1\n\n    def rfind(self, T, start=0):\n\
    \        alpha=self.__hasher(T)\n\n        for i in range(len(self)-len(T), start-1,\
    \ -1):\n            if alpha==self[i: i+len(T)]:\n                return i\n \
    \       return -1\n\n    def index(self, T, start=0):\n        ind = self.find(T,\
    \ start)\n        if ind == -1:\n            raise ValueError(\"substring not\
    \ found\")\n        return ind\n\n    def __len__(self):\n        return self.__length\n\
    \n    def docking(self, l0, r0, l1, r1):\n        \"\"\" ranges: tuple (l,r) \u304B\
    \u3089\u306A\u308B\u30EA\u30B9\u30C8, i \u756A\u76EE\u306E (l,r) \u306F\u90E8\u5206\
    \u5217 [l,r) \u3092\u610F\u5473\u3059\u308B.\n        \"\"\"\n\n        return\
    \ self.encode(self.rh0.docking(l0, r0, l1, r1), self.rh1.docking(l0, r0, l1, r1))\n\
    \n#=================================================\nclass Hasher():\n    def\
    \ __init__(self, length, base, mod, hash_function = None):\n        self.length\
    \ = length\n        self.base = base\n        self.mod = mod\n        self.hash_function\
    \ = hash_function = hash_function if hash_function is not None else lambda x:\
    \ x\n\n        self.power = pw = [1] * length\n        for i in range(1, length):\n\
    \            pw[i] = (base * pw[i - 1]) % mod\n\n    def __repr__(self):\n   \
    \     return f\"[Hasher] length: {self.length}, base: {self.base}, mod: {self.mod}\"\
    \n\n    def encode(self, S):\n        hash_function = self.hash_function\n   \
    \     N = len(S)\n        code=0\n        for i in range(N):\n               \
    \ code += hash_function(S[i]) * self.power[N - 1 - i] % self.mod\n\n        return\
    \ code % self.mod\n\n#=================================================\nclass\
    \ Double_Hasher():\n    def __init__(self, length, base, mod0, mod1, hash_function\
    \ = None):\n        self.hasher_0 = Hasher(length, base, mod0, hash_function)\n\
    \        self.hasher_1 = Hasher(length, base, mod1, hash_function)\n\n    def\
    \ __repr__(self):\n        return f\"[Double Hasher]: {self.hasher_0}, {self.hasher_1}\"\
    \n\n    def encode(self, S):\n        return self.hasher_0.encode(S) * self.hasher_1.mod\
    \ + self.hasher_1.encode(S)\n"
  dependsOn: []
  isVerificationFile: false
  path: Rolling_Hash.py
  requiredBy: []
  timestamp: '2024-07-14 11:46:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Rolling_Hash.py
layout: document
title: Rolling  Hash
---

## Outline

列に対して, Rolling Hash を用いて一致判定を高速化する.

## Theory

$\mathcal{A}$ をアルファベット (文字全体の集合) とし, $p$ を $\\# \mathcal{A}$ より非常に大きい **素数** とする.

また, $\beta \in \mathbb{F}\_p$ とし, $h: \mathcal{A} \to \mathbb{F}\_p$ を単射とする. このとき, $\mathcal{A}$ の列 $S=(S\_i)\_{i=1}^{\left \lvert S \right \rvert}$ に対する Rolling Hash $\operatorname{hash}(S)$ を

$$\operatorname{hash}(S):=\sum_{i=1}^{\left \lvert S \right \rvert} S_i \beta^{\left \lvert S \right \rvert-i}$$

と定義する.

$R=0,1,2, \dots, \lvert S \rvert$ に対して, $H_R$ を

$$H_R:=\begin{cases} \operatorname{hash}(S[1:R]) & (R \geq 0) \\ 0 & (R=0) \end{cases}$$

と定義する. すると, $1 \leq L \leq R \leq \lvert S \rvert$ に対して,

$$\operatorname{hash}(S[L:R])=H_R-H_{L-1}\beta^{R-L}$$

が成り立つ.
