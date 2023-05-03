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
  code: "class Lazy_Evaluation_Proportion_Tree():\n    def __init__(self,L,calc,unit,act,comp,id,prop,index=1):\n\
    \        \"\"\"calc\u3092\u6F14\u7B97,act\u3092\u4F5C\u7528\u3068\u3059\u308B\u30EA\
    \u30B9\u30C8L\u306ESegment Tree\u3092\u4F5C\u6210\n\n        calc:\u6F14\u7B97\
    \n        unit:\u30E2\u30CE\u30A4\u30C9calc\u306E\u5358\u4F4D\u5143 (xe=ex=x\u3092\
    \u6E80\u305F\u3059e)\n        act:\u4F5C\u7528\u7D20\n        comp:\u4F5C\u7528\
    \u7D20\u306E\u5408\u6210\n        id:\u6052\u7B49\u5199\u50CF\n        prop:\u6BD4\
    \u4F8B\u306E\u4ED5\u65B9\n\n        [\u6761\u4EF6] M:Monoid,F={f:F x M\u2192 M:\u4F5C\
    \u7528\u7D20},prop:F x N \u2192F\u306B\u5BFE\u3057\u3066,\u4EE5\u4E0B\u304C\u6210\
    \u7ACB\u3059\u308B.\n        \u30FBF\u306F\u6052\u7B49\u5199\u50CF id \u3092\u542B\
    \u3080.\u3064\u307E\u308A,\u4EFB\u610F\u306E x in M \u306B\u5BFE\u3057\u3066 id(x)=x\n\
    \        \u30FBF\u306F\u5199\u50CF\u306E\u5408\u6210\u306B\u9589\u3058\u3066\u3044\
    \u308B.\u3064\u307E\u308A,\u4EFB\u610F\u306E f,g in F \u306B\u5BFE\u3057\u3066\
    , comp(f,g) in F\n        \u30FB\u4EFB\u610F\u306E f in F, x,y in M \u306B\u5BFE\
    \u3057\u3066,f(x*y)=f(x)*f(y)\u3067\u3042\u308B.\n        \u30FBprop(f,2n)(x,y)=prop(f,n)(x)*prop(f,n)(y)\n\
    \n        [\u6CE8\u8A18]\n        \u4F5C\u7528\u7D20\u306F\u5DE6\u304B\u3089\u639B\
    \u3051\u308B.\u66F4\u65B0\u3082\u5DE6\u304B\u3089.\n        calc(a,b,l,r):a,b:\u8A08\
    \u7B97\u306B\u7528\u3044\u308B\u5024,l,r:a,b\u304C\u683C\u7D0D\u3055\u308C\u3066\
    \u3044\u308BIndex (l\u304Ca,r\u304Cb)\n        prop(a,l,r):l\u304B\u3089r\u307E\
    \u3067\u306E\u30D6\u30ED\u30C3\u30AF\u304Ca\u3067\u3042\u308B\u3068\u304D\u306E\
    \u6BD4\u4F8B\u306E\u4ED5\u65B9.\n        \"\"\"\n        self.calc=calc\n    \
    \    self.unit=unit\n        self.act=act\n        self.comp=comp\n        self.id=id\n\
    \        self.prop=prop\n        self.index=index\n\n        N=len(L)\n      \
    \  d=max(1,(N-1).bit_length())\n        k=1<<d\n\n        self.data=[unit]*k+L+[unit]*(k-len(L))\n\
    \        self.lazy=[self.id]*(2*k)\n        self.N=k\n        self.depth=d\n \
    \       self.len=[0]*(2*k)\n\n        for i in range(k-1,0,-1):\n            self.data[i]=calc(self.data[i<<1],self.data[i<<1|1],i<<1,i<<1|1)\n\
    \n        self.Left=[0]*k+[x for x in range(1,k+1)]\n        self.Right=[0]*k+[x\
    \ for x in range(1,k+1)]\n\n        for i in range(k-1,0,-1):\n            self.Left[i]=self.Left[i<<1]\n\
    \            self.Right[i]=self.Right[i<<1|1]\n\n    def _eval_at(self,m):\n \
    \       if self.lazy[m]==self.id:\n            return self.data[m]\n        return\
    \ self.act(self.prop(self.lazy[m],self.Left[m],self.Right[m]),self.data[m])\n\n\
    \    #\u914D\u5217\u306E\u7B2Cm\u8981\u7D20\u3092\u4E0B\u306B\u4F1D\u642C\n  \
    \  def _propagate_at(self,m):\n        self.data[m]=self._eval_at(m)\n\n     \
    \   if m<self.N and self.lazy[m]!=self.id:\n            self.lazy[m<<1]=self.comp(\n\
    \                self.lazy[m],\n                self.lazy[m<<1]\n            \
    \    )\n\n            self.lazy[m<<1|1]=self.comp(\n                self.lazy[m],\n\
    \                self.lazy[m<<1|1]\n                )\n\n        self.lazy[m]=self.id\n\
    \n    #\u914D\u5217\u306E\u7B2Cm\u8981\u7D20\u3088\u308A\u4E0A\u3092\u5168\u3066\
    \u4F1D\u642C\n    def _propagate_above(self,m):\n        H=m.bit_length()\n  \
    \      for h in range(H-1,0,-1):\n            self._propagate_at(m>>h)\n\n   \
    \ #\u914D\u5217\u306E\u7B2Cm\u8981\u7D20\u3088\u308A\u4E0A\u3092\u5168\u3066\u518D\
    \u8A08\u7B97\n    def _recalc_above(self,m):\n        l=1<<(self.depth+1-m.bit_length())\n\
    \        while m>1:\n            m>>=1\n            l<<=1\n\n            self.data[m]=self.calc(\n\
    \                self._eval_at(m<<1),\n                self._eval_at(m<<1|1)\n\
    \            )\n\n    def get(self,k):\n        m=k-self.index+self.N\n      \
    \  self._propagate_above(m)\n\n        self.data[m]=self._eval_at(m)\n\n     \
    \   self.lazy[m]=self.id\n        return self.data[m]\n\n    #\u4F5C\u7528\n \
    \   def action(self,From,To,alpha,left_closed=True,right_closed=True):\n     \
    \   L=(From-self.index)+self.N+(not left_closed)\n        R=(To-self.index)+self.N+(right_closed)\n\
    \n        L0=R0=-1\n        X,Y=L,R-1\n        while X<Y:\n            if X&1:\n\
    \                L0=max(L0,X)\n                X+=1\n\n            if Y&1==0:\n\
    \                R0=max(R0,Y)\n                Y-=1\n\n            X>>=1\n   \
    \         Y>>=1\n\n        L0=max(L0,X)\n        R0=max(R0,Y)\n\n        self._propagate_above(L0)\n\
    \        self._propagate_above(R0)\n\n        while L<R:\n            if L&1:\n\
    \                self.lazy[L]=self.comp(alpha,self.lazy[L])\n                L+=1\n\
    \n            if R&1:\n                R-=1\n                self.lazy[R]=self.comp(alpha,self.lazy[R])\n\
    \n            L>>=1\n            R>>=1\n\n        self._recalc_above(L0)\n   \
    \     self._recalc_above(R0)\n\n    def update(self,k,x):\n        \"\"\" \u7B2C\
    k\u8981\u7D20\u3092x\u306B\u5909\u66F4\u3059\u308B.\n\n        \"\"\"\n      \
    \  m=k-self.index+self.N\n        self._propagate_above(m)\n        self.data[m]=x\n\
    \        self.lazy[m]=self.id\n        self._recalc_above(m)\n\n    def product(self,From,To,left_closed=True,right_closed=True):\n\
    \        L=(From-self.index)+self.N+(not left_closed)\n        R=(To-self.index)+self.N+(right_closed)\n\
    \n        L0=R0=-1\n        X,Y=L,R-1\n        while X<Y:\n            if X&1:\n\
    \                L0=max(L0,X)\n                X+=1\n\n            if Y&1==0:\n\
    \                R0=max(R0,Y)\n                Y-=1\n\n            X>>=1\n   \
    \         Y>>=1\n\n        L0=max(L0,X)\n        R0=max(R0,Y)\n\n        self._propagate_above(L0)\n\
    \        self._propagate_above(R0)\n\n        vL=vR=self.unit\n\n        while\
    \ L<R:\n            if L&1:\n                #vL=self.calc(vL,self._eval_at(L))\n\
    \                L+=1\n\n            if R&1:\n                R-=1\n         \
    \       #vR=self.calc(self._eval_at(R),vR)\n\n            L>>=1\n            R>>=1\n\
    \n            print(L,R)\n\n        return self.calc(vL,vR)\n\n    def all_product(self):\n\
    \        return self.product(self.index,self.N+(self.index-1))\n\n    #\u30EA\u30D5\
    \u30EC\u30C3\u30B7\u30E5\n    def refresh(self):\n        for m in range(1,2*self.N):\n\
    \            self.data[m]=self._eval_at(m)\n\n            if m<self.N and self.lazy[m]!=self.id:\n\
    \                self.lazy[m<<1]=self.comp(\n                    self.lazy[m],\n\
    \                    self.lazy[m<<1]\n                    )\n\n              \
    \  self.lazy[m<<1|1]=self.comp(\n                    self.lazy[m],\n         \
    \           self.lazy[m<<1|1]\n                    )\n\n            self.lazy[m]=self.id\n"
  dependsOn: []
  isVerificationFile: false
  path: Segment_Tree/Lazy_Evaluation_Proportion_Tree.py
  requiredBy: []
  timestamp: '2023-03-20 03:47:37+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Segment_Tree/Lazy_Evaluation_Proportion_Tree.py
layout: document
redirect_from:
- /library/Segment_Tree/Lazy_Evaluation_Proportion_Tree.py
- /library/Segment_Tree/Lazy_Evaluation_Proportion_Tree.py.html
title: Segment_Tree/Lazy_Evaluation_Proportion_Tree.py
---
