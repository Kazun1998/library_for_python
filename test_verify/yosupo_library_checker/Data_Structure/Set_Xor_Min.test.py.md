---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Binary_Trie.py
    title: Binary_Trie.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/set_xor_min
    links:
    - https://judge.yosupo.jp/problem/set_xor_min
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/set_xor_min\n\
    \n#==================================================\nfrom Binary_Trie import\
    \ *\n\nimport sys\ninput = sys.stdin.readline\nwrite = sys.stdout.write\n\n#================================================\n\
    def verify():\n    Q = int(input())\n    B = Binary_Trie((1 << 30) - 1, query_number\
    \ = Q)\n    ans = []\n    for _ in range(Q):\n        c , x = map(int, input().split())\n\
    \        if c == 0:\n            B.insert(x)\n        elif c == 1:\n         \
    \   B.discard(x)\n        elif c == 2:\n            B ^= x\n            ans.append(B.min)\n\
    \            B ^= x\n\n    write(\"\\n\".join(map(str, ans)))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Binary_Trie.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Set_Xor_Min.test.py
  requiredBy: []
  timestamp: '2025-05-18 20:48:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Set_Xor_Min.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Set_Xor_Min.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Set_Xor_Min.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Set_Xor_Min.test.py
---
