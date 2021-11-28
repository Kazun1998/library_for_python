from math import gcd

class Fraction():
    __slots__=["a","b"]

    ##入力定義
    def __init__(self, Numerator=0, Denominator=1, expanded=False, reduction=False):
        """分数のオブジェクトを生成する.

        Numerator: 分子
        Denominator: 分母 (!=0)
        """
        assert Denominator or expanded,"分母が0"

        if Denominator<0:
            Numerator*=-1
            Denominator*=-1

        self.a=Numerator
        self.b=Denominator
        if reduction:
            g=gcd(Numerator, Denominator)
            self.a=Numerator//g
            self.b=Denominator//g

    #表示定義
    def __str__(self):
        if self.b==1:
            return str(self.a)
        else:
            return "{}/{}".format(self.a,self.b)

    __repr__=__str__

    #四則演算定義
    def __add__(self,other):
        if other.__class__==Fraction:
            x=self.a*other.b+self.b*other.a
            y=self.b*other.b
        elif other.__class__==int:
            x=self.a-self.b*other
            y=self.b
        else:
            assert 0,"型が違う"
        return Fraction(x,y)

    def __radd__(self,other):
        return self+other

    def __sub__(self,other):
        if other.__class__==Fraction:
            x=self.a*other.b-self.b*other.a
            y=self.b*other.b
        elif other.__class__==int:
            x=self.a+self.b*other
            y=self.b
        else:
            assert 0,"型が違う"
        return Fraction(x,y)

    def __rsub__(self,other):
        return -self+other

    def __mul__(self,other):
        if other.__class__==Fraction:
            x=self.a*other.a
            y=self.b*other.b
        elif other.__class__==int:
            x=self.a*other
            y=self.b
        else:
            assert 0,"型が違う"

        return Fraction(x,y)

    def __rmul__(self,other):
        return self*other

    def __floordiv__(self,other):
        if other==Fraction():
            raise ZeroDivisionError

        H=self/other
        return H.a//H.b

    def __rfloordiv__(self,other):
        if self==Fraction():
            raise ZeroDivisionError

        H=other/self
        return H.a//H.b

    def __truediv__(self,other):
        assert other,"除数が0"

        if other.__class__==Fraction:
            x=self.a*other.b
            y=self.b*other.a
        elif other.__class__==int:
            x=self.a
            y=self.b*other
        else:
            assert 0,"型が違う"

        return Fraction(x,y)

    def __rtruediv__(self,other):
        assert self,"除数が0"
        if other.__class__==Fraction:
            x=other.a*self.b
            y=other.b*self.a
        elif other.__class__==int:
            x=other*self.b
            y=self.a
        else:
            assert 0,"型が違う"
        return Fraction(x,y)

    def __pow__(self,m):
        alpha,beta=self.a,self.b
        if m<0:
            alpha,beta=beta,alpha
            m=-m

        return Fraction(pow(alpha,m),pow(beta,m))

    #丸め
    def __floor__(self):
        return self.a//self.b

    def __ceil__(self):
        return (self.a+self.b-1)//self.b

    #真偽値
    def __bool__(self):
        return bool(self.a)

    #比較
    def __eq__(self,other):
        if other.__class__==Fraction:
            return self.a*other.b==self.b*other.a
        elif other.__class__==int:
            return self.a==self.b*other
        else:
            assert 0,"型が違う"

    def __nq__(self,other):
        return not(self==other)

    def __lt__(self,other):
        return self<=other and self!=other

    def __le__(self,other):
        if other.__class__==Fraction:
            return self.a*other.b<=self.b*other.a
        elif other.__class__==int:
            return self.a<=self.b*other
        else:
            assert 0,"型が違う"

    def __gt__(self,other):
        return other<=self and other!=self

    def __ge__(self,other):
        return other<=self

    #その他
    def __float__(self):
        return self.a/self.b

    def sign(self):
        s=self.a*self.b
        if s>0:return 1
        elif s==0:return 0
        else:return -1

    #符号
    def __pos__(self):
        return self

    def __neg__(self):
        return Fraction(-self.a,self.b)

    def __abs__(self):
        if self.a>0:
            return self
        else:
            return -self

    #その他
    def is_unit(self):
        return self.a==1

    def __hash__(self):
        return hash(10**9*self.a+self.b)
