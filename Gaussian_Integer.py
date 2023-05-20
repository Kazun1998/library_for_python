class Gaussian_Integer():
    #入力定義
    def __init__(self, Real_part=0, Imaginary_part=0):
        self.re=Real_part
        self.im=Imaginary_part

    #表示定義
    def __str__(self):
        if self.re==0:
            if self.im==0:
                return "0"
            elif self.im==1:
                return "i"
            elif self.im==-1:
                return "-i"
            else:
                return "{}i".format(self.im)
        else:
            if self.im==0:
                return str(self.re)
            elif self.im==1:
                return "{}+i".format(self.re)
            elif self.im==-1:
                return "{}-i".format(self.re)
            else:
                return "{}{:+}i".format(self.re,self.im)

    __repr__=__str__

    #四則演算定義
    #加法
    def __add__(self,other):
        if isinstance(other,Gaussian_Integer):
            return Gaussian_Integer(self.re+other.re,self.im+other.im)
        else:
            return Gaussian_Integer(self.re+other,self.im)

    def __radd__(self,other):
        if isinstance(other,int):
            return Gaussian_Integer(self.re+other,self.im)

    #減法
    def __sub__(self,other):
        return self+(-other)

    def __rsub__(self,other):
        if isinstance(other,int):
            return (-self)+other

    #乗法
    def __mul__(self,other):
        a,b=self.re,self.im
        if isinstance(other,Gaussian_Integer):
            c,d=other.re,other.im
            return Gaussian_Integer(a*c-b*d,a*d+b*c)
        else:
            return Gaussian_Integer(other*a,other*b)

    def __rmul__(self,other):
        if isinstance(other,int):
            a,b=self.re,self.im
            return Gaussian_Integer(other*a,other*b)

    #除法
    def __truediv__(self,other):
        pass

    def __rtruediv__(self,other):
        pass

    def __floordiv__(self,other):
        if isinstance(other,int):
            other=Gaussian_Integer(other,0)

        a,b=self.re,self.im
        c,d=other.re,other.im

        n=other.norm()

        p=(2*(a*c+b*d)+n)//(2*n)
        q=(2*(b*c-a*d)+n)//(2*n)

        return Gaussian_Integer(p,q)

    def __divmod__(self,other):
        x=self//other
        return (x,self-other*x)

    def __mod__(self,other):
        return  self-other*(self//other)

    #比較演算子
    def __eq__(self,other):
        if isinstance(other,Gaussian_Integer):
            return (self.re==other.re) and (self.im==other.im)
        else:
            return (self-other)==Gaussian_Integer(0,0)

    def __bool__(self):
        return not(self==0)

    #その他
    def conjugate(self):
        return Gaussian_Integer(self.re,-self.im)

    def __abs__(self):
        import math
        return math.sqrt(self.norm())

    def norm(self):
        return self.re*self.re+self.im*self.im

    #実数から複素数に変換
    def Real_to_Complex(self):
        pass

    #正負判定

    #要約

    #逆数
    def __inverse(self):
        pass

    #符号
    def __pos__(self):
        return self

    def __neg__(self):
        return Gaussian_Integer(-self.re,-self.im)

    #コピー
    def __copy__(self):
        return self

    #ハッシュ
    def __hash__(self):
        return hash((self.re,self.im))

#最大公約数
def gcd(x,y):
    """Gauss整数 x,yの最大公約数を求める.

    x,y:Gauss整数
    """

    while y:
        x,y=y,x%y

    return x

#拡張Euclidの互除法
def Extended_Euclid(x,y):
    """拡張Euclidの互除法を用いて,xa+yb=gcd(x,y)を満たすGauss整数a,bを求める.

    x,y:Gauss整数

    [出力]:(a,b,gcd(x,y))
    """

    a0,b0,a1,b1=1,0,0,1
    while y:
        q,x,y=x//y,y,x%y
        a0,a1=a1,a0-q*a1
        b0,b1=b1,b0-q*b1
    return a0,b0,x

#同伴?
def Is_Associate(x,y):
    """x,yは同伴?

    x,y:Gauss整数
    """
    e=Gaussian_Integer(0,1)

    a=(x==y)
    b=(x==-y)
    c=(x==y*e)
    d=(x==y*(-e))

    return a|b|c|d

