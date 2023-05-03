---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Longest_Increasing_Subsequence.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Longest_Increasing_Subsequence.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Longest_Increasing_Subsequence(A, mode=False, equal=False):\n    \"\"\
    \" \u5217 L \u306B\u304A\u3051\u308B LIS \u306E\u9577\u3055\u3092\u6C42\u3081\u308B\
    .\n\n    Mode=False \u306E\u3068\u304D ... LIS \u306E\u9577\u3055, True \u306E\
    \u3068\u304D ... (\u9577\u3055, \u4E00\u4F8B, \u4E00\u4F8B\u306E\u5404\u8981\u7D20\
    \u306E\u5834\u6240)\n    equal: False \u306E\u3068\u304D ... \u72ED\u7FA9\u5358\
    \u8ABF\u5897\u52A0, True \u306E\u3068\u304D... \u5E83\u7FA9\u5358\u8ABF\u5897\u52A0\
    \n    \"\"\"\n\n    if equal:\n        from bisect import bisect_right as bis\n\
    \    else:\n        from bisect import bisect_left as bis\n\n    if mode:\n  \
    \      L=[]\n        Ind=[0]*len(A)\n        for i in range(len(A)):\n       \
    \     a=A[i]\n            k=bis(L,a)\n            if k==len(L):\n            \
    \    L.append(a)\n            else:\n                L[k]=a\n            Ind[i]=k\n\
    \n        X=[]\n        I=[]\n        j=len(L)-1\n        for i in range(len(A)-1,-1,-1):\n\
    \            if Ind[i]==j:\n                j-=1\n                X.append(A[i])\n\
    \                I.append(i)\n\n        return len(L), X[::-1], I[::-1]\n    else:\n\
    \        L=[]\n        for a in A:\n            k=bis(L,a)\n            if k==len(L):\n\
    \                L.append(a)\n            else:\n                L[k]=a\n    \
    \    return len(L)\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Longest_Increasing_Subsequence.py
  requiredBy: []
  timestamp: '2022-11-25 03:34:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Longest_Increasing_Subsequence.test.py
documentation_of: Sequence/Longest_Increasing_Subsequence.py
layout: document
redirect_from:
- /library/Sequence/Longest_Increasing_Subsequence.py
- /library/Sequence/Longest_Increasing_Subsequence.py.html
title: Sequence/Longest_Increasing_Subsequence.py
---
