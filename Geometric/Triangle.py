from Point import *

class Triangle():
    __slots__=["A","B","C","id"]
    ep=1e-9
    def __init__(self,A,B,C):
        """ 3点 A,B,C を頂点とする三角形を生成する.

        A,B,C: Point
        """

        assert A!=B and B!=C and C!=A
        self.A=A
        self.B=B
        self.C=C
        self.id=6

    def __str__(self):
        return "[Triangle] {}, {}, {}".format(self.A,self.B,self.C)

    __repr__=__str__

    def area(self):
        return abs((self.B-self.A).det(self.C-self.A)/2)

    def three_edges(self):
        """ 辺 BC, CA, AB の長さを求める.

        """
        return abs(self.B-self.C),abs(self.C-self.A),abs(self.A-self.B)

#=== 三角形の心
def Center_of_Gravity(T):
    """ 三角形 T の重心を求める.

    T: Triangle
    """

    return (T.A+T.B+T.C)/3

def CircumCenter(T):
    """ 三角形 T の外心を求める.

    T: Triangle
    """

    da=(T.B-T.C).norm_2()
    db=(T.C-T.A).norm_2()
    dc=(T.A-T.B).norm_2()
    ta=da*(-da+db+dc)
    tb=db*(da-db+dc)
    tc=dc*(da+db-dc)
    s=ta+tb+tc
    return (ta/s)*T.A+(tb/s)*T.B+(tc/s)*T.C

def InnerCenter(T):
    """ 三角形 T の内心を求める.

    T: Triangle
    """
    a,b,c=T.three_edges()
    return (a*T.A+b*T.B+c*T.C)/(a+b+c)

def OrthoCenter(T):
    """ 三角形 T の垂心を求める.

    T: Triangle
    """
    return T.A+T.B+T.C-2*CircumCenter(T)

def Excenter(T):
    """ 三角形 T の傍心 (3個) を求める.

    T: Triangle
    """
    a,b,c=T.three_edges()
    Ea=(-a*T.A+b*T.B+c*T.C)/(-a+b+c)
    Eb=(a*T.A-b*T.B+c*T.C)/(a-b+c)
    Ec=(a*T.A+b*T.B-c*T.C)/(a+b-c)
    return [Ea,Eb,Ec]

#=== 三角形の形状
def is_Acute_Triangle(T):
    """ 三角形 T が鋭角三角形かどうかを判定する.

    T: Triangle
    """

    a,b,c=T.three_edges()
    m=max(a,b,c)
    return compare(a*a+b*b+c*c-2*m*m,0,T.ep)==1

def is_Right_Triangle(T):
    """ 三角形 T が直角三角形かどうかを判定する.

    T: Triangle
    """

    a,b,c=T.three_edges()
    m=max(a,b,c)
    return compare(a*a+b*b+c*c-2*m*m,0,T.ep)==0

def is_Obtuse_Triangle(T):
    """ 三角形 T が鈍角三角形かどうかを判定する.

    T: Triangle
    """

    a,b,c=T.three_edges()
    m=max(a,b,c)
    return compare(a*a+b*b+c*c-2*m*m,0,T.ep)==-1

def Triangle_Division_by_Angle(T):
    """ 三角形 T が鋭角か直角か鈍角かを判定する.

    [Input]
    T: Triangle

    [Output]
    1: 鋭角, 0: 直角, -1: 鈍角
    """

    a,b,c=T.three_edges()
    m=max(a,b,c)
    return compare(a*a+b*b+c*c-2*m*m,0,T.ep)

def is_Isosceles_Triangle(T):
    """ 三角形 T が二等辺三角形かを判定する.

    [Input]
    T: Triangle
    """

    a,b,c=T.three_edges()
    return compare(a,b,T.ep)==0 or compare(b,c,T.ep)==0 or compare(c,a,T.ep)==0

def is_Isosceles_Right_Triangle(T):
    """ 三角形 T が直角二等辺三角形かを判定する.

    [Input]
    T: Triangle
    """

    return is_Right_Triangle(T) and is_Isosceles_Triangle(T)


def is_Equilateral_Triangle(T):
    """ 三角形 T が正三角形かを判定する.

    [Input]
    T: Triangle
    """

    a,b,c=T.three_edges()
    return compare(a,b,T.ep)==0 and compare(b,c,T.ep)==0 and compare(c,a,T.ep)==0

#=== 三角形の決定
def SSS_Triangle(a, b, c):
    """ 3 辺の長さが a,b,c である三角形を生成する.

    a,b,c: int or float
    """
    assert 2*max(a,b,c)<a+b+c

    t=a+b+c

    A=Point(); B=Point(c,0)
    C=Point((-a*a+b*b+c*c)/(2*c), sqrt(t*(t-2*a)*(t-2*b)*(t-2*c))/(2*c))
    return Triangle(A,B,C)

def SAS_Triangle(a, gamma, b):
    """ 2 辺の長さが a,b で ,間の角度が gamma である三角形を生成する.

    a,b: int or float
    gamma: int or float
    """

    t=sqrt(a*a+b*b-2*a*b*cos(gamma))

    A=Point(); B=Point(t,0)
    C=Point((b*b-a*b*cos(gamma))/t, (a*b*sin(gamma))/t)
    return Triangle(A,B,C)

def ASA_Triangle(alpha ,c, beta):
    """ 1辺の長さが c で, 両端の角度が alpha, beta である三角形を生成する.

    c: int or float
    alpha, beta: int or float (alpha+beta<pi)
    """

    assert alpha+beta<pi
    t=sin(beta)/sin(alpha+beta)

    A=Point(); B=Point(c,0)
    C=Point(c*t*cos(alpha), c*t*sin(alpha))
    return Triangle(A,B,C)

def AAS_Triangle(alpha, beta, a):
    """ 1辺の長さが a で, 2つの角が alpha, beta である三角形を生成する (a の対角が alpha).

    a: int or float
    alpha ,beta: int or float
    """

    assert alpha+beta<pi

    A=Point(); B=Point(a*sin(alpha+beta)/sin(alpha),0)
    C=Point(a*sin(beta)*cos(alpha)/ sin(alpha), a*sin(beta))
    return Triangle(A,B,C)
