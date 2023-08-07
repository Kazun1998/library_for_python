---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Matrix/Determinant.test.py
    title: test_verify/yosupo_library_checker/Matrix/Determinant.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Matrix/Inverse.test.py
    title: test_verify/yosupo_library_checker/Matrix/Inverse.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Matrix/Product.test.py
    title: test_verify/yosupo_library_checker/Matrix/Product.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from copy import deepcopy\n\nclass Modulo_Matrix():\n    __slots__=(\"ele\"\
    ,\"row\",\"col\",\"size\")\n\n    #\u5165\u529B\n    def __init__(self,M):\n \
    \       \"\"\" \u884C\u5217 M \u306E\u5B9A\u7FA9\n\n        M: \u884C\u5217\n\
    \        \u203B Mod: \u6CD5\u306F\u30B0\u30ED\u30FC\u30D0\u30EB\u5909\u6570\u304B\
    \u3089\u6307\u5B9A\n        \"\"\"\n\n        self.ele=[[x%Mod for x in X] for\
    \ X in M]\n        R=len(M)\n        if R!=0:\n            C=len(M[0])\n     \
    \   else:\n            C=0\n        self.row=R\n        self.col=C\n        self.size=(R,C)\n\
    \n    #\u51FA\u529B\n    def __str__(self):\n        return \"[\"+\"\\n\".join(map(str,self.ele))+\"\
    ]\"\n\n    def __repr__(self):\n        return str(self)\n\n    #+,-\n    def\
    \ __pos__(self):\n        return self\n\n    def __neg__(self):\n        return\
    \ self.__scale__(-1)\n\n    #\u52A0\u6CD5\n    def __add__(self,other):\n    \
    \    M=self.ele; N=other.ele\n\n        L=[[0]*self.col for _ in range(self.row)]\n\
    \        for i in range(self.row):\n            Li,Mi,Ni=L[i],M[i],N[i]\n    \
    \        for j in range(self.col):\n                Li[j]=Mi[j]+Ni[j]\n      \
    \  return Modulo_Matrix(L)\n\n    def __iadd__(self,other):\n        M=self.ele;\
    \ N=other.ele\n\n        for i in range(self.row):\n            Mi,Ni=M[i],N[i]\n\
    \            for j in range(self.col):\n                Mi[j]+=Ni[j]\n       \
    \         Mi[j]%=Mod\n        return self\n\n    #\u6E1B\u6CD5\n    def __sub__(self,other):\n\
    \        M=self.ele; N=other.ele\n\n        L=[[0]*self.col for _ in range(self.row)]\n\
    \        for i in range(self.row):\n            Li,Mi,Ni=L[i],M[i],N[i]\n    \
    \        for j in range(self.col):\n                Li[j]=Mi[j]-Ni[j]\n      \
    \  return Modulo_Matrix(L)\n\n    def __isub__(self,other):\n        M=self.ele;\
    \ N=other.ele\n\n        for i in range(self.row):\n            Mi,Ni=M[i],N[i]\n\
    \            for j in range(self.col):\n                Mi[j]-=Ni[j]\n       \
    \         Mi[j]%=Mod\n        return self\n\n    #\u4E57\u6CD5\n    def __mul__(self,other):\n\
    \        if isinstance(other,Modulo_Matrix):\n            assert self.col==other.row,\
    \ \"\u5DE6\u5074\u306E\u5217\u3068\u53F3\u5074\u306E\u884C\u304C\u4E00\u81F4\u3057\
    \u307E\u305B\u3093.({},{})\".format(self.size,other.size)\n\n            M=self.ele;\
    \ N=other.ele\n            E=[[0]*other.col for _ in range(self.row)]\n\n    \
    \        for i in range(self.row):\n                Ei,Mi=E[i],M[i]\n        \
    \        for k in range(self.col):\n                    m_ik,Nk=Mi[k],N[k]\n \
    \                   for j in range(other.col):\n                        Ei[j]+=m_ik*Nk[j]\n\
    \                        Ei[j]%=Mod\n            return Modulo_Matrix(E)\n   \
    \     elif isinstance(other,int):\n            return self.__scale__(other)\n\n\
    \    def __rmul__(self,other):\n        if isinstance(other,int):\n          \
    \  return self.__scale__(other)\n\n    def inverse(self):\n        assert self.row==self.col,\"\
    \u6B63\u65B9\u884C\u5217\u3067\u306F\u3042\u308A\u307E\u305B\u3093.\"\n\n    \
    \    M=self\n        N=M.row\n        R=[[1 if i==j else 0 for j in range(N)]\
    \ for i in range(N)]\n        T=deepcopy(M.ele)\n\n        for j in range(N):\n\
    \            if T[j][j]==0:\n                for i in range(j+1,N):\n        \
    \            if T[i][j]:\n                        break\n                else:\n\
    \                    assert 0, \"\u6B63\u5247\u884C\u5217\u3067\u306F\u3042\u308A\
    \u307E\u305B\u3093\"\n\n                T[j],T[i]=T[i],T[j]\n                R[j],R[i]=R[i],R[j]\n\
    \            Tj,Rj=T[j],R[j]\n            inv=pow(Tj[j], -1, Mod)\n          \
    \  for k in range(N):\n                Tj[k]*=inv; Tj[k]%=Mod\n              \
    \  Rj[k]*=inv; Rj[k]%=Mod\n            for i in range(N):\n                if\
    \ i==j: continue\n                c=T[i][j]\n                Ti,Ri=T[i],R[i]\n\
    \                for k in range(N):\n                    Ti[k]-=Tj[k]*c; Ti[k]%=Mod\n\
    \                    Ri[k]-=Rj[k]*c; Ri[k]%=Mod\n        return Modulo_Matrix(R)\n\
    \n    #\u30B9\u30AB\u30E9\u30FC\u500D\n    def __scale__(self,r):\n        M=self.ele\n\
    \        r%=Mod\n        L=[[(r*M[i][j])%Mod for j in range(self.col)] for i in\
    \ range(self.row)]\n        return Modulo_Matrix(L)\n\n    #\u7D2F\u4E57\n   \
    \ def __pow__(self,n):\n        assert self.row==self.col, \"\u6B63\u65B9\u884C\
    \u5217\u3067\u306F\u3042\u308A\u307E\u305B\u3093.\"\n\n        r=self.col\n\n\
    \        def __mat_mul(A,B):\n            E=[[0]*r for _ in range(r)]\n      \
    \      for i in range(r):\n                a=A[i]; e=E[i]\n                for\
    \ k in range(r):\n                    b=B[k]\n                    for j in range(r):\n\
    \                        e[j]+=a[k]*b[j]\n                        e[j]%=Mod\n\
    \            return E\n\n        X=deepcopy(self.ele)\n        E=[[1 if i==j else\
    \ 0 for j in range(r)] for i in range(r)]\n\n        sgn=1 if n>=0 else -1\n \
    \       n=abs(n)\n\n        while True:\n            if n&1:\n               \
    \ E=__mat_mul(E,X)\n            n>>=1\n            if n:\n                X=__mat_mul(X,X)\n\
    \            else:\n                break\n\n        if sgn==1:\n            return\
    \ Modulo_Matrix(E)\n        else:\n            return Modulo_Matrix(E).inverse()\n\
    \n    #\u7B49\u53F7\n    def __eq__(self,other):\n        return self.ele==other.ele\n\
    \n    #\u4E0D\u7B49\u53F7\n    def __neq__(self,other):\n        return not(self==other)\n\
    \n    #\u8EE2\u7F6E\n    def transpose(self):\n        return Modulo_Matrix(list(map(list,zip(*self.ele))))\n\
    \n    #\u884C\u57FA\u672C\u5909\u5F62\n    def row_reduce(self):\n        M=self\n\
    \        (R,C)=M.size\n        T=[]\n\n        for i in range(R):\n          \
    \  U=[]\n            for j in range(C):\n                U.append(M.ele[i][j])\n\
    \            T.append(U)\n\n        I=0\n        for J in range(C):\n        \
    \    if T[I][J]==0:\n                for i in range(I+1,R):\n                \
    \    if T[i][J]!=0:\n                        T[i],T[I]=T[I],T[i]\n           \
    \             break\n\n            if T[I][J]!=0:\n                u=T[I][J]\n\
    \                u_inv=pow(u, -1, Mod)\n                for j in range(C):\n \
    \                   T[I][j]*=u_inv\n                    T[I][j]%=Mod\n\n     \
    \           for i in range(R):\n                    if i!=I:\n               \
    \         v=T[i][J]\n                        for j in range(C):\n            \
    \                T[i][j]-=v*T[I][j]\n                            T[i][j]%=Mod\n\
    \                I+=1\n                if I==R:\n                    break\n\n\
    \        return Modulo_Matrix(T)\n\n    #\u5217\u57FA\u672C\u5909\u5F62\n    def\
    \ column_reduce(self):\n        M=self\n        (R,C)=M.size\n\n        T=[]\n\
    \        for i in range(R):\n            U=[]\n            for j in range(C):\n\
    \                U.append(M.ele[i][j])\n            T.append(U)\n\n        J=0\n\
    \        for I in range(R):\n            if T[I][J]==0:\n                for j\
    \ in range(J+1,C):\n                    if T[I][j]!=0:\n                     \
    \   for k in range(R):\n                            T[k][j],T[k][J]=T[k][J],T[k][j]\n\
    \                        break\n\n            if T[I][J]!=0:\n               \
    \ u=T[I][J]\n                u_inv=pow(u, -1, Mod)\n                for i in range(R):\n\
    \                    T[i][J]*=u_inv\n                    T[i][J]%=Mod\n\n    \
    \            for j in range(C):\n                    if j!=J:\n              \
    \          v=T[I][j]\n                        for i in range(R):\n           \
    \                 T[i][j]-=v*T[i][J]\n                            T[i][j]%=Mod\n\
    \                J+=1\n                if J==C:\n                    break\n\n\
    \        return Modulo_Matrix(T)\n\n    #\u884C\u5217\u306E\u968E\u6570\n    def\
    \ rank(self):\n        M=self.row_reduce()\n        (R,C)=M.size\n        T=M.ele\n\
    \n        rnk=0\n        for i in range(R):\n            f=False\n           \
    \ for j in range(C):\n                if T[i][j]!=0:\n                    f=True\n\
    \                    break\n\n            if f:\n                rnk+=1\n    \
    \        else:\n                break\n\n        return rnk\n\n    #\u884C\u306E\
    \u7D50\u5408\n    def row_union(self,other):\n        return Modulo_Matrix(self.ele+other.ele)\n\
    \n    #\u5217\u306E\u7D50\u5408\n    def column_union(self,other):\n        E=[]\n\
    \        for i in range(self.row):\n            E.append(self.ele[i]+other.ele[i])\n\
    \n        return Modulo_Matrix(E)\n\n    def __getitem__(self,index):\n      \
    \  if isinstance(index, int):\n            return self.ele[index]\n        else:\n\
    \            return self.ele[index[0]][index[1]]\n\n    def __setitem__(self,index,val):\n\
    \        assert isinstance(index,tuple) and len(index)==2\n        self.ele[index[0]][index[1]]=val\n\
    \n#=================================================\n#\u5358\u4F4D\u884C\u5217\
    \ndef Identity_Matrix(N):\n    \"\"\" N \u6B21\u5358\u4F4D\u884C\u5217\u3092\u4F5C\
    \u6210\u3059\u308B. \"\"\"\n\n    return Modulo_Matrix([[1 if i==j else 0 for\
    \ j in range(N)] for i in range(N)])\n\n#\u96F6\u884C\u5217\ndef Zero_Matrix(row,\
    \ col):\n    \"\"\" row \u884C col \u5217\u306E\u30BC\u30ED\u884C\u5217\u3092\u4F5C\
    \u6210\u3059\u308B. \"\"\"\n\n    return Modulo_Matrix([[0]*col for i in range(row)])\n\
    \n#\u6B63\u65B9\u884C\u5217?\ndef Is_Square(M):\n    return M.row==M.col\n\n#\u5BFE\
    \u89D2\u884C\u5217\ndef Diagonal_Matrix(D):\n    \"\"\" D \u306E\u7B2C i \u8981\
    \u7D20\u304C (i,i) \u6210\u5206\u3067\u3042\u308B\u5BFE\u89D2\u884C\u5217\u3092\
    \u751F\u6210\u3059\u308B.\n\n    D: \u30EA\u30B9\u30C8\n    \"\"\"\n\n    N=len(D)\n\
    \    return Modulo_Matrix([[D[i] if i==j else 0 for j in range(N)] for i in range(N)])\n\
    \n#\u884C\u5217\u306E\u76F4\u548C\ndef Direct_Sum(*A):\n    \"\"\" A=[A_0, A_1,\
    \ ..., A_{N-1}] \u306B\u5BFE\u3059\u308B\u76F4\u548C\u884C\u5217\u3092\u6C42\u3081\
    \u308B.\n\n    \"\"\"\n\n    r=c=0\n    for a in A:\n        r+=a.row\n      \
    \  c+=a.col\n\n    M=[[0]*c for _ in range(r)]\n    x=y=0\n    for p in range(len(A)):\n\
    \        a=A[p]\n        for i in range(a.row):\n            b=A[p].ele[i]\n \
    \           m=M[x+i]\n            for j in range(a.col):\n                m[y+j]=b[j]\n\
    \        x+=a.row; y+=a.col\n    return Modulo_Matrix(M)\n\n#\u30AF\u30ED\u30CD\
    \u30C3\u30AB\u30FC\u7A4D\ndef Kronecker_Product(*X):\n    A=[[1]]\n    for B in\
    \ X:\n        A=[[A[i//B.row][j//B.col]*B[i%B.row][j%B.col]%Mod for j in range(len(A[0])*B.col)]\
    \ for i in range(len(A)*B.row)]\n    return Modulo_Matrix(A)\n\n#\u30AF\u30ED\u30CD\
    \u30C3\u30AB\u30FC\u548C\ndef Kronecker_Sum(*X):\n    A=Modulo_Matrix([[0]])\n\
    \    for B in X:\n        A=Kronecker_Product(A, Identity_Matrix(B.row))+Kronecker_Product(Identity_Matrix(A.row),B)\n\
    \    return A\n\n#\u8DE1\ndef Trace(M):\n    \"\"\" \u6B63\u65B9\u884C\u5217 M\
    \ \u306E\u8DE1 (=\u5BFE\u89D2\u6210\u5206\u306E\u548C) \u3092\u6C42\u3081\u308B\
    . \"\"\"\n\n    assert Is_Square(M)\n\n    T=0\n    for i in range(M.row):\n \
    \       T+=M.ele[i][i]\n        T%=Mod\n    return T\n\ndef Determinant(M):\n\
    \    \"\"\" \u6B63\u65B9\u884C\u5217 M \u306E\u884C\u5217\u5F0F (\u7D20\u6570\
    \ mod) \u3092\u6C42\u3081\u308B.\"\"\"\n\n    assert Is_Square(M)\n\n    N=M.row\n\
    \    T=deepcopy(M.ele)\n    det=1\n\n    for j in range(N):\n        if T[j][j]==0:\n\
    \            for i in range(j+1,N):\n                if T[i][j]:\n           \
    \         break\n            else:\n                return 0\n            T[j],T[i]=T[i],T[j]\n\
    \            det=-det\n        Tj=T[j]\n        inv=pow(Tj[j], -1, Mod)\n    \
    \    for i in range(j+1,N):\n            Ti=T[i]\n            c=-inv*Ti[j]%Mod\n\
    \            for k in range(N):\n                Ti[k]+=c*Tj[k]\n            \
    \    Ti[k]%=Mod\n\n    for i in range(N):\n        det*=T[i][i]\n        det%=Mod\n\
    \    return det\n\ndef Determinant_Arbitrary_Mod(A):\n    \"\"\" \u6B63\u65B9\u884C\
    \u5217 M \u306E\u884C\u5217\u5F0F (\u4EFB\u610F mod) \u3092\u6C42\u3081\u308B\
    .\"\"\"\n\n    N=A.row\n    A=deepcopy(A.ele)\n    det=1\n\n    for i in range(N):\n\
    \        Ai=A[i]\n        for j in range(i+1, N):\n            Aj=A[j]\n     \
    \       while Aj[i]:\n                alpha=Ai[i]//Aj[i]\n                if alpha:\n\
    \                    for k in range(i, N):\n                        Ai[k]-=alpha*Aj[k]\n\
    \                        Ai[k]%=Mod\n                A[i], A[j]=A[j], A[i]\n \
    \               Ai=A[i]; Aj=A[j]\n                det*=-1\n        det*=Ai[i]\n\
    \        det%=Mod\n        if det==0:\n            break\n    return det\n\ndef\
    \ Characteristic_Polynomial(M):\n    \"\"\" M \u306E\u56FA\u6709\u591A\u9805\u5F0F\
    \u3092 sum(P[i] X^i) \u3068\u3057\u305F\u3068\u304D, P \u3092\u6C42\u3081\u308B\
    .\n\n    M: Modulo Matrix\n    \"\"\"\n\n    T=deepcopy(M.ele)\n    N=M.row\n\n\
    \    for j in range(N-2):\n        for i in range(j+1, N):\n            if T[i][j]:\n\
    \                break\n        else:\n            continue\n\n        T[j+1],T[i]=T[i],T[j+1]\n\
    \        for k in range(N):\n            T[k][j+1],T[k][i]=T[k][i],T[k][j+1]\n\
    \n        if T[j+1][j]:\n            Tjj=T[j+1]\n            inv=pow(Tjj[j], -1,\
    \ Mod)\n            for i in range(j+2, N):\n                Ti=T[i]\n       \
    \         c=inv*Ti[j]%Mod\n                for k in range(j,N):\n            \
    \        Ti[k]-=c*Tjj[k]\n                    Ti[k]%=Mod\n\n                for\
    \ k in range(N):\n                    T[k][j+1]+=c*T[k][i]\n                 \
    \   T[k][j+1]%=Mod\n\n    dp=[[0]*(i+1) for i in range(N+1)]; dp[0][0]=1\n   \
    \ for i in range(N):\n        P=dp[i+1]\n        for k in range(i+1):\n      \
    \      P[k+1]=dp[i][k]\n        for k in range(i+1):\n            P[k]+=T[i][i]*dp[i][k]\n\
    \            P[k]%=Mod\n\n        p=1\n        for j in range(i-1,-1,-1):\n  \
    \          p*=-T[j+1][j]; p%=Mod\n            c=p*T[j][i]%Mod\n            for\
    \ k in range(j+1):\n                P[k]+=c*dp[j][k]\n                P[k]%=Mod\n\
    \    P=dp[-1]\n    for i in range(N+1):\n        if i%2:\n            P[~i]*=-1;\
    \ P[~i]%=Mod\n    return P\n\n#===\nMod=998244353\n"
  dependsOn: []
  isVerificationFile: false
  path: Modulo_Matrix/Modulo_Matrix.py
  requiredBy: []
  timestamp: '2023-08-06 21:18:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Matrix/Determinant.test.py
  - test_verify/yosupo_library_checker/Matrix/Product.test.py
  - test_verify/yosupo_library_checker/Matrix/Inverse.test.py
documentation_of: Modulo_Matrix/Modulo_Matrix.py
layout: document
redirect_from:
- /library/Modulo_Matrix/Modulo_Matrix.py
- /library/Modulo_Matrix/Modulo_Matrix.py.html
title: Modulo_Matrix/Modulo_Matrix.py
---
