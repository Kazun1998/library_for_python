from Point import *
from Line import *

class Circle():
    __slots__=["center","radius","id"]

    ep=1e-9
    def __init__(self,Center:Point,Radius:float):
        """ 2点 P を中心とする半径 r の円を生成する.

        P: Point
        r>=0
        """
        assert Radius>=0

        self.center=Center
        self.radius=Radius
        self.id=5

    def __str__(self):
        return "[Circle] Center: {}, Radius: {}".format(self.center,self.radius)

    __repr__=__str__

    def __contains__(self,Point):
        return compare(abs(Point-self.center),self.radius,self.ep)==0

#=== 交差判定
def has_Intersection_between_Circle_and_Segment(C,L,endpoint=True):
    """円 C と線分 L の交差判定を行う.

    """

    c=C.center
    ep=max(C.ep,L.ep)
    flag1=(compare(
        Distance_betweem_Point_and_Segment(c,L),
        C.radius,
        ep)<=0)
    flag2=(compare(max(abs(c-L.begin),abs(c-L.end)),C.radius,ep)>=0)
    return flag1 and flag2

def has_Intersection_between_Circle_and_Line(C,L,endpoint=True):
    """円 C と直線 L の交差判定を行う.

    """
    return compare(
        Distance_betweem_Point_and_Line(C.center,L),
        C.radius,
        max(C.ep,L.ep))<=0

def has_Intersection_between_Circle_and_Circle(C,D):
    """2つの円 C,D の交差判定を行う.

    """

    r=C.radius; s=D.radius;
    d=abs(C.center-D.center)
    ep=max(C.ep,D.ep)

    return compare(d,abs(r-s),ep)>=0 and compare(d,r+s,ep)<=0

#=== 交点を求める
def Intersection_between_Circle_and_Line(C,L):
    """ 円 C と直線 L の交点を求める.

    """

    if not has_Intersection_between_Circle_and_Line(C,L):
        return []

    H=Projection(C.Center,L)
    d=Distance_betweem_Point_and_Line(C.Center,L)
    x=sqrt(max(C.radius*C.radius-d*d,0))
    v=L.vectorize(); v.normalization()

    return [H+x*v,H-x*v]

def Intersection_between_Circle_and_Circle(C,D):
    """ 2つの円 C,D の交点を求める.

    """

    if not has_Intersection_between_Circle_and_Circle(C,D):
        return []

    r=C.radius; s=D.radius

    v=D.center-C.center
    d=abs(v)
    v.normalization()
    w=v*Point(0,1)

    x=(d*d+r*r-s*s)/(2*d)
    y=sqrt(max(r*r-x*x,0))
    return [C.center+x*v+y*w,C.center+x*v-y*w]

def Tangent_Circle_from_Point(P,C):
    """ 点 P から引く円 C への接線を求める."""

    v=C.center-P
    d=abs(v); v.normalization()
    r=C.radius

    x=sqrt(max(d*d-C.radius*C.radius,0))
    theta=asin(r/d)

    return [P+x*v.rotate(theta),P+x*v.rotate(-theta)]

def Circles_Intersection_Area(C,D):
    """ 2つの円 C, D の共通部分の面積を求める.

    C, D: Circle
    """

    d=abs(C.P-D.P)
    r=C.r; s=D.r
    ep=max(C.ep, D.ep)

    if compare(d,r+s,ep)==1:
        return 0
    if compare(d,abs(r-s),ep)==-1:
        a=min(r,s)
        return pi*a*a

    alpha=acos((d*d+r*r-s*s)/(2*d*r))
    beta =acos((d*d-r*r+s*s)/(2*d*s))

    X=r*r*alpha
    Y=s*s*beta
    Z=d*r*sin(alpha)
    return X+Y-Z
