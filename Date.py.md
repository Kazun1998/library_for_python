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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Date():\n    Month_End=[0,31,28,31,30,31,30,31,31,30,31,30,31]\n  \
    \  def __init__(self,Y,M,D):\n        self.Y=Y\n        self.M=M\n        self.D=D\n\
    \n    def __str__(self):\n        y=str(self.Y)\n        m=str(self.M)\n     \
    \   d=str(self.D)\n        return \"{} / {} / {}\".format(y,m.zfill(2),d.zfill(2))\n\
    \n    def __iter__(self):\n        yield from [self.Y, self.M, self.D]\n\n   \
    \ def __repr__(self):\n        return self.__str__()\n\n    def __eq__(self,other):\n\
    \        return (self.Y==other.Y) and (self.M==other.M) and (self.D==other.D)\n\
    \n    def __neq__(self,other):\n        return not(self==other)\n\n    def __le__(self,other):\n\
    \        if self.Y!=other.Y:\n            return self.Y<other.Y\n        elif\
    \ self.M!=other.M:\n            return self.M<other.M\n        else:\n       \
    \     return self.D<=other.D\n\n    def __lt__(self,other):\n        return self<=other\
    \ and self!=other\n\n    def __ge__(self,other):\n        return other<=self\n\
    \n    def __gt__(self,other):\n        return other<self\n\n    def is_leap_year(self):\n\
    \        Y=self.Y\n        if Y%4:\n            return False\n        elif Y%100:\n\
    \            return True\n        elif Y%400:\n            return False\n    \
    \    else:\n            return True\n\n    def next_day(self, day=1):\n      \
    \  Y,M,D=self.Y,self.M,self.D\n\n        x=400*365+97\n        if day>=x:\n  \
    \          t,day=divmod(day,x)\n            Y+=400*t\n\n        def leap(Y):\n\
    \            if Y%4:\n                return False\n            elif Y%100:\n\
    \                return True\n            else:\n                return (Y%400)==0\n\
    \n        T=leap(Y)\n        for _ in range(day):\n            D+=1\n        \
    \    if (M!=2) and (self.Month_End[M]<D):\n                D=1\n             \
    \   M=M%12+1\n                Y+=1 if M==1 else 0\n\n                if M==1:\n\
    \                    T=leap(Y)\n\n            elif (M==2) and (not T) and D>28:\n\
    \                M,D=3,1\n            elif (M==2) and T and D>29:\n          \
    \      M,D=3,1\n        return Date(Y,M,D)\n\n    def day_of_week(self):\n   \
    \     \"\"\"\u66DC\u65E5\u3092\u6C42\u3081\u308B.\n\n        \u203B\u7D00\u5143\
    \u5F8C4\u5E74~\u7D00\u5143\u5F8C1582\u5E74\u306F\u30E6\u30EA\u30A6\u30B9\u6B74\
    \u3067\u306E\u8A08\u7B97\n        \"\"\"\n        Y,M,D=self.Y,self.M,self.D\n\
    \n        if M<=2:\n            Y-=1\n            M+=12\n\n        C=Y//100\n\
    \        if 1582<=Y:\n            G=5*C+(C//4)\n        else:\n            G=6*C+5\n\
    \n        Y%=100\n\n        a=D+(26*(M+1))//10+Y+(Y//4)+G\n        h=a%7\n   \
    \     return [\"Saturday\",\"Sunday\",\"Monday\",\"Tuesday\",\"Wednesday\",\"\
    Thursday\",\"Friday\"][h]\n\ndef Today():\n    import datetime\n    X=datetime.datetime.now()\n\
    \    Y,M,D=X.year,X.month,X.day\n    return Date(Y,M,D)\n"
  dependsOn: []
  isVerificationFile: false
  path: Date.py
  requiredBy: []
  timestamp: '2023-01-01 16:03:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Date.py
layout: document
redirect_from:
- /library/Date.py
- /library/Date.py.html
title: Date.py
---
