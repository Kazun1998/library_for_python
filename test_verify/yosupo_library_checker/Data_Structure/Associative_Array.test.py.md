---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Hash_Table.py
    title: Hash_Table.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/associative_array
    links:
    - https://judge.yosupo.jp/problem/associative_array
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array\n\
    \n#==================================================\nfrom Hash_Table import\
    \ *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    Q=int(input())\n\n    H=Hash_Table()\n    ans=[]\n    for q\
    \ in range(Q):\n        mode,*query=map(int,input().split())\n\n        if mode==0:\n\
    \            H[query[0]]=query[1]\n        else:\n            ans.append(H.get(query[0],0))\n\
    \n    write(\"\\n\".join(map(str,ans)))\n\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Hash_Table.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Associative_Array.test.py
  requiredBy: []
  timestamp: '2022-11-24 23:19:31+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Associative_Array.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Associative_Array.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Associative_Array.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Associative_Array.test.py
---
