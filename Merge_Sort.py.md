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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Merge_Sort_by_Index(X):\n    \"\"\" \u30DE\u30FC\u30B8\u30BD\u30FC\u30C8\
    \u3059\u308B (\u8FD4\u308A\u5024\u306F\u6DFB\u5B57).\n\n    X: \u30EA\u30B9\u30C8\
    \n    \"\"\"\n\n    def merge(left, mid, right):\n        i=left; j=mid; k=0\n\
    \n        J=[0]*(right-left)\n        while (i<mid and j<right):\n           \
    \ if X[I[i]] <= X[I[j]]:\n                J[k]=I[i]\n                i+=1\n  \
    \          else:\n                J[k]=I[j]\n                j+=1\n          \
    \  k+=1\n\n        if i==mid:\n            J[k:]=I[j:right]\n        else:\n \
    \           J[k:]=I[i:mid]\n\n        I[left:right]=J\n\n    def sort(left, right):\n\
    \        if right-left<=1:\n            return\n\n        mid=(left+right)//2\n\
    \        sort(left, mid)\n        sort(mid, right)\n        merge(left, mid, right)\n\
    \n    N=len(X)\n    I=list(range(N))\n    sort(0,N)\n    return I\n\ndef Merge_Sort(X):\n\
    \    \"\"\" \u30DE\u30FC\u30B8\u30BD\u30FC\u30C8\u3059\u308B.\n\n    X: \u30EA\
    \u30B9\u30C8\n    \"\"\"\n\n    return [X[i] for i in Merge_Sort_by_Index(X)]\n"
  dependsOn: []
  isVerificationFile: false
  path: Merge_Sort.py
  requiredBy: []
  timestamp: '2023-08-09 23:57:48+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Merge_Sort.py
layout: document
redirect_from:
- /library/Merge_Sort.py
- /library/Merge_Sort.py.html
title: Merge_Sort.py
---
