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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Imos_1:\n    def __init__(self, N):\n        \"\"\" \u533A\u9593 0<=t<N\
    \ \u306B\u5BFE\u3059\u308B Imos \u6CD5\u3092\u6E96\u5099\u3059\u308B.\n      \
    \  \"\"\"\n        self.__N=N\n        self.list=[0]*(N+1)\n\n    def __len__(self):\n\
    \        return len(self.list)-1\n\n    def add(self, l, r, x=1):\n        \"\"\
    \"\u9589\u533A\u9593 [l, r] \u306B x \u3092\u52A0\u7B97\u3059\u308B.\"\"\"\n\n\
    \        assert 0<=l<self.__N\n        assert 0<=r<self.__N\n\n        if l<=r:\n\
    \            self.list[l]+=x\n            self.list[r+1]-=x\n\n    def cumulative_sum(self):\n\
    \        \"\"\"\u7D2F\u7A4D\u548C\u3092\u6C42\u3081\u308B.\n        \"\"\"\n \
    \       X=self.list.copy()[:-1]\n        for i in range(1,len(self)):\n      \
    \      X[i]+=X[i-1]\n        return X\n\n#=================================================\n\
    from collections import defaultdict\nclass Sparse_Imos_1:\n    def __init__(self):\n\
    \        self.dict=defaultdict(int)\n\n    def add(self, l, r, x=1):\n       \
    \ \"\"\"\u9589\u533A\u9593 [l,r] \u306B x \u3092\u52A0\u7B97\u3059\u308B.\n  \
    \      \"\"\"\n\n        if l<=r:\n            self.dict[l]+=x\n            self.dict[r+1]-=x\n\
    \n    def cumulative_sum(self, since, until):\n        \"\"\"\u7D2F\u7A4D\u548C\
    \u3092\u6C42\u3081\u308B.\n\n        [Output]\n        (y, l, r) \u3068\u3044\u3046\
    \u5F62\u306E\u30EA\u30B9\u30C8. \u305F\u3060\u3057, (y, l, r) \u306F l<=x<=y \u306E\
    \u7BC4\u56F2\u3067\u306F y \u3067\u3042\u308B\u3068\u3044\u3046\u3053\u3068\u3092\
    \u610F\u5473\u3059\u308B.\n        \"\"\"\n        Y=[]\n        S=0\n       \
    \ t_old=since\n        dic=self.dict\n        for t in sorted(dic):\n        \
    \    if t>until:\n                break\n            if dic[t]==0:\n         \
    \       continue\n\n            if t_old<=t-1:\n                Y.append((S, t_old,t-1))\n\
    \n            S+=dic[t]\n            t_old=t\n\n        if t_old<=until:\n   \
    \         Y.append((S, t_old,until))\n        return Y\n\n#=================================================\n\
    class Linear_Imos_1:\n    def __init__(self, N):\n        \"\"\" \u533A\u9593\
    \ 0<=t<N \u306B\u5BFE\u3059\u308B Imos \u6CD5\u3092\u6E96\u5099\u3059\u308B.\n\
    \        \"\"\"\n        self.__N=N\n        self.list=[0]*(N+2)\n\n    def __len__(self):\n\
    \        return len(self.list)-2\n\n    def add(self, l, r, x=1):\n        \"\"\
    \"\u9589\u533A\u9593 [l, r] \u306B x \u3092\u52A0\u7B97\u3059\u308B.\"\"\"\n\n\
    \        assert 0<=l<self.__N\n        assert 0<=r<self.__N\n\n        self.add_linear(l,r,x,0)\n\
    \n    def add_linear(self, l, r, a, b):\n        \"\"\" \u9589\u533A\u9593 [l,r]\
    \ \u306B\u6B21\u306E\u3088\u3046\u306B\u3057\u3066\u52A0\u7B97\u3059\u308B.\n\
    \        I[l]+=a, I[l+1]+=a+b, I[l+2]+=a+2b, ..., I[t]+=a+(t-r)b, ...,  I[r]+=a+(r-l)b\n\
    \        \"\"\"\n\n        assert 0<=l<self.__N\n        assert 0<=r<self.__N\n\
    \n        if l<=r:\n            self.list[l]+=a\n            self.list[l+1]+=-a+b\n\
    \            self.list[r+1]+=-a-(r-l+1)*b\n            self.list[r+2]+=a+(r-l)*b\n\
    \n    def cumulative_sum(self):\n        \"\"\"\u7D2F\u7A4D\u548C\u3092\u6C42\u3081\
    \u308B.\n        \"\"\"\n        X=self.list.copy()[:len(self)]\n        for _\
    \ in range(2):\n            for i in range(1,len(self)):\n                X[i]+=X[i-1]\n\
    \        return X\n\n#=================================================\nclass\
    \ Imos_2:\n    def __init__(self,W,H):\n        self.width=W\n        self.height=H\n\
    \        self.list=[[0]*(W+1) for _ in range(H+1)]\n\n    def add(self, i0, j0,\
    \ i1, j1, x=1):\n        \"\"\" \u9589\u533A\u9593 [i0, j0] x [i1,j1] \u306B x\
    \ \u3092\u52A0\u7B97\u3059\u308B.\n        \"\"\"\n\n        self.list[i0][j0]+=x\n\
    \        self.list[i0][j1+1]-=x\n        self.list[i1+1][j0]-=x\n        self.list[i1+1][j1+1]+=x\n\
    \n    def add_row(self, i, x):\n        \"\"\" \u7B2C i \u884C (i, *) \u306B x\
    \ \u3092\u52A0\u3048\u308B.\"\"\"\n        self.add(i, 0, i, self.width-1, x)\n\
    \n    def add_column(self, j, x):\n        \"\"\" \u7B2C j \u5217 (*, j) \u306B\
    \ x \u3092\u52A0\u3048\u308B.\"\"\"\n        self.add(0, j, self.height-1, j,\
    \ x)\n\n    def cumulative_sum(self):\n        Y=[self.list[i].copy()[:-1] for\
    \ i in range(self.height)]\n\n        for _ in range(2):\n            for i in\
    \ range(len(Y)):\n                y=Y[i]\n                for j in range(1,len(y)):\n\
    \                    y[j]+=y[j-1]\n            Y=[list(y) for y in zip(*Y)]\n\
    \        return Y\n"
  dependsOn: []
  isVerificationFile: false
  path: Imos.py
  requiredBy: []
  timestamp: '2022-09-28 11:02:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Imos.py
layout: document
redirect_from:
- /library/Imos.py
- /library/Imos.py.html
title: Imos.py
---
