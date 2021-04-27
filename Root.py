import math
from copy import *
from Number  import Number
from Fraction  import Fraction
from functools import total_ordering


class root(Fraction):
    def __init__(self,c=0,b=1):
        self.c=c
        self.b=b

    def __str__(self):
        if self.c==0:return ""

        if self.b==1:
            if self.c>0:return "+"+str(self.c)
            else:return str(self.c)

        t="sqrt["+str(self.b)+"]"

        if self.c>0:
            if self.c==1:return "+"+t
            else:return "+"+str(self.c)+t
        else:
            if self.c==-1:return  "-"+t
            else:return str(self.c)+t

    def string(self):
        if self.c==0:return ""

        if self.b==1:
            if self.c>0:return "+"+str(self.c)
            else:return str(self.c)

        t="sqrt["+str(self.b)+"]"

        if self.c>0:
            if self.c==1:return "+"+t
            else:return "+"+str(self.c)+t
        else:
            if self.c==-1:return  "-"+t
            else:return str(self.c)+t

    def __add__(self,other):
        r=root()
        if self.b!=other.b:
            print("Unmatch base!")
        else:
            r=root(self.c+other.c,self.b)
        return r

    def __radd__(self,other):
        r=root()
        if self.b!=other.b:
            print("Unmatch base!")
        else:
            r=root(self.c+other.c,self.b)
        return r

    def __sub__(self,other):
        return self+(-other)

    def __rsub__(self,other):
        return -self+other

    def __mul__(self,other):
        return root.__reduce(root(self.c*other.c,self.b*other.b))

    def __rmul__(self,other):
        return root.__reduce(root(self.c*other.c,self.b*other.b))

    def __truediv__(self,other):
        a=self.c
        b=self.b
        c=other.c
        d=other.b
        return root.__reduce(root(Fraction(a,c*d),b*d))

    def __rtruediv__(self,other):
        a=other.c
        b=other.b
        c=self.c
        d=self.b
        return root.__reduce(root(Fraction(a,c*d),b*d))

    def __eq__(self,other):
        if self.b!=other.b:return False
        return (self-other).c==0

    def __pos__(self):
        return self

    def __neg__(self):
        return root(-self.c,self.b)

    def __reduce(self):
        for i in range(2,math.floor(math.sqrt(self.b)+1)):
            while(self.b % (i*i)==0):
                self.c*=i
                self.b//=i*i

        return root(self.c,self.b)

@total_ordering
class Root(root):
    ##入力定義
    def __init__(self,*Term):
        self.term=[]
        for t in Term:
            self.term.append(root(t[0],t[1]))

    #表示定義
    def __str__(self):
        s=""
        for t in self.term:
            s+=root.string(t)

        if s=="":return "0"
        else:return s

    #四則演算定義
    def __add__(self,other):
        r=Root()
        if not(isinstance(other,Root)):other=Root((other,1))
        r.term=[]
        r.term+=self.term
        r.term+=other.term
        return Root.__reduce(r)

    def __radd__(self,other):
        r=Root()
        if not(isinstance(other,Root)):other=Root((other,1))
        r.term=[]
        r.term+=self.term
        r.term+=other.term
        return Root.__reduce(r)

    def __sub__(self,other):
        return self+(-other)

    def __rsub__(self,other):
        return -self+other

    def __mul__(self,other):
        r=Root()
        for t in self.term:
            for u in other.term:
                r.term.append(t*u)
        return Root.__reduce(r)

    def __rmul__(self,other):
        r=Root()
        for t in self.term:
            for u in other.term:
                r.term.append(t*u)
        return Root.__reduce(r)

    def __truediv__(self,other):
        if not(isinstance(self,Fraction)):self=Root((self,1))

        u=Root()
        u.term=copy(self.term)

        if len(u.term)==1:
            r=Root()
            for a in u.term:
                r+=a/u
        else:
            p=Root()
            v=Root()
            p.term=copy(other.term)
            v.term=list.pop(u.term)
            return (p*(u-v))/(u*u+v*v)

        return r

    def __rtruediv__(self,other):
        if not(isinstance(other,Fraction)):other=Root((other,1))

        u=Root()
        u.term=copy(other.term)

        if len(u.term)==1:
            r=Root()
            for a in u.term:
                r+=a/u
        else:
            p=Root()
            v=Root()
            p.term=copy(self.term)
            v.term=list.pop(u.term)
            return (p*(u-v))/(u*u+v*v)

        return r

    #比較演算子
    def __eq__(self,other):
        return (self-other).a==0

    def __lt__(self,other):
        return (self-other).a<0

    #その他
    def ToNumber(self):
        return self.a/self.b

    def sign(self):
        s=self.a*self.b
        if s>0:return 1
        elif s==0:return 0
        else:return -1

    def __reduce(self):
        r=Root()
        r.term=copy(self.term)

        for t in range(len(self.term)):
            for u in range(t+1,len(self.term)):
                if r.term[t].b==r.term[u].b:
                    r.term[t]+=r.term[u]
                    r.term[u]=root(0,1)

        s=Root()
        s.term=copy(r.term)

        for t in s.term:
            if t==root():r.term.remove(t)
        return

    def __pos__(self):
        return self

    def __neg__(self):
        r=Root()
        r.term=[]
        for t in self.term:
            r.term+=[-t]
        return r

    def __abs__(self):
        if self>=0:return self
        else:return -self

    def __len__(self):
        return len(self.term)
