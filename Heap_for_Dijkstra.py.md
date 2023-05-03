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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Dijkstra_Heap:\n    inf=float(\"inf\")\n\n    def __init__(self,N):\n\
    \        \"\"\" \u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\u5C02\u7528\u306E\u30D2\u30FC\
    \u30D7\u3092\u751F\u6210\u3059\u308B.\n        \"\"\"\n\n        self.N=N\n  \
    \      self.remain=N\n\n        self.value=[Dijkstra_Heap.inf]*N\n        self.dist=[-1]*N\n\
    \        self.tree=list(range(N))\n        self.inverse=list(range(N))\n\n   \
    \ def __bool__(self):\n        return self.value[0]<Dijkstra_Heap.inf\n\n    def\
    \ __swap(self, i, j):\n        \"\"\" \u30D2\u30FC\u30D7\u6728\u306E\u7B2C i \u8981\
    \u7D20\u3068\u7B2C j \u8981\u7D20\u3092\u4EA4\u63DB\u3059\u308B. \"\"\"\n\n  \
    \      self.value[i],self.value[j]=self.value[j],self.value[i]\n\n        p=self.tree[i];\
    \ q=self.tree[j]\n\n        self.tree[i],self.tree[j]=q,p\n        self.inverse[p],self.inverse[q]=j,i\n\
    \n    def pop(self):\n        assert bool(self.remain)\n\n        p=self.tree[0]\n\
    \        d=self.value[0]\n\n        self.dist[p]=d\n        self.remain-=1\n\n\
    \        self.__swap(0,self.remain)\n        self.value[self.remain]=Dijkstra_Heap.inf\n\
    \n        V=self.value\n        k=0\n        while True:\n            if 2*k+1>=self.N:\n\
    \                break\n\n            if 2*k+2==self.N:\n                if V[k]<=V[2*k+1]:\n\
    \                    break\n                j=2*k+1\n            else:\n     \
    \           u=V[2*k+1]; v=V[2*k+2]\n\n                if V[k]<=u and V[k]<=v:\n\
    \                    break\n\n                if u<=v:\n                    j=2*k+1\n\
    \                else:\n                    j=2*k+2\n            self.__swap(k,j)\n\
    \            k=j\n\n        return (p,d)\n\n    def __setitem__(self, index, value):\n\
    \        if self.dist[index]!=-1:\n            return\n\n        V=self.value\n\
    \        i=self.inverse[index]\n\n        if V[i]<=value:\n            return\n\
    \n        V[i]=value\n        while i>0 and V[(i-1)>>1]>V[i]:\n            j=(i-1)>>1\n\
    \            self.__swap(i,j)\n            i=j\n\n    def __getitem__(self, index):\n\
    \        return self.dist[index] if self.dist[index]>=0 else self.value[self.inverse[index]]\n\
    \n    def final_answer(self, index,default):\n        return self.dist[index]\
    \ if self.dist[index]>=0 else default\n"
  dependsOn: []
  isVerificationFile: false
  path: Heap_for_Dijkstra.py
  requiredBy: []
  timestamp: '2021-11-28 16:23:48+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Heap_for_Dijkstra.py
layout: document
redirect_from:
- /library/Heap_for_Dijkstra.py
- /library/Heap_for_Dijkstra.py.html
title: Heap_for_Dijkstra.py
---
