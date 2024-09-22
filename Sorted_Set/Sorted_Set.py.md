---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://qiita.com/tatyam/items/492c70ac4c955c055602"
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\" Reference: https://qiita.com/tatyam/items/492c70ac4c955c055602\"\n# \u203B\
    \ \u8A08\u7B97\u91CF\u304C O(sqrt(N)) per query \u306A\u306E\u3067, \u904E\u5EA6\
    \u306A\u671F\u5F85\u306F\u3057\u306A\u3044\u3053\u3068.\n\nfrom bisect import\
    \ bisect_left, bisect_right\nclass Sorted_Set:\n    BUCKET_RATIO=50\n    REBUILD_RATIO=170\n\
    \n    def __init__(self, A=[]):\n        A=list(A)\n        if not all(A[i]<A[i+1]\
    \ for i in range(len(A)-1)):\n            A=sorted(set(A))\n        self.__build(A)\n\
    \        return\n\n    def __build(self, A=None):\n        if A is None:\n   \
    \         A=list(self)\n\n        self.N=N=len(A)\n        K=1\n        while\
    \ self.BUCKET_RATIO*K*K<N:\n            K+=1\n\n        self.list=[A[N*i//K: N*(i+1)//K]\
    \ for i in range(K)]\n\n    def __iter__(self):\n        for A in self.list:\n\
    \            for a in A:\n                yield a\n\n    def __reversed__(self):\n\
    \        for A in reversed(self.list):\n            for a in reversed(A):\n  \
    \              yield a\n\n    def __len__(self):\n        return self.N\n\n  \
    \  def __bool__(self):\n        return bool(self.N)\n\n    def is_empty(self):\n\
    \        return self.N == 0\n\n    def __str__(self):\n        string=str(list(self))\n\
    \        return \"{\"+string[1:-1]+\"}\"\n\n    def __repr__(self):\n        return\
    \ \"Sorted Set: \"+str(self)\n\n    def __find_bucket(self, x):\n        for A\
    \ in self.list:\n            if x<=A[-1]:\n                return A\n        else:\n\
    \            return A\n\n    def __contains__(self, x):\n        if self.N==0:\n\
    \            return False\n\n        A=self.__find_bucket(x)\n        i=bisect_left(A,x)\n\
    \        return i!=len(A) and A[i]==x\n\n    def add(self, x):\n        if self.N==0:\n\
    \            self.list=[[x]]\n            self.N+=1\n            return True\n\
    \n        A=self.__find_bucket(x)\n        i=bisect_left(A, x)\n\n        if i!=len(A)\
    \ and A[i]==x:\n            return False # x \u304C\u65E2\u306B\u5B58\u5728\u3059\
    \u308B\u306E\u3067...\n\n        A.insert(i,x)\n        self.N+=1\n\n        if\
    \ len(A)>len(self.list)*self.REBUILD_RATIO:\n            self.__build()\n    \
    \    return True\n\n    def discard(self, x):\n        if self.N==0:\n       \
    \     return False\n\n        A=self.__find_bucket(x)\n        i=bisect_left(A,\
    \ x)\n\n        if not(i!=len(A) and A[i]==x):\n            return False # x \u304C\
    \u5B58\u5728\u3057\u306A\u3044\u306E\u3067...\n\n        A.pop(i)\n        self.N-=1\n\
    \n        if len(A)==0:\n            self.__build()\n\n        return True\n\n\
    \    def remove(self, x):\n        if not self.discard(x):\n            raise\
    \ KeyError(x)\n\n    #=== get, pop\n\n    def __getitem__(self, index):\n    \
    \    if index<0:\n            index+=self.N\n            if index<0:\n       \
    \         raise IndexError(\"index out of range\")\n\n        for A in self.list:\n\
    \            if index<len(A):\n                return A[index]\n            index-=len(A)\n\
    \        else:\n            raise IndexError(\"index out of range\")\n\n    def\
    \ get_min(self):\n        if self.N==0:\n            raise ValueError(\"This is\
    \ empty set.\")\n\n        return self.list[0][0]\n\n    def pop_min(self):\n\
    \        if self.N==0:\n            raise ValueError(\"This is empty set.\")\n\
    \n        A=self.list[0]\n        value=A.pop(0)\n        self.N-=1\n\n      \
    \  if len(A)==0:\n            self.__build()\n\n        return value\n\n    def\
    \ get_max(self):\n        if self.N==0:\n            return ValueError(\"This\
    \ is empty set.\")\n\n        return self.list[-1][-1]\n\n    def pop_max(self):\n\
    \        if self.N==0:\n            raise ValueError(\"This is empty set.\")\n\
    \n        A=self.list[-1]\n        value=A.pop(-1)\n        self.N-=1\n\n    \
    \    if len(A)==0:\n            self.__build()\n\n        return value\n\n   \
    \ #=== k-th element\n    def kth_min(self, k):\n        \"\"\" k (0-indexed) \u756A\
    \u76EE\u306B\u5C0F\u3055\u3044\u6574\u6570\u3092\u6C42\u3081\u308B.\n\n      \
    \  k: int (0<=k<|S|)\n        \"\"\"\n\n        assert 0<=k<len(self)\n\n    \
    \    return self[k]\n\n    def kth_max(self, k):\n        \"\"\" k (0-indexed)\
    \ \u756A\u76EE\u306B\u5927\u304D\u3044\u6574\u6570\u3092\u6C42\u3081\u308B.\n\n\
    \        k: int (0<=k<|S|)\n        \"\"\"\n\n        assert 0<=k<len(self)\n\n\
    \        return self[len(self)-1-k]\n\n    #=== previous, next\n\n    def previous(self,\
    \ value, mode=False):\n        \"\"\" S \u306B\u3042\u308B value \u672A\u6E80\u3067\
    \u6700\u5927\u306E\u8981\u7D20\u3092\u8FD4\u3059 (\u5B58\u5728\u3057\u306A\u3044\
    \u5834\u5408\u306F None)\n\n        mode: True \u306E\u3068\u304D\u306F \"\u672A\
    \u6E80\" \u304C \"\u4EE5\u4E0B\" \u306B\u306A\u308B.\n        \"\"\"\n\n     \
    \   if self.N==0:\n            return None\n\n        if mode:\n            for\
    \ A in reversed(self.list):\n                if A[0]<=value:\n               \
    \     return A[bisect_right(A,value)-1]\n        else:\n            for A in reversed(self.list):\n\
    \                if A[0]<value:\n                    return A[bisect_left(A,value)-1]\n\
    \n    def next(self, value, mode=False):\n        \"\"\" S \u306B\u3042\u308B\
    \ value \u3088\u308A\u5927\u304D\u3044\u6700\u5C0F\u306E\u8981\u7D20\u3092\u8FD4\
    \u3059 (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F None)\n\n        mode:\
    \ True \u306E\u3068\u304D\u306F \"\u3088\u308A\u5927\u304D\u3044\" \u304C \"\u4EE5\
    \u4E0A\" \u306B\u306A\u308B.\n        \"\"\"\n\n        if self.N==0:\n      \
    \      return None\n\n        if mode:\n            for A in self.list:\n    \
    \            if A[-1]>=value:\n                    return A[bisect_left(A,value)]\n\
    \        else:\n            for A in self.list:\n                if A[-1]>value:\n\
    \                    return A[bisect_right(A,value)]\n\n    #=== count\n    def\
    \ less_count(self, value, equal=False):\n        \"\"\" a < value \u3068\u306A\
    \u308B S \u306E\u5143 a \u306E\u500B\u6570\u3092\u6C42\u3081\u308B.\n\n      \
    \  equal=True \u306A\u3089\u3070, a < value \u304C a <= value \u306B\u306A\u308B\
    .\n        \"\"\"\n\n        if self.is_empty():\n            return 0\n\n   \
    \     count=0\n        if equal:\n            for A in self.list:\n          \
    \      if A[-1]>value:\n                    return count+bisect_right(A, value)\n\
    \                count+=len(A)\n        else:\n            for A in self.list:\n\
    \                if A[-1]>=value:\n                    return count+bisect_left(A,\
    \ value)\n                count+=len(A)\n        return count\n\n    def more_count(self,\
    \ value, equal=False):\n        \"\"\" a > value \u3068\u306A\u308B S \u306E\u5143\
    \ a \u306E\u500B\u6570\u3092\u6C42\u3081\u308B.\n\n        equal=True \u306A\u3089\
    \u3070, a > value \u304C a >= value \u306B\u306A\u308B.\n        \"\"\"\n\n  \
    \      return self.N-self.less_count(value, not equal)\n\n    #===\n    def is_upper_bound(self,\
    \ x, equal=True):\n        if self.N:\n            a=self.list[-1][-1]\n     \
    \       return (a<x) or (bool(equal) and a==x)\n        else:\n            return\
    \ True\n\n    def is_lower_bound(self, x, equal=True):\n        if self.N:\n \
    \           a=self.list[0][0]\n            return (x<a) or (bool(equal) and a==x)\n\
    \        else:\n            return True\n\n    #=== index\n    def index(self,\
    \ value):\n        index=0\n        for A in self.list:\n            if A[-1]>value:\n\
    \                i=bisect_left(A, value)\n                if A[i]==value:\n  \
    \                  return index+i\n                else:\n                   \
    \ raise ValueError(\"{} is not in Set\".format(value))\n            index+=len(A)\n\
    \        raise ValueError(\"{} is not in Set\".format(value))\n"
  dependsOn: []
  isVerificationFile: false
  path: Sorted_Set/Sorted_Set.py
  requiredBy: []
  timestamp: '2024-06-26 00:20:40+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Sorted_Set/Sorted_Set.py
layout: document
redirect_from:
- /library/Sorted_Set/Sorted_Set.py
- /library/Sorted_Set/Sorted_Set.py.html
title: Sorted_Set/Sorted_Set.py
---
