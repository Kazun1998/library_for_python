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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\" Bitset \u8AAC\u660E\u66F8\n\u4E8B\u524D\u306B N (Biset \u306E\u30B5\
    \u30A4\u30BA) \u3068 __bit_size (\u5404\u30D6\u30ED\u30C3\u30AF\u3054\u3068\u306B\
    \u53CE\u3081\u308B\u30B5\u30A4\u30BA) \u3092\u6C7A\u3081\u306A\u304F\u3066\u306F\
    \u3044\u3051\u306A\u3044.\n\n[\u304A\u3059\u3059\u3081]\nN=10^5, __bit_size=N//k\
    \ (4<=k<=10)\nN=3000, __bit_size=63?\n\n\u203B count, len \u3092\u4F7F\u3044\u305F\
    \u3044\u5834\u5408\u306F __bit_size=63 \u3067\u306A\u3044\u3068\u4F7F\u3048\u306A\
    \u3044!!!\n\"\"\"\n\nclass Bitset:\n    # \u203B \u4E8B\u524D\u306B\u8A2D\u5B9A\
    \u3057\u3066\u304A\u304F\u3053\u3068!!!\n    N=100\n    __bit_size=63*1\n    #\
    \ \u3053\u3053\u307E\u3067\n\n    @staticmethod\n    def __popcount(n):\n    \
    \    n -= ((n >> 1) & 0x5555555555555555)\n        n = (n & 0x3333333333333333)\
    \ + ((n >> 2) & 0x3333333333333333)\n        n = (n + (n >> 4)) & 0x0f0f0f0f0f0f0f0f\n\
    \        n += ((n >> 8) & 0x00ff00ff00ff00ff)\n        n += ((n >> 16) & 0x0000ffff0000ffff)\n\
    \        n += ((n >> 32) & 0x00000000ffffffff)\n        return n & 0x7f\n\n  \
    \  __block=(N+__bit_size-1)//__bit_size\n\n    __msk_b=(1<<__bit_size)-1\n   \
    \ __msk_s=(1<<(N%__bit_size))-1\n\n    __on=[1<<i for i in range(__bit_size)]\n\
    \    __off=[0]*__bit_size\n    for k in range(__bit_size):\n        __off[k]=((1<<__bit_size)-1)\
    \ ^ (1<<k)\n    del k\n\n    def __init__(self):\n        self.__bit=[0]*Bitset.__block\n\
    \n    def __len__(self):\n        assert Bitset.__bit_size<=63\n        x=0\n\
    \        for bit in self.__bit:\n            x+=Bitset.__popcount(bit)\n     \
    \   return x\n\n    def __bool__(self):\n        return self.any()\n\n    def\
    \ __str__(self):\n        return \" \".join(map(str, [i for i in range(self.N)\
    \ if i in self]))\n\n    def __repr__(self):\n        return \"[Bitset] : \"+(str(self)\
    \ if self else \"empty\")\n\n    def __contains__(self, index):\n        k,i=divmod(index,\
    \ Bitset.__bit_size)\n        return bool((self.__bit[k]>>i)&1)\n\n    __getitem__=__contains__\n\
    \n    def __setitem__(self, index, value):\n        self.set(index, value)\n\n\
    \    def set(self, index=-1, value=1):\n        if index==-1:\n            if\
    \ value:\n                self.__bit[-1]=Bitset.__msk_s\n                for k\
    \ in range(Bitset.__block-1):\n                    self.__bit[k]=Bitset.__msk_b\n\
    \            else:\n                for k in range(Bitset.__block):\n        \
    \            self.__bit[k]=0\n        else:\n            k,i=divmod(index, Bitset.__bit_size)\n\
    \            if value:\n                self.__bit[k]|=Bitset.__on[i]\n      \
    \      else:\n                self.__bit[k]&=Bitset.__off[i]\n\n    def reset(self,\
    \ index=-1):\n        self.set(index, value=0)\n\n    def flip(self, index=-1):\n\
    \        if index==-1:\n            for k in range(Bitset.__block-1):\n      \
    \          self.__bit[k]=self.__bit[k]^Bitset.__msk_b\n            if self.N%Bitset.__bit_size:\n\
    \                self.__bit[-1]=self.__bit[-1]^Bitset.__msk_s\n            else:\n\
    \                self.__bit[-1]=self.__bit[-1]^Bitset.__msk_b\n        else:\n\
    \            k,i=divmod(index, Bitset.__bit_size)\n            self.__bit[k]^=Bitset.__on[i]\n\
    \n    test=__contains__\n\n    def any(self):\n        for bit in self.__bit:\n\
    \            if bit:\n                return True\n        return False\n\n  \
    \  def all(self):\n        for k in range(Bitset.__block-1):\n            if self.__bit[k]!=Bitset.__msk_b:\n\
    \                return False\n        if self.N%Bitset.__bit_size:\n        \
    \    return self.__bit[-1]==Bitset.__msk_s\n        else:\n            return\
    \ self.__bit[-1]==Bitset.__msk_b\n\n    def __iand__(self, other):\n        for\
    \ k in range(Bitset.__block):\n            self.__bit[k]&=other.__bit[k]\n   \
    \     return self\n\n    def __and__(self, other):\n        X=self.copy()\n  \
    \      X&=other\n        return X\n\n    def __ior__(self, other):\n        for\
    \ k in range(Bitset.__block):\n            self.__bit[k]|=other.__bit[k]\n   \
    \     return self\n\n    def __or__(self, other):\n        X=self.copy()\n   \
    \     X|=other\n        return X\n\n    def __ixor__(self, other):\n        for\
    \ k in range(Bitset.__block):\n            self.__bit[k]^=other.__bit[k]\n   \
    \     return self\n\n    def __xor__(self, other):\n        X=self.copy()\n  \
    \      X^=other\n        return X\n\n    def __eq__(self, other):\n        for\
    \ k in range(Bitset.__block):\n            if self.__bit[k]!=other.__bit[k]:\n\
    \                return False\n        return True\n\n    def __neq__(self, other):\n\
    \        return not(self==other)\n\n    def copy(self):\n        X=Bitset()\n\
    \        X.__bit=self.__bit.copy()\n        return X\n\n    count=__len__\n"
  dependsOn: []
  isVerificationFile: false
  path: Bitset.py
  requiredBy: []
  timestamp: '2022-12-24 16:45:16+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Bitset.py
layout: document
redirect_from:
- /library/Bitset.py
- /library/Bitset.py.html
title: Bitset.py
---
