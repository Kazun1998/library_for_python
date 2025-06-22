---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Stern_Brocot_Tree.py
    title: Stern_Brocot_Tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/stern_brocot_tree
    links:
    - https://judge.yosupo.jp/problem/stern_brocot_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/stern_brocot_tree\n\
    \n#==================================================\nfrom Stern_Brocot_Tree\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    T = int(input())\n\
    \n    ans = [None] * T\n    for t in range(T):\n        command, *value = input().split()\n\
    \        if command == 'ENCODE_PATH':\n            a, b = map(int, value)\n  \
    \          code = Stern_Brocot_Tree.encode(a, b)\n            ans[t] = ' '.join([str(len(code))]\
    \ + [f'{c} {n}' for c, n in code])\n        elif command == 'DECODE_PATH':\n \
    \           k, *seq = value\n            k = int(k)\n            code = [(seq[2\
    \ * i], int(seq[2 * i + 1])) for i in range(k)]\n            a, b = Stern_Brocot_Tree.decode(code)\n\
    \            ans[t] = f'{a} {b}'\n        elif command == 'LCA':\n           \
    \ a, b, c, d = map(int, value)\n            f, g = Stern_Brocot_Tree.lowest_common_ancestor(a,\
    \ b, c, d)\n            ans[t] = f'{f} {g}'\n        elif command == 'ANCESTOR':\n\
    \            k, a, b = map(int, value)\n            f, g = Stern_Brocot_Tree.ancestor(a,\
    \ b, k, (None, None))\n            if f is None:\n                ans[t] = '-1'\n\
    \            else:\n                ans[t] = f'{f} {g}'\n        elif command\
    \ == 'RANGE':\n            a, b = map(int, value)\n            f, g, h, k = Stern_Brocot_Tree.range(a,\
    \ b)\n            ans[t] = f'{f} {g} {h} {k}'\n    return ans\n\n#==================================================\n\
    \nwrite(\"\\n\".join(map(str, verify())))\n"
  dependsOn:
  - Stern_Brocot_Tree.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Math/Stern_Brocot_Tree.test.py
  requiredBy: []
  timestamp: '2025-06-22 15:30:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Math/Stern_Brocot_Tree.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Math/Stern_Brocot_Tree.test.py
- /verify/test_verify/yosupo_library_checker/Math/Stern_Brocot_Tree.test.py.html
title: test_verify/yosupo_library_checker/Math/Stern_Brocot_Tree.test.py
---
