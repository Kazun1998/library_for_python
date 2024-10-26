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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Integer_Range:\n    def __init__(self,L,R):\n        self.L=L\n   \
    \     self.R=R\n        self.valid=1 if L<=R else 0\n\n    def __str__(self):\n\
    \        if self:\n            return \"[{}, {}]\".format(self.L,self.R)\n   \
    \     else:\n            return \"O\"\n\n    def __repr__(self):\n        return\
    \ str(self)\n\n    def __bool__(self):\n        return bool(self.valid)\n\n  \
    \  def __contains__(self,x):\n        return self.valid and self.L<=x<=self.R\n\
    \n    def __and__(self,other):\n        if self and other:\n            return\
    \ Integer_Range(max(self.L,other.L),min(self.R,other.R))\n        else:\n    \
    \        return Integer_Range(0,-1)\n\n    def __iter__(self):\n        yield\
    \ from range(self.L,self.R+1)\n\n    #\u4E0D\u7B49\u53F7\n    def __eq__(self,other):\n\
    \        if bool(self)^bool(other):\n            return False\n\n        if self:\n\
    \            return (self.L==other.L) and (self.R==other.R)\n        else:\n \
    \           return True\n\n    def __ne__(self,other):\n        return not(self==other)\n\
    \n    def __le__(self,other):\n        if not self:\n            return True\n\
    \        if self==other:\n            return True\n        return (other.L<=self.L)\
    \ and (self.R<=other.R)\n\n    def __lt__(self,other):\n        return self<=other\
    \ and self!=other\n\n    def __ge__(self,other):\n        return other<=self\n\
    \n    def __gt__(self,other):\n        return other<self\n\n    def Is_disjoint(self,other):\n\
    \        \"\"\"\u4E92\u3044\u306B\u7D20\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\
    \u3059\u308B.\n        \"\"\"\n        if (not self) or (not other):\n       \
    \     return True\n        return max(self.L,other.L)>min(self.R,other.R)\n\n\
    \    def Cardinality(self):\n        \"\"\"\u6FC3\u5EA6\u3092\u6C42\u3081\u308B\
    .\n\n        \"\"\"\n        return max(self.R-self.L+1,0)\n\nclass Integer_Interval(Integer_Range):\n\
    \    def __init__(self,*I):\n        X=[x for x in I if x]\n        X.sort(key=lambda\
    \ x:x.L)\n\n        self.I=[]\n        if not X:return\n\n        N=len(X)\n \
    \       l,r=X[0].L,X[0].R\n        for k in range(1,N):\n            s,t=X[k].L,X[k].R\n\
    \            if r+1<s:\n                self.I.append(Integer_Range(l,r))\n  \
    \              l=s\n            r=max(r,t)\n        self.I.append(Integer_Range(l,r))\n\
    \n    def __str__(self):\n        if self:\n            return \" | \".join(map(str,self.I))\n\
    \        else:\n            return \"O\"\n\n    def __repr__(self):\n        return\
    \ str(self)\n\n    def __bool__(self):\n        return bool(self.I)\n\n    def\
    \ __and__(self,other):\n        A=[]\n        for x in self.I:\n            for\
    \ y in other.I:\n                A.append(x&y)\n        return Integer_Interval(*A)\n\
    \n    def __or__(self,other):\n        return Integer_Interval(*(self.I+other.I))\n\
    \n    def __iter__(self):\n        for I in self.I:\n            yield from I\n\
    \n    def __eq__(self,other):\n        if len(self.I)!=len(other.I):\n       \
    \     return False\n\n        A=self.I\n        B=other.I\n        for k in range(len(self.I)):\n\
    \            if A!=B:\n                return False\n        return True\n\n \
    \   def __neq__(self,other):\n        return not(self==other)\n\n    def __contains__(self,x):\n\
    \        for I in self.I:\n            if x in I:\n                return True\n\
    \        return  False\n\n    def Is_disjoint(self,other):\n        \"\"\"\u4E92\
    \u3044\u306B\u7D20\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n  \
    \      \"\"\"\n        for I in self.I:\n            for J in other.I:\n     \
    \           if not I.Is_disjoint(J):\n                    return False\n     \
    \   return True\n\n    def Cardinality(self):\n        \"\"\"\u6FC3\u5EA6\u3092\
    \u6C42\u3081\u308B.\n\n        \"\"\"\n        X=0\n        for I in self.I:\n\
    \            X+=I.Cardinality()\n        return X\n\n    def Slide(self,a):\n\
    \        \"\"\"a\u3060\u3051\u305A\u3089\u3059.\n        \"\"\"\n\n        for\
    \ I in self.I:\n            I.L+=a\n            I.R+=a\n\n    def Scale(self,a):\n\
    \        \"\"\"a\u500D\u3059\u308B.\n        \"\"\"\n\n        if not self:\n\
    \            return\n\n        X=[]\n        if a>=0:\n            for I in self.I:\n\
    \                X.append(Integer_Range(a*I.L,a*I.R))\n        else:\n       \
    \     for I in self.I:\n                X.append(Integer_Range(a*I.R,a*I.L))\n\
    \        return Integer_Interval(*X)\n\ndef Addition(I,J):\n    X=[]\n    for\
    \ i in I.I:\n        for j in J.I:\n            X.append(Integer_Range(i.L+j.L,i.R+j.R))\n\
    \    return  Integer_Interval(*X)\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer_Interval.py
  requiredBy: []
  timestamp: '2021-04-27 14:48:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer_Interval.py
layout: document
redirect_from:
- /library/Integer_Interval.py
- /library/Integer_Interval.py.html
title: Integer_Interval.py
---
