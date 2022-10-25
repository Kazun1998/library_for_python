# 代数的構造

## 定義

- 集合 $A$ と $n$ 個の $k$ 項演算子 $R_n: A^k \to A$ の組 $(A,R_1, \dots, R_n)$ を代数系という.
- 正式には集合と演算子の組を代数系というが, 以降では集合のみを指定して代数系ということがある.

次のように集合 $A$ の演算子 $\circ$ に関する性質を定める.

- 任意の $a,b,c \in A$ に対して, $a \circ (b \circ c)=(a \circ b) \circ c$ を満たすとき, $\circ$ は **結合則** を満たすという.
- $e \in A$ のうち, 任意の $a \in A$ に対して, $e \circ a=a \circ e=a$ となるような元を $\circ$ の **単位元** という.
  - 単位元は存在するならば一意である.
- $e \in A$ を $\circ$ の単位元とする. $a \in A$ で $a \circ b=b \circ a=e$ を満たすような $b \in A$ が存在するとき, $a$ は $\circ$ に関して **可逆** であるという.
  - $a \in A$ が **可逆** であるとき, このような $b \in A$ は一意である. この $b$ のことを (積の場合) $a^{-1}$, (和の場合) $-a$ と書く.
- $a,b \in A$ で $a \circ b=b \circ a$ を満たすとき, $a,b$ は **可換** であるという.
  - 任意の2元 $a,b \in A$ が可換となるとき, $A$ は **可換** であるという.

$\circ, \bullet$ を演算とする.

- 以下の2条件を満たすとき, $\circ$ を和, $\bullet$ を積とする **分配則** を満たすいう.
  - 任意の $a,b,c \in A$ に対して, $a \bullet (b \circ c)=(a \bullet b) \circ (a \bullet c)$
  - 任意の $a,b,c \in A$ に対して, $(a \circ b) \bullet c=(a \bullet c) \circ (b \bullet c)$

## 1個の演算子からなる代数系

演算は $\circ$ であるとする. 1つの演算子が定められている代数系をマグマという.

- 結合則を満たす代数系を **半群** という.
- 単位元が存在する半群を **モノイド** という.
- 任意の元が可逆であるようなモノイドを **群** という.
- 可換な群を **可換群** (**アーベル群**) という.

## 2個の演算子からなる代数系

2個の演算を $+,\cdot$ とする. また, $+$ を加法, $\cdot$ を乗法という.

- 加法に関して可換群, 乗法に関してモノイドであり, 加法を和, 乗法を積として分配則を満たすような代数系を **環** であるという.
- 加法の単位元以外の任意の元が逆元を持つような環を **体** という.

## 例

- モノイド
  - $(\mathbb{N}, \gcd), (\mathbb{N}, \operatorname{lcm})$
  - $\mathbb{N}':=\mathbb{N} \cup \\{ \pm \infty \\}$ としたときの $(\mathbb{N}, \max), (\mathbb{N}', \min)$
  - $\mathbb{Z}':=\mathbb{Z} \cup \\{ \pm \infty \\}$ としたときの $(\mathbb{Z}', \max), (\mathbb{Z}', \min)$
  - 写像の合成 $f \circ g$
  - $\mathcal{A}$ をアルファベットとする. $W(\mathcal{A})$ を $\mathcal{A}$ の語全体の集合としたときの文字列の結合 $\oplus$
  - 論理和, 論理積
  - bitwise or, bitwise and
- 群 (この節で挙げる例は全て非可換群)
  - $n$ 次対称群 $\mathfrak{S}_n$
  - $R$ を可換環としたときの正則行列全体 $\operatorname{GL}_n(R)$.
- 可換群
  - $(\mathbb{Z}, +, \times)$
  - $(\mathbb{Z}/m\mathbb{Z}, +, \times) \quad (m \in \mathbb{Z})$
  - 排他的論理和
  - bitwise xor
- 環
  - $\mathbb{Z}$
  - $m \in \mathbb{Z}$ としたときの $\mathbb{Z}/m \mathbb{Z}$
  - $R$ を可換環としたときの $n$ 次行列環 $M_n(R)$ ($n \geq 2$ ならば可換ではない!!)
  - $R$ を可換環としたときの多項式環 $R[X]$ (こちらは可換環).
- 体
  - $\mathbb{Q}, \mathbb{R}, \mathbb{C}$
  - $p$ を素数としたときの $\mathbb{F}_p:=\mathbb{Z}/p \mathbb{Z}$
