---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Strongly_Connected_Components.py
    title: "Strongly Connected Components (\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3\
      )"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/scc
    links:
    - https://judge.yosupo.jp/problem/scc
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc\n\n#==================================================\n\
    from Strongly_Connected_Components import *\n\nimport sys\ninput=sys.stdin.readline\n\
    write=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    N,M=map(int,input().split())\n    S=Strongly_Connected_Components(N)\n\
    \    for _ in range(M):\n        a,b=map(int,input().split())\n        S.add_arc(a,b)\n\
    \n    S.decomposition()\n    print(len(S.components))\n    for component in S.components:\n\
    \        write(f\"{len(component)} {' '.join(map(str, component))}\\n\")\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Strongly_Connected_Components.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Graph/Strongly_Connected_Components-class.test.py
  requiredBy: []
  timestamp: '2025-03-13 23:55:26+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Graph/Strongly_Connected_Components-class.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Graph/Strongly_Connected_Components-class.test.py
- /verify/test_verify/yosupo_library_checker/Graph/Strongly_Connected_Components-class.test.py.html
title: test_verify/yosupo_library_checker/Graph/Strongly_Connected_Components-class.test.py
---
