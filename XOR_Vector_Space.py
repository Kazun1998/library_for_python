"""Tips
自然数全体の集合 N において, 加法と F_2 とのスカラー倍を
    x+y:=x xor y, [0] x:=0, [1] x:=x
と定めると, N は F_2 上のベクトル空間になる.
"""

class XOR_Vector_Space:
    def __init__(self):
        self.S=[]

    def __contains__(self,x):
        for v in self.S:
            if x&v&(-v):
                x^=v
            if x==0:
                return True
        return False

    def __add__(self,other):
        W=XOR_Vector_Space()

        W.S=self.S[:]
        W.add_vector(*other.S)
        return W

    def add_vector(self,*T):
        for x in T:
            for v in self.S:
                if x&v&(-v):
                    x^=v
                    if x==0:
                        break
            if x:
                self.S.append(x)

    def dim(self):
        return len(self.S)

    def reduction(self):
        S=self.S
        for i in range(len(S)):
            vb=S[i]&(-S[i])
            for j in  range(len(S)):
                if i==j: continue

                if S[j]&vb:
                    S[j]^=S[i]
        self.S=[s for s in S if s]

    def __le__(self,other):
        for u in self.S:
            if not u in other:
                return False
        return True

    def __ge__(self,other):
        return other<=self

    def __eq__(self,other):
        return (self<=other) and (other<=self)

def Generate_Space(*S):
    V=XOR_Vector_Space()
    V.add_vector(*S)
    V.reduction()
    return V

def Get_Basis(*S):
    B=[]
    V=XOR_Vector_Space()
    k=0
    for v in S:
        V.add_vector(v)
        if k+1==V.dim():
            B.append(v)
            k+=1
    return B
