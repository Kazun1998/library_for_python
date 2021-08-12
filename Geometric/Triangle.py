from Point import *

class Triangle():
    def __init__(self,A,B,C):
        """ 3点 A,B,C を頂点とする三角形を生成する.

        A,B,C: Point
        """

        assert A!=B and B!=C and C!=A
        self.A=A
        self.B=B
        self.C=C

    def __str__(self,A,B,C):
        return "[Triangle] {}, {}, {}".format(self.A,self.B,self.C)

    __repr__=__str__

    def area(self):
        return abs((self.B-self.A).det(self.C-self.A)/2)

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

    a=abs(T.B-T.C)
    b=abs(T.C-T.A)
    c=abs(T.A-T.B)
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
    a=abs(T.B-T.C)
    b=abs(T.C-T.A)
    c=abs(T.A-T.B)

    Ea=(-a*T.A+b*T.B+c*T.C)/(-a+b+c)
    Eb=(a*T.A-b*T.B+c*T.C)/(a-b+c)
    Ec=(a*T.A+b*T.B-c*T.C)/(a+b-c)
    return [Ea,Eb,Ec]
