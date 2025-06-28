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
    - https://qiita.com/tatyam/items/492c70ac4c955c055602
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# Reference: https://qiita.com/tatyam/items/492c70ac4c955c055602\n# \u203B\
    \ \u8A08\u7B97\u91CF\u304C O(sqrt(N)) per query \u306A\u306E\u3067, \u904E\u5EA6\
    \u306A\u671F\u5F85\u306F\u3057\u306A\u3044\u3053\u3068.\n\nfrom bisect import\
    \ bisect_left, bisect_right\nfrom typing import Generic, Iterable, Iterator, TypeVar\n\
    T = TypeVar('T')\n\nclass Sorted_Set(Generic[T]):\n    BUCKET_RATIO=50\n    REBUILD_RATIO=170\n\
    \n    def __init__(self, A: Iterable[T] = None):\n        if A is None:\n    \
    \        A = []\n\n        A = list(A)\n\n        # Sorted ?\n        if not all(A[i]\
    \ < A[i+1] for i in range(len(A) - 1)):\n            A = sorted(set(A))\n\n  \
    \      # Unique ?\n        if not all(A[i] == A[i + 1] for i in range(len(A) -\
    \ 1)):\n            A, A_cand = [], A\n            for a in A_cand:\n        \
    \        if (not A) or (A[-1] != a):\n                    A.append(a)\n\n    \
    \    self.__build(A)\n\n    def __build(self, A: list = None):\n        if A is\
    \ None:\n            A = list(self)\n\n        self._N = N = len(A)\n        K\
    \ = 0\n        while self.BUCKET_RATIO * K * K < N:\n            K += 1\n\n  \
    \      self._buckets: list[list[T]] = [A[N * i // K: N * (i + 1) // K] for i in\
    \ range(K)]\n        self._last : list[T] = [bucket[-1] for bucket in self._buckets]\n\
    \n    @property\n    def N(self) -> int:\n        return self._N\n\n    def __iter__(self)\
    \ -> Iterator[T]:\n        for A in self._buckets:\n            yield from A\n\
    \n    def __reversed__(self) -> Iterator[T]:\n        for A in reversed(self._buckets):\n\
    \            yield from reversed(A)\n\n    def __len__(self) -> int:\n       \
    \ return self.N\n\n    def __bool__(self) -> bool:\n        return self.N > 0\n\
    \n    def is_empty(self) -> bool:\n        \"\"\" \u7A7A\u96C6\u5408\u304B\u3069\
    \u3046\u304B\u3092\u5224\u65AD\u3059\u308B.\n\n        Returns:\n            bool:\
    \ \u7A7A\u96C6\u5408\u306A\u3089\u3070 True\n        \"\"\"\n        return self.N\
    \ == 0\n\n    def __str__(self) -> str:\n        return f\"{{{', '.join([str(x)\
    \ for x in self])}}}\"\n\n    def __repr__(self) -> str:\n        return f\"{self.__class__.__name__}({list(self)})\"\
    \n\n    def __find_bucket_index(self, x):\n        if self._last[-1] < x:\n  \
    \          return len(self._last) -1\n\n        return bisect_left(self._last,\
    \ x)\n\n    def _set_last(self, i: int, bucket: list[T]):\n        self._last[i]\
    \ = bucket[-1]\n\n    def __contains__(self, x: T) -> bool:\n        if self.is_empty():\n\
    \            return False\n\n        i = self.__find_bucket_index(x)\n       \
    \ A = self._buckets[i]\n        j = bisect_left(A, x)\n        return (j != len(A))\
    \ and (A[j] == x)\n\n    def add(self, x: T) -> bool:\n        \"\"\" \u96C6\u5408\
    \u306B\u8981\u7D20 x \u3092\u8FFD\u52A0\u3059\u308B.\n\n        Args:\n      \
    \      x (T): \u8FFD\u52A0\u3059\u308B\u8981\u7D20\n\n        Returns:\n     \
    \       bool: \u8FFD\u52A0\u306B\u3088\u308B\u5DEE\u5206\u304C\u767A\u751F\u3059\
    \u308C\u3070 True\n        \"\"\"\n\n        if self.is_empty():\n           \
    \ self._buckets=[[x]]\n            self._last = [x]\n            self._N += 1\n\
    \            return True\n\n        i = self.__find_bucket_index(x)\n        A\
    \ = self._buckets[i]\n        j = bisect_left(A, x)\n\n        if (j != len(A))\
    \ and (A[j] == x):\n            return False # x \u304C\u65E2\u306B\u5B58\u5728\
    \u3059\u308B\u306E\u3067...\n\n        A.insert(j, x)\n        self._set_last(i,\
    \ A)\n        self._N += 1\n\n        if len(A)>len(self._buckets)*self.REBUILD_RATIO:\n\
    \            self.__build()\n\n        return True\n\n    def discard(self, x:\
    \ T) -> bool:\n        \"\"\" \u96C6\u5408\u304B\u3089\u8981\u7D20 x \u3092\u524A\
    \u9664\u3059\u308B.\n\n        Args:\n            x (T): \u524A\u9664\u3059\u308B\
    \u8981\u7D20\n\n        Returns:\n            bool: \u524A\u9664\u306B\u3088\u308B\
    \u5DEE\u5206\u304C\u767A\u751F\u3059\u308C\u3070 True\n        \"\"\"\n\n    \
    \    if self.is_empty():\n            return False\n\n        i = self.__find_bucket_index(x)\n\
    \        A = self._buckets[i]\n        j = bisect_left(A, x)\n\n        if not(j\
    \ != len(A) and A[j] == x):\n            return False # x \u304C\u5B58\u5728\u3057\
    \u306A\u3044\u306E\u3067...\n\n        A.pop(j)\n        self._N -= 1\n\n    \
    \    if A:\n            self._set_last(i, A)\n        else:\n            self.__build()\n\
    \n        return True\n\n    def remove(self, x: T):\n        \"\"\" \u96C6\u5408\
    \u304B\u3089 x \u3092\u524A\u9664\u3059\u308B.\n\n        Args:\n            x\
    \ (T): \u524A\u9664\u3059\u308B\u8981\u7D20\n\n        Raises:\n            KeyError:\
    \ x \u304C\u5B58\u5728\u3057\u306A\u3044\u3068\u304D\u306B\u767A\u751F.\n    \
    \    \"\"\"\n        if not self.discard(x):\n            raise KeyError(x)\n\n\
    \    #=== get, pop\n\n    def __getitem__(self, index):\n        if index<0:\n\
    \            index+=self.N\n            if index<0:\n                raise IndexError(\"\
    index out of range\")\n\n        for A in self._buckets:\n            if index<len(A):\n\
    \                return A[index]\n            index-=len(A)\n        else:\n \
    \           raise IndexError(\"index out of range\")\n\n    def get_min(self)\
    \ -> T:\n        \"\"\" \u6700\u5C0F\u5024\u3092\u53D6\u5F97\u3059\u308B.\n\n\
    \        Raises:\n            ValueError: \u7A7A\u96C6\u5408\u3067\u3042\u3063\
    \u3066\u306F\u306A\u3089\u306A\u3044.\n\n        Returns:\n            T: \u6700\
    \u5C0F\u5024\n        \"\"\"\n\n        if self.is_empty():\n            raise\
    \ ValueError(\"This is empty set.\")\n\n        return self._buckets[0][0]\n\n\
    \    def pop_min(self) -> T:\n        \"\"\" \u6700\u5C0F\u5024\u3092\u524A\u9664\
    \u3057, \u305D\u306E\u6700\u5C0F\u5024\u3092\u8FD4\u308A\u5024\u3068\u3059\u308B\
    .\n\n        Raises:\n            ValueError: \u7A7A\u96C6\u5408\u3067\u3042\u3063\
    \u3066\u306F\u306A\u3089\u306A\u3044.\n\n        Returns:\n            T: \u6700\
    \u5C0F\u5024\n        \"\"\"\n\n        if self.is_empty():\n            raise\
    \ ValueError(\"This is empty set.\")\n\n        A=self._buckets[0]\n        value=A.pop(0)\n\
    \        self._N -= 1\n\n        if len(A)==0:\n            self.__build()\n\n\
    \        return value\n\n    def get_max(self) -> T:\n        \"\"\" \u6700\u5927\
    \u5024\u3092\u53D6\u5F97\u3059\u308B.\n\n        Raises:\n            ValueError:\
    \ \u7A7A\u96C6\u5408\u3067\u3042\u3063\u3066\u306F\u306A\u3089\u306A\u3044.\n\n\
    \        Returns:\n            T: \u6700\u5927\u5024\n        \"\"\"\n\n     \
    \   if self.is_empty():\n            return ValueError(\"This is empty set.\"\
    )\n\n        return self._buckets[-1][-1]\n\n    def pop_max(self) -> T:\n   \
    \     \"\"\" \u6700\u5927\u5024\u3092\u524A\u9664\u3057, \u305D\u306E\u6700\u5927\
    \u5024\u3092\u8FD4\u308A\u5024\u3068\u3059\u308B.\n\n        Raises:\n       \
    \     ValueError: \u7A7A\u96C6\u5408\u3067\u3042\u3063\u3066\u306F\u306A\u3089\
    \u306A\u3044.\n\n        Returns:\n            T: \u6700\u5927\u5024\n       \
    \ \"\"\"\n\n        if self.is_empty():\n            raise ValueError(\"This is\
    \ empty set.\")\n\n        A=self._buckets[-1]\n        value=A.pop(-1)\n    \
    \    self._N -= 1\n\n        if A:\n            self._set_last(len(self._buckets)\
    \ - 1, A)\n        else:\n            self.__build()\n\n        return value\n\
    \n    #=== k-th element\n    def kth_min(self, k: int) -> T:\n        \"\"\" k\
    \ (0-indexed) \u756A\u76EE\u306B\u5C0F\u3055\u3044\u5024\u3092\u6C42\u3081\u308B\
    .\n\n        Args:\n            k (int): \u8981\u7D20\u756A\u53F7\n\n        Returns:\n\
    \            T: k \u756A\u76EE\u306B\u5C0F\u3055\u3044\u5024\n        \"\"\"\n\
    \n        if not(0 <= k < len(self)):\n            raise IndexError\n\n      \
    \  return self[k]\n\n    def kth_max(self, k: int) -> T:\n        \"\"\" k (0-indexed)\
    \ \u756A\u76EE\u306B\u5927\u304D\u3044\u5024\u3092\u6C42\u3081\u308B.\n\n    \
    \    Args:\n            k (int): \u8981\u7D20\u756A\u53F7\n\n        Returns:\n\
    \            T: k \u756A\u76EE\u306B\u5927\u304D\u3044\u5024\n        \"\"\"\n\
    \n        if not(0 <= k < len(self)):\n            raise IndexError\n\n      \
    \  return self[len(self) - 1 - k]\n\n    #=== previous, next\n\n    def previous(self,\
    \ value: T, equal: bool = False) -> T | None:\n        \"\"\" value \u672A\u6E80\
    \u306E\u6700\u5927\u5024\u3092\u6C42\u3081\u308B.\n\n        Args:\n         \
    \   value (T): \u95BE\u5024\n            equal (bool, optional): True \u306B\u3059\
    \u308B\u3068, \"\u672A\u6E80\" \u304C \"\u4EE5\u4E0B\"\u306B\u306A\u308B. Defaults\
    \ to False.\n\n        Returns:\n            T | None: value \u672A\u6E80\u306E\
    \u6700\u5927\u5024 (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F None)\n \
    \       \"\"\"\n\n        if self.is_empty():\n            return None\n\n   \
    \     if equal:\n            for bucket in reversed(self._buckets):\n        \
    \        if bucket[0] <= value:\n                    return bucket[bisect_right(bucket,value)\
    \ - 1]\n        else:\n            for bucket in reversed(self._buckets):\n  \
    \              if bucket[0] <value:\n                    return bucket[bisect_left(bucket,\
    \ value) - 1]\n\n    def next(self, value: T, equal: bool = False) -> T | None:\n\
    \        \"\"\" value \u3088\u308A\u5927\u304D\u3044\u6700\u5C0F\u5024\u3092\u6C42\
    \u3081\u308B.\n\n        Args:\n            value (T): \u95BE\u5024\n        \
    \    mode (bool, optional): True \u306B\u3059\u308B\u3068, \"\u3088\u308A\u5927\
    \u304D\u3044\" \u304C \"\u4EE5\u4E0A\"\u306B\u306A\u308B. Defaults to False.\n\
    \n        Returns:\n            T | None: value \u3088\u308A\u5927\u304D\u3044\
    \u6700\u5C0F\u5024 (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F None)\n \
    \       \"\"\"\n\n        if self.is_empty():\n            return None\n\n   \
    \     if equal:\n            for bucket in self._buckets:\n                if\
    \ bucket[-1] >= value:\n                    return bucket[bisect_left(bucket,\
    \ value)]\n        else:\n            for bucket in self._buckets:\n         \
    \       if bucket[-1] > value:\n                    return bucket[bisect_right(bucket,\
    \ value)]\n\n    #=== count\n    def less_count(self, value: T, equal: bool =\
    \ False) -> int:\n        \"\"\" value \u672A\u6E80\u306E\u5143\u306E\u500B\u6570\
    \u3092\u6C42\u3081\u308B.\n\n        Args:\n            value (T): \u95BE\u5024\
    \n            equal (bool, optional): True \u306B\u3059\u308B\u3068, \"\u672A\u6E80\
    \" \u304C \"\u4EE5\u4E0B\" \u306B\u306A\u308B. Defaults to False.\n\n        Returns:\n\
    \            int: value \u672A\u6E80\u306E\u5143\u306E\u500B\u6570\n        \"\
    \"\"\n\n        if self.is_empty():\n            return 0\n\n        count=0\n\
    \        if equal:\n            for A in self._buckets:\n                if A[-1]>value:\n\
    \                    return count+bisect_right(A, value)\n                count+=len(A)\n\
    \        else:\n            for A in self._buckets:\n                if A[-1]>=value:\n\
    \                    return count+bisect_left(A, value)\n                count+=len(A)\n\
    \        return count\n\n    def more_count(self, value: T, equal: bool = False)\
    \ -> int:\n        \"\"\" value \u3088\u308A\u5927\u304D\u3044\u306E\u5143\u306E\
    \u500B\u6570\u3092\u6C42\u3081\u308B.\n\n        Args:\n            value (T):\
    \ \u95BE\u5024\n            equal (bool, optional): True \u306B\u3059\u308B\u3068\
    , \"\u3088\u308A\u5927\u304D\u3044\" \u304C \"\u4EE5\u4E0A\" \u306B\u306A\u308B\
    . Defaults to False.\n\n        Returns:\n            int: value \u3088\u308A\u5927\
    \u304D\u3044\u5143\u306E\u500B\u6570\n        \"\"\"\n\n        return self.N\
    \ - self.less_count(value, not equal)\n\n    #===\n    def is_upper_bound(self,\
    \ x: T, equal: bool = True) -> bool:\n        \"\"\" x \u306F\u3053\u306E\u96C6\
    \u5408\u306E\u4E0A\u754C (\u4EFB\u610F\u306E\u5143 a \u306B\u5BFE\u3057\u3066\
    , a <= x) \u304B ?\n\n        Args:\n            x (T): \u5024\n            equal\
    \ (bool, optional): False \u306B\u3059\u308B\u3068, \u771F\u306E\u4E0A\u754C\u304B\
    ? \u306B\u306A\u308B. Defaults to True.\n\n        Returns:\n            bool:\
    \ \u4E0A\u754C ?\n        \"\"\"\n\n        if self.is_empty():\n            return\
    \ True\n\n        a=self._buckets[-1][-1]\n        return (a<x) or (bool(equal)\
    \ and a==x)\n\n    def is_lower_bound(self, x: T, equal: bool = True) -> bool:\n\
    \        \"\"\" x \u306F\u3053\u306E\u96C6\u5408\u306E\u4E0B\u754C (\u4EFB\u610F\
    \u306E\u5143 a \u306B\u5BFE\u3057\u3066, x <= a) \u304B ?\n\n        Args:\n \
    \           x (T): \u5024\n            equal (bool, optional): False \u306B\u3059\
    \u308B\u3068, \u771F\u306E\u4E0B\u754C\u304B? \u306B\u306A\u308B. Defaults to\
    \ True.\n\n        Returns:\n            bool: \u4E0B\u754C ?\n        \"\"\"\n\
    \n        if self.is_empty():\n            return True\n\n        a=self._buckets[0][0]\n\
    \        return (x<a) or (bool(equal) and a==x)\n\n\n    #=== index\n    def index(self,\
    \ value: T) -> int:\n        \"\"\" \u8981\u7D20 x \u306E\u8981\u7D20\u756A\u53F7\
    \u3092\u6C42\u3081\u308B.\n\n        Args:\n            value (T): \u8981\u7D20\
    \n\n        Raises:\n            ValueError: \u5B58\u5728\u3057\u306A\u3044\u5834\
    \u5408\u306B\u767A\u751F\n\n        Returns:\n            int: \u8981\u7D20\u756A\
    \u53F7\n        \"\"\"\n\n        index=0\n        for A in self._buckets:\n \
    \           if A[-1]>value:\n                i=bisect_left(A, value)\n       \
    \         if A[i]==value:\n                    return index+i\n              \
    \  else:\n                    raise ValueError(f\"{value} is not in Set\")\n \
    \           index+=len(A)\n        raise ValueError(f\"{value} is not in Set\"\
    )\n"
  dependsOn: []
  isVerificationFile: false
  path: Sorted_Set/Sorted_Set.py
  requiredBy: []
  timestamp: '2025-03-09 01:40:46+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Sorted_Set/Sorted_Set.py
layout: document
redirect_from:
- /library/Sorted_Set/Sorted_Set.py
- /library/Sorted_Set/Sorted_Set.py.html
title: Sorted_Set/Sorted_Set.py
---
