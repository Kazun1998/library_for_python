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
    - https://github.com/tatyam-prime/SortedSet/blob/main/BucketList.py
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# Reference: https://github.com/tatyam-prime/SortedSet/blob/main/BucketList.py\n\
    from typing import TypeVar, Generic, Iterable, Iterator\n\nT = TypeVar('T')\n\
    class Bucket_List(Generic[T]):\n    BUCKET_RATIO = 16\n    SPLIT_RATIO = 24\n\n\
    \    def __init__(self, A: Iterable[T] = []) -> None:\n        A = list(A)\n \
    \       N = self.size = len(A)\n\n        bucket_number = int(pow(N / self.BUCKET_RATIO,\
    \ 0.5) + 1)\n        self.buckets = [A[N * i // bucket_number: N * (i + 1) //\
    \ bucket_number] for i in range(bucket_number)]\n\n    def __iter__(self) -> Iterator[T]:\n\
    \        for bucket in self.buckets:\n            yield from bucket\n\n    def\
    \ __reversed__(self) -> Iterator[T]:\n        for bucket in reversed(self.buckets):\n\
    \            yield from reversed(bucket)\n\n    def __len__(self) -> int:\n  \
    \      return self.size\n\n    def __str__(self) -> str:\n        return str(list(self))\n\
    \n    def __repr__(self) -> str:\n        return f\"[Bucket List] {str(self)}\"\
    \n\n    def __eq__(self, other):\n        if len(self) != len(other):\n      \
    \      return False\n\n        for x, y in zip(self, other):\n            if x\
    \ != y:\n                return False\n        return True\n\n    def __contains__(self,\
    \ x: T) -> bool:\n        for y in self:\n            if x == y:\n           \
    \     return True\n        return False\n\n    def __insert(self, bucket: list[T],\
    \ bucket_index: int, index: int, x: T) -> None:\n        bucket.insert(index,\
    \ x)\n        self.size += 1\n        if len(bucket) > len(self.buckets) * self.SPLIT_RATIO:\n\
    \            mid = len(bucket) >> 1\n            self.buckets[bucket_index: bucket_index\
    \ + 1] = [bucket[:mid], bucket[mid:]]\n\n    def insert(self, i: int, x: T) ->\
    \ None:\n        if len(self) == 0:\n            if not(i == 0 or i == -1):\n\
    \                raise IndexError\n\n            self.buckets = [[x]]\n      \
    \      self.size = 1\n            return\n\n        if i < 0:\n            for\
    \ reversed_bucket_index, bucket in enumerate(reversed(self.buckets)):\n      \
    \          i += len(bucket)\n                if i >= 0:\n                    return\
    \ self.__insert(bucket, len(self.buckets) + (~reversed_bucket_index), i, x)\n\
    \        else:\n            for bucket_index, bucket in enumerate(self.buckets):\n\
    \                if i <= len(bucket):\n                    return self.__insert(bucket,\
    \ bucket_index, i, x)\n                i -= len(bucket)\n\n    def append(self,\
    \ x: T) -> None:\n        bucket = self.buckets[-1]\n        return self.__insert(bucket,\
    \ len(self.buckets) - 1, len(bucket), x)\n\n    def extend(self, X: list[T]) ->\
    \ None:\n        for x in X:\n            self.append(x)\n\n    def __getitem__(self,\
    \ i: int) -> T:\n        if i >= 0:\n            for bucket in self.buckets:\n\
    \                if i < len(bucket):\n                    return bucket[i]\n \
    \               i -= len(bucket)\n        else:\n            for bucket in reversed(self.buckets):\n\
    \                i += len(bucket)\n                if i >= 0:\n              \
    \      return bucket[i]\n        raise IndexError\n\n    def __pop(self, bucket:\
    \ list[T], bucket_index: int, i: int) -> T:\n        res = bucket.pop(i)\n   \
    \     self.size -= 1\n        if not bucket:\n            del self.buckets[bucket_index]\n\
    \        return res\n\n    def pop(self, i: int = -1):\n        if i >= 0:\n \
    \           for bucket_index, bucket in enumerate(self.buckets):\n           \
    \     if i < len(bucket):\n                    return self.__pop(bucket, bucket_index,\
    \ i)\n                i -= len(bucket)\n        else:\n            for reversed_bucket_index,\
    \ bucket in enumerate(self.buckets):\n                i += len(bucket)\n     \
    \           if i < len(bucket):\n                    return self.__pop(bucket,\
    \ ~reversed_bucket_index, i)\n        raise IndexError\n\n    def count(self,\
    \ x: T) -> int:\n        return sum(bucket.count(x) for bucket in self.buckets)\n\
    \n    def index(self, x: T) -> int:\n        for i, y in self:\n            if\
    \ x == y:\n                return i\n        raise ValueError\n\n    def remove(self,\
    \ x: T) -> None:\n        self.pop(self.index(x))\n\n    def clear(self) -> None:\n\
    \        self.buckets = []\n        self.size = 0\n\n    def reverse(self) ->\
    \ None:\n        self.buckets.reverse()\n        for bucket in self.buckets:\n\
    \            bucket.reverse()\n"
  dependsOn: []
  isVerificationFile: false
  path: Bucket_List.py
  requiredBy: []
  timestamp: '2025-02-15 11:46:37+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Bucket_List.py
layout: document
redirect_from:
- /library/Bucket_List.py
- /library/Bucket_List.py.html
title: Bucket_List.py
---
