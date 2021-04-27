class Integer_Range:
    def __init__(self,L,R):
        self.L=L
        self.R=R
        self.valid=1 if L<=R else 0

    def __str__(self):
        if self:
            return "[{}, {}]".format(self.L,self.R)
        else:
            return "O"

    def __repr__(self):
        return str(self)

    def __bool__(self):
        return bool(self.valid)

    def __contains__(self,x):
        return self.valid and self.L<=x<=self.R

    def __and__(self,other):
        if self and other:
            return Integer_Range(max(self.L,other.L),min(self.R,other.R))
        else:
            return Integer_Range(0,-1)

    def __iter__(self):
        yield from range(self.L,self.R+1)

    #不等号
    def __eq__(self,other):
        if bool(self)^bool(other):
            return False

        if self:
            return (self.L==other.L) and (self.R==other.R)
        else:
            return True

    def __ne__(self,other):
        return not(self==other)

    def __le__(self,other):
        if not self:
            return True
        if self==other:
            return True
        return (other.L<=self.L) and (self.R<=other.R)

    def __lt__(self,other):
        return self<=other and self!=other

    def __ge__(self,other):
        return other<=self

    def __gt__(self,other):
        return other<self

    def Is_disjoint(self,other):
        """互いに素かどうかを判定する.
        """
        if (not self) or (not other):
            return True
        return max(self.L,other.L)>min(self.R,other.R)

    def Cardinality(self):
        """濃度を求める.

        """
        return max(self.R-self.L+1,0)

class Integer_Interval(Integer_Range):
    def __init__(self,*I):
        X=[x for x in I if x]
        X.sort(key=lambda x:x.L)

        self.I=[]
        if not X:return

        N=len(X)
        l,r=X[0].L,X[0].R
        for k in range(1,N):
            s,t=X[k].L,X[k].R
            if r+1<s:
                self.I.append(Integer_Range(l,r))
                l=s
            r=max(r,t)
        self.I.append(Integer_Range(l,r))

    def __str__(self):
        if self:
            return " | ".join(map(str,self.I))
        else:
            return "O"

    def __repr__(self):
        return str(self)

    def __bool__(self):
        return bool(self.I)

    def __and__(self,other):
        A=[]
        for x in self.I:
            for y in other.I:
                A.append(x&y)
        return Integer_Interval(*A)

    def __or__(self,other):
        return Integer_Interval(*(self.I+other.I))

    def __iter__(self):
        for I in self.I:
            yield from I

    def __eq__(self,other):
        if len(self.I)!=len(other.I):
            return False

        A=self.I
        B=other.I
        for k in range(len(self.I)):
            if A!=B:
                return False
        return True

    def __neq__(self,other):
        return not(self==other)

    def __contains__(self,x):
        for I in self.I:
            if x in I:
                return True
        return  False

    def Is_disjoint(self,other):
        """互いに素かどうかを判定する.
        """
        for I in self.I:
            for J in other.I:
                if not I.Is_disjoint(J):
                    return False
        return True

    def Cardinality(self):
        """濃度を求める.

        """
        X=0
        for I in self.I:
            X+=I.Cardinality()
        return X

    def Slide(self,a):
        """aだけずらす.
        """

        for I in self.I:
            I.L+=a
            I.R+=a

    def Scale(self,a):
        """a倍する.
        """

        if not self:
            return

        X=[]
        if a>=0:
            for I in self.I:
                X.append(Integer_Range(a*I.L,a*I.R))
        else:
            for I in self.I:
                X.append(Integer_Range(a*I.R,a*I.L))
        return Integer_Interval(*X)

def Addition(I,J):
    X=[]
    for i in I.I:
        for j in J.I:
            X.append(Integer_Range(i.L+j.L,i.R+j.R))
    return  Integer_Interval(*X)
