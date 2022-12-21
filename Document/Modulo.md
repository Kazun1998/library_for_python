---
title: Modulo
documentation_of: //Modulo.py
---

## Theory

### 定義

$\mathbb{Z}$ を整数環とし, $m$ を正の整数とする. このとき, $m \mathbb{Z}$ は $\mathbb{Z}$ のイデアルであるから, 剰余環 $\mathbb{Z}/m \mathbb{Z}$ を考えることができる.

$x \in \mathbb{Z}$ の属する類を $[x], [x]\_m$ と書くことにする. このとき, $x,y \in \mathbb{Z}$ に対して, 以下は同値になる.

* $[x]=[y]$
* $(x-y)$ は $m$ の倍数
* $x \equiv y \pmod{m}$

よって, 各整数の余りを考えることにより,

$$\mathbb{Z}/m\mathbb{Z}=\{[0], [1], \dots, [m-1] \}$$

となることがわかる.

この剰余環は次の和と積によって可換環になる.

* $[x]+[y]:=[x+y]$
* $[x] [y]:=[xy]$

$[x] \in \mathbb{Z}/m \mathbb{Z}$ が可逆元になることの必要十分条件は $x,m$ が互いに素になることである.

よって, $\mathbb{Z}/m\mathbb{Z}$ が体になることの必要十分条件は $m$ が素数であることである.

### 中国剰余定理

$m$ の素因数分解を $m=p_1^{e_1} \dots p_k^{e_k}$ とする. このとき, 中国剰余定理から

$$\displaystyle \mathbb{Z}/m\mathbb{Z} \simeq \prod_{i=1}^k (\mathbb{Z}/p_i^{e_i} \mathbb{Z})$$

である. このとき, 同型写像 $\varphi$ として

$$\varphi([x]):=([x \bmod{p_1^{e_1}}]_{p_1^{e_1}}, \dots, [x \bmod{p_k^{e_k}}]_{p_k^{e_k}})$$

が挙げられる.

### 剰余の合成

$x \in \mathbb{Z}$ としたとき,

$$x \equiv a \pmod{m} \cdots (\spadesuit), \quad x \equiv b \pmod{n} \cdots (\heartsuit)$$

を共にみたすような整数 $x$ の特徴づけをする (中国剰余定理の節における $\varphi$ の逆関数の構成).

$(\spadesuit), (\heartsuit)$ を書き換えると,

* $x=a+mp$ となる整数 $p$ が存在する.
* $x=b+nq$ となる整数 $q$ が存在する.

となることから, 合わせると

* $a+mp=b+nq$ となる整数 $p,q$ が存在する.

ということになる. 式変形をし, $d:=b-a$ とおくと,

* $mp-nq=d \cdots (\diamondsuit)$ となる整数 $p,q$ が存在する.

となる. このような整数 $p,q$ が存在することの必要十分条件は $d$ が $g:=\gcd(m,n)$ の倍数であることである.

以降, $d$ が $\gcd(m,n)$ の倍数であるとし, 整数 $m',n',d'$ をそれぞれ

$$m=gm', \quad n=gn', \quad d=gd'$$

とすると, $(\diamondsuit)$ は $mp \equiv d \pmod{n}$ と同値である.

$m,n,d$ は全て $g$ の倍数であるから, $m'p \equiv d' \pmod{n'}$ と同値になる.

$m', n'$ は互いに素であるので, $m' k \equiv 1 \pmod{n'}$ となる整数 $k$ が存在する. これを両辺にかけることにより,

$$p \equiv dk \pmod{n'}$$

を得る.

これを $x=a+mp$ に代入することによって, $mn'=\dfrac{mn}{\gcd(m,n)}=\operatorname{lcm}(m,n)$ であるから,

$$x \equiv a+mdk \pmod{\operatorname{lcm}(m,n)}$$

を得る. 逆に, これを満たす整数 $x$ は全て $(\spadesuit), (\heartsuit)$ を満たす.

### 線形方程式

$ax \equiv b \pmod{m}$ を満たす整数 $x$ の特徴づけを行う.

まず, $b$ が $g:=\gcd(a,m)$ の倍数でない場合はこのような整数 $x$ は存在しない. 整数 $a', b', m'$ は $a=ga', b=gb', m=gm'$ を満たすようにとる.

このとき, $a', m'$ は互いに素なので, $a'k \equiv 1 \pmod{m'}$ なる整数 $k$ が存在する. よって,

$$ax \equiv b \pmod{m} \iff x \equiv bk \pmod{m'}$$

となる.

### ルジャンドル記号

$p$ を素数とする. 整数 $a \in \mathbb{Z}$ におけるルジャンドル記号 $\displaystyle \left( \dfrac{a}{p} \right)$ を

$$\left( \dfrac{a}{p} \right) \equiv a^{(p-1)/2} \pmod{p}, \quad \left( \dfrac{a}{p} \right) \in \{-1,0,1\}$$

をみたす (唯一の) 整数と定義する (well-defindness はフェルマーの小定理より従う).

このとき,

* $\left( \dfrac{a}{p} \right)=1 \iff a \not \equiv 0 \pmod{p}$ かつ $\exists b \in \mathbb{Z} {\rm ~s.t.~} b^2=a$ (平方剰余)
* $\left( \dfrac{a}{p} \right)=-1 \iff a \not \equiv 0 \pmod{p}$ かつ $\exists b \in \mathbb{Z} {\rm ~s.t.~} b^2=a$ (平方非剰余)
* $\left( \dfrac{a}{p} \right)=0 \iff a \equiv 0 \pmod{p}$

よって, $a$ が $p$ を法にして平方剰余であることと, $\left( \dfrac{a}{p} \right) \neq -1$ であることは同値になる.

### 位数

$[a] \in \mathbb{Z}/m \mathbb{Z}$ に対して, $[a]^n=[1]$ となる 正の整数 $n$ が存在するか? 存在するならばその $n$ の最小値 $\operatorname{ord} [a]$を求める.

まず, 存在性については $[a]^n=[1]$ が存在することと, $[a]$ が可逆である. つまり, $a,m$ が互いに素になることが同値になる.

実際, $[a]^n=[1]$ となる正の整数 $n$ が存在するならば, $[a]^{-1}=[a]^{n-1}$ であるから, $[a]$ は可逆である. 一方で, $[a]$ が可逆であるとき, $[a]^0, [a]^1, \dots, [a]^m$ には鳩ノ巣原理から, $0 \leq i<j \leq m$ で $[a]^i=[a]^j$ となるようなものが存在する. $[a]$ は可逆と仮定しているので, $[a]^{j-i}=[1]$ である.

可逆元 $[a]$ に対して, 積に関して生成される $\left \langle [a] \right \rangle$ は $(\mathbb{Z}/m\mathbb{Z})^\times$ の部分群である. このとき, ラグランジュの定理から次のことが従う.

* $\\# \left \langle [a] \right \rangle$ は $\\# (\mathbb{Z}/m\mathbb{Z})^\times$ の約数である.

また, この2つの群の位数について,

* $\operatorname{ord} [a]=\left \langle [a] \right \rangle$
* $\\# (\mathbb{Z}/m\mathbb{Z})^\times=\varphi(m)$ (Euler's totient function)

が成り立つ.

以上のことから,

$$\operatorname{ord} [a]=\min \{d \mid 1 \leq d \leq m, d~|~\varphi(m), [a]^d=1 \}$$

となる.

### 原始根

次のような定理がある.

> 原始根の存在定理
>
> $p$ を素数とする. このとき, $\mathbb{Z}/p \mathbb{Z}$ には位数 $(p-1)$ の元が存在する.
>
> このような元のことを原始根という.

$p$ を素数とすると, 任意の $p$ の倍数ではない整数 $a$ に対して, $[x]^{p-1}=[1]$ である.

$[g] \in (\mathbb{Z}/p \mathbb{Z})^\times$ が原始根であることの必要十分条件は任意の $(p-1)$ の素因数 $q$ に対して, $[a]^{(p-1)/q} \neq [1]$ となることである.

[参考ページ](https://37zigen.com/primitive-root/)
