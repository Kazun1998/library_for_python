"""
[Tips]
自然数全体の集合 N において, 加法と F_2 とのスカラー倍を
    x+y:=x xor y, [0] x:=0, [1] x:=x
と定めると, N は F_2 上のベクトル空間になる.
"""

class XOR_Vector_Space:
    def __init__(self):
        self.basis=[]

    def __contains__(self, x):
        for v in self.basis:
            x=min(x, x^v)
        return x==0

    def __add__(self, other):
        W=XOR_Vector_Space()

        W.basis=self.basis[:]
        W.add_vector(*other.bais)
        return W

    def add_vector(self, *T):
        for x in T:
            for v in self.basis:
                x=min(x, x^v)

            if x:
                self.basis.append(x)

    def dimension(self):
        return len(self.basis)

    def reduction(self):
        S=self.basis
        for i in range(len(S)):
            vb=S[i]&(-S[i])
            for j in  range(len(S)):
                if i==j:
                    continue

                if S[j]&vb:
                    S[j]^=S[i]
        self.basis=[s for s in S if s]

    def projection(self, x):
        for v in self.basis:
            x=min(x, x^v)
        return x

    def __repr__(self):
        return f"[XOR Vector Space]: dim: {self.dimension()}, basis: {self.basis}"

    def __le__(self, other):
        return all(u in other for u in self.basis)

    def __ge__(self,other):
        return other<=self

    def __eq__(self,other):
        return (self <= other) and self.dimension() == other.dimension()

def Generate_Space(*S):
    """ S によって生成される XOR ベクトル空間を求める.

    """

    V=XOR_Vector_Space()
    V.add_vector(*S)
    V.reduction()
    return V

def Get_Basis(*S):
    """ S によって生成される XOR ベクトル空間 V において, S の部分集合でもあるV の基底を求める

    """

    B=[]
    V=XOR_Vector_Space()
    for v in S:
        w=V.projection(v)
        if w:
            B.append(v)
            V.basis.append(w)
    return B
