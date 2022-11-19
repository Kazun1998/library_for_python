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
    - https://tsubo.hatenablog.jp/entry/2020/06/15/124657
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"\u53C2\u8003\u5143\nhttps://tsubo.hatenablog.jp/entry/2020/06/15/124657\n\
    \"\"\"\nimport heapq\nclass Heap_Dict:\n    def __init__(self, mode=True):\n \
    \       \"\"\" Heap Dict \u30AF\u30E9\u30B9\u306E\u4F5C\u6210.\n\n        Mode:\
    \ True \u2192 \u6700\u5C0F\u5024, False \u2192 \u6700\u5927\u5024\n        \"\"\
    \"\n        self.heap=[]\n        self.dict={}\n        self.__mode=bool(mode)\n\
    \        self.__length=0\n\n    def __bool__(self):\n        return bool(self.heap)\n\
    \n    def __len__(self):\n        return self.__length\n\n    def __contains__(self,\
    \ x):\n        return self.is_exist(x)\n\n    def insert(self, x):\n        \"\
    \"\" \u8981\u7D20 x \u3092\u8FFD\u52A0\u3059\u308B. \"\"\"\n\n        if self.__mode\
    \ and not self.is_exist(x):\n            heapq.heappush(self.heap,x)\n       \
    \ elif not self.__mode and not self.is_exist(x):\n            heapq.heappush(self.heap,-x)\n\
    \n        if x in self.dict:\n            self.dict[x]+=1\n        else:\n   \
    \         self.dict[x]=1\n\n        self.__length+=1\n\n    def erase(self, x):\n\
    \        \"\"\" x \u3092\u6D88\u3059 (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\
    \u306F KeyError) . \"\"\"\n\n        if x not in self:\n            raise KeyError(x)\n\
    \n        self.dict[x]-=1\n        self.__length-=1\n        while self.heap:\n\
    \            y=self.heap[0]\n            if not self.__mode:y=-y\n           \
    \ if self.dict[y]==0:\n                heapq.heappop(self.heap)\n            else:\n\
    \                break\n\n    def discard(self, x):\n        \"\"\" x \u3092\u6D88\
    \u3059 (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F\u4F55\u3082\u3057\u306A\
    \u3044). \"\"\"\n\n        if x not in self:\n            return\n\n        self.dict[x]-=1\n\
    \        self.__length-=1\n        while self.heap:\n            y=self.heap[0]\n\
    \            if not self.__mode:y=-y\n            if self.dict[y]==0:\n      \
    \          heapq.heappop(self.heap)\n            else:\n                break\n\
    \n    def is_exist(self, x):\n        \"\"\" \u30AD\u30E5\u30FC\u306B x \u304C\
    \u5B58\u5728\u3059\u308B\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B\
    . \"\"\"\n\n        return bool(self.dict.get(x,0))\n\n    def get_min(self, default=float(\"\
    inf\")):\n        \"\"\" \u30AD\u30E5\u30FC\u306B\u3042\u308B\u6700\u5C0F\u5024\
    \u3092\u8FD4\u3059.\n        \u203B Mode=True \u3067\u306A\u3044\u3068\u4F7F\u3048\
    \u306A\u3044.\n\n        \"\"\"\n\n        assert self.__mode\n\n        if self.heap:\n\
    \            return self.heap[0]\n        else:\n            return default\n\n\
    \    def pop_min(self):\n        \"\"\" \u30AD\u30E5\u30FC\u306B\u3042\u308B\u6700\
    \u5C0F\u5024\u3092\u53D6\u308A\u51FA\u3059.\n        \u203B Mode=True \u3067\u306A\
    \u3044\u3068\u4F7F\u3048\u306A\u3044.\n\n        \"\"\"\n\n        assert self.__mode\
    \ and bool(self)\n\n        x=self.get_min()\n        self.erase(x)\n        return\
    \ x\n\n    def get_max(self, default=-float(\"inf\")):\n        \"\"\" \u30AD\u30E5\
    \u30FC\u306B\u3042\u308B\u6700\u5927\u5024\u3092\u8FD4\u3059.\n        \u203B\
    \ Mode=False \u3067\u306A\u3044\u3068\u4F7F\u3048\u306A\u3044.\n\n        \"\"\
    \"\n\n        assert not self.__mode\n\n        if self.heap:\n            return\
    \ -self.heap[0]\n        else:\n            return default\n\n    def pop_max(self):\n\
    \        \"\"\" \u30AD\u30E5\u30FC\u306B\u3042\u308B\u6700\u5C0F\u5024\u3092\u53D6\
    \u308A\u51FA\u3059.\n        \u203B Mode = False \u3067\u306A\u3044\u3068\u4F7F\
    \u3048\u306A\u3044.\n\n        \"\"\"\n\n        assert (not self.__mode) and\
    \ bool(self)\n\n        x=self.get_max()\n        self.erase(x)\n        return\
    \ x\n\n    def count(self, x):\n        \"\"\" x \u306E\u500B\u6570\u3092\u6C42\
    \u3081\u308B. \"\"\"\n\n        return self.dict.get(x,0)\n"
  dependsOn: []
  isVerificationFile: false
  path: HeapDict.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: HeapDict.py
layout: document
redirect_from:
- /library/HeapDict.py
- /library/HeapDict.py.html
title: HeapDict.py
---
