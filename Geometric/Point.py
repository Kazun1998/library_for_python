from math import sqrt,sin,cos,tan,atan2,pi

def compare(a,b,ep):
    if a+ep<b:
        return 1
    elif a>b+ep:
        return -1
    else:
        return 0

#===
#点
#===
class Point():
    ep=1e-9

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sign(self,a):
        return compare(0,a,self.ep)

    #文字列
    def __str__(self):
        return "({}, {})".format(self.x,self.y)

    def __repr__(self):
        return self.__str__()

    #Bool
    def __bool__(self):
        return self.sign(self.x)!=0 or self.sign(self.y)!=0

    #等号
    def __eq__(self,other):
        return self.sign(self.x-other.x)==0 and self.sign(self.y-other.y)==0

    #不等号
    def __ne__(self,other):
        return not self==other

    #比較(<)
    def __lt__(self,other):
        T=self.sign(self.x-other.x)
        if T:
            return T<0
        else:
            return self.sign(self.y-other.y)

    #比較(<=)
    def __le__(self,other):
        return self<other or self==other

    #比較(>)
    def __gt__(self,other):
        return other<self

    #比較(>=)
    def __ge__(self,other):
        return other<=self


    #正と負
    def __pos__(self):
        return self

    def __neg__(self):
        return Point(-self.x,-self.y)


    #加法
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)

    #減法
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)

    #乗法
    def __mul__(self,other):
        x,y=self.x,self.y
        u,v=other.x,other.y
        return Point(x*u-y*v,x*v+y*u)

    def __rmul__(self,other):
        if isinstance(other,(int,float)):
            return Point(other*self.x,other*self.y)

    #除法
    def __truediv__(self,other):
        if other==0:
            raise ZeroDivisionError
        return Point(self.x/other,self.y/other)

    #絶対値
    def __abs__(self):
        return sqrt(self.x*self.x+self.y*self.y)

    #回転
    def rotate(self,theta):
        x,y=self.x,self.y
        s,c=sin(theta),cos(theta)
        return Point(c*x-s*y,s*x+c*y)

def Inner(P,Q):
    """点P,Qの内積を求める.

    P,Q:Point
    """
    return P.x*Q.x+P.y*Q.y

def Det(P,Q):
    """点P,Qが張る平行四辺形の符号付き面積を求める.

    P,Q:Point
    """
    return P.x*Q.y-P.y*Q.x

def Arg(P):
    """点Pの偏角を求める.

    P:Point
    """
    return atan2(P.y,P.x)

def Internal_Division_Point(P,Q,p,q):
    """線分PQをp:qに内分する点を求める.

    P,Q:Point
    p,q:int or float
    """
    assert p+q
    return (q*P+p*Q)/(p+q)

def External_Division_Point(P,Q,p,q):
    """線分PQをp:qに内分する点を求める.

    P,Q:Point
    p,q:int or float
    """
    assert p-q
    return (-q*P+p*Q)/(p-q)

def MidPoint(P,Q):
    """線分PQの中点を求める.

    P,Q:Point
    """
    a=(P.x+Q.x)/2
    b=(P.y+Q.y)/2
    return Point(a,b)
