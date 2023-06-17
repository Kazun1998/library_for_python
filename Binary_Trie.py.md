---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Set_Xor_Min.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Set_Xor_Min.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://judge.yosupo.jp/submission/35057
    - https://judge.yosupo.jp/submission/53782
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Binary_Trie:\n    \"\"\" Reference\n    https://judge.yosupo.jp/submission/35057\n\
    \    https://judge.yosupo.jp/submission/53782\n    \"\"\"\n\n    def __init__(self,\
    \ max_value, allow_multiple=False, query_number=None):\n        self.bit=max_value.bit_length()\n\
    \        self.upper=1<<self.bit\n        self.multi=allow_multiple\n\n       \
    \ if query_number!=None:\n            self.arc=[-1]*2*(self.bit*query_number+1)\n\
    \            self.size=[0]*(self.bit*query_number+1)\n            self.terminal=[0]*(self.bit*query_number+1)\n\
    \            self.id=0\n        else:\n            self.arc=[-1,-1]\n        \
    \    self.size=[0]\n            self.terminal=[0]\n\n        self.query_number=query_number\n\
    \        self.v_list=[0]*(self.bit+1)\n        self.lazy_xor=0\n\n    def xor_all(self,\
    \ x):\n        assert 0<=x<self.upper\n        self.lazy_xor^=x\n\n    def __ixor__(self,\
    \ x):\n        self.xor_all(x)\n        return self\n\n    def insert(self, x):\n\
    \        \"\"\" x \u3092\u8FFD\u52A0\u3059\u308B. \"\"\"\n\n        assert 0<=x<self.upper\n\
    \n        x^=self.lazy_xor\n        v=0\n        for i in reversed(range(self.bit)):\n\
    \            d=(x>>i)&1\n            if self.arc[2*v+d]==-1:\n               \
    \ if self.query_number!=None:\n                    self.id+=1\n              \
    \      self.arc[2*v+d]=self.id\n                else:\n                    self.arc[2*v+d]=len(self.size)\n\
    \                    self.arc.append(-1); self.arc.append(-1)\n              \
    \      self.terminal.append(0)\n                    self.size.append(0)\n\n  \
    \          v=self.arc[2*v+d]\n            self.v_list[i]=v\n\n        if self.multi\
    \ or self.terminal[v]==0:\n            self.terminal[v]+=1\n            for w\
    \ in self.v_list:\n                self.size[w]+=1\n\n    def discard(self, x):\n\
    \        \"\"\" x \u304C\u5B58\u5728\u3059\u308B\u5834\u5408, x \u3092\u524A\u9664\
    \u3059\u308B. \"\"\"\n\n        if not (0<=x<self.upper):\n            return\n\
    \n        x^=self.lazy_xor\n        v=0\n        for i in reversed(range(self.bit)):\n\
    \            d=(x>>i)&1\n            if self.arc[2*v+d]==-1:\n               \
    \ return\n\n            v=self.arc[2*v+d]\n            self.v_list[i]=v\n\n  \
    \      if self.terminal[v]>0:\n            self.terminal[v]-=1\n            for\
    \ w in self.v_list:\n                self.size[w]-=1\n\n    def erase(self, x,\
    \ k):\n        \"\"\" x \u3092\u9AD8\u3005 k \u56DE\u524A\u9664\u3059\u308B (\u305F\
    \u3060\u3057, k=-1 \u306E\u3068\u304D\u306F\u7121\u9650\u56DE)\"\"\"\n\n     \
    \   assert -1<=k\n        if not (0<=x<self.upper):\n            return\n\n  \
    \      x^=self.lazy_xor\n        v=0\n        for i in reversed(range(self.bit)):\n\
    \            d=(x>>i)&1\n            if self.arc[2*v+d]==-1:\n               \
    \ return\n\n            v=self.arc[2*v+d]\n            self.v_list[i]=v\n\n  \
    \      if (k==-1) or (self.terminal[v]<k):\n            k=self.terminal[v]\n\n\
    \        if self.terminal[v]>0:\n            self.terminal[v]-=k\n           \
    \ for w in self.v_list:\n                self.size[w]-=k\n\n    def count(self,\
    \ x):\n        \"\"\" x \u306E\u500B\u6570\u3092\u6C42\u3081\u308B. \"\"\"\n \
    \       if not (0<=x<self.upper):\n            return 0\n\n        x^=self.lazy_xor\n\
    \        v=0\n        for i in reversed(range(self.bit)):\n            d=(x>>i)&1\n\
    \            if self.arc[2*v+d]==-1:\n                return 0\n            v=self.arc[2*v+d]\n\
    \        return self.terminal[v]\n\n    def __contains__(self, x):\n        return\
    \ bool(self.count(x))\n\n    def __len__(self):\n        return self.size[0]\n\
    \n    def __bool__(self):\n        return bool(len(self))\n\n    def less_count(self,\
    \ x, equal=False):\n        \"\"\" x \u672A\u6E80\u306E\u8981\u7D20\u6570\u3092\
    \u6C42\u3081\u308B (equal=True \u306E\u3068\u304D\u306F, \"\u672A\u6E80\" \u304C\
    \ \"\u4EE5\u4E0B\" \u306B\u306A\u308B)\"\"\"\n\n        x^=self.lazy_xor\n   \
    \     if equal:\n            x+=1\n\n        if x<0:\n            return 0\n\n\
    \        if self.upper<=x:\n            return len(self)\n\n        v=0\n    \
    \    res=0\n        for i in reversed(range(self.bit)):\n            d=(x>>i)&1\n\
    \            lc=self.arc[2*v]\n            rc=self.arc[2*v+1]\n\n            if\
    \ (self.lazy_xor>>i)&1:\n                lc,rc=rc,lc\n\n            if d:\n  \
    \              if lc!=-1:\n                    res+=self.size[lc]\n          \
    \      if rc==-1:\n                    return res\n                v=rc\n    \
    \        else:\n                if lc==-1:\n                    return res\n \
    \               v=lc\n        return res\n\n    def more_count(self, x, equal=False):\n\
    \        \"\"\" x \u3088\u308A\u5927\u304D\u3044\u8981\u7D20\u6570\u3092\u6C42\
    \u3081\u308B (equal=True \u306E\u3068\u304D\u306F, \"\u3088\u308A\u5927\u304D\u3044\
    \" \u304C \"\u4EE5\u4E0A\" \u306B\u306A\u308B)\"\"\"\n\n        return len(self)-self.less_count(x,not\
    \ equal)\n\n    def low_value(self, x, equal=False, default=None):\n        \"\
    \"\" x \u672A\u6E80\u306E\u6574\u6570\u306E\u3046\u3061, \u6700\u5927\u306E\u6574\
    \u6570\u3092\u6C42\u3081\u308B (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F\
    \ default).\n\n        equal: True \u306E\u3068\u304D, \"\u672A\u6E80\" \u304C\
    \ \"\u4EE5\u4E0B\" \u306B\u306A\u308B.\n        \"\"\"\n\n        x^=self.lazy_xor\n\
    \        if equal:\n            x+=1\n\n        alpha=self.less_count(x,False)\n\
    \        if alpha==0:\n            return default\n        else:\n           \
    \ return self.kth_element(alpha,1)\n\n    def high_value(self, x, equal=False,\
    \ default=None):\n        \"\"\" x \u3088\u308A\u5927\u304D\u3044\u6574\u6570\u306E\
    \u3046\u3061, \u6700\u5C0F\u306E\u6574\u6570\u3092\u6C42\u3081\u308B (\u5B58\u5728\
    \u3057\u306A\u3044\u5834\u5408\u306F default)\n\n        equal: True \u306E\u3068\
    \u304D, \"\u3088\u308A\u5927\u304D\u3044\" \u304C \"\u4EE5\u4E0A\" \u306B\u306A\
    \u308B.\n        \"\"\"\n\n        x^=self.lazy_xor\n        if equal:\n     \
    \       x-=1\n\n        beta=self.more_count(x,False)\n        if beta==0:\n \
    \           return default\n        else:\n            return self.kth_element(-beta,0)\n\
    \n    def kth_element(self, k, index=0, default=-1):\n        \"\"\" index -indexed\
    \ \u3067 k \u756A\u76EE\u306B\u5C0F\u3055\u3044\u5024\u3092\u6C42\u3081\u308B\
    .\n        \u305F\u3060\u3057, index=0, k<0 \u306E\u3068\u304D\u306F |k| \u756A\
    \u76EE\u306B\u5927\u304D\u3044\u5024\u306B\u306A\u308B.\n\n        \"\"\"\n\n\
    \        if k<0:\n            k+=self.size[0]\n        k-=index\n        if not\
    \ (0<=k<self.size[0]):\n            return default\n\n        v=0\n        res=0\n\
    \        for i in reversed(range(self.bit)):\n            lc=self.arc[2*v]\n \
    \           rc=self.arc[2*v+1]\n\n            if (self.lazy_xor>>i)&1:\n     \
    \           lc,rc=rc,lc\n\n            if lc==-1:\n                v=rc\n    \
    \            res|=1<<i\n            elif self.size[lc]<=k:\n                k-=self.size[lc]\n\
    \                v=rc\n                res|=1<<i\n            else:\n        \
    \        v=lc\n        return res\n\n    def get_min(self):\n        return self.kth_element(1,1)\n\
    \n    def get_max(self):\n        return self.kth_element(-1)\n\n    def get_median(self,\
    \ mode=0, func=None):\n        \"\"\" \u4E2D\u592E\u5024\u3092\u6C42\u3081\u308B\
    .\n\n        [mode] \u9805\u306E\u6570\u304C\u5076\u6570\u306E\u3068\u304D\u306E\
    \u4E2D\u592E\u5024\u306E\u6C42\u3081\u65B9\u3092\u6307\u5B9A\u3059\u308B (\u305D\
    \u306E 2\u5024\u3092 a,b (a<=b) \u3068\u3059\u308B).\n        mode=-1 \u2192 a\n\
    \        mode= 0 \u2192 (a+b)/2 (float \u578B)\n        mode= 1 \u2192 b\n   \
    \     mode=(\u305D\u306E\u4ED6) \u2192 \u305D\u306E\u4ED6 ( 2\u5909\u6570\u95A2\
    \u6570 func(a,b) \u3067\u6307\u5B9A)\n        \"\"\"\n\n        if len(self)%2==1:\n\
    \            return self.kth_element(len(self)//2)\n        else:\n          \
    \  a=self.kth_element(len(self)//2)\n            b=self.kth_element(len(self)//2-1)\n\
    \n            if mode==-1:\n                return a\n            elif mode==1:\n\
    \                return b\n            elif mode==0:\n                return (a+b)/2\n\
    \            else:\n                return func(a,b)\n\n    def __getitem__(self,\
    \ index):\n        return self.kth_element(index)\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Trie.py
  requiredBy: []
  timestamp: '2022-12-13 00:51:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Set_Xor_Min.test.py
documentation_of: Binary_Trie.py
layout: document
redirect_from:
- /library/Binary_Trie.py
- /library/Binary_Trie.py.html
title: Binary_Trie.py
---
