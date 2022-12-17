---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Sparse_Table.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Sparse_Table.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://qiita.com/recuraki/items/0fcbc9e2abbc4fae5f62"""
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Sparse_Table:\n    \"\"\" \u53C2\u8003: https://qiita.com/recuraki/items/0fcbc9e2abbc4fae5f62\"\
    \"\"\n\n    def __init__(self, A, op):\n        \"\"\" A \u306E\u6F14\u7B97 op\
    \ \u306B\u5BFE\u3059\u308B Sparse Table \u3092\u751F\u6210\u3059\u308B.\n\n  \
    \      A: list\n        op: \u4E8C\u9805\u6F14\u7B97\n        (op \u306F\u7D50\
    \u5408\u5247, \u53EF\u63DB\u5247, \u51AA\u7B49\u901F\u3092\u6E80\u305F\u3057\u3066\
    \u3044\u308B\u3053\u3068\u3092\u8981\u6C42\u3059\u308B)\n        \"\"\"\n\n  \
    \      self.op=op\n        self.N=N=len(A)\n        self.depth=max(1,(N-1).bit_length())\n\
    \n        self.table=[[a for a in A]]\n        for k in range(1, self.depth):\n\
    \            tab=self.table[-1]\n            m=1<<(k-1)\n            B=[op(tab[i],\
    \ tab[i+m]) for i in range(N-2*m+1)]\n            self.table.append(B)\n\n   \
    \ def product(self, l, r, default=None, left_close=True, right_close=True):\n\
    \        \"\"\" l<=i<=r \u306B\u5BFE\u3059\u308B\u7A4D\u3092\u751F\u6210\u3059\
    \u308B.\n\n        \"\"\"\n\n        if not left_close:\n            l+=1\n\n\
    \        if right_close:\n            r+=1\n\n        length=r-l\n        if length==1:\n\
    \            return self.table[0][l]\n        elif length<=0:\n            return\
    \ default\n\n        lv=(length-1).bit_length()-1\n        tab=self.table[lv]\n\
    \        return self.op(tab[l], tab[r-(2**lv)])\n"
  dependsOn: []
  isVerificationFile: false
  path: Sparse_Table.py
  requiredBy: []
  timestamp: '2022-12-18 03:53:02+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Sparse_Table.test.py
documentation_of: Sparse_Table.py
layout: document
redirect_from:
- /library/Sparse_Table.py
- /library/Sparse_Table.py.html
title: Sparse_Table.py
---
