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
  code: "class Modulo_Error(Exception):\n    pass\n\nclass Modulo():\n    __slots__=(\"\
    a\",\"n\")\n\n    def __init__(self,a,n):\n        self.a=a%n\n        self.n=n\n\
    \n    def __str__(self):\n        return \"{} (mod {})\".format(self.a,self.n)\n\
    \n    def __repr__(self):\n        return self.__str__()\n\n    #+,-\n    def\
    \ __pos__(self):\n        return self\n\n    def __neg__(self):\n        return\
    \  Modulo(-self.a,self.n)\n\n    #\u7B49\u53F7,\u4E0D\u7B49\u53F7\n    def __eq__(self,other):\n\
    \        if isinstance(other,Modulo):\n            return (self.a==other.a) and\
    \ (self.n==other.n)\n        elif isinstance(other,int):\n            return (self-other).a==0\n\
    \n    def __neq__(self,other):\n        return not(self==other)\n\n    def __le__(self,other):\n\
    \        a,p=self.a,self.n\n        b,q=other.a,other.n\n        return (a-b)%q==0\
    \ and p%q==0\n\n    def __ge__(self,other):\n        return other<=self\n\n  \
    \  def __lt__(self,other):\n        return (self<=other) and (self!=other)\n\n\
    \    def __gt__(self,other):\n        return (self>=other) and (self!=other)\n\
    \n    def __contains__(self,val):\n        return val%self.n==self.a\n\n    #\u52A0\
    \u6CD5\n    def __add__(self,other):\n        if isinstance(other,Modulo):\n \
    \           if self.n!=other.n:\n                raise Modulo_Error(\"\u7570\u306A\
    \u308B\u6CD5\u540C\u58EB\u306E\u6F14\u7B97\u3067\u3059.\")\n            return\
    \ Modulo(self.a+other.a,self.n)\n        elif isinstance(other,int):\n       \
    \     return Modulo(self.a+other,self.n)\n\n    def __radd__(self,other):\n  \
    \      if isinstance(other,int):\n            return Modulo(self.a+other,self.n)\n\
    \n    def __iadd__(self,other):\n        if isinstance(other,Modulo):\n      \
    \      if self.n!=other.n: raise Modulo_Error(\"\u7570\u306A\u308B\u6CD5\u540C\
    \u58EB\u306E\u6F14\u7B97\u3067\u3059.\")\n            self.a+=other.a\n      \
    \      if self.a>=self.n: self.a-=self.n\n        elif isinstance(other,int):\n\
    \            self.a+=other\n            if self.a>=self.n: self.a-=self.n\n  \
    \      return self\n\n    #\u6E1B\u6CD5\n    def __sub__(self,other):\n      \
    \  return self+(-other)\n\n    def __rsub__(self,other):\n        if isinstance(other,int):\n\
    \            return -self+other\n\n    def __isub__(self,other):\n        if isinstance(other,Modulo):\n\
    \            if self.n!=other.n: raise Modulo_Error(\"\u7570\u306A\u308B\u6CD5\
    \u540C\u58EB\u306E\u6F14\u7B97\u3067\u3059.\")\n            self.a-=other.a\n\
    \            if self.a<0: self.a+=self.n\n        elif isinstance(other,int):\n\
    \            self.a-=other\n            if self.a<0: self.a+=self.n\n        return\
    \ self\n\n    #\u4E57\u6CD5\n    def __mul__(self,other):\n        if isinstance(other,Modulo):\n\
    \            if self.n!=other.n:\n                raise Modulo_Error(\"\u7570\u306A\
    \u308B\u6CD5\u540C\u58EB\u306E\u6F14\u7B97\u3067\u3059.\")\n            return\
    \ Modulo(self.a*other.a,self.n)\n        elif isinstance(other,int):\n       \
    \     return Modulo(self.a*other,self.n)\n\n    def __rmul__(self,other):\n  \
    \      if isinstance(other,int):\n            return Modulo(self.a*other,self.n)\n\
    \n    def __imul__(self,other):\n        if isinstance(other,Modulo):\n      \
    \      if self.n!=other.n: raise Modulo_Error(\"\u7570\u306A\u308B\u6CD5\u540C\
    \u58EB\u306E\u6F14\u7B97\u3067\u3059.\")\n            self.a*=other.a\n      \
    \  elif isinstance(other,int):\n            self.a*=other\n        self.a%=self.n\n\
    \        return self\n\n    #Modulo\u9006\u6570\n    def inverse(self):\n    \
    \    return self.Modulo_Inverse()\n\n    def Modulo_Inverse(self):\n        s,t=1,0\n\
    \        a,b=self.a,self.n\n        while b:\n            q,a,b=a//b,b,a%b\n \
    \           s,t=t,s-q*t\n\n        if a!=1:\n            raise Modulo_Error(\"\
    {}\u306E\u9006\u6570\u304C\u5B58\u5728\u3057\u307E\u305B\u3093\".format(self))\n\
    \        else:\n            return Modulo(s,self.n)\n\n    #\u9664\u6CD5\n   \
    \ def __truediv__(self,other):\n        return self*(other.Modulo_Inverse())\n\
    \n    def __rtruediv__(self,other):\n        return other*(self.Modulo_Inverse())\n\
    \n    #\u7D2F\u4E57\n    def __pow__(self,other):\n        if isinstance(other,int):\n\
    \            u=abs(other)\n\n            r=Modulo(pow(self.a,u,self.n),self.n)\n\
    \            if other>=0:\n                return r\n            else:\n     \
    \           return r.Modulo_Inverse()\n        else:\n            b,n=other.a,other.n\n\
    \            if pow(self.a,n,self.n)!=1:\n                raise Modulo_Error(\"\
    \u77DB\u76FE\u306A\u304F\u5B9A\u7FA9\u3067\u304D\u307E\u305B\u3093.\")\n     \
    \       else:\n                return self**b\n\n\"\"\"\n\u521D\u7B49\u7684\n\"\
    \"\"\ndef Modulo_Inverse_List(M:int,K:int):\n    \"\"\"\n    1^(-1), 2^(-1), ...\
    \ , K^(-1) (mod N) \u306E\u30EA\u30B9\u30C8\u3092\u51FA\u529B\u3059\u308B.\n\n\
    \    [\u5165\u529B]\n    M,K:\u6574\u6570\n    M>0, K>=1\n    K=min(M-1,K) \u306B\
    \u5909\u63DB\u3055\u308C\u308B.\n\n    [\u51FA\u529B]\n    \u9577\u3055 K+1 \u306E\
    \u30EA\u30B9\u30C8 F\n    k=1,2,...,K \u306B\u5BFE\u3057\u3066, F[k]=k^(-1) mod\
    \ M\n    \u307E\u305F, k^(-1) mod M \u304C\u5B58\u5728\u3057\u306A\u3044\u5834\
    \u5408, F[k]=None\n    \"\"\"\n\n    assert M>0 and K>=1\n\n    if K==None:\n\
    \        K=M-1\n    K=min(K,M-1)\n\n    F=[None,Modulo(1,M)]\n    for k in range(2,K+1):\n\
    \        q,r=divmod(M,k)\n        if F[r]!=None:\n            F.append(-q*F[r])\n\
    \        else:\n            F.append(None)\n    return F\n\n#\u7D30\u5206\u5316\
    \ndef Subdivision(X:Modulo,M:int):\n    \"\"\" X \u3092x (mod M) \u306E\u5F62\u306B\
    \u7D30\u5206\u5316\u3059\u308B.\n\n    X.n | M\u3067\u306A\u304F\u3066\u306F\u306A\
    \u3089\u306A\u3044.\n    \"\"\"\n\n    assert M%X.n==0,\"X.n | M \u3067\u306F\u3042\
    \u308A\u307E\u305B\u3093.\"\n\n    k=M//X.n\n    return [Modulo(X.n*i+X.a,M) for\
    \ i in range(k)]\n\n#\u9000\u5316\ndef Degenerate(X:Modulo, M:int):\n    \"\"\"\
    \ X \u306E\u60C5\u5831\u3092\u9000\u5316\u3055\u305B\u308B. X=x (mod N) \u3067\
    \u3042\u308B\u3068\u304D, mod M \u3067\u306E\u60C5\u5831\u306B\u9000\u5316\u3055\
    \u305B\u308B.\n\n    M | X.n \u3067\u306A\u304F\u3066\u306F\u306A\u3089\u306A\u3044\
    .\n    \"\"\"\n\n    assert X.n%M==0,\"M | X.n \u3067\u306F\u3042\u308A\u307E\u305B\
    \u3093.\"\n    return Modulo(X.a%M,M)\n\ndef Chinese_Remainder(X: Modulo):\n \
    \   \"\"\" \u4E2D\u56FD\u5270\u4F59\u5B9A\u7406\u306B\u3088\u308A, X\u3092\u5206\
    \u89E3\u3059\u308B.\n\n    \"\"\"\n\n    Y=[]\n\n    a,N=X.a,X.n\n    e=(N&(-N)).bit_length()-1\n\
    \    if e>0:\n        N>>=e\n        Y.append(Modulo(a,1<<e))\n\n    e=0\n   \
    \ while N%3==0:\n        e+=1\n        N//=3\n\n    if e>0:\n        Y.append(Modulo(a,pow(3,e)))\n\
    \n    flag=0\n    p=5\n    while p*p<=N:\n        if N%p==0:\n            e=0\n\
    \            while N%p==0:\n                e+=1\n                N//=p\n\n  \
    \          Y.append(Modulo(a,pow(p,e)))\n\n        p+=2+2*flag\n        flag^=1\n\
    \n    if N>1:\n        Y.append(Modulo(a,N))\n\n    return Y\n    \n\"\"\"\n\u7DDA\
    \u5F62\u5408\u540C\u65B9\u7A0B\u5F0F\u95A2\u9023\n\"\"\"\n#\u6CD5\u306E\u5408\u6210\
    \ndef __modulo_composite__(p:Modulo,q:Modulo):\n    \"\"\"2\u3064\u306E\u7B49\u5F0F\
    \ x \u2261 p.a (mod p.n), x \u2261 q.a (mod q.n) \u3092\u3068\u3082\u306B\u6E80\
    \u305F\u3059 x \u3092\u5168\u3066\u6C42\u3081\u308B.\n    \"\"\"\n    from math\
    \ import gcd\n\n    a,n=p.a,p.n\n    b,m=q.a,q.n\n\n    d=b-a\n\n    g,h=n,m\n\
    \    while h:\n        g,h=h,g%h\n\n    if d%g:\n        return None\n       \
    \ #raise Modulo_Error(\"{}\u3068{}\u306F\u4E21\u7ACB\u3057\u307E\u305B\u3093.\"\
    .format(p,q))\n\n    n//=g;m//=g;d//=g\n\n    s=(1/Modulo(n,m)).a\n\n    return\
    \ Modulo(a+(n*g)*d*s,n*m*g)\n\ndef Modulo_Composite(*X: Modulo):\n    \"\"\" N\u500B\
    \u306E\u65B9\u7A0B\u5F0F x \u2261 a (mod n) \u3092\u5168\u3066\u6E80\u305F\u3059\
    \ x \u3092 mod \u306E\u5F62\u3067\u6C42\u3081\u308B.\n    \"\"\"\n    x=Modulo(0,1)\n\
    \    for a in X:\n        x=__modulo_composite__(x,a)\n    return x\n\ndef Is_Included(X:\
    \ Modulo, Y: Modulo):\n    \"\"\" X \u3092\u5168\u3066\u6E80\u305F\u3059\u6574\
    \u6570\u306F Y \u3092\u5168\u3066\u6E80\u305F\u3059\u304B?\n\n    X,Y: Modulo\n\
    \    \"\"\"\n    a,p=X.a,X.n\n    b,q=Y.a,Y.n\n    return (a-b)%q==0 and p%q==0\n\
    \n#\u62E1\u5F35Euclid\u306E\u4E92\u9664\u6CD5\ndef Extended_Euclid(a: int, b:\
    \ int):\n    \"\"\"ax+by=gcd(a,b) \u3092\u6E80\u305F\u3059(x,y,gcd(a,b))\u3092\
    1\u3064\u6C42\u3081\u308B.\n\n    a,b:\u6574\u6570\n    \"\"\"\n    s,t,u,v=1,0,0,1\n\
    \    while b:\n        q,a,b=a//b,b,a%b\n        s,t=t,s-q*t\n        u,v=v,u-q*v\n\
    \    return s,u,a\n\n#1\u6B21\u5408\u540C\u65B9\u7A0B\u5F0F\u3092\u89E3\u304F\n\
    def First_Order_Congruent_Equation(a: int, b: int, m: int):\n    \"\"\"1\u6B21\
    \u5408\u540C\u65B9\u7A0B\u5F0F ax\u2261b (mod m) \u3092\u6C42\u3081\u308B.\n\n\
    \    a,b,m:\u6574\u6570\n    m!=0\n    \"\"\"\n    assert m\n    g=a;h=m\n   \
    \ while h:\n        g,h=h,g%h\n\n    if b%g:\n        return None\n\n    a,b,m=a//g,b//g,m//g\n\
    \    c,_,_=Extended_Euclid(a,m)\n    return Modulo(b*c,m)\n\n#1\u6B21\u9023\u7ACB\
    \u5408\u540C\u65B9\u7A0B\u5F0F\u3092\u89E3\u304F\ndef First_Order_Simultaneous_Congruent_Equation(*X):\n\
    \    \"\"\"1\u6B21\u5408\u540C\u65B9\u7A0B\u5F0F a_i x\u2261b_i (mod m_i) \u3092\
    \u6C42\u3081\u308B.\n\n    [Input]\n    X:(a,b,m) \u3068\u3044\u3046\u5F62\u306E\
    \u30BF\u30D7\u30EB\n    \"\"\"\n    R=Modulo(0,1)\n    for (a,b,m) in X:\n   \
    \     T=First_Order_Congruent_Equation(a,b,m)\n        if T==None:\n         \
    \   return None\n        R=__modulo_composite__(R,T)\n    return R\n\n\"\"\"\n\
    \u6709\u9650\u4F53\u306E\u64CD\u4F5C\u95A2\u9023\n\"\"\"\n#\u30EB\u30B8\u30E3\u30F3\
    \u30C9\u30EB\u8A18\u53F7\ndef Legendre(X):\n    \"\"\"\u30EB\u30B8\u30E3\u30F3\
    \u30C9\u30EB\u8A18\u53F7(a/p)\u3092\u8FD4\u3059.\n\n    \u203B\u6CD5\u304C\u7D20\
    \u6570\u306E\u3068\u304D\u306E\u307F\u6210\u7ACB\u3059\u308B.\n    \"\"\"\n\n\
    \    if X==0:\n        return 0\n    elif pow(X,(X.n-1)//2)==1:\n        return\
    \ 1\n    else:\n        return -1\n\n#\u6839\u53F7\ndef sqrt(X, All=False):\n\
    \    \"\"\" X=a (mod p) \u306E\u3068\u304D, r*r=a (mod p) \u3092\u6E80\u305F\u3059\
    \ r \u3092 (\u5B58\u5728\u3059\u308C\u3070) \u8FD4\u3059.\n\n    [Input]\n   \
    \ All: False \u306A\u3089\u3070\u4E00\u65B9\u306E\u307F, True \u306A\u3089\u3070\
    \u4E21\u65B9\n    \u203B \u6CD5 p \u304C\u7D20\u6570\u306E\u3068\u304D\u306E\u307F\
    \u6709\u52B9\n    \u203B \u5B58\u5728\u3057\u306A\u3044\u3068\u304D\u306F None\
    \ \u304C\u8FD4\u308A\u5024\n    \"\"\"\n    if Legendre(X)==-1:\n        return\
    \ None\n\n    a,p=X.a,X.n\n\n    if X==0:\n        return X\n    elif p==2:\n\
    \        return X\n    elif p%8==3 or p%8==7:\n        r=pow(X,(p+1)//4)\n   \
    \     if All:\n            return (r,-r)\n        else:\n            return r\n\
    \    elif p%8==5:\n        if pow(X,(p-1)//4)==1:\n            r=pow(X,(p+3)//8)\n\
    \        else:\n            r=pow(2,(p-1)//4,p)*pow(X,(p+3)//8)\n\n        if\
    \ All:\n            return (r,-r)\n        else:\n            return r\n\n   \
    \ from random import randint as ri\n    u=2\n    s=1\n    while (p-1)%(2*u)==0:\n\
    \        u*=2\n        s+=1\n    q=(p-1)//u\n\n    z=Modulo(0,p)\n    while pow(z,(p-1)//2)!=-1:\n\
    \        z=Modulo(ri(1,p-1),p)\n\n    m,c,t,r=s,z**q,X**q,pow(X,(q+1)//2)\n  \
    \  while m>1:\n        if pow(t,2**(m-2))==1:\n            c=c*c\n           \
    \ m=m-1\n        else:\n            c,t,r,m=c*c,c*c*t,c*r,m-1\n\n    if All:\n\
    \        return (r,-r)\n    else:\n        return r\n\n#\u96E2\u6563\u5BFE\u6570\
    \ndef Discrete_Log(A,B):\n    \"\"\" A^X=B (mod M) \u3092\u6E80\u305F\u3059\u6700\
    \u5C0F\u306E\u975E\u8CA0\u6574\u6570 X \u3092\u6C42\u3081\u308B.\n\n    [\u5165\
    \u529B]\n    A:\u5E95\n    B:\n    [\u51FA\u529B]\n    A^X=B (mod M)\u3092\u6E80\
    \u305F\u3059\u975E\u8CA0\u6574\u6570X\u304C\u5B58\u5728\u3059\u308C\u3070\u305D\
    \u306E\u4E2D\u3067\u6700\u5C0F\u306E\u3082\u306E\n    \u5B58\u5728\u3057\u306A\
    \u3051\u308C\u3070-1\n    \"\"\"\n\n    if isinstance(B,int):\n        B%=A.n\n\
    \    elif isinstance(B,Modulo):\n        assert A.n==B.n,\"A,B\u306E\u6CD5\u304C\
    \u9055\u3044\u307E\u3059.\"\n        B=B.a\n    else:\n        raise TypeError\n\
    \n    A,M=A.a,A.n\n\n    #A=0\u306E\u6642\u3092\u51E6\u7406\n    if M==1:\n  \
    \      return 0\n    if B==1:\n        return 0\n    if A==B==0:\n        return\
    \ 1\n\n    D={1:0}\n    S=int(M**0.5)+2\n\n    #Baby-Step\n    Baby=1\n    for\
    \ i in range(S):\n        if Baby==B:\n            return i\n        D[(Baby*B)%M]=i\n\
    \        Baby=(Baby*A)%M\n\n    #Giant-Step\n    Giant=1\n    H=pow(A,S,M)\n \
    \   for i in range(1,S+1):\n        Giant=(Giant*H)%M\n        if Giant in D:\n\
    \            j=D[Giant]\n            X=i*S-j\n            return X if pow(A,X,M)==B\
    \ else None\n    return None\n\ndef Order(X):\n    \"\"\" X \u306E\u4F4D\u6570\
    \u3092\u6C42\u3081\u308B. \u3064\u307E\u308A, X^k=[1] \u3092\u6E80\u305F\u3059\
    \u6700\u5C0F\u306E\u6B63\u6574\u6570 k \u3092\u6C42\u3081\u308B.\n    \"\"\"\n\
    \    phi=1\n    N=X.n\n\n    e=(N&(-N)).bit_length()-1\n    if e>0:\n        phi=1<<(e-1)\n\
    \        N>>=e\n    else:\n        phi=1\n\n    e=0\n    while N%3==0:\n     \
    \   e+=1\n        N//=3\n\n    if e>0:\n        phi*=pow(3,e-1)*2\n\n    flag=0\n\
    \    p=5\n    while p*p<=N:\n        if N%p==0:\n            e=0\n           \
    \ while N%p==0:\n                e+=1\n                N//=p\n\n            phi*=pow(p,e-1)*(p-1)\n\
    \n        p+=2+2*flag\n        flag^=1\n\n    if N>1:\n        phi*=N-1\n\n  \
    \  a=float(\"inf\")\n    k=1\n    while k*k<=phi:\n        if phi%k==0:\n    \
    \        if k<a and pow(X,k)==1:\n                a=k\n                break\n\
    \n            if phi//k<a and pow(X,phi//k)==1:\n                a=phi//k\n  \
    \      k+=1\n\n    return a\n\ndef Primitive_Root(p):\n    \"\"\" Z/pZ \u4E0A\u306E\
    \u539F\u59CB\u6839\u3092\u898B\u3064\u3051\u308B\n\n    p: \u7D20\u6570\n    \"\
    \"\"\n    if p==2:\n        return 1\n    if p==998244353:\n        return 3\n\
    \    if p==10**9+7:\n        return 5\n    if p==163577857:\n        return 23\n\
    \    if p==167772161:\n        return 3\n    if p==469762049:\n        return\
    \ 3\n\n    fac=[]\n    q=2\n    v=p-1\n\n    while v>=q*q:\n        e=0\n    \
    \    while v%q==0:\n            e+=1\n            v//=q\n\n        if e>0:\n \
    \           fac.append(q)\n        q+=1\n\n    if v>1:\n        fac.append(v)\n\
    \n    g=2\n    while g<p:\n        if pow(g,p-1,p)!=1:\n            return None\n\
    \n        flag=True\n        for q in fac:\n            if pow(g,(p-1)//q,p)==1:\n\
    \                flag=False\n                break\n\n        if flag:\n     \
    \       return g\n\n        g+=1\n\nMod=10**9+7\nX=Modulo(3,Mod)\nY=Modulo(193,Mod)\n\
    \n\"\"\"\n\u6570\u3048\u4E0A\u3052\u95A2\u9023\n\"\"\"\ndef Factor_Modulo(N,Mod,Mode=0):\n\
    \    \"\"\"\n    Mode=0: N! (mod Mod) \u3092\u6C42\u3081\u308B.\n    Mode=1: k!\
    \ (mod Mod) (k=0,1,...,N) \u306E\u30EA\u30B9\u30C8\u3082\u51FA\u529B\u3059\u308B\
    .\n\n    [\u8A08\u7B97\u91CF]\n    O(N)\n    \"\"\"\n\n    if Mode==0:\n     \
    \   X=1\n        for k in range(1,N+1):\n            X*=k; X%=Mod\n        return\
    \ Modulo(X,Mod)\n    else:\n        L=[Modulo(1,Mod)]*(N+1)\n        for k in\
    \ range(1,N+1):\n            L[k]=k*L[k-1]\n        return L\n\ndef Factor_Modulo_with_Inverse(N,\
    \ Mod):\n    \"\"\" k=0,1,...,N \u306B\u5BFE\u3059\u308B k! (mod Mod) \u3068 (k!)^(-1)\
    \ (mod Mod) \u306E\u30EA\u30B9\u30C8\u3092\u51FA\u529B\u3059\u308B.\n\n    [\u5165\
    \u529B]\n    N, Mod: \u6574\u6570\n    Mod >0\n    [\u51FA\u529B]\n    \u9577\u3055\
    \ N+1 \u306E\u30EA\u30B9\u30C8\u306E\u30BF\u30D7\u30EB (F,G): F[k]=k! (mod M),\
    \ G[k]=(k!)^(-1) (mod M)\n    [\u8A08\u7B97\u91CF]\n    O(N+log Mod)\n    \"\"\
    \"\n\n    assert Mod>0\n\n    F=Factor_Modulo(N,Mod,Mode=1)\n    G=[0]*(N+1)\n\
    \n    G[-1]=F[-1].inverse()\n    for k in range(N,0,-1):\n        G[k-1]=k*G[k]\n\
    \    return F,G\n\ndef Binomial_Coefficient_Modulo(n: int, r: int, Mod:int):\n\
    \    \"\"\" nCr (mod Mod) \u3092\u611A\u76F4\u306A\u65B9\u6CD5\u3067\u6C42\u3081\
    \u308B.\n\n    [\u5165\u529B]\n    n, r, Mod: \u6574\u6570\n    Mod>0\n    [\u51FA\
    \u529B]\n    nCr (mod Mod)\n    [\u8A08\u7B97\u91CF]\n    O(r)\n    \"\"\"\n \
    \   assert Mod>0\n    if r<0 or n<r:\n        return Modulo(0,Mod)\n\n    X=Y=1\n\
    \n    r=min(r,n-r)\n    for i in range(r):\n        X*=n-i; X%=Mod\n        Y*=r-i;\
    \ Y%=Mod\n    return Modulo(X,Mod)/Modulo(Y,Mod)\n\ndef Binomial_Coefficient_Modulo_List(n:int,\
    \ Mod:int):\n    \"\"\" n \u3092\u56FA\u5B9A\u3057, r=0,1,...,n \u3068\u3057\u305F\
    \u3068\u304D\u306E nCr (mod Mod) \u306E\u30EA\u30B9\u30C8\u3092\u51FA\u529B\u3059\
    \u308B.\n\n    [\u5165\u529B]\n    n,Mod: \u6574\u6570\n    Mod>0\n    [\u51FA\
    \u529B]\n    [nC0 (mod Mod), nC1 (mod Mod),..., nCn (mod Mod)]\n    [\u8A08\u7B97\
    \u91CF]\n    O(n)\n    \"\"\"\n\n    assert Mod>0\n    L=[Modulo(1,Mod) for _\
    \ in range(n+1)]\n\n    I=Modulo_Inverse_List(Mod,n)\n    for r in range(1,n+1):\n\
    \        L[r]=(n+1-r)*I[r]*L[r-1]\n    return L\n\ndef Pascal_Triangle(N,M):\n\
    \    \"\"\"\n    0<=n<=N, 0<=r<=n \u306E\u5168\u3066\u306B\u5BFE\u3057\u3066 nCr\
    \ (mod M) \u306E\u30EA\u30B9\u30C8\u3092\u51FA\u529B\u3059\u308B.\n\n    [\u5165\
    \u529B]\n    N,M:\u6574\u6570\n    M>0\n    [\u51FA\u529B] (mod M) \u3092\u7701\
    \u7565.\n    [[0C0], [1C0, 1C1], ... , [nC0, ... , nCn], ..., [NC0, ..., NCN]]\n\
    \    [\u8A08\u7B97\u91CF]\n    O(N^2)\n    \"\"\"\n\n    X=[Modulo(1,M)]\n   \
    \ L=[[Modulo(1,M)]]\n    for n in range(N):\n        Y=[Modulo(1,M)]\n       \
    \ for k in range(1,n+1):\n            Y.append(X[k]+X[k-1])\n        Y.append(Modulo(1,M))\n\
    \        X=Y\n        L.append(Y)\n    return L\n"
  dependsOn: []
  isVerificationFile: false
  path: Modulo.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Modulo.py
layout: document
redirect_from:
- /library/Modulo.py
- /library/Modulo.py.html
title: Modulo.py
---
