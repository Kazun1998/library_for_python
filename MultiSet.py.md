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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class MultiSet():\n    def __init__(self):\n        self.num={}\n       \
    \ self.set=set()\n\n    def __bool__(self):\n        return bool(self.set)\n\n\
    \    #\u8981\u7D20\u306E\u6DFB\u52A0\n    def add(self,x,k=1):\n        \"\"\"\
    \u8981\u7D20x\u3092k\u500B\u52A0\u3048\u308B.\n\n        x:\u8981\u7D20\n    \
    \    k=1:\u500B\u6570\n        \"\"\"\n\n        if k==0:\n            return\n\
    \        elif k<0:\n            self.discard(x,-k)\n            return\n\n   \
    \     self.set.add(x)\n        if x in self.num:\n            self.num[x]+=k\n\
    \        else:\n            self.num[x]=k\n\n    #\u8981\u7D20\u306E\u524A\u9664\
    \n    def discard(self,x,k=1):\n        \"\"\"\u8981\u7D20x\u304B\u3089k\u500B\
    \u9664\u304F.\n\n        x:\u8981\u7D20\n        k=1:\u500B\u6570\n        \u305F\
    \u3060\u3057, \u591A\u91CD\u96C6\u5408\u306B\u8981\u7D20x\u304Ck\u500B\u306A\u3044\
    \u3068\u304D\u306F\u5168\u3066\u53D6\u308A\u9664\u304F.\n        \"\"\"\n    \
    \    if k==0:\n            return\n        elif k<0:\n            self.add(x,-k)\n\
    \            return\n\n        if x not in self.set:\n            return\n\n \
    \       self.num[x]=max(0,self.num[x]-k)\n        if self.num[x]==0:\n       \
    \     self.set.remove(x)\n\n    def remove(self,x,k=1):\n        \"\"\"\u8981\u7D20\
    x\u304B\u3089k\u500B\u9664\u304F.\n\n        x:\u8981\u7D20\n        k=1:\u500B\
    \u6570\n        \u305F\u3060\u3057, \u591A\u91CD\u96C6\u5408\u306B\u8981\u7D20\
    x\u304Ck\u500B\u306A\u3044\u3068\u304D\u306FValue Error.\n        \"\"\"\n\n \
    \       if x not in self.set:\n            raise KeyError(x)\n\n        if self.num[x]<k:\n\
    \            raise ValueError(x,k)\n\n        self.num[x]-=k\n        if self.num[x]==0:\n\
    \            self.set.remove(x)\n\n    def pop(self):\n        \"\"\"\u591A\u91CD\
    \u96C6\u5408\u304B\u3089\u9069\u5F53\u306B1\u500B\u306E\u8981\u7D20\u3092\u524A\
    \u9664\u3057, \u305D\u306E\u8981\u7D20\u3092\u51FA\u529B\u3059\u308B.\n      \
    \  \"\"\"\n\n        a=self.set.pop()\n        self.num[a]-=1\n        if self.num[a]:\n\
    \            self.set.add(a)\n        return a\n\n    def clear(self):\n     \
    \   \"\"\"\u591A\u91CD\u96C6\u5408\u304B\u3089\u5168\u3066\u306E\u8981\u7D20\u3092\
    \u524A\u9664\u3059\u308B.\n        \"\"\"\n\n        self.set=set()\n        self.num={}\n\
    \n    #\u96C6\u5408\u306E\u6F14\u7B97\n    #\u5171\u901A\u90E8\u5206\n    def\
    \ __and__(self,other):\n        A=MultiSet()\n        for x in self.set:\n   \
    \         if x in other:\n                A.set.add(x)\n                A.num[x]=min(self.num[x],other.num[x])\n\
    \        return A\n\n    def intersection(self,other):\n        return self&other\n\
    \n    #\u548C\u96C6\u5408\n    def __or__(self,other):\n        A=MultiSet()\n\
    \        A.set=self.set.copy()\n        A.num=self.num.copy()\n\n        for x\
    \ in other.set:\n            if x in A.set:\n                A.num[x]=max(A.num[x],other.num[x])\n\
    \            else:\n                A.num[x]=other.num[x]\n        return A\n\n\
    \    def union(self,other):\n        return self|other\n\n    #\u5DEE\u96C6\u5408\
    \n    def __sub__(self,other):\n        A=MultiSet()\n\n        for x in self.set:\n\
    \            t=self.count(x)-other.count(x)\n            if t>0:\n           \
    \     A.set.add(x)\n                A.num[x]=t\n        return A\n\n    def difference(self,other):\n\
    \        return self-other\n\n    #\u5BFE\u79F0\u5DEE\n    def __xor__(self,other):\n\
    \        A=MultiSet()\n        A.set=self.set.copy()\n        A.num=self.num.copy()\n\
    \n        for y in other.set:\n            if y in self:\n                t=abs(self.count(y)-other.count(y))\n\
    \                A.num[y]=t\n\n                if t==0:\n                    A.set.discard(y)\n\
    \            else:\n                A.set.add(y)\n                A.num[y]=other.num[y]\n\
    \        return A\n\n    def symmetric_difference(self,other):\n        return\
    \ self^other\n\n    #\u90E8\u5206\u96C6\u5408?\n    def __le__(self,other):\n\
    \        for x in self.set:\n            if not self.count(x)<=other.count(x):\n\
    \                return False\n        return True\n\n    def issubset(self,other):\n\
    \        return self<=other\n\n    def __ge__(self,other):\n        for x in self.set:\n\
    \            if not self.count(x)>=other.count(x):\n                return False\n\
    \        return True\n\n    def issuperset(self,other):\n        return self>=other\n\
    \n    def __eq__(self,other):\n        return (self<=other) and (other<=self)\n\
    \n    #\u4E92\u3044\u306B\u7D20?\n    def isdisjoint(self,other):\n        return\
    \ not(self & other)\n\n    #\u8981\u7D20\u306E\u5B58\u5728\n    def __contains__(self,x):\n\
    \        return x in self.set\n\n    #\u96C6\u5408\u306E\u6BD4\u8F03\n    def\
    \ count(self,x):\n        \"\"\"\u8981\u7D20x\u306E\u500B\u6570\u3092\u8FD4\u3059\
    .\n\n        x:\u8981\u7D20\n        \"\"\"\n\n        if x not in self.set:\n\
    \            return 0\n        return self.num[x]\n\n    def refresh(self):\n\
    \        L=[]\n        for x in self.num:\n            if x not in self.set:\n\
    \                L.append(x)\n\n        for x in L:\n            del self.num[x]\n\
    \ndef mex(S,start=0):\n    x=start\n    while x in S:\n        x+=1\n    return\
    \ x\n\nS=MultiSet()\nS.add(1,3);S.add(2,5);S.add(3,8);S.add(4,3);S.add(\"x\",2)\n\
    \nT=MultiSet()\nT.add(1,2);T.add(2,8);T.add(4,1);T.add(\"x\",2)\n\nU=MultiSet()\n\
    U.add(1,3);U.add(2,19);U.add(4,3);U.add(\"x\",2)\n\nV=MultiSet()\nV.add(\"y\"\
    ,4);V.discard(1,-3)\n"
  dependsOn: []
  isVerificationFile: false
  path: MultiSet.py
  requiredBy: []
  timestamp: '2021-04-27 14:48:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: MultiSet.py
layout: document
redirect_from:
- /library/MultiSet.py
- /library/MultiSet.py.html
title: MultiSet.py
---
