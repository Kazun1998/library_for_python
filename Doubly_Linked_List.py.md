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
  code: "class Doubly_Linked_List:\n    def __init__(self, N):\n        self.__N=N\n\
    \        self.__front=[-1]*N\n        self.__back=[-1]*N\n\n    def __len__(self):\n\
    \        return self.__N\n\n    def __str__(self):\n        res=[]\n        used=[0]*self.__N\n\
    \n        for x in range(self.__N):\n            if used[x]:\n               \
    \ continue\n\n            a=self.enumerate(x)\n            for y in a:\n     \
    \           used[y]=1\n            res.append(a)\n        return str(res)\n\n\
    \    def __repr__(self):\n        return \"[Doubly Linked List]: \"+str(self)\n\
    \n    def previous(self, x, default=-1):\n        return self.__front[x] if self.__front[x]!=-1\
    \ else default\n\n    def next(self, x, default=-1):\n        return self.__back[x]\
    \ if self.__back[x]!=-1 else default\n\n    def disconnect_front(self, x):\n \
    \       \"\"\" x \u304B\u3089\u524D\u306B\u4F38\u3073\u308B\u30EA\u30F3\u30AF\u3092\
    \u524A\u9664\u3059\u308B.\n\n        \"\"\"\n\n        front=self.__front; back=self.__back\n\
    \n        y=front[x]\n        if y>=0:\n            front[x]=-1\n            back[y]=-1\n\
    \n    def disconnect_back(self, x):\n        \"\"\" x \u304B\u3089\u5F8C\u308D\
    \u306B\u4F38\u3073\u308B\u30EA\u30F3\u30AF\u3092\u524A\u9664\u3059\u308B.\n\n\
    \        \"\"\"\n\n        front=self.__front; back=self.__back\n\n        y=back[x]\n\
    \        if y>=0:\n            back[x]=-1\n            front[y]=-1\n\n    def\
    \ extract(self, x):\n        \"\"\" x \u306B\u63A5\u7D9A\u3059\u308B\u30EA\u30F3\
    \u30AF\u3092\u524A\u9664\u3057, x \u306E\u524D\u5F8C\u304C\u5B58\u5728\u3059\u308B\
    \u306A\u3089\u3070, \u305D\u308C\u3089\u3092\u3064\u306A\u3050.\n        \"\"\"\
    \n\n        a=self.__front[x]\n        b=self.__back[x]\n\n        self.disconnect_front(x)\n\
    \        self.disconnect_back(x)\n\n        if a!=-1 and b!=-1:\n            self.connect(a,b)\n\
    \n    def connect(self, x, y):\n        \"\"\" x \u304B\u3089 y \u3078\u306E\u30EA\
    \u30F3\u30AF\u3092\u751F\u6210\u3059\u308B (\u3059\u3067\u306B\u3042\u308B x \u304B\
    \u3089\u306E\u30EA\u30F3\u30AF\u3068 y \u3078\u306E\u30EA\u30F3\u30AF\u306F\u524A\
    \u9664\u3055\u308C\u308B).\n\n        \"\"\"\n\n        self.disconnect_back(x)\n\
    \        self.disconnect_front(y)\n        self.__back[x]=y\n        self.__front[y]=x\n\
    \n    def insert_front(self, x, y):\n        \"\"\" x \u306E\u524D\u306B y \u3092\
    \u633F\u5165\u3059\u308B.\n\n        \"\"\"\n\n        z=self.__front[x]\n   \
    \     self.connect(y,x)\n        if z!=-1:\n            self.connect(z,y)\n\n\
    \    def insert_back(self, x, y):\n        \"\"\" x \u306E\u5F8C\u306B y \u3092\
    \u633F\u5165\u3059\u308B.\n\n        \"\"\"\n\n        z=self.__back[x]\n    \
    \    self.connect(x,y)\n        if z!=-1:\n            self.connect(y,z)\n\n \
    \   def head(self, x):\n        \"\"\" x \u304C\u5C5E\u3059\u308B\u5F31\u9023\u7D50\
    \u6210\u5206\u306E\u5148\u982D\u3092\u6C42\u3081\u308B.\n        \"\"\"\n\n  \
    \      while self.__front[x]!=-1:\n            x=self.__front[x]\n        return\
    \ x\n\n    def tail(self, x):\n        \"\"\" x \u304C\u5C5E\u3059\u308B\u5F31\
    \u9023\u7D50\u6210\u5206\u306E\u672B\u5C3E\u3092\u6C42\u3081\u308B.\n        \"\
    \"\"\n\n        while self.__back[x]!=-1:\n            x=self.__back[x]\n    \
    \    return x\n\n    def enumerate(self, x):\n        \"\"\" x \u304C\u5C5E\u3057\
    \u3066\u3044\u308B\u5F31\u9023\u7D50\u6210\u5206\u3092\u5148\u982D\u304B\u3089\
    \u9806\u306B\u51FA\u529B\u3059\u308B.\n\n        \"\"\"\n\n        x=self.head(x)\n\
    \        res=[x]\n        while self.__back[x]>=0:\n            x=self.__back[x]\n\
    \            res.append(x)\n        return res\n\n    def depth(self, x):\n  \
    \      dep=0\n        while self.__front[x]!=-1:\n            x=self.__front[x]\n\
    \            dep+=1\n        return dep\n"
  dependsOn: []
  isVerificationFile: false
  path: Doubly_Linked_List.py
  requiredBy: []
  timestamp: '2023-05-06 03:51:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Doubly_Linked_List.py
layout: document
redirect_from:
- /library/Doubly_Linked_List.py
- /library/Doubly_Linked_List.py.html
title: Doubly_Linked_List.py
---
