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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Suffix_Array(S, encoder=lambda x:x):\n    \"\"\" \u6587\u5B57\u5217 S\
    \ \u306E Suffix Array (\u63A5\u5C3E\u8F9E\u914D\u5217) (S[0...], S[1...],... \u3092\
    \u8F9E\u66F8\u5F0F\u306B\u4E26\u3079\u305F\u6642\u306E\u958B\u59CB\u30A4\u30F3\
    \u30C7\u30C3\u30AF\u30B9\u306E\u5217) \u3092 SA-IS \u306B\u3088\u3063\u3066\u6C42\
    \u3081\u308B.\n\n    S: \u5217\n    encoder: \u6B63\u306E\u6574\u6570\u3078\u306E\
    \u9806\u5E8F\u57CB\u3081\u8FBC\u307F (\u203B max encoder(S) \u304C\u5C0F\u3055\
    \u3044\u307B\u3069\u8A08\u7B97\u91CF\u304C\u3088\u3044)\n    \"\"\"\n\n    A=[encoder(x)\
    \ for x in S]+[0]\n    assert min(A[:-1])>0,\"encoder \u306E\u5024\u57DF\u304C\
    \u6B63\u304B\u3089\u5916\u308C\u3066\u3044\u307E\u3059\"\n    k=max(A)+1\n   \
    \ n=len(A)\n\n    def induce_l(sa, a, n, k, stype):\n        bucket = get_buckets(a,\
    \ k, 1)\n        for i in range(n):\n            j = sa[i] - 1\n            if\
    \ j >= 0 and (not stype[j]):\n                sa[bucket[a[j]]] = j\n         \
    \       bucket[a[j]] += 1\n\n    def induce_s(sa, a, n, k, stype):\n        bucket\
    \ = get_buckets(a, k, 0)\n        for i in range(n)[::-1]:\n            j = sa[i]\
    \ - 1\n            if j >= 0 and stype[j]:\n                bucket[a[j]] -= 1\n\
    \                sa[bucket[a[j]]] = j\n\n    def get_buckets(a, k, start = 0):\n\
    \        bucket = [0] * k\n        for item in a:\n            bucket[item] +=\
    \ 1\n        s = 0\n        for i in range(k):\n            s += bucket[i]\n \
    \           bucket[i] = s - (bucket[i] if start else 0)\n        return bucket\n\
    \n    def set_lms(a, n, k, default_order):\n        bucket = get_buckets(a, k)\n\
    \        sa = [-1] * n\n        for i in default_order[::-1]:\n            bucket[a[i]]\
    \ -= 1\n            sa[bucket[a[i]]] = i\n        return sa\n\n    def induce(a,\
    \ n, k, stype, default_order):\n        sa = set_lms(a, n, k, default_order)\n\
    \        induce_l(sa, a, n, k, stype)\n        induce_s(sa, a, n, k, stype)\n\
    \        return sa\n\n    def rename_LMS_substring(sa, a, n, stype, LMS, l):\n\
    \        sa = [_s for _s in sa if LMS[_s]]\n        tmp = [-1] * (n//2) + [0]\n\
    \        dupl = 0\n        for _ in range(1, l):\n            i, j = sa[_-1],\
    \ sa[_]\n            for ii in range(n):\n                if a[i+ii] != a[j+ii]\
    \ or stype[i+ii] != stype[j+ii]:\n                    break\n                if\
    \ ii and (LMS[i+ii] or LMS[j+ii]):\n                    dupl += 1\n          \
    \          break\n            tmp[j//2] = _ - dupl\n        tmp = [t for t in\
    \ tmp if t >= 0]\n        return tmp, dupl\n\n    def calc(a, n, k):\n       \
    \ stype = [1] * n\n        for i in range(n-1)[::-1]:\n            if a[i] > a[i+1]\
    \ or (a[i] == a[i+1] and stype[i+1] == 0):\n                stype[i] = 0\n\n \
    \       LMS = [1 if stype[i] and not stype[i-1] else 0 for i in range(n-1)] +\
    \ [1]\n        l = sum(LMS)\n        lms = [i for i in range(n) if LMS[i]]\n \
    \       sa = induce(a, n, k, stype, lms)\n        renamed_LMS, dupl = rename_LMS_substring(sa,\
    \ a, n, stype, LMS, l)\n\n        if dupl:\n            sub_sa = calc(renamed_LMS,\
    \ l, l - dupl)\n        else:\n            sub_sa = [0] * l\n            for i\
    \ in range(l):\n                sub_sa[renamed_LMS[i]] = i\n\n        lms = [lms[sub_sa[i]]\
    \ for i in range(l)]\n        sa = induce(a, n, k, stype, lms)\n        return\
    \ sa\n\n    return calc(A,n,k)[1:]\n\ndef Longest_Commom_Prefix(S, encoder=lambda\
    \ x:x, with_SA=False):\n    SA=Suffix_Array(S,encoder)\n    N=len(S)\n    rank=[0]*N\n\
    \n    for i in range(N):\n        rank[SA[i]] = i\n\n    LCP=[0]*(N - 1)\n   \
    \ h=0\n    for i in range(N):\n        if h: h -= 1\n        if rank[i] == 0:\
    \ continue\n        j = SA[rank[i] - 1]\n        while j + h < N and i + h < N:\n\
    \            if S[j+h] != S[i+h]: break\n            h += 1\n        LCP[rank[i]\
    \ - 1] = h\n\n    if with_SA:\n        return SA,LCP\n    else:\n        return\
    \ LCP\n"
  dependsOn: []
  isVerificationFile: false
  path: String/Suffix_Array.py
  requiredBy: []
  timestamp: '2022-11-26 03:55:08+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: String/Suffix_Array.py
layout: document
redirect_from:
- /library/String/Suffix_Array.py
- /library/String/Suffix_Array.py.html
title: String/Suffix_Array.py
---
