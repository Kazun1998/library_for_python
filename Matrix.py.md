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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from copy import copy,deepcopy\n\nclass Matrix_Error(Exception):\n    pass\n\
    \nclass Matrix():\n    #\u5165\u529B\n    def __init__(self,M=[]):\n        self.ele=M\n\
    \        R=len(M)\n        if R!=0:\n            C=len(M[0])\n        else:\n\
    \            C=0\n        self.row=R\n        self.col=C\n        self.size=(R,C)\n\
    \n    #\u51FA\u529B\n    def __str__(self):\n        T=\"\"\n        (r,c)=self.size\n\
    \        for i in range(r):\n            U=\"[\"\n            for j in range(c):\n\
    \                U+=str(self.ele[i][j])+\" \"\n            T+=U[:-1]+\"]\\n\"\n\
    \n        return \"[\"+T[:-1]+\"]\"\n    #+,-\n    def __pos__(self):\n      \
    \  return self\n\n    def __neg__(self):\n        return self.__scale__(-1)\n\n\
    \    #\u52A0\u6CD5\n    def __add__(self,other):\n        A=self\n        B=other\n\
    \        if A.size!=B.size:\n            raise Matrix_Error(\"2\u3064\u306E\u884C\
    \u5217\u306E\u30B5\u30A4\u30BA\u304C\u7570\u306A\u308A\u307E\u3059.({},{})\".format(A.size,B.size))\n\
    \        M=A.ele\n        N=B.ele\n\n        L=[]\n        for i in range(A.row):\n\
    \            E=[]\n            for j in range(A.col):\n                E.append(M[i][j]+N[i][j])\n\
    \n            L.append(E)\n        return Matrix(L)\n\n    #\u6E1B\u6CD5\n   \
    \ def __sub__(self,other):\n        return self+(-other)\n\n    #\u4E57\u6CD5\n\
    \    def __mul__(self,other):\n        A=self\n        B=other\n        if isinstance(B,Matrix):\n\
    \            R=A.row\n            C=B.col\n\n            if A.col!=B.row:\n  \
    \              raise Matrix_Error(\"\u5DE6\u5074\u306E\u5217\u3068\u53F3\u5074\
    \u306E\u884C\u304C\u4E00\u81F4\u3057\u307E\u305B\u3093.({},{})\".format(A.size,B.size))\n\
    \            G=A.col\n\n            M=A.ele\n            N=B.ele\n\n         \
    \   E=[]\n            for i in range(R):\n                F=[]\n             \
    \   for j in range(C):\n                    S=0\n                    for k in\
    \ range(G):\n                        S+=M[i][k]*N[k][j]\n                    F.append(S)\n\
    \                E.append(F)\n\n            return Matrix(E)\n\n        elif isinstance(B,int):\n\
    \            return A.__scale__(B)\n\n    def __rmul__(self,other):\n        if\
    \ isinstance(other,int):\n            return self*other\n\n    def Inverse(self):\n\
    \        from copy import copy\n        M=self\n        if M.row!=M.col:\n   \
    \         raise Matrix_Error(\"\u6B63\u65B9\u884C\u5217\u3067\u306F\u3042\u308A\
    \u307E\u305B\u3093.\")\n\n        R=M.row\n        I=[[1*(i==j) for j in range(R)]\
    \ for i in range(R)]\n        G=M.Column_Union(Matrix(I))\n        G=G.Row_Reduce()\n\
    \n        A,B=[],[]\n        for i in range(R):\n            A.append(copy(G.ele[i][:R]))\n\
    \            B.append(copy(G.ele[i][R:]))\n\n        if A==I:\n            return\
    \ Matrix(B)\n        else:\n            raise Matrix_Error(\"\u6B63\u5247\u3067\
    \u306F\u3042\u308A\u307E\u305B\u3093.\")\n\n    #\u30B9\u30AB\u30E9\u30FC\u500D\
    \n    def __scale__(self,r):\n        M=self.ele\n        L=[[r*M[i][j] for j\
    \ in range(self.col)] for i in range(self.row)]\n        return Matrix(L)\n\n\
    \    #\u7D2F\u4E57\n    def __pow__(self,n):\n        A=self\n        if A.row!=A.col:\n\
    \            raise Matrix_Error(\"\u6B63\u65B9\u884C\u5217\u3067\u306F\u3042\u308A\
    \u307E\u305B\u3093.\")\n\n        if n<0:\n            return (A**(-n)).Inverse()\n\
    \n        R=Matrix([[1*(i==j) for j in range(A.row)] for i in range(A.row)])\n\
    \        D=A\n\n        while n>0:\n            if n%2==1:\n                R*=D\n\
    \            D*=D\n            n=n>>1\n\n        return R\n\n    #\u7B49\u53F7\
    \n    def __eq__(self,other):\n        A=self\n        B=other\n        if A.size!=B.size:\n\
    \            return False\n\n        for i in range(A.row):\n            for j\
    \ in range(A.col):\n                if A.ele[i][j]!=B.ele[i][j]:\n           \
    \         return False\n\n        return True\n\n    #\u4E0D\u7B49\u53F7\n   \
    \ def __neq__(self,other):\n        return not(self==other)\n\n    #\u8EE2\u7F6E\
    \n    def Transpose(self):\n        self.col,self.row=self.row,self.col\n    \
    \    self.ele=list(map(list,zip(*self.ele)))\n\n    #\u884C\u57FA\u672C\u5909\u5F62\
    \n    def Row_Reduce(self):\n        M=self\n        (R,C)=M.size\n        T=[]\n\
    \n        for i in range(R):\n            U=[]\n            for j in range(C):\n\
    \                U.append(M.ele[i][j])\n            T.append(U)\n\n        I=0\n\
    \        for J in range(C):\n            if T[I][J]==0:\n                for i\
    \ in range(I+1,R):\n                    if T[i][J]!=0:\n                     \
    \   T[i],T[I]=T[I],T[i]\n                        break\n\n            if T[I][J]!=0:\n\
    \                u=T[I][J]\n                for j in range(C):\n             \
    \       T[I][j]/=u\n\n                for i in range(R):\n                   \
    \ if i!=I:\n                        v=T[i][J]\n                        for j in\
    \ range(C):\n                            T[i][j]-=v*T[I][j]\n                I+=1\n\
    \                if I==R:\n                    break\n\n        return Matrix(T)\n\
    \n    #\u5217\u57FA\u672C\u5909\u5F62\n    def Column_Reduce(self):\n        M=self\n\
    \        (R,C)=M.size\n\n        T=[]\n        for i in range(R):\n          \
    \  U=[]\n            for j in range(C):\n                U.append(M.ele[i][j])\n\
    \            T.append(U)\n\n        J=0\n        for I in range(R):\n        \
    \    if T[I][J]==0:\n                for j in range(J+1,C):\n                \
    \    if T[I][j]!=0:\n                        for k in range(R):\n            \
    \                T[k][j],T[k][J]=T[k][J],T[k][j]\n                        break\n\
    \n            if T[I][J]!=0:\n                u=T[I][J]\n                for i\
    \ in range(R):\n                    T[i][J]/=u\n\n                for j in range(C):\n\
    \                    if j!=J:\n                        v=T[I][j]\n           \
    \             for i in range(R):\n                            T[i][j]-=v*T[i][J]\n\
    \                J+=1\n                if J==C:\n                    break\n\n\
    \        return Matrix(T)\n\n    #\u884C\u5217\u306E\u968E\u6570\n    def Rank(self,ep=None):\n\
    \        M=self.Row_Reduce()\n        (R,C)=M.size\n        T=M.ele\n\n      \
    \  S=0\n        for i in range(R):\n            f=False\n            if ep==None:\n\
    \                for j in range(C):\n                    if T[i][j]!=0:\n    \
    \                    f=True\n            else:\n                for j in range(C):\n\
    \                    if abs(T[i][j])>=ep:\n                        f=True\n\n\
    \            if f:\n                S+=1\n            else:\n                break\n\
    \n        return S\n\n    #\u884C\u306E\u7D50\u5408\n    def Row_Union(self,other):\n\
    \        return Matrix(self.ele+other.ele)\n\n    #\u5217\u306E\u7D50\u5408\n\
    \    def Column_Union(self,other):\n        E=[]\n        for i in range(self.row):\n\
    \            E.append(self.ele[i]+other.ele[i])\n\n        return Matrix(E)\n\
    #------------------------------------------------------------\n#\u5358\u4F4D\u884C\
    \u5217\ndef Identity_Matrix(n):\n    return Matrix([[1*(i==j) for j in range(n)]\
    \ for i in range(n)])\n\n#\u96F6\u884C\u5217\ndef Zero_Matrix(r,c=None):\n   \
    \ if c==None:\n        c=r\n    return Matrix([[0]*c for i in range(r)])\n\n#\u6B63\
    \u65B9\u884C\u5217?\ndef Is_Square(M):\n    return M.row==M.col\n\n#\u5BFE\u89D2\
    \u884C\u5217\ndef Diagonal_Matrix(*A):\n    N=len(A)\n    return Matrix([[A[i]*(i==j)\
    \ for j in range(N)] for i in range(N)])\n\n#\u8DE1\ndef Trace(M):\n    if not\
    \ Is_Square(M):\n        raise Matrix_Error(\"\u6B63\u65B9\u884C\u5217\u3067\u306F\
    \u3042\u308A\u307E\u305B\u3093\")\n\n    T=0\n    for i in range(M.col):\n   \
    \     T+=M.ele[i][i]\n\n    return T\n\n#\u884C\u5217\u5F0F\ndef Det(M):\n   \
    \ if not Is_Square(M):\n        raise Matrix_Error(\"\u6B63\u65B9\u884C\u5217\u3067\
    \u306F\u3042\u308A\u307E\u305B\u3093\")\n\n    R=M.row\n    T=deepcopy(M.ele)\n\
    \n    I=0\n    D=1\n    for J in range(R):\n        if T[I][J]==0:\n         \
    \   for i in range(I+1,R):\n                if T[i][J]!=0:\n                 \
    \   T[i],T[I]=T[I],T[i]\n                    D*=-1\n                    break\n\
    \n        if T[I][J]!=0:\n            u=T[I][J]\n            for j in range(R):\n\
    \                T[I][j]/=u\n            D*=u\n\n            for i in range(I+1,R):\n\
    \                v=T[i][J]\n                for j in range(R):\n             \
    \       T[i][j]-=v*T[I][j]\n            I+=1\n            if I==R:\n         \
    \       break\n\n    for i in range(R):\n        D*=T[i][i]\n\n    return D\n\n\
    #\u8981\u7D20\u6BCE\u306B1\u5909\u6570\u95A2\u6570\u3092\u901A\u3059.\ndef Element_Map(M,f):\n\
    \    T=deepcopy(M.ele)\n\n    for i in range(M.row):\n        for j in range(M.col):\n\
    \            T[i][j]=f(T[i][j])\n\n    return Matrix(T)\n"
  dependsOn: []
  isVerificationFile: false
  path: Matrix.py
  requiredBy: []
  timestamp: '2021-04-27 14:48:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Matrix.py
layout: document
redirect_from:
- /library/Matrix.py
- /library/Matrix.py.html
title: Matrix.py
---
