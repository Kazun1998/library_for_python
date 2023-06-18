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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Rolling_Hash():\n    def __init__(self,S, base, mod, type=0):\n   \
    \     \"\"\" type=0: \u6574\u6570\u5217 (\u5404\u8981\u7D20\u306F mod \u672A\u6E80\
    ), type=1: \u6587\u5B57\u5217 (mod>(\u6700\u5927\u306E\u6587\u5B57\u30B3\u30FC\
    \u30C9))\n\n        \"\"\"\n\n        self.mod=mod\n        self.base=base\n \
    \       self.length=len(S)\n        self.power=power=[1]*(len(S)+1)\n        self.type=type\n\
    \n        L=len(S)\n        self.hash=h=[0]*(L+1)\n\n        for i in range(L):\n\
    \            if type:\n                h[i+1]=(base*h[i]+ord(S[i]))%mod\n    \
    \        else:\n                h[i+1]=(base*h[i]+S[i])%mod\n\n        for i in\
    \ range(L):\n            power[i+1]=base*power[i]%mod\n\n    def __hasher(self,\
    \ X):\n        assert len(X)<=len(self)\n        h=0\n        for i in range(len(X)):\n\
    \            h=(h*self.base+X[i])%self.mod\n        return h\n\n    def get(self,\
    \ l, r):\n        return (self.hash[r]-self.hash[l]*self.power[r-l])%self.mod\n\
    \n    def count(self, T, start=0):\n        alpha=self.__hasher(T)\n\n       \
    \ K=0\n        for i in range(start, len(self)-len(T)+1):\n            if alpha==self[i:\
    \ i+len(T)]:\n                K+=1\n        return K\n\n    def find(self, T,\
    \ start=0):\n        alpha=self.__hasher(T)\n\n        for i in range(start, len(self)-len(T)+1):\n\
    \            if alpha==self[i: i+len(T)]:\n                return i\n        return\
    \ -1\n\n    def rfind(self, T, start=0):\n        alpha=self.__hasher(T)\n\n \
    \       for i in range(len(self)-len(T), start-1, -1):\n            if alpha==self[i:\
    \ i+len(T)]:\n                return i\n        return -1\n\n    def index(self,\
    \ T, start=0):\n        alpha=self.__hasher(T)\n\n        for i in range(start,\
    \ len(self)-len(T)+1):\n            if alpha==self[i: i+len(T)]:\n           \
    \     return i\n        raise ValueError(\"substring not found\")\n\n    def __getitem__(self,\
    \ index):\n        if index.__class__==int:\n            if index<0:\n       \
    \         index+=self.length\n            assert 0<=index<self.length\n      \
    \      return self.get(index, index+1)\n        elif index.__class__==slice:\n\
    \            assert (index.step==None) or (index.step==1)\n            L=index.start\
    \ if index.start else 0\n            R=index.stop if index.stop else len(self)\n\
    \            if L<0:\n                L+=len(self)\n            if R<0:\n    \
    \            R+=len(self)\n            return self.get(L,R)\n\n    def __len__(self):\n\
    \        return self.length\n\n    def docking(self, l0, r0, l1, r1):\n      \
    \  \"\"\" [l0, r0) \u3068 [l1, r1) \u306E\u90E8\u5206\u5217\u3092\u30C9\u30C3\u30AD\
    \u30F3\u30B0\u3057\u305F\u30CF\u30C3\u30B7\u30E5\u3092\u8FD4\u3059.\n        \"\
    \"\"\n\n        h0=self.get(l0,r0); h1=self.get(l1,r1)\n        return (h0*self.power[r1-l1]+h1)%self.mod\n\
    \n#=================================================\nclass Double_Rolling_Hash():\n\
    \    def __init__(self, S, base, mod0, mod1, type):\n        self.__length=len(S)\n\
    \        self.__base=base\n        self.__mod0=mod0\n        self.__mod1=mod1\n\
    \        self.__type=type\n\n        self.rh0=Rolling_Hash(S, base, mod0, type)\n\
    \        self.rh1=Rolling_Hash(S, base, mod1, type)\n\n    def encode(self, a0,\
    \ a1):\n        return a0*self.__mod1+a1\n\n    def get(self, l, r):\n       \
    \ a0=self.rh0.get(l,r)\n        a1=self.rh1.get(l,r)\n        return self.encode(a0,a1)\n\
    \n    def __hasher(self, X):\n        assert len(X)<=len(self)\n        a0=0;\
    \ a1=0\n        for x in X:\n            if self.__type==0:\n                a0=(a0*self.__base+x)%self.__mod0\n\
    \                a1=(a1*self.__base+x)%self.__mod1\n        return self.encode(a0,a1)\n\
    \n    def __getitem__(self, index):\n        if index.__class__==int:\n      \
    \      if index<0:\n                index+=self.__length\n            assert 0<=index<self.__length\n\
    \            return self.encode(self.rh0[index], self.rh1[index])\n        elif\
    \ index.__class__==slice:\n            assert (index.step==None) or (index.step==1)\n\
    \            L=index.start if index.start else 0\n            R=index.stop if\
    \ index.stop else len(self)\n            if L<0:\n                L+=len(self)\n\
    \            if R<0:\n                R+=len(self)\n            return self.encode(self.rh0[L:\
    \ R], self.rh1[L: R])\n\n    def count(self, T, start=0):\n        alpha=self.__hasher(T)\n\
    \        K=0\n        T_len=len(T)\n        for i in range(start, len(self)-len(T)+1):\n\
    \            if alpha==self[i: i+T_len]:\n                K+=1\n        return\
    \ K\n\n    def find(self, T, start=0):\n        alpha=self.__hasher(T)\n\n   \
    \     for i in range(start, len(self)-len(T)+1):\n            if alpha==self[i:\
    \ i+len(T)]:\n                return i\n        return -1\n\n    def rfind(self,\
    \ T, start=0):\n        alpha=self.__hasher(T)\n\n        for i in range(len(self)-len(T),\
    \ start-1, -1):\n            if alpha==self[i: i+len(T)]:\n                return\
    \ i\n        return -1\n\n    def index(self, T, start=0):\n        alpha=self.__hasher(T)\n\
    \n        for i in range(start, len(self)-len(T)+1):\n            if alpha==self[i:\
    \ i+len(T)]:\n                return i\n        raise ValueError(\"substring not\
    \ found\")\n\n    def __len__(self):\n        return self.__length\n\n    def\
    \ docking(self, l0, r0, l1, r1):\n        \"\"\" ranges: tuple (l,r) \u304B\u3089\
    \u306A\u308B\u30EA\u30B9\u30C8, i \u756A\u76EE\u306E (l,r) \u306F\u90E8\u5206\u5217\
    \ [l,r) \u3092\u610F\u5473\u3059\u308B.\n        \"\"\"\n\n        return self.encode(self.rh0.docking(l0,\
    \ r0, l1, r1), self.rh1.docking(l0, r0, l1, r1))\n\n#=================================================\n\
    class Hasher():\n    def __init__(self, length, base, mod, type=0):\n        self.length=length\n\
    \        self.base=base\n        self.mod=mod\n        self.type=type\n\n    \
    \    self.power=pw=[1]*length\n        for i in range(1, length):\n          \
    \  pw[i]=(base*pw[i-1])%mod\n\n    def __repr__(self):\n        return \"length:\
    \ {}\\nbase: {}\\nmod: {}\".format(self.length, self.base, self.mod)\n\n    def\
    \ encode(self, S):\n        code=0; N=len(S)\n        for i in range(N):\n   \
    \         if self.type:\n                code+=ord(S[i])*self.power[N-1-i]%self.mod\n\
    \            else:\n                code+=S[i]*self.power[N-1-i]%self.mod\n\n\
    \        return code%self.mod\n\n    def decode(self, S):\n        pass\n\n#=================================================\n\
    class Double_Hasher():\n    def __init__(self, length, base, mod0, mod1, type=0):\n\
    \        self.length=length\n        self.base=base\n        self.mod0=mod0\n\
    \        self.mod1=mod1\n        self.type=type\n\n        self.power0=pw0=[1]*length\n\
    \        self.power1=pw1=[1]*length\n        for i in range(1, length):\n    \
    \        pw0[i]=(base*pw0[i-1])%mod0\n            pw1[i]=(base*pw1[i-1])%mod1\n\
    \n    def __repr__(self):\n        return \"length: {}\\nbase: {}\\nmod: {}\"\
    .format(self.length, self.base, self.mod)\n\n    def encode(self, S):\n      \
    \  code0=0; code1=0\n        N=len(S)\n        for i in range(N):\n          \
    \  if self.type:\n                code0+=ord(S[i])*self.power0[N-1-i]%self.mod0\n\
    \                code1+=ord(S[i])*self.power1[N-1-i]%self.mod1\n            else:\n\
    \                code0+=S[i]*self.power0[N-1-i]%self.mod0\n                code1+=S[i]*self.power1[N-1-i]%self.mod1\n\
    \n        code0%=self.mod0; code1%=self.mod1\n        return code1*self.mod0+code0\n"
  dependsOn: []
  isVerificationFile: false
  path: Rolling_Hash.py
  requiredBy: []
  timestamp: '2023-05-20 13:26:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Rolling_Hash.py
layout: document
title: Rolling  Hash
---

## Outline

列に対して, Rolling Hash を用いて一致判定を高速化する.

## Theory

$\mathcal{A}$ をアルファベット (文字全体の集合) とし, $p$ を $\# \mathcal{A}$ より非常に大きい **素数** とする.

また, $\beta \in \mathbb{F}\_p$ とし, $h: \mathcal{A} \to \mathbb{F}\_p$ を単射とする. このとき, $\mathcal{A}$ の列 $S=(S\_i)\_{i=1}^{\left \lvert S \right \rvert}$ に対する Rolling Hash $\operatorname{hash}(S)$ を

$$\operatorname{hash}(S):=\sum_{i=1}^{\left \lvert S \right \rvert} S_i \beta^{\left \lvert S \right \rvert-i}$$

と定義する.

$R=0,1,2, \dots, \lvert S \rvert$ に対して, $H_R$ を

$$H_R:=\begin{cases} \operatorname{hash}(S[1:R]) & (R \geq 0) \\ 0 & (R=0) \end{cases}$$

と定義する. すると, $1 \leq L \leq R \leq \lvert S \rvert$ に対して,

$$\operatorname{hash}(S[L:R])=H_R-H_{L-1}\beta^{R-L}$$

が成り立つ.
