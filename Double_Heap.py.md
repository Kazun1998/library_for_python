---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: Median.py
    title: Median.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Double_Heap.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Double_Heap.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import heapq\n\nclass Double_Heap:\n    def __init__(self):\n        self.__small=[]\n\
    \        self.__large=[]\n        self.__dict={}\n        self.__length=0\n  \
    \      self.__sum=0\n\n    def __bool__(self):\n        return bool(self.__length)\n\
    \n    def __len__(self):\n        return self.__length\n\n    def __contains__(self,\
    \ x):\n        return self.is_exist(x)\n\n    def push(self, x):\n        self.__length+=1\n\
    \        self.__sum+=x\n\n        heapq.heappush(self.__small, x)\n        heapq.heappush(self.__large,\
    \ -x)\n\n        if x in self.__dict:\n            self.__dict[x]+=1\n       \
    \ else:\n            self.__dict[x]=1\n\n    def discard(self, x):\n        \"\
    \"\" x \u3092\u6D88\u3059 (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F\u4F55\
    \u3082\u3057\u306A\u3044). \"\"\"\n\n        if x not in self:\n            return\n\
    \n        self.__dict[x]-=1\n        if self.__dict[x]==0:\n            del self.__dict[x]\n\
    \n        self.__length-=1\n        self.__sum-=x\n\n        while self.__small\
    \ and (self.__small[0] not in self):\n                heapq.heappop(self.__small)\n\
    \n        while self.__large and (-self.__large[0] not in self):\n           \
    \     heapq.heappop(self.__large)\n\n    def is_exist(self, x):\n        \"\"\"\
    \ \u30AD\u30E5\u30FC\u306B x \u304C\u5B58\u5728\u3059\u308B\u304B\u3069\u3046\u304B\
    \u3092\u5224\u5B9A\u3059\u308B. \"\"\"\n        return x in self.__dict\n\n  \
    \  def get_min(self):\n        assert self\n        return self.__small[0]\n\n\
    \    def pop_min(self):\n        assert self\n        x=self.get_min()\n     \
    \   self.discard(x)\n        return x\n\n    def get_max(self):\n        assert\
    \ self\n        return -self.__large[0]\n\n    def pop_max(self):\n        assert\
    \ self\n        x=self.get_max()\n        self.discard(x)\n        return x\n\n\
    \    def count(self, x):\n        \"\"\" x \u306E\u500B\u6570\u3092\u6C42\u3081\
    \u308B. \"\"\"\n\n        return self.__dict.get(x,0)\n\n    def sum(self):\n\
    \        return self.__sum\n\n    def __str__(self):\n        return str(self.__dict)\n\
    \n    def __repr__(self):\n        return \"[Double Heap]: \"+str(self)\n"
  dependsOn: []
  isVerificationFile: false
  path: Double_Heap.py
  requiredBy:
  - Median.py
  timestamp: '2022-12-11 17:04:31+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Double_Heap.test.py
documentation_of: Double_Heap.py
layout: document
redirect_from:
- /library/Double_Heap.py
- /library/Double_Heap.py.html
title: Double_Heap.py
---
