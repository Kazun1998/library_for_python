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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Rolling_Hash():\n    def __init__(self,S,base,mod):\n        self.mod=mod\n\
    \        self.base=base\n        self.string=S\n        self.power=power=[1]*(len(S)+1)\n\
    \n        L=len(S)\n        self.hash=h=[0]*(L+1)\n\n        v=0\n        for\
    \ i in range(L):\n            h[i+1]=v=(v*base+ord(S[i]))%mod\n            #h[i+1]=v=(v*base+S[i])%mod\n\
    \n        v=1\n        for i in range(L):\n            power[i+1]=v=(v*base)%mod\n\
    \n    def get(self,l,r):\n        return (self.hash[r]-self.hash[l]*self.power[r-l])%self.mod\n\
    \n    def count(self,T,start=0):\n        alpha=0\n        for t in T:\n     \
    \       alpha=(alpha*self.base+ord(t))%self.mod\n\n        K=0\n        for i\
    \ in range(start,len(self)-len(T)+1):\n            if alpha==self[i:i+len(T)]:\n\
    \                K+=1\n        return K\n\n    def find(self,T,start=0):\n   \
    \     alpha=0\n        for t in T:\n            alpha=(alpha*self.base+ord(t))%self.mod\n\
    \n        for i in range(start,len(self)-len(T)+1):\n            if alpha==self[i:i+len(T)]:\n\
    \                return i\n        return -1\n\n    def rfind(self,T,start=0):\n\
    \        alpha=0\n        for t in T:\n            alpha=(alpha*self.base+ord(t))%self.mod\n\
    \n        for i in range(len(self)-len(T),start-1):\n            if alpha==self[i:i+len(T)]:\n\
    \                return i\n        return -1\n\n    def index(self,T,start=0):\n\
    \        alpha=0\n        for t in T:\n            alpha=(alpha*self.base+ord(t))%self.mod\n\
    \n        for i in range(start,len(self)-len(T)+1):\n            if alpha==self[i:i+len(T)]:\n\
    \                return i\n        raise ValueError(\"substring not found\")\n\
    \n    def index(self,T,start=0):\n        alpha=0\n        for t in T:\n     \
    \       alpha=(alpha*self.base+ord(t))%self.mod\n\n        for i in range(len(self)-len(T),start-1):\n\
    \            if alpha==self[i:i+len(T)]:\n                return i\n        raise\
    \ ValueError(\"substring not found\")\n\n    def __getitem__(self,index):\n  \
    \      if index.__class__==int:\n            if index<0:\n                index+=len(self.string)\n\
    \            assert 0<=index<len(self.string)\n            return self.get(index,index+1)\n\
    \        elif index.__class__==slice:\n            assert (index.step==None) or\
    \ (index.step==1)\n            L=index.start if index.start else 0\n         \
    \   R=index.stop if index.stop else len(self)\n            if L<0:L+=len(self)\n\
    \            if R<0:R+=len(self)\n            return self.get(L,R)\n\n    def\
    \ __len__(self):\n        return len(self.string)\n\n#=================================================\n\
    class Hasher():\n    def __init__(self, length, base, mod):\n        self.length=length\n\
    \        self.base=base\n        self.mod=mod\n\n        self.power=pw=[1]*length\n\
    \        for i in range(1,length):\n            pw[i]=(base*pw[i-1])%mod\n\n \
    \   def __repr__(self):\n        return \"length: {}\\nbase: {}\\nmod: {}\".format(self.length,\
    \ self.base, self.mod)\n\n    def encode(self, S):\n        code=0; N=len(S)\n\
    \        for i in range(N):\n            #code+=ord(S[i])*self.power[N-1-i]%self.mod\n\
    \            code+=S[i]*self.power[N-1-i]%self.mod\n\n        return code%self.mod\n\
    \n    def decode(self, S):\n        pass\n"
  dependsOn: []
  isVerificationFile: false
  path: Rolling_Hash.py
  requiredBy: []
  timestamp: '2022-03-06 04:28:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Rolling_Hash.py
layout: document
redirect_from:
- /library/Rolling_Hash.py
- /library/Rolling_Hash.py.html
title: Rolling_Hash.py
---
