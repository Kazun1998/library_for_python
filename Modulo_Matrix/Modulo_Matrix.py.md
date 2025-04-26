---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Matrix/Adjugate_Matrix.test.py
    title: test_verify/yosupo_library_checker/Matrix/Adjugate_Matrix.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Matrix/Determinant.test.py
    title: test_verify/yosupo_library_checker/Matrix/Determinant.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Matrix/Inverse.test.py
    title: test_verify/yosupo_library_checker/Matrix/Inverse.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Matrix/Matrix_Rank.test.py
    title: test_verify/yosupo_library_checker/Matrix/Matrix_Rank.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Matrix/Power.test.py
    title: test_verify/yosupo_library_checker/Matrix/Power.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Matrix/Product.test.py
    title: test_verify/yosupo_library_checker/Matrix/Product.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from copy import deepcopy\n\nclass SingularMatrixError(Exception):\n    def\
    \ __str__(self):\n        return \"\u975E\u6B63\u5247\u884C\u5217\u306E\u9006\u884C\
    \u5217\u3092\u6C42\u3081\u3088\u3046\u3068\u3057\u307E\u3057\u305F.\"\n\nclass\
    \ Modulo_Matrix():\n    __slots__ = (\"ele\", \"__row\", \"__col\")\n\n    # property\n\
    \    @property\n    def row(self):\n        return self.__row\n\n    @property\n\
    \    def col(self):\n        return self.__col\n\n    @property\n    def size(self):\n\
    \        return (self.row, self.col)\n\n    #\u5165\u529B\n    def __init__(self,\
    \ M: list[list[int]]):\n        \"\"\" \u884C\u5217 M \u3092\u751F\u6210\u3059\
    \u308B.\n        \u203B Mod: \u6CD5\u306F\u30B0\u30ED\u30FC\u30D0\u30EB\u5909\u6570\
    \u304B\u3089\u6307\u5B9A\n\n        Args:\n            M (list[int]): \u884C\u5217\
    \n        \"\"\"\n\n        self.ele=[[x%Mod for x in X] for X in M]\n       \
    \ self.__row = len(M)\n        self.__col = len(M[0]) if self.row > 0 else 0\n\
    \n    #\u51FA\u529B\n    def __str__(self):\n        return \"[\"+\"\\n\".join(map(str,self.ele))+\"\
    ]\"\n\n    def __repr__(self):\n        return str(self)\n\n    # \u96F6\u884C\
    \u5217, \u5358\u4F4D\u884C\u5217\n    @classmethod\n    def Zero_Matrix(cls, row:\
    \ int, col: int) -> \"Modulo_Matrix\":\n        \"\"\" row \u884C col \u5217\u306E\
    \u30BC\u30ED\u884C\u5217\u3092\u751F\u6210\u3059\u308B.\n\n        Args:\n   \
    \         row (int): \u884C\n            col (int): \u5217\n\n        Returns:\n\
    \            Modulo_Matrix: row \u884C col \u5217\u306E\u30BC\u30ED\u884C\u5217\
    \n        \"\"\"\n\n        return Modulo_Matrix([[0] * col for _ in range(row)])\n\
    \n    @classmethod\n    def Identity_Matrix(cls, N: int) -> \"Modulo_Matrix\"\
    :\n        \"\"\" N \u6B21\u306E\u5358\u4F4D\u884C\u5217\u3092\u751F\u6210\u3059\
    \u308B.\n\n        Args:\n            N (int): \u6B21\u6570\n\n        Returns:\n\
    \            Modulo_Matrix: N \u6B21\u5358\u4F4D\u884C\u5217\n        \"\"\"\n\
    \n        return Modulo_Matrix([[1 if i==j else 0 for j in range(N)] for i in\
    \ range(N)])\n\n    #+,-\n    def __pos__(self):\n        return self\n\n    def\
    \ __neg__(self):\n        return self.__scale__(-1)\n\n    #\u52A0\u6CD5\n   \
    \ def __add__(self, other):\n        C = [None] * self.row\n        for i, (Ai,\
    \ Bi) in enumerate(zip(self.ele, other.ele)):\n            C[i] = [Ai[j] + Bi[j]\
    \ for j in range(self.col)]\n\n        return Modulo_Matrix(C)\n\n    def __iadd__(self,other):\n\
    \        M=self.ele; N=other.ele\n\n        for i in range(self.row):\n      \
    \      Mi,Ni=M[i],N[i]\n            for j in range(self.col):\n              \
    \  Mi[j]+=Ni[j]\n                Mi[j]%=Mod\n        return self\n\n    #\u6E1B\
    \u6CD5\n    def __sub__(self,other):\n        C = [None] * self.row\n        for\
    \ i, (Ai, Bi) in enumerate(zip(self.ele, other.ele)):\n            C[i] = [Ai[j]\
    \ - Bi[j] for j in range(self.col)]\n\n        return Modulo_Matrix(C)\n\n   \
    \ def __isub__(self,other):\n        M=self.ele; N=other.ele\n\n        for i\
    \ in range(self.row):\n            Mi,Ni=M[i],N[i]\n            for j in range(self.col):\n\
    \                Mi[j]-=Ni[j]\n                Mi[j]%=Mod\n        return self\n\
    \n    #\u4E57\u6CD5\n    def __mul__(self, other):\n        if isinstance(other,\
    \ int):\n            return self.__scale__(other)\n\n        if not isinstance(other,\
    \ Modulo_Matrix):\n            raise TypeError\n\n        assert self.col == other.row,\
    \ f\"\u5DE6\u5074\u306E\u5217\u3068\u53F3\u5074\u306E\u884C\u304C\u4E00\u81F4\u3057\
    \u307E\u305B\u3093 (left: {self.col}, right:{other.row}).\"\n\n        A = self.ele;\
    \ B = other.ele\n        C = [[0] * other.col for _ in range(self.row)]\n\n  \
    \      for i, Ci in enumerate(C):\n            for k, a_ik in enumerate(A[i]):\n\
    \                for j, b_kj in enumerate(B[k]):\n                    Ci[j] =\
    \ (Ci[j] + a_ik * b_kj) % Mod\n\n        return Modulo_Matrix(C)\n\n    def __rmul__(self,other):\n\
    \        if isinstance(other,int):\n            return self.__scale__(other)\n\
    \n    def inverse(self) -> \"Modulo_Matrix\":\n        \"\"\" \u9006\u884C\u5217\
    \u3092\u6C42\u3081\u308B\n\n        Raises:\n            SingularMatrixError:\
    \ \u975E\u6B63\u5247\u884C\u5217\u306E\u9006\u884C\u5217\u3092\u6C42\u3081\u3088\
    \u3046\u3068\u3057\u305F\u3068\u304D\u306B\u767A\u751F\n\n        Returns:\n \
    \           Modulo_Matrix: \u9006\u884C\u5217\n        \"\"\"\n\n        inverse,\
    \ _ = self.inverse_with_determinant()\n        if inverse is None:\n         \
    \   raise SingularMatrixError()\n\n        return inverse\n\n    def inverse_with_determinant(self)\
    \ -> tuple[\"Modulo_Matrix\", int] | tuple[None, int]:\n        \"\"\" self \u306E\
    \u9006\u884C\u5217\u3068 self \u306E\u884C\u5217\u5F0F\u3092\u6C42\u3081\u308B\
    .\n\n        Returns:\n            tuple[\"Modulo_Matrix\", int] | tuple[None,\
    \ int]: (\u9006\u884C\u5217 (\u975E\u6B63\u5247\u306E\u5834\u5408\u306F None),\
    \ \u884C\u5217\u5F0F)\n        \"\"\"\n\n        assert self.row == self.col,\"\
    \u6B63\u65B9\u884C\u5217\u3067\u306F\u3042\u308A\u307E\u305B\u3093.\"\n\n    \
    \    M = self\n        N = M.row\n        R = [[1 if i == j else 0 for j in range(N)]\
    \ for i in range(N)]\n        T = deepcopy(M.ele)\n        det = 1\n\n       \
    \ for j in range(N):\n            if T[j][j] == 0:\n                for i in range(j+1,N):\n\
    \                    if T[i][j]:\n                        break\n            \
    \    else:\n                    return None, 0\n\n                T[j], T[i] =\
    \ T[i], T[j]\n                R[j], R[i] = R[i], R[j]\n                det = -det\
    \ % Mod\n\n            Tj, Rj = T[j] ,R[j]\n            inv = pow(Tj[j], -1, Mod)\n\
    \            det = (Tj[j] * det) % Mod\n\n            for k in range(N):\n   \
    \             Tj[k] *=inv; Tj[k] %= Mod\n                Rj[k] *=inv; Rj[k] %=\
    \ Mod\n\n            for i in range(N):\n                if i == j:\n        \
    \            continue\n\n                c = T[i][j]\n                Ti, Ri =\
    \ T[i], R[i]\n                for k in range(N):\n                    Ti[k] -=\
    \ Tj[k] * c; Ti[k] %= Mod\n                    Ri[k] -= Rj[k] * c; Ri[k] %= Mod\n\
    \n        for i in range(N):\n            det = (T[i][i] * det) % Mod\n\n    \
    \    return Modulo_Matrix(R), det\n\n    #\u30B9\u30AB\u30E9\u30FC\u500D\n   \
    \ def __scale__(self, r: int) -> \"Modulo_Matrix\":\n        \"\"\" r \u500D\u3059\
    \u308B\n\n        Args:\n            r (int): \u30B9\u30AB\u30E9\u30FC\u500D\n\
    \n        Returns:\n            Modulo_Matrix: r \u500D\n        \"\"\"\n\n  \
    \      r %= Mod\n        return Modulo_Matrix([[r * m_ij for m_ij in Mi] for Mi\
    \ in self.ele])\n\n    #\u7D2F\u4E57\n    def __pow__(self, n):\n        assert\
    \ self.row==self.col, \"\u6B63\u65B9\u884C\u5217\u3067\u306F\u3042\u308A\u307E\
    \u305B\u3093.\"\n\n        sgn = 1 if n >= 0 else -1\n        n = abs(n)\n\n \
    \       C = Modulo_Matrix.Identity_Matrix(self.row)\n        tmp = self\n    \
    \    while n:\n            if n & 1:\n                C = C * tmp\n          \
    \  tmp = tmp * tmp\n            n >>= 1\n\n        return C if sgn == 1 else C.inverse()\n\
    \n    #\u7B49\u53F7\n    def __eq__(self,other):\n        return self.ele==other.ele\n\
    \n    #\u4E0D\u7B49\u53F7\n    def __neq__(self,other):\n        return not(self==other)\n\
    \n    #\u8EE2\u7F6E\n    def transpose(self) -> \"Modulo_Matrix\":\n        \"\
    \"\" \u8EE2\u7F6E\u884C\u5217\u3092\u6C42\u3081\u308B.\n\n        Returns:\n \
    \           Modulo_Matrix: \u8EE2\u7F6E\u884C\u5217\n        \"\"\"\n\n      \
    \  return Modulo_Matrix(list(map(list,zip(*self.ele))))\n\n    #\u884C\u57FA\u672C\
    \u5909\u5F62\n    def row_reduce(self) -> \"Modulo_Matrix\":\n        \"\"\" \u884C\
    \u57FA\u672C\u5909\u5F62\u3092\u3067\u304D\u308B\u3060\u3051\u65BD\u3057\u305F\
    \u5F8C\u306E\u884C\u5217\u3092\u6C42\u3081\u308B.\n\n        Returns:\n      \
    \      Modulo_Matrix: \u884C\u57FA\u672C\u5909\u5F62\u3092\u3067\u304D\u308B\u3060\
    \u3051\u65BD\u3057\u305F\u5F8C\u306E\u884C\u5217\n        \"\"\"\n\n        (row,\
    \ col) = self.size\n\n        T = deepcopy(self.ele)\n\n        I = 0\n      \
    \  for J in range(col):\n            if T[I][J] == 0:\n                for i in\
    \ range(I + 1, row):\n                    if T[i][J] != 0:\n                 \
    \       T[i], T[I] = T[I], T[i]\n                        break\n             \
    \   else:\n                    continue\n\n            u = T[I][J]\n         \
    \   u_inv = pow(u, -1, Mod)\n            for j in range(col):\n              \
    \  T[I][j] *= u_inv\n                T[I][j] %= Mod\n\n            for i in range(row):\n\
    \                if i == I:\n                    continue\n\n                v\
    \ = T[i][J]\n                for j in range(col):\n                    T[i][j]\
    \ -= v * T[I][j]\n                    T[i][j] %= Mod\n            I += 1\n   \
    \         if I == row:\n                break\n\n        return Modulo_Matrix(T)\n\
    \n    #\u5217\u57FA\u672C\u5909\u5F62\n    def column_reduce(self) -> \"Modulo_Matrix\"\
    :\n        \"\"\" \u5217\u57FA\u672C\u5909\u5F62\u3092\u3067\u304D\u308B\u3060\
    \u3051\u65BD\u3057\u305F\u5F8C\u306E\u884C\u5217\u3092\u6C42\u3081\u308B.\n\n\
    \        Returns:\n            Modulo_Matrix: \u5217\u57FA\u672C\u5909\u5F62\u3092\
    \u3067\u304D\u308B\u3060\u3051\u65BD\u3057\u305F\u5F8C\u306E\u884C\u5217\n   \
    \     \"\"\"\n\n        (row, col) = self.size\n\n        T = deepcopy(self.ele)\n\
    \n        J = 0\n        for I in range(row):\n            if T[I][J] ==0 :\n\
    \                for j in range(J + 1, col):\n                    if T[I][j] !=\
    \ 0:\n                        for k in range(row):\n                         \
    \   T[k][j], T[k][J] = T[k][J], T[k][j]\n                        break\n     \
    \           else:\n                    continue\n\n            u = T[I][J]\n \
    \           u_inv = pow(u, -1, Mod)\n            for i in range(row):\n      \
    \          T[i][J] *= u_inv\n                T[i][J] %= Mod\n\n            for\
    \ j in range(col):\n                if j != J:\n                    v = T[I][j]\n\
    \                    for i in range(row):\n                        T[i][j] -=\
    \ v * T[i][J]\n                        T[i][j] %= Mod\n            J += 1\n  \
    \          if J == col:\n                break\n\n        return Modulo_Matrix(T)\n\
    \n    #\u884C\u5217\u306E\u968E\u6570\n    def rank(self) -> int:\n        \"\"\
    \" \u884C\u5217\u306E\u30E9\u30F3\u30AF\u3092\u6C42\u3081\u308B\n\n        Returns:\n\
    \            int: \u30E9\u30F3\u30AF\n        \"\"\"\n\n        row_reduced =\
    \ self.row_reduce()\n        (row, col) = row_reduced.size\n\n        rnk = 0\n\
    \        for i in range(row):\n            Ti = row_reduced.ele[i]\n         \
    \   if any(Ti[j] for j in range(col)):\n                rnk += 1\n\n        return\
    \ rnk\n\n    # \u5358\u5C04 ?\n    def is_injection(self) -> bool:\n        \"\
    \"\" \u884C\u5217\u304C\u8868\u3059\u7DDA\u5F62\u5199\u50CF\u306F\u5358\u5C04\
    ?\n\n        Returns:\n            bool: \u5358\u5C04 ?\n        \"\"\"\n\n  \
    \      return self.rank() == self.col\n\n    # \u5168\u5C04 ?\n    def is_surjective(self)\
    \ -> bool:\n        \"\"\" \u884C\u5217\u304C\u8868\u3059\u7DDA\u5F62\u5199\u50CF\
    \u306F\u5168\u5C04?\n\n        Returns:\n            bool: \u5168\u5C04 ?\n  \
    \      \"\"\"\n\n        return self.rank() == self.row\n\n    # \u5168\u5358\u5C04\
    \ ?\n    def is_bijection(self) -> bool:\n        \"\"\" \u884C\u5217\u304C\u8868\
    \u3059\u7DDA\u5F62\u5199\u50CF\u306F\u5168\u5358\u5C04?\n\n        Returns:\n\
    \            bool: \u5168\u5358\u5C04 ?\n        \"\"\"\n\n        return self.col\
    \ == self.row == self.rank()\n\n    #\u884C\u306E\u7D50\u5408\n    def row_union(self,other):\n\
    \        return Modulo_Matrix(self.ele+other.ele)\n\n    #\u5217\u306E\u7D50\u5408\
    \n    def column_union(self,other):\n        E=[]\n        for i in range(self.row):\n\
    \            E.append(self.ele[i]+other.ele[i])\n\n        return Modulo_Matrix(E)\n\
    \n    def __getitem__(self,index):\n        if isinstance(index, int):\n     \
    \       return self.ele[index]\n        else:\n            return self.ele[index[0]][index[1]]\n\
    \n    def __setitem__(self,index,val):\n        assert isinstance(index,tuple)\
    \ and len(index)==2\n        self.ele[index[0]][index[1]]=val\n\n#=================================================\n\
    #\u6B63\u65B9\u884C\u5217?\ndef Is_Square(M: Modulo_Matrix) -> bool:\n    \"\"\
    \" M \u306F\u6B63\u65B9\u884C\u5217\u304B?\n\n    Args:\n        M (Modulo_Matrix):\
    \ \u884C\u5217\n\n    Returns:\n        bool: \u6B63\u65B9\u884C\u5217 ?\n   \
    \ \"\"\"\n\n    return M.row == M.col\n\n#\u5BFE\u89D2\u884C\u5217\ndef Diagonal_Matrix(D:\
    \ list[int]) -> Modulo_Matrix:\n    \"\"\" D \u306E\u7B2C i \u6210\u5206\u304C\
    \ (i, i) \u6210\u5206\u306B\u306A\u308B\u5BFE\u89D2\u884C\u5217\u3092\u751F\u6210\
    \u3059\u308B.\n\n    Args:\n        D (list[int]): \u5BFE\u89D2\u6210\u5206\u306E\
    \u30EA\u30B9\u30C8\n\n    Returns:\n        Modulo_Matrix: \u5BFE\u89D2\u884C\u5217\
    \n    \"\"\"\n\n    N=len(D)\n    return Modulo_Matrix([[D[i] if i==j else 0 for\
    \ j in range(N)] for i in range(N)])\n\n#\u884C\u5217\u306E\u76F4\u548C\ndef Direct_Sum(*A):\n\
    \    \"\"\" A=[A_0, A_1, ..., A_{N-1}] \u306B\u5BFE\u3059\u308B\u76F4\u548C\u884C\
    \u5217\u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n    r=c=0\n    for a in A:\n\
    \        r+=a.row\n        c+=a.col\n\n    M=[[0]*c for _ in range(r)]\n    x=y=0\n\
    \    for p in range(len(A)):\n        a=A[p]\n        for i in range(a.row):\n\
    \            b=A[p].ele[i]\n            m=M[x+i]\n            for j in range(a.col):\n\
    \                m[y+j]=b[j]\n        x+=a.row; y+=a.col\n    return Modulo_Matrix(M)\n\
    \n#\u30AF\u30ED\u30CD\u30C3\u30AB\u30FC\u7A4D\ndef Kronecker_Product(*X):\n  \
    \  A=[[1]]\n    for B in X:\n        A=[[A[i//B.row][j//B.col]*B[i%B.row][j%B.col]%Mod\
    \ for j in range(len(A[0])*B.col)] for i in range(len(A)*B.row)]\n    return Modulo_Matrix(A)\n\
    \n#\u30AF\u30ED\u30CD\u30C3\u30AB\u30FC\u548C\ndef Kronecker_Sum(*X):\n    A=Modulo_Matrix([[0]])\n\
    \    for B in X:\n        A=Kronecker_Product(A, Modulo_Matrix.Identity_Matrix(B.row))+Kronecker_Product(Modulo_Matrix.Identity_Matrix(A.row),B)\n\
    \    return A\n\n#\u8DE1\ndef Trace(M: Modulo_Matrix) -> int:\n    \"\"\" \u6B63\
    \u65B9\u884C\u5217 M \u306E\u8DE1 (\u5BFE\u89D2\u6210\u5206\u306E\u548C) \u3092\
    \u6C42\u3081\u308B.\n\n    Args:\n        M (Modulo_Matrix): \u6B63\u65B9\u884C\
    \u5217\n\n    Returns:\n        int: \u8DE1\n    \"\"\"\n\n    assert Is_Square(M)\n\
    \    return sum(M.ele[i][i] for i in range(M.row)) % Mod\n\ndef Determinant(M:\
    \ Modulo_Matrix) -> int:\n    \"\"\" \u6B63\u65B9\u884C\u5217 M \u306E\u884C\u5217\
    \u5F0F (\u7D20\u6570 mod) \u3092\u6C42\u3081\u308B.\n\n    Args:\n        M (Modulo_Matrix):\
    \ \u6B63\u65B9\u884C\u5217\n\n    Returns:\n        int: \u884C\u5217\u5F0F (mod\
    \ \u7D20\u6570)\n    \"\"\"\n\n    assert Is_Square(M)\n\n    N=M.row\n    T=deepcopy(M.ele)\n\
    \    det=1\n\n    for j in range(N):\n        if T[j][j]==0:\n            for\
    \ i in range(j+1,N):\n                if T[i][j]:\n                    break\n\
    \            else:\n                return 0\n            T[j],T[i]=T[i],T[j]\n\
    \            det=-det\n        Tj=T[j]\n        inv=pow(Tj[j], -1, Mod)\n    \
    \    for i in range(j+1,N):\n            Ti=T[i]\n            c=-inv*Ti[j]%Mod\n\
    \            for k in range(N):\n                Ti[k]+=c*Tj[k]\n            \
    \    Ti[k]%=Mod\n\n    for i in range(N):\n        det*=T[i][i]\n        det%=Mod\n\
    \    return det\n\ndef Determinant_Arbitrary_Mod(A: Modulo_Matrix) -> int:\n \
    \   \"\"\" \u6B63\u65B9\u884C\u5217 M \u306E\u884C\u5217\u5F0F (\u4EFB\u610F mod)\
    \ \u3092\u6C42\u3081\u308B.\n\n    Args:\n        M (Modulo_Matrix): \u6B63\u65B9\
    \u884C\u5217\n\n    Returns:\n        int: \u884C\u5217\u5F0F (mod \u4EFB\u610F\
    )\n    \"\"\"\n    N=A.row\n    A=deepcopy(A.ele)\n    det=1\n\n    for i in range(N):\n\
    \        Ai=A[i]\n        for j in range(i+1, N):\n            Aj=A[j]\n     \
    \       while Aj[i]:\n                alpha=Ai[i]//Aj[i]\n                if alpha:\n\
    \                    for k in range(i, N):\n                        Ai[k]-=alpha*Aj[k]\n\
    \                        Ai[k]%=Mod\n                A[i], A[j]=A[j], A[i]\n \
    \               Ai=A[i]; Aj=A[j]\n                det*=-1\n        det*=Ai[i]\n\
    \        det%=Mod\n        if det==0:\n            break\n    return det\n\ndef\
    \ Characteristic_Polynomial(M: Modulo_Matrix) -> list[int]:\n    \"\"\" \u6B63\
    \u65B9\u884C\u5217 M \u306E\u56FA\u6709\u591A\u9805\u5F0F\u3092 sum(P[i] X^i)\
    \ \u3068\u3057\u305F\u3068\u304D, P \u3092\u6C42\u3081\u308B.\n\n    Args:\n \
    \       M (Modulo_Matrix): \u6B63\u65B9\u884C\u5217\n\n    Returns:\n        list[int]:\
    \ \u56FA\u6709\u591A\u9805\u5F0F\u3092 sum(P[i] X^i) \u3068\u3057\u305F\u3068\u304D\
    \u306E P \u3092\u6C42\u3081\u308B.\n    \"\"\"\n\n    T=deepcopy(M.ele)\n    N=M.row\n\
    \n    for j in range(N-2):\n        for i in range(j+1, N):\n            if T[i][j]:\n\
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
    \ P[~i]%=Mod\n    return P\n\ndef Adjugate_Matrix(A: Modulo_Matrix) -> Modulo_Matrix:\n\
    \    \"\"\" \u6B63\u65B9\u884C\u5217 A \u306E\u4F59\u56E0\u5B50\u884C\u5217 adj\
    \ A := ((-1)^(i+j) det A_{i,j}) \u3092\u6C42\u3081\u308B.\n\n    Args:\n     \
    \   A (Modulo_Matrix): \u6B63\u65B9\u884C\u5217\n\n    Returns:\n        Modulo_Matrix:\
    \ \u4F59\u56E0\u5B50\u884C\u5217\n    \"\"\"\n\n    from random import randint\n\
    \n    N = A.row\n    A_ext = [[0] * (N + 1) for _ in range(N + 1)]\n    for i\
    \ in range(N):\n        for j in range(N):\n            A_ext[i][j] = A[i][j]\n\
    \n    for i in range(N):\n        A_ext[i][N] = A_ext[N][i] = randint(0, Mod -\
    \ 1)\n\n    A_ext_inv, det = Modulo_Matrix(A_ext).inverse_with_determinant()\n\
    \n    if A_ext_inv is None:\n        return Modulo_Matrix.Zero_Matrix(N, N)\n\n\
    \    adj = [[det * ((A_ext_inv[N][N] * A_ext_inv[i][j] - A_ext_inv[i][N] * A_ext_inv[N][j])\
    \ % Mod) for j in range(N)] for i in range(N)]\n    return Modulo_Matrix(adj)\n\
    \n#===\nMod=998244353\n"
  dependsOn: []
  isVerificationFile: false
  path: Modulo_Matrix/Modulo_Matrix.py
  requiredBy: []
  timestamp: '2025-02-24 11:37:33+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Matrix/Adjugate_Matrix.test.py
  - test_verify/yosupo_library_checker/Matrix/Determinant.test.py
  - test_verify/yosupo_library_checker/Matrix/Power.test.py
  - test_verify/yosupo_library_checker/Matrix/Inverse.test.py
  - test_verify/yosupo_library_checker/Matrix/Product.test.py
  - test_verify/yosupo_library_checker/Matrix/Matrix_Rank.test.py
documentation_of: Modulo_Matrix/Modulo_Matrix.py
layout: document
title: Modulo_Matrix
---

## Outline

$m$ を素数とする. $\mathbb{Z}/m \mathbb{Z}$ を要素に持つ行列に対する様々な計算を行うクラス, 関数.

ただし, たいていの場合は $m$ が素数であることを要求する. これにより, $\mathbb{Z}/m \mathbb{Z}$ は体になる.

以降, $p$ が素数の時には体 $\mathbb{Z}/p \mathbb{Z}$ を $\mathbb{F}_p$ と書く.

## Theory

### 逆行列

行列に対する次の操作を行基本変形という.

* $i$ 行目と $j$ 行目を交換する $(i \neq j)$
* $i$ 行目を $\alpha$ 倍 $(\alpha \in \mathbb{F}_p^\times)$ する.
* $i$ 行目に $j$ 行目の $\beta$ 倍 $(\beta \in \mathbb{F}_p)$ を加える.

次のような行列を基本行列という.

* $P_{N,i,j}:=(\bm{e}_1, \dots, \bm{e}_{i-1}, \bm{e}_j, \bm{e}_{i+1}, \dots, \bm{e}_{j-1}, \bm{e}_i, \bm{e}_{j+1}, \dots \bm{e}_N)$
* $Q_{N,i,\alpha}:=(\bm{e}_1, \dots, \bm{e}_{i-1}, \alpha \bm{e}_i, \bm{e}_{i+1}, \dots, \bm{e}_N)$
* $R_{N,i,j,\beta}:=(\bm{e}_1, \dots, \bm{e}_{j-1}, \bm{e}_j+\beta \bm{e}_i, \bm{e}_{j+1}, \dots \bm{e}_N)$

ここで, $A \in M_N(\mathbb{F}_p)$ に対して,

* $P_{N,i,j}A$ は $A$ の第 $i$ 行と第 $j$ 行を入れ替えた行列
* $Q_{N,i,\alpha} A$ は $A$ の第 $i$ 行を $\alpha$ 倍した行列
* $R_{N,i,j,\beta} A$ は $A$ の第 $i$ 行に第 $j$ 行の $\beta$ 倍を加えた行列

になり, 左から基本行列を掛けることと, 行基本変形を行うことが1対1に対応する.

ここで, 任意の $A \in M_N(\mathbb{F}_p)$ に対して, 基本行列 $S_1, \dots, S_L$ と $0 \leq K \leq N$ が存在して,

$$S_L S_{L-1} \dots S_1 A=(\bm{e}_1, \dots, \bm{e}_K, \bm{0}, \dots \bm{0})$$

となる. ここで, $K$ については $S_1, \dots, S_L$ の取り方に依らず, $A$ のみによって定まる. よって, この $K$ のことを行列 $A$ の Rank (階数) といい, $\operatorname{rank} A$ と表す.

そして, $A \in M_N(\mathbb{F}_p)$ に対して, 以下は同値になる.

* $A \in M_N(\mathbb{F}_p)^\times$
* $\operatorname{rank} A=N$

つまり, $A \in M_N(\mathbb{F}_p)^\times$ のとき,

$$S_L S_{L-1} \dots S_1 A=(\bm{e}_1, \dots, \bm{e}_N)=I_N$$

である. $S:=_L S_{L-1} \dots S_1$ とすると, $SA=I_N$ となる. このとき, $A^{-1}=S$ であることも導ける.

### 行列式

行列式 $\det: M_N(\mathbb{F}_p) \to \mathbb{F}_p$ を以下で定義する. ただし,$\mathfrak{S}_N$ で $N$ 次対称群を表すとする.

$$ \det A:=\sum_{\sigma \in \mathfrak{S}_N} \operatorname{sgn} \sigma \prod_{i=1}^N A_{i, \sigma(i)}$$

この行列式は次のような性質を満たす.

* 各行に対する多重線形性
* 交代性
* $\det I_N=1$

実はこの3条件を満たすような写像は行列式のみである.

また, 行列式は積に関して準同型を成す. つまり, $A,B \in M_N(\mathbb{F}_p)$ に対して,

$$ \det (AB)=(\det A)(\det B)$$

となる.

このとき, 逆行列の求め方と同様にして, 行基本行列 $S_1, \dots, S_L$ と上三角行列が存在して,

$$S_1 S_2 \dots S_K A=U$$

となる.

そして,

* $\det P_{i,j}=-1$
* $\det Q_{i,\alpha}=\alpha$
* $\det R_{i,j,\beta}=1$
* $\det U$ は $N$ 個の対角成分の積

である.

これによって,

$$\det A=\dfrac{\det U}{(\det S_1) \dots (\det S_K)}$$

として求められることができる. 計算量は $O(N^3)$ である.
