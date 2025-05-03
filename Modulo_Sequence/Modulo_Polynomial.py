class Modulo_Polynomial:
    __slots__= ("poly", "max_degree")

    def __init__(self, poly: list[int] = None, max_degree: int = 2 * 10 ** 5):
        """ 多項式を定義する (各係数の法 Mod はグローバル変数から指定する).

        Args:
            poly (list[int], optional): 係数のリスト. 第 d 要素は d 次の係数を表す. None のときは [0] と同義. Defaults to None.
            max_degree (int, optional): (mod X^n) を考えるときの n. Defaults to 2*10**5.
        """

        if poly is None:
            poly = [0]

        self.poly: list[int] = [a % Mod for a in poly[:max_degree]]
        self.max_degree = max_degree

    def __str__(self) -> str:
        return str(self.poly)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.poly})"

    def __iter__(self):
        yield from self.poly

    def __eq__(self, other: "Modulo_Polynomial") -> bool:
        from itertools import zip_longest
        return all([a == b for a, b in zip_longest(self.poly, other.poly, fillvalue = 0)])

    #+,-
    def __pos__(self) -> "Modulo_Polynomial":
        return self

    def __neg__(self) -> "Modulo_Polynomial":
        return self.scale(-1)

    #items
    def __getitem__(self, index):
        if isinstance(index, slice):
            return Modulo_Polynomial(self.poly[index], self.max_degree)
        else:
            if index<0:
                raise IndexError(f"index is negative (index: {index})")
            elif index>=len(self.poly):
                return 0
            else:
                return self.poly[index]

    def __setitem__(self, index, value):
        if index<0:
            raise IndexError(f"index is negative (index: {index})")
        elif index>=self.max_degree:
            return

        if index>=len(self.poly):
            self.poly+=[0]*(index-len(self.poly)+1)
        self.poly[index]=value%Mod

    #Boole
    def __bool__(self) -> bool:
        return any(self.poly)

    #簡略化
    def reduce(self):
        """ 先頭の 0 を削除する.
        """

        poly = self.poly
        while poly and (poly[-1] == 0):
            poly.pop()


    #シフト
    def __lshift__(self, depth: int) -> "Modulo_Polynomial":
        if depth < 0:
            return self >> (-depth)

        if depth > self.max_degree:
            return Modulo_Polynomial([0], self.max_degree)

        return Modulo_Polynomial([0] * depth + self.poly, self.max_degree)

    def __rshift__(self, depth: int) -> "Modulo_Polynomial":
        if depth < 0:
            return  self << (-depth)

        return Modulo_Polynomial(self.poly[depth:], self.max_degree)

    #次数
    def degree(self) -> int:
        """ この多項式の次数を求める.

        Returns:
            int: 次数 (係数が 0 ではない最大次数)
        """

        for d in range(len(self.poly) - 1, -1, -1):
            if self.poly[d]:
                return d
        else:
            return -float("inf")

    #加法
    def __add__(self, other) -> "Modulo_Polynomial":
        P=self; Q=other

        if Q.__class__==Modulo_Polynomial:
            N=min(P.max_degree,Q.max_degree)
            A=P.poly; B=Q.poly
        else:
            N=P.max_degree
            A=P.poly; B=Q
        return Modulo_Polynomial(Calc.add(A, B), N)

    def __radd__(self, other) -> "Modulo_Polynomial":
        return self+other

    #減法
    def __sub__(self, other) -> "Modulo_Polynomial":
        P=self; Q=other
        if Q.__class__==Modulo_Polynomial:
            N=min(P.max_degree,Q.max_degree)
            A=P.poly; B=Q.poly
        else:
            N=P.max_degree
            A=P.poly; B=Q
        return Modulo_Polynomial(Calc.sub(A, B), N)

    def __rsub__(self, other) -> "Modulo_Polynomial":
        return (-self) + other

    #乗法
    def __mul__(self, other) -> "Modulo_Polynomial":
        P=self
        Q=other
        if Q.__class__==Modulo_Polynomial:
            a=b=0
            for x in P.poly:
                if x:
                    a+=1
            for y in Q.poly:
                if y:
                    b+=1

            if a>b:
                P,Q=Q,P

            P.reduce();Q.reduce()
            U,V=P.poly,Q.poly
            M=min(P.max_degree,Q.max_degree)
            if a<2*P.max_degree.bit_length():
                B=[0]*(len(U)+len(V)-1)
                for i in range(len(U)):
                    if U[i]:
                        for j in range(len(V)):
                            B[i+j]+=U[i]*V[j]
                            if B[i+j]>Mod:
                                B[i+j]-=Mod
            else:
                B=Calc.convolution(U,V)[:M]
            B=Modulo_Polynomial(B,M)
            B.reduce()
            return B
        else:
            return self.scale(other)

    def __rmul__(self, other) -> "Modulo_Polynomial":
        return self.scale(other)

    #除法
    def __floordiv__(self, other) -> "Modulo_Polynomial":
        if not other:
            raise ZeroDivisionError
        if isinstance(other,int):
            return self/other

        self.reduce()
        other.reduce()

        return Modulo_Polynomial(Calc.flood_div(self.poly, other.poly), max(self.max_degree, other.max_degree))

    def __rfloordiv__(self, other) -> "Modulo_Polynomial":
        if not self:
            raise ZeroDivisionError

        if isinstance(other,int):
            return Modulo_Polynomial([],self.max_degree)

    #剰余
    def __mod__(self, other) -> "Modulo_Polynomial":
        if not other:
            return ZeroDivisionError
        self.reduce(); other.reduce()
        r = Modulo_Polynomial(Calc.mod(self.poly, other.poly), min(self.max_degree, other.max_degree))
        r.reduce()
        return r

    def __rmod__(self, other) -> "Modulo_Polynomial":
        if not self:
            raise ZeroDivisionError
        r=other-(other//self)*self
        r.reduce()
        return r

    def __divmod__(self, other) -> tuple["Modulo_Polynomial", "Modulo_Polynomial"]:
        q=self//other
        r=self-q*other; r.reduce()
        return (q,r)

    #累乗
    def __pow__(self, other) -> "Modulo_Polynomial":
        if other.__class__==int:
            n=other
            m=abs(n)

            Q=self
            A=Modulo_Polynomial([1],self.max_degree)
            while m>0:
                if m&1:
                    A*=Q
                m>>=1
                Q*=Q

            if n>=0:
                return A
            else:
                return A.inverse()
        else:
            P=Log(self)
            return Exp(P*other)

    def inverse(self, deg: int = None) -> "Modulo_Polynomial":
        """ この多項式の (mod X^d) での逆元を求める.

        Args:
            deg (int, optional): 逆元の精度 ((mod X^d) の逆元を求める際の d) を指定する. None のときは元の多項式の精度をそのまま採用. Defaults to None.

        Returns:
            Modulo_Polynomial: _description_
        """
        assert self.poly[0], "定数項が0"

        if deg is None:
            deg = self.max_degree

        return Modulo_Polynomial(Calc.inverse(self.poly, deg), self.max_degree)

    #除法
    def __truediv__(self, other) -> "Modulo_Polynomial":
        if isinstance(other, Modulo_Polynomial):
            if Calc.is_sparse(other.poly):
                d,f=Calc.coefficients_list(other.poly)
                K=len(d)
                H=[0]*self.max_degree

                alpha=pow(other[0], -1, Mod)
                H[0]=alpha*self[0]%Mod

                for i in range(1, self.max_degree):
                    c=0
                    for j in range(1, K):
                        if d[j]<=i:
                            c+=f[j]*H[i-d[j]]%Mod
                        else:
                            break
                    c%=Mod
                    H[i]=alpha*(self[i]-c)%Mod
                H=Modulo_Polynomial(H, min(self.max_degree, other.max_degree))
                return H
            else:
                return self*other.inverse()
        else:
            return pow(other, -1, Mod)*self

    def __rtruediv__(self, other: "Modulo_Polynomial") -> "Modulo_Polynomial":
        return other*self.inverse()

    #スカラー倍
    def scale(self, s: int) -> "Modulo_Polynomial":
        """ 多項式に s 倍を掛けた多項式を求める.

        Args:
            s (int): スカラー倍の係数

        Returns:
            Modulo_Polynomial: s 倍した多項式
        """

        return Modulo_Polynomial(Calc.times(self.poly,s), self.max_degree)

    #最高次の係数
    def leading_coefficient(self) -> int:
        """ 最高次の係数を求める

        Returns:
            int: 最高次の係数 (0 多項式の返り値は 0 とする)
        """

        for a in self.poly[::-1]:
            if a:
                return a
        else:
            return 0

    def censor(self, m: int = None):
        """ m 次以降の係数を切り捨てる.

        Args:
            m (int, optional): 切り捨てる精度. Defaults to None.
        """

        if m is None:
            m = self.max_degree

        m = min(m, self.max_degree)
        self.poly[:m]

    def resize(self, m: int):
        """ この多項式の情報を持っている配列の長さを m にする (短い場合は末尾に 0 を追加し, 長い場合は m 次以上を切り捨てる).

        Args:
            m (int): 次数
        """
        m = min(m, self.max_degree)
        if len(self.poly) > m:
            del self.poly[:m]
        elif len(self.poly) < m:
            self.poly.extend([0] * (m - len(self.poly)))

    #代入
    def substitution(self, a: int) -> int:
        """ 多項式の変数に a を形式的に代入した式の値を求める.

        Args:
            a (int): 代入する値

        Returns:
            int: 式の値
        """

        y = 0
        a_pow = 1
        for p in self.poly:
            y += p * a_pow % Mod
            a_pow = (a_pow * a) % Mod
        return y % Mod

    def order(self, default: int = None) -> int:
        """ この形式的ベキ級数の位数 (係数が 0 でない次数のうちの最低次数) を求める.

        Args:
            default (int, optional): ゼロ多項式の返り値. Defaults to None.

        Returns:
            int: 位数
        """

        for d in range(len(self.poly)):
            if self.poly[d]:
                return d
        else:
            return default

#=================================================
class Calculator:
    def __init__(self):
        self.primitive = self.__primitive_root()
        self.__build_up()

    def __primitive_root(self) -> int:
        """ Mod の原始根を求める.

        Returns:
            int: Mod の原始根
        """

        p = Mod
        if p == 2:
            return 1
        if p == 998244353:
            return 3
        if p == 10**9 + 7:
            return 5
        if p == 163577857:
            return 23
        if p == 167772161:
            return 3
        if p == 469762049:
            return 3

        fac=[]
        q=2
        v=p-1

        while v>=q*q:
            e=0
            while v%q==0:
                e+=1
                v//=q

            if e>0:
                fac.append(q)
            q+=1

        if v>1:
            fac.append(v)

        for g in range(2, p):
            if pow(g, p-1, p) != 1:
                return None

            flag=True
            for q in fac:
                if pow(g, (p-1) // q, p) == 1:
                    flag = False
                    break

            if flag:
                return g

    #参考元: https://judge.yosupo.jp/submission/72676
    def __build_up(self):
        rank2=(~(Mod-1) & ((Mod-1)-1)).bit_length()
        root=[0]*(rank2+1); iroot=[0]*(rank2+1)
        rate2=[0]*max(0, rank2-1); irate2=[0]*max(0, rank2-1)
        rate3=[0]*max(0, rank2-2); irate3=[0]*max(0, rank2-2)

        root[-1]=pow(self.primitive, (Mod-1)>>rank2, Mod)
        iroot[-1]=pow(root[-1], -1, Mod)

        for i in range(rank2)[::-1]:
            root[i]=root[i+1]*root[i+1]%Mod
            iroot[i]=iroot[i+1]*iroot[i+1]%Mod

        prod=iprod=1
        for i in range(rank2-1):
            rate2[i]=root[i+2]*prod%Mod
            irate2[i]=iroot[i+2]*prod%Mod
            prod*=iroot[i+2]; prod%=Mod
            iprod*=root[i+2]; iprod%=Mod

        prod=iprod = 1
        for i in range(rank2-2):
            rate3[i]=root[i + 3]*prod%Mod
            irate3[i]=iroot[i + 3]*iprod%Mod
            prod*=iroot[i + 3]; prod%=Mod
            iprod*=root[i + 3]; iprod%=Mod

        self.root=root; self.iroot=iroot
        self.rate2=rate2; self.irate2=irate2
        self.rate3=rate3; self.irate3=irate3

    def add(self, A: list[int] | int, B: list[int] | int) -> list[int]:
        """ 必要ならば末尾に元を追加して, [A[i] + B[i]] を求める.

        """

        if type(A) == list:
            pass
        elif type(A) == int:
            A = [A]
        else:
            raise NotImplementedError

        if type(B) == list:
            pass
        elif type(B) == int:
            B = [B]
        else:
            raise NotImplementedError

        m = min(len(A), len(B))
        C = [(A[i] + B[i]) %Mod for i in range(m)]
        C.extend(A[m:])
        C.extend(B[m:])
        return C

    def sub(self, A: list[int] | int, B: list[int] | int) -> list[int]:
        """ 必要ならば末尾に元を追加して, [A[i] - B[i]] を求める.

        """

        if type(A) == list:
            pass
        elif type(A) == int:
            A = [A]
        else:
            raise NotImplementedError

        if type(B) == list:
            pass
        elif type(B) == int:
            B = [B]
        else:
            raise NotImplementedError

        m = min(len(A), len(B))
        C = [(A[i] - B[i]) % Mod for i in range(m)]
        C.extend(A[m:])
        C.extend([-b % Mod for b in B[m:]])
        return C

    def times(self, A: list[int], k: int) -> list[int]:
        """ [k * A[i]] を求める.

        """
        return [k * a % Mod for a in A]

    #参考元 https://judge.yosupo.jp/submission/72676
    def ntt(self, A: list[int]):
        """ A に Mod を法とする数論変換を施す

        ※ Mod はグローバル変数から指定

        References:
        https://github.com/atcoder/ac-library/blob/master/atcoder/convolution.hpp
        https://judge.yosupo.jp/submission/72676
        """

        N=len(A)
        H=(N-1).bit_length()
        l=0

        I=self.root[2]
        rate2=self.rate2; rate3=self.rate3

        while l<H:
            if H-l==1:
                p=1<<(H-l-1)
                rot=1
                for s in range(1<<l):
                    offset=s<<(H-l)
                    for i in range(p):
                        x=A[i+offset]; y=A[i+offset+p]*rot%Mod
                        A[i+offset]=(x+y)%Mod
                        A[i+offset+p]=(x-y)%Mod

                    if s+1!=1<<l:
                        rot*=rate2[(~s&-~s).bit_length()-1]
                        rot%=Mod
                l+=1
            else:
                p=1<<(H-l-2)
                rot=1
                for s in range(1<<l):
                    rot2=rot*rot%Mod
                    rot3=rot2*rot%Mod
                    offset=s<<(H-l)
                    for i in range(p):
                        a0=A[i+offset]
                        a1=A[i+offset+p]*rot
                        a2=A[i+offset+2*p]*rot2
                        a3=A[i+offset+3*p]*rot3

                        alpha=(a1-a3)%Mod*I

                        A[i+offset]=(a0+a2+a1+a3)%Mod
                        A[i+offset+p]=(a0+a2-a1-a3)%Mod
                        A[i+offset+2*p]=(a0-a2+alpha)%Mod
                        A[i+offset+3*p]=(a0-a2-alpha)%Mod

                    if s+1!=1<<l:
                        rot*=rate3[(~s&-~s).bit_length()-1]
                        rot%=Mod
                l+=2

    #参考元 https://judge.yosupo.jp/submission/72676
    def inverse_ntt(self, A):
        """ A を Mod を法とする逆数論変換を施す

        ※ Mod はグローバル変数から指定

        References:
        https://github.com/atcoder/ac-library/blob/master/atcoder/convolution.hpp
        https://judge.yosupo.jp/submission/72676
        """
        N=len(A)
        H=(N-1).bit_length()
        l=H

        J=self.iroot[2]
        irate2=self.rate2; irate3=self.irate3

        while l:
            if l==1:
                p=1<<(H-l)
                irot=1
                for s in range(1<<(l-1)):
                    offset=s<<(H-l+1)
                    for i in range(p):
                        x=A[i+offset]; y=A[i+offset+p]
                        A[i+offset]=(x+y)%Mod
                        A[i+offset+p]=(x-y)*irot%Mod

                    if s+1!=1<<(l-1):
                        irot*=irate2[(~s&-~s).bit_length()-1]
                        irot%=Mod
                l-=1
            else:
                p=1<<(H-l)
                irot=1
                for s in range(1<<(l-2)):
                    irot2=irot*irot%Mod
                    irot3=irot2*irot%Mod
                    offset=s<<(H-l+2)
                    for i in range(p):
                        a0=A[i+offset]
                        a1=A[i+offset+p]
                        a2=A[i+offset+2*p]
                        a3=A[i+offset+3*p]

                        beta=(a2-a3)*J%Mod

                        A[i+offset]=(a0+a1+a2+a3)%Mod
                        A[i+offset+p]=(a0-a1+beta)*irot%Mod
                        A[i+offset+2*p]=(a0+a1-a2-a3)*irot2%Mod
                        A[i+offset+3*p]=(a0-a1-beta)*irot3%Mod

                    if s+1!=1<<(l-2):
                        irot*=irate3[(~s&-~s).bit_length()-1]
                        irot%=Mod
                l-=2
        N_inv=pow(N, -1, Mod)
        for i in range(N):
            A[i]=N_inv*A[i]%Mod

    def non_zero_count(self, A: list[int]) -> int:
        """ A にある非零要素の個数を求める.

        Args:
            A (list[int]):

        Returns:
            int: 非零要素の個数
        """
        return len(A) - A.count(0)

    def is_sparse(self, A: list[int], threshold: int = 25) -> bool:
        """A が疎かどうかを判定する.

        Args:
            A (list[int]):
            threshold (int, optional): 非零要素の個数が threshold 以下ならば疎と判定する. Defaults to 25.

        Returns:
            bool: 疎?
        """

        return self.non_zero_count(A) <= threshold

    def coefficients_list(self, A: list[int]) -> tuple[list[int], list[int]]:
        """ A にある非零要素のリストを求める.

        Args:
            A (list[int]):

        Returns:
            tuple[list[int], list[int]]: ([d[0], ..., d[k-1]], [f[0], ..., f[k-1]]) の形のリスト.
                j = 0, 1, ..., k - 1 に対して, a[d[j]] = f[j] であることを意味する.
        """

        f = []; d = []
        for i in range(len(A)):
            if A[i] == 0:
                continue

            d.append(i)
            f.append(A[i])
        return d, f

    def convoluton_greedy(self, A: list[int], B: list[int]) -> list[int]:
        """ 畳み込み積 A * B を愚直な方法で求める.

        Args:
            A (list[int]):
            B (list[int]):

        Returns:
            list[int]: 畳み込み積 A * B
        """

        if len(A) < len(B):
            A, B = B, A

        n = len(A)
        m = len(B)
        C = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                C[i + j] += A[i] * B[j] % Mod

        for k in range(n + m - 1):
            C[k] %= Mod

        return C

    def convolution(self, A: list[int], B: list[int]) -> list[int]:
        """ 畳み込み積 A * B を求める.

        Args:
            A (list[int]):
            B (list[int]):

        Returns:
            list[int]: 畳み込み積 A * B
        """

        if (not A) or (not B):
            return []

        N=len(A)
        M=len(B)
        L=M+N-1

        if min(N,M)<=50:
            return self.convoluton_greedy(A, B)

        H=L.bit_length()
        K=1<<H

        A=A+[0]*(K-N)
        B=B+[0]*(K-M)

        self.ntt(A)
        self.ntt(B)

        for i in range(K):
            A[i]=A[i]*B[i]%Mod

        self.inverse_ntt(A)

        return A[:L]

    def autocorrelation(self, A: list[int]) -> list[int]:
        """ 自分自身との畳み込み積を求める.

        Args:
            A (list[int]):

        Returns:
            list[int]: 畳み込み積 A * A
        """

        N=len(A)
        L=2*N-1

        if N<=50:
            C=[0]*L
            for i in range(N):
                for j in range(N):
                    C[i+j]+=A[i]*A[j]
                    C[i+j]%=Mod
            return C

        H=L.bit_length()
        K=1<<H

        A=A+[0]*(K-N)

        self.ntt(A)

        for i in range(K):
            A[i]=A[i]*A[i]%Mod
        self.inverse_ntt(A)

        return A[:L]

    def multiple_convolution(self, *A: list[int]) -> list[int]:
        """ A = (A[0], A[1], ..., A[k - 1]) に対して, この k 個の畳み込み積 A[0] * A[1] * ... * A[k - 1] を求める.

        Args:
            A (list[list[int]]): 畳み込む k 個の整数のリスト

        Returns:
            list[int]: k 個の畳み込み積 A[0] * A[1] * ... * A[k - 1]
        """

        from collections import deque

        if not A:
            return [1]

        Q=deque(list(range(len(A))))
        A=list(A)

        while len(Q)>=2:
            i=Q.popleft(); j=Q.popleft()
            A[i]=self.convolution(A[i], A[j])
            A[j]=None
            Q.append(i)

        i=Q.popleft()
        return A[i]

    def inverse(self, F: list[int], length: int = None) -> list[int]:
        """ F * G = [1, 0, 0, ..., 0] (0 が (length - 1) 個) を満たす長さ length のリスト G を求める.

        Args:
            F (list[int]):
            length (int, optional): 求める G の長さ. None のときは length = len(F) とする. Defaults to None.

        Returns:
            list[int]: _description_
        """

        M = len(F) if length is None else length

        if M <= 0:
            return []

        if self.is_sparse(F):
            # 愚直に漸化式を用いて求める.
            # 計算量: F にある係数が非零の項の個数を K, 求める最大次数を N として, O(NK) 時間

            d,f=self.coefficients_list(F)

            G=[0]*M
            alpha=pow(F[0], -1, Mod)
            G[0]=alpha

            for i in range(1, M):
                for j in range(1, len(d)):
                    if d[j]<=i:
                        G[i]+=f[j]*G[i-d[j]]%Mod
                    else:
                        break

                G[i]%=Mod
                G[i]=(-alpha*G[i])%Mod
            del G[M:]
        else:
            # FFTの理論を応用して求める.
            # 計算量: 求めたい項の個数をNとして, O(N log N)
            # Reference: https://judge.yosupo.jp/submission/42413

            N=len(F)
            r=pow(F[0], -1, Mod)

            m=1
            G=[r]
            while m<M:
                A=F[:min(N, 2*m)]; A+=[0]*(2*m-len(A))
                B=G.copy(); B+=[0]*(2*m-len(B))

                Calc.ntt(A); Calc.ntt(B)
                for i in range(2*m):
                    A[i]=A[i]*B[i]%Mod

                Calc.inverse_ntt(A)
                A=A[m:]+[0]*m
                Calc.ntt(A)
                for i in range(2*m):
                    A[i]=-A[i]*B[i]%Mod
                Calc.inverse_ntt(A)

                G.extend(A[:m])
                m<<=1
            G=G[:M]
        return G

    def flood_div(self, F: list[int], G: list[int]) -> list[int]:
        assert F[-1]
        assert G[-1]

        F_deg=len(F)-1
        G_deg=len(G)-1

        if F_deg<G_deg:
            return []

        m=F_deg-G_deg+1
        return self.convolution(F[::-1], Calc.inverse(G[::-1],m))[m-1::-1]

    def mod(self, F: list[int], G: list[int]) -> list[int]:
        while F and F[-1] == 0:
            F.pop()

        while G and G[-1] == 0:
            G.pop()

        if not F:
            return []

        return Calc.sub(F, Calc.convolution(Calc.flood_div(F, G), G))

# 以下 参考元: https://judge.yosupo.jp/submission/28304
def Differentiate(P: Modulo_Polynomial) -> Modulo_Polynomial:
    """ 形式的ベキ級数 P の形式的微分 P' を求める.

    Args:
        P (Modulo_Polynomial): 形式的ベキ級数

    Returns:
        Modulo_Polynomial: 形式的微分 P'
    """

    poly = P.poly
    diff_poly = [(k * poly[k]) % Mod for k in range(1, len(poly))]
    return Modulo_Polynomial(diff_poly, P.max_degree)

def Integrate(P: Modulo_Polynomial, constant: int = 0) -> Modulo_Polynomial:
    """ 形式的ベキ級数 P の形式的な不定積分 Int(P) を求める. ただし, 定数項は constant とする.

    Args:
        P (Modulo_Polynomial): 形式的ベキ級数
        constant (int, optional): 定数項. Defaults to 0.

    Returns:
        Modulo_Polynomial: P の形式的な不定積分
    """

    if not P.poly:
        return Modulo_Polynomial([constant], P.max_degree)

    n = len(P.poly)
    inv = [0] * (n + 1)
    inv[1] = 1
    for x in range(2, n + 1):
        q, r = divmod(Mod, x)
        inv[x] = (-q * inv[r]) % Mod

    integrate_poly = [0] + [(inv[k] * a) % Mod for k, a in enumerate(P.poly,1)]
    return Modulo_Polynomial(integrate_poly, P.max_degree + 1)

# 累乗,指数,対数
def Log(P: Modulo_Polynomial) -> Modulo_Polynomial:
    """ 定数項が 1 である形式的ベキ級数 P の対数 Log(P) を求める.

    Args:
        P (Modulo_Polynomial): 定数項が 1 である形式的ベキ級数

    Raises:
        ValueError: 定数項が 1 でないときに発生

    Returns:
        Modulo_Polynomial: Log(P)
    """

    if P[0] != 1:
        raise ValueError("定数項が 1 ではありません")

    return Integrate(Differentiate(P) / P)

def Exp(P: Modulo_Polynomial) -> Modulo_Polynomial:
    """ 定数項が 0 である形式的ベキ級数 P に対する Exp(P) を求める.

    Args:
        P (Modulo_Polynomial): 定数項が 0 である形式的ベキ級数

    Raises:
        ValueError: 定数項が 0 ではない場合に発生

    Returns:
        Modulo_Polynomial: Exp(P)

    References:
        (1) https://arxiv.org/pdf/1301.5804.pdf
        (2) https://opt-cp.com/fps-fast-algorithms/
    """

    from itertools import zip_longest

    if P[0] != 0:
        raise ValueError("定数項が 0 ではありません")

    n = P.max_degree
    inv = [0] * (2 * n + 1)
    inv[1] = 1
    for x in range(2, 2 * n + 1):
        q, r = divmod(Mod, x)
        inv[x] = (-q * inv[r]) % Mod

    H = P.poly
    H.extend([0] * (n - len(H)))

    # 疎の場合にはそれ専用の処理を行う.
    if Calc.is_sparse(H):
        F = [0] * n
        F[0] = 1

        d, f = Calc.coefficients_list(H)
        K = len(d)

        for t in range(K):
            f[t] = (d[t] * f[t]) %Mod
            d[t] -= 1

        for i in range(1, n):
            a = 0
            for j in range(K):
                if d[j] > i - 1:
                    break

                a += f[j] * F[(i - 1) - d[j]] % Mod

            a %= Mod
            F[i] = a * inv[i] % Mod

        return Modulo_Polynomial(F[:n], P.max_degree)

    dH = [(k * a) % Mod for k, a in enumerate(H[1:], 1)]
    F, G, m = [1], [1], 1

    while m <= n:
        #2.a'
        if m > 1:
            E = Calc.convolution(F, Calc.autocorrelation(G)[:m])[:m]
            G = [(2 * a - b) % Mod for a, b in zip_longest(G, E, fillvalue = 0)]

        #2.b', 2.c'
        C = Calc.convolution(F, dH[:m - 1])
        R = [0] * m
        for i, a in enumerate(C):
            R[i % m] += a
        R = [a % Mod for a in R]

        #2.d'
        dF = [(k * a) % Mod for k, a in enumerate(F[1:], 1)]
        D = [0] + [(a - b) % Mod for a, b in zip_longest(dF, R, fillvalue = 0)]
        S = [0] * m
        for i, a in enumerate(D):
            S[i % m] += a
        S = [a % Mod for a in S]

        #2.e'
        T = Calc.convolution(G, S)[:m]

        #2.f'
        E = [0] * (m - 1) + T
        E = [0] + [(inv[k] * a) % Mod for k, a in enumerate(E, 1)]
        U = [(a - b) % Mod for a, b in zip_longest(H[:2 * m], E, fillvalue = 0)][m:]

        #2.g'
        V = Calc.convolution(F, U)[:m]

        #2.h'
        F.extend(V)

        #2.i'
        m <<= 1

    return Modulo_Polynomial(F[:n], P.max_degree)

def Root(P: Modulo_Polynomial, k: int) -> Modulo_Polynomial:
    """ 定数項が 1 である形式的ベキ級数 P の k 乗根を求める

    Args:
        P (Modulo_Polynomial): 定数項が 1 である形式的ベキ級数
        k (int): Mod の倍数ではない整数

    Raises:
        ValueError: 定数項が 0 でない場合に発生
        ValueError: k が Mod の倍数である場合に発生

    Returns:
        Modulo_Polynomial: Q^k = P, [X^0]Q = 1 を満たす形式的ベキ級数 Q
    """

    if P[0] != 1:
        raise ValueError("定数項が 1 ではありません")

    k %= Mod
    if k == 0:
        raise ValueError("k が特異です")

    return Power(P, pow(k, -1, Mod))


# 三角関数
# 正弦
def Sin(P: Modulo_Polynomial) -> Modulo_Polynomial:
    """ 定数項が 0 である形式的ベキ級数 P に対して, Sin(P) を求める.

    Args:
        P (Modulo_Polynomial): 定数項が 0 である形式的ベキ級数

    Raises:
        ValueError: 定数項が 0 でない場合に発生

    Returns:
        Modulo_Polynomial: Sin(P)
    """

    if P[0] != 0:
        raise ValueError("定数項が 0 ではありません")

    I = Tonelli_Shanks(-1)
    B = I * P
    B_exp = Exp(B)
    C = B_exp - (1 / B_exp)
    return C * pow(2 * I, -1, Mod)

#余弦
def Cos(P: Modulo_Polynomial) -> Modulo_Polynomial:
    """ 定数項が 0 である形式的ベキ級数 P に対して, Cos(P) を求める.

    Args:
        P (Modulo_Polynomial): 定数項が 0 である形式的ベキ級数

    Raises:
        ValueError: 定数項が 0 でない場合に発生

    Returns:
        Modulo_Polynomial: Cos(P)
    """
    if P[0] != 0:
        raise ValueError("定数項が 0 ではありません")

    I = Tonelli_Shanks(-1)
    B = I * P
    B_exp = Exp(B)
    C = B_exp + (1 / B_exp)
    return C * pow(2, -1, Mod)

#正接
def Tan(P: Modulo_Polynomial) -> Modulo_Polynomial:
    """ 定数項が 0 である形式的ベキ級数 P に対して, Tan(P) を求める.

    Args:
        P (Modulo_Polynomial): 定数項が 0 である形式的ベキ級数

    Raises:
        ValueError: 定数項が 0 でない場合に発生

    Returns:
        Modulo_Polynomial: Tan(P)
    """

    if P[0] != 0:
        raise ValueError("定数項が 0 ではありません")

    I = Tonelli_Shanks(-1)
    B = I * P
    B_exp = Exp(B)
    B_sin = (B_exp - 1 / B_exp) * pow(2 * I, -1, Mod)
    B_cos = (B_exp + 1 / B_exp) * pow(2, -1, Mod)
    return B_sin / B_cos

#逆正弦
def ArcSin(P: Modulo_Polynomial) -> Modulo_Polynomial:
    """ 定数項が 0 である形式的ベキ級数に対して, ArcSin(P) を求める.

    Args:
        P (Modulo_Polynomial): 定数項が 0 である形式的ベキ級数

    Raises:
        ValueError: 定数項が 0 でない場合に発生

    Returns:
        Modulo_Polynomial: ArcSin(P)
    """

    if P[0] != 0:
        raise ValueError("定数項が 0 ではありません")

    return Integrate(Differentiate(P) / Sqrt(1 - P * P))

#逆余弦
def ArcCos(P: Modulo_Polynomial) -> Modulo_Polynomial:
    """ 定数項が 0 である形式的ベキ級数に対して, ArcCos(P) を求める. ※ 実際には, ArcCos(0) = pi / 2 であるため, 注意が必要である.

    Args:
        P (Modulo_Polynomial): 定数項が 0 である形式的ベキ級数

    Raises:
        ValueError: 定数項が 0 でない場合に発生

    Returns:
        Modulo_Polynomial: ArcCos(P) の 1 次以降の係数
    """

    if P[0] != 0:
        raise ValueError("定数項が 0 ではありません")

    return -ArcSin(P)

#逆正接
def ArcTan(P: Modulo_Polynomial) -> Modulo_Polynomial:
    """ 定数項が 0 である形式的ベキ級数に対して, ArcTan(P) を求める.
    Args:
        P (Modulo_Polynomial): 定数項が 0 である形式的ベキ級数

    Raises:
        ValueError: 定数項が 0 でない場合に発生

    Returns:
        Modulo_Polynomial: ArcCos(P) の 1 次以降の係数
    """

    if P[0] != 0:
        raise ValueError("定数項が 0 ではありません")

    return Integrate(Differentiate(P) / (1 + P * P))

def Power(P: Modulo_Polynomial, M: int) -> Modulo_Polynomial:
    """ 形式的ベキ級数 P の M 乗を求める.

    Args:
        P (Modulo_Polynomial): 形式的ベキ級数
        M (int): 非負整数

    Raises:
        ValueError: M が負のときに発生

    Returns:
        Modulo_Polynomial: P の M 乗
    """

    if M < 0:
        raise ValueError("M は非負でなくてはなりません")
    elif M == 0:
        # M = 0　のときは P^0 = 1 確定.
        return Modulo_Polynomial([1], P.max_degree)

    n = P.max_degree
    F = P.poly
    F.extend([0] *((n + 1) - len(F)))

    # 係数が 0 ではない最低次の次数とその係数を求める.
    if (ord := P.order(-1)) == -1:
        return Modulo_Polynomial([0], P.max_degree)

    if ord * M > n:
        # M 乗
        return Modulo_Polynomial([0], P.max_degree)

    lowest = F[ord]
    lowest_inv = pow(lowest, -1, Mod)
    M_mod = M % Mod

    if Calc.is_sparse(F):
        # P が疎な場合
        H = [(lowest_inv * a) % Mod for a in F[ord:]] + [0]
        Nh = len(H) - 1
        d, _ = Calc.coefficients_list(H)
        K = len(d)

        inv = [0] * (Nh + 1)
        inv[1] = 1
        for x in range(2, Nh+1):
            q, r = divmod(Mod, x)
            inv[x] = (-q * inv[r]) % Mod

        G = [0] * Nh; G[0] = 1
        for i in range(Nh - 1):
            g = (M_mod * (i + 1) % Mod) * H[i + 1] % Mod
            for j in range(K):
                if not (1 <= d[j] <= i):
                    continue

                alpha = (d[j] * M_mod - (i - d[j] + 1)) % Mod
                beta = G[i + 1 - d[j]] * H[d[j]] % Mod
                g += alpha * beta % Mod
            g %= Mod

            G[i + 1] = g * inv[i + 1] % Mod
    else:
        # P が密な場合
        # P^M = Exp(M Log(P)) を利用する

        Q = Modulo_Polynomial([(lowest_inv * a) % Mod for a in F[ord:]], P.max_degree)
        G = Exp(M_mod*Log(Q)).poly

    lowest_k = pow(lowest, M, Mod)
    G = [0] * (ord * M) + [(lowest_k * a) % Mod for a in G]
    return Modulo_Polynomial(G, P.max_degree)

#根号
def Tonelli_Shanks(X, default=-1):
    """ X=a (mod Mod) のとき, r*r=a (mod Mod) を満たす r を返す.

    ※法pが素数のときのみ有効
    ※存在しないときは default が返り値
    """

    #ルジャンドル記号
    def Legendre(X):
        """ルジャンドル記号 (a/Mod) を返す.

        ※法が素数のときのみ成立する.
        """

        if X%Mod==0:
            return 0
        elif pow(X,(Mod-1)//2,Mod)==1:
            return 1
        else:
            return -1

    X%=Mod
    if Legendre(X)==-1:
        return default

    from random import randint as ri
    if X==0:
        return X
    elif Mod==2:
        return X
    elif Mod%4==3:
        return pow(X,(Mod+1)//4,Mod)

    u=2
    s=1
    while (Mod-1)%(2*u)==0:
        u*=2
        s+=1
    q=(Mod-1)//u

    z=0
    while pow(z,(Mod-1)//2,Mod)!=Mod-1:
        z=ri(1,Mod-1)

    m,c,t,r=s,pow(z,q,Mod),pow(X,q,Mod),pow(X,(q+1)//2,Mod)
    while m>1:
        if pow(t,2**(m-2),Mod)==1:
            c=(c*c)%Mod
            m=m-1
        else:
            c,t,r,m=(c*c)%Mod,(c*c*t)%Mod,(c*r)%Mod,m-1
    return r

#多項式の根号
def __sqrt(F, N):
    F+=[0]*(N-len(F))
    s=Tonelli_Shanks(F[0])
    if s==-1:
        return None

    two_inv=pow(2, -1, Mod)

    if not Calc.is_sparse(F):
        # P が疎な場合
        F.append(0)
        d,f=Calc.coefficients_list(F); K=len(d)

        Inv=[0]*(N+1); Inv[1]=1
        for i in range(2, N+1):
            q,r=divmod(Mod, i)
            Inv[i]=(-q*Inv[r])%Mod

        G=[0]*N; G[0]=1
        for i in range(N):
            g=(two_inv*(i+1)%Mod)*F[i+1]%Mod
            for j in range(K):
                if 1<=d[j]<=i:
                    alpha=(d[j]*two_inv-(i-d[j]+1))%Mod
                    beta=G[i+1-d[j]]*F[d[j]]%Mod
                    g+=alpha*beta
            g%=Mod
            G[i+1]=g*Inv[i+1]%Mod
    else:
        m=1
        G=[min(s,Mod-s)]

        while m<N:
            G+=[0]*m
            m<<=1
            H=Calc.convolution(F[:m], Calc.inverse(G))
            G=[two_inv*(a+b)%Mod for a,b in zip(G,H)]
    return G[:N]

def Sqrt(P):
    N=P.max_degree
    F=P.poly
    F+=[0]*(N-len(F))

    for d,p in enumerate(F):
        if p:
            break
    else:
        return Modulo_Polynomial([0],P.max_degree)

    if d%2==1:
        return

    E=__sqrt(F[d:],N-d//2)

    if E==None:
        return

    if d>0:
        E=[0]*(d//2)+E
    return Modulo_Polynomial(E,P.max_degree)

"""
形式的ベキ級数に対する特別な操作
"""
def Composition(P,Q):
    """ P o Q=P(Q) を求める (※ 順番注意) ([X^0]Q=0 でなくてはならない).

    Reference: https://judge.yosupo.jp/submission/42372
    """

    assert Q[0]==0

    deg=min(P.max_degree, Q.max_degree)
    k=int(deg**0.5+1)
    d=(deg+k)//k

    X=[[1]]
    for i in range(k):
        X.append(Calc.convolution(X[-1],Q.poly)[:deg+1])

    Y=[[0]*len(X[k]) for _ in range(k)]
    for i,y in enumerate(Y):
        for j,x in enumerate(X[:d]):
            if i*d+j>deg:
                break

            for t in range(deg+1):
                if t>=len(x):
                    break
                if t<len(y):
                    y[t]+=x[t]*P[i*d+j]%Mod

    F=[0]*(deg+1)
    Z=[1]
    x=X[d]
    for i in range(k):
        Y[i]=Calc.convolution(Y[i],Z)[:deg+1]
        for j in range(len(Y[i])):
            F[j]+=Y[i][j]
        Z=Calc.convolution(Z,x)[:deg+1]
    return Modulo_Polynomial(F, deg)

def Taylor_Shift(P, a):
    """与えられた多項式 P に対して, P(X+a) を求める.

    P: Polynominal
    a: int
    """

    N=len(P.poly)-1

    fact=[0]*(N+1)
    fact[0]=1
    for i in range(1,N+1):
        fact[i]=(fact[i-1]*i)%Mod

    fact_inv=[0]*(N+1)
    fact_inv[-1]=pow(fact[-1], -1, Mod)

    for i in range(N-1,-1,-1):
        fact_inv[i]=(fact_inv[i+1]*(i+1))%Mod

    F=P.poly.copy()
    for i in range(N+1):
        F[i]=(F[i]*fact[i])%Mod

    G=[0]*(N+1)
    c=1
    for i in range(N+1):
        G[i]=(c*fact_inv[i])%Mod
        c=(c*a)%Mod
    G.reverse()

    H=Calc.convolution(F,G)[N:]
    for i in range(len(H)):
        H[i]=(H[i]*fact_inv[i])%Mod

    return Modulo_Polynomial(H,P.max_degree)

def Polynominal_Coefficient(P,Q,N):
    """ [X^N] P/Q を求める.

    References:
    http://q.c.titech.ac.jp/docs/progs/polynomial_division.html
    https://arxiv.org/abs/2008.08822
    https://arxiv.org/pdf/2008.08822.pdf
    """

    P=P.poly.copy(); Q=Q.poly.copy()
    m=1<<((len(Q)-1).bit_length())
    P.extend([0]*(2*m-len(P)))
    Q.extend([0]*(2*m-len(Q)))

    while N:
        R=[Q[i] if i&1==0 else -Q[i] for i in range(2*m)]

        Calc.ntt(P); Calc.ntt(Q); Calc.ntt(R)
        for i in range(2*m):
            P[i]*=R[i]; P[i]%=Mod
            Q[i]*=R[i]; Q[i]%=Mod

        Calc.inverse_ntt(P); Calc.inverse_ntt(Q)
        if N&1==0:
            for i in range(m):
                P[i]=P[2*i]
        else:
            for i in range(m):
                P[i]=P[2*i+1]

        for i in range(m):
            Q[i]=Q[2*i]

        for i in range(m,2*m):
            P[i]=Q[i]=0

        N>>=1

    if Q[0]==1:
        return P[0]
    else:
        return P[0]*pow(Q[0], -1, Mod)%Mod

def Multipoint_Evaluation(P, X):
    """ 多項式 P に対して, X=[x[0], ..., x[N-1]] としたとき, [P(x[0]), ..., P(x[N-1])] を求める.
    """

    N=len(X)
    size=1<<(N-1).bit_length()

    G=[[1] for _ in range(2*size)]

    for i in range(N):
        G[i+size]=[-X[i],1]

    for i in range(size-1,0,-1):
        G[i]=Calc.convolution(G[2*i],G[2*i+1])

    for i in range(1, 2*size):
        A=P.poly if i==1 else G[i>>1]
        m=len(A)-len(G[i])+1
        v=Calc.convolution(A[::-1][:m], Calc.inverse(G[i][::-1],m))[m-1::-1]
        w=Calc.convolution(v,G[i])

        G[i]=A.copy()
        g=G[i]

        for j in range(len(w)):
            g[j]-=w[j]; g[j]%=Mod

        while len(g)>1 and g[-1]==0:
            g.pop()

    return [G[i+size][0] for i in range(N)]

def Polynominal_Interpolation(X, Y):
    """ N=|X|=|Y| とする. P(x_i)=y_i (0<=i<|X|-1) を満たす高々 (N-1) 次の多項式 P を求める.

    """

    assert len(X)==len(Y)

    N=len(X)
    size=1<<(N-1).bit_length()

    T=[[1] for _ in range(2*size)]

    for i in range(N):
        T[i+size]=[-X[i],1]

    for i in range(size-1,0,-1):
        T[i]=Calc.convolution(T[2*i], T[2*i+1])

    U=[[] for _ in range(2*size)]
    U[1]=[k*a for k,a in enumerate(T[1][1:],1)]

    for i in range(2,N+size):
        m=len(U[i//2])-len(T[i])+1
        v=Calc.convolution(U[i//2][::-1][:m],Calc.inverse(T[i][::-1],m))[m-1::-1]
        w=Calc.convolution(v,T[i])

        U[i]=U[i//2].copy()
        u=U[i]
        for j in range(len(w)):
            u[j]-=w[j]; u[j]%=Mod

        while len(u)>1 and u[-1]==0:
            u.pop()

    for i in range(N):
        U[i+size]=[(Y[i]*pow(U[i+size][0], -1, Mod))%Mod]

    for i in range(size-1,0,-1):
        A=Calc.convolution(U[2*i], T[2*i+1])
        B=Calc.convolution(T[2*i], U[2*i+1])

        m=min(len(A), len(B))

        u=[0]*m
        for j in range(m):
            u[j]=(A[j]+B[j])%Mod
        u.extend(A[m:])
        u.extend(B[m:])
        U[i]=u

    return Modulo_Polynomial(U[1], N)

#多項式同士の最大公約数
def _gcd(F,G):
    while G:
        F,G=G,F%G

    a_inv=pow(F.leading_coefficient(), -1, Mod)
    X=F.poly
    for i in range(len(X)):
        X[i]=(a_inv*X[i])%Mod
    return F

def gcd(*X):
    from functools import reduce
    return reduce(_gcd,X)

#多項式同士の最小公倍数
def _lcm(F,G):
    return (F//gcd(F,G))*G

def lcm(*X):
    from functools import reduce
    L=reduce(_lcm,X)
    a_inv=pow(L.leading_coefficient(), -1, Mod)
    X=L.poly
    for i in range(len(X)):
        X[i]=(a_inv*X[i])%Mod
    return L

"""
スライドさせる畳み込み
"""
def Slide_Convolution(A, B, cyclic=False):
    """

    """
    assert len(A)>=len(B)

    N,M=len(A)-1,len(B)-1
    if cyclic:
        A=A+A[:M]
        return Calc.convolution(A,B[::-1])[M:N+M+1]
    else:
        return Calc.convolution(A,B[::-1])[M:N+1]

#=================================================
Mod = 998244353
Calc = Calculator()
