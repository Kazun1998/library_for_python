from Point import *
from Line import *
from Affine import *

class Circle:
    __slots__ = ("center", "radius")

    def __init__(self, center: Point, radius: float):
        """ 点 center を中心とする半径 radius の円を生成する.

        Args:
            center (Point): 中心
            radius (float): 半径
        """
        assert radius >= 0

        self.center = center
        self.radius = radius

    def __str__(self) -> str:
        return f"[Circle] center: {self.center}, radius: {self.radius}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(center = {repr(self.center)}, radius = {repr(self.radius)})"

    def __contains__(self, Point):
        return equal(abs(Point - self.center), self.radius)

#=== 交差判定
def has_Intersection_between_Circle_and_Segment(C,L,endpoint=True):
    """円 C と線分 L の交差判定を行う.

    """

    c = C.center
    flag1 = compare(Distance_between_Point_and_Segment(c, L), C.radius) <= 0
    flag2 = compare(max(abs(c - L.begin), abs(c - L.end)), C.radius) >=0
    return flag1 and flag2

def has_Intersection_between_Circle_and_Line(C,L):
    """円 C と直線 L の交差判定を行う.

    """
    return compare(Distance_between_Point_and_Line(C.center,L), C.radius) <= 0

def has_Intersection_between_Circle_and_Circle(C,D):
    """2つの円 C,D の交差判定を行う.

    """

    r=C.radius; s=D.radius;
    d=abs(C.center-D.center)

    return compare(d, abs(r - s)) >= 0 and compare(d, r + s) <= 0

#=== 交点を求める
def Intersection_between_Circle_and_Line(C,L):
    """ 円 C と直線 L の交点を求める.

    """

    if not has_Intersection_between_Circle_and_Line(C,L):
        return []

    H=Projection(C.Center,L)
    d=Distance_between_Point_and_Line(C.Center,L)
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

#=== 接線
def Tangent_to_Circle_on_Point(P,C):
    """ 円 C 上の点 P を接点とする接線を求める.

    """

    assert P in C
    v=(P-C.center)*Point(0,1)

    return Line(P,P+v)

def Tangent_to_Circle_from_Point(P,C):
    """ 点 P から引く円 C への接線を求める."""

    v=C.center-P
    d=abs(v); v.normalization()
    r=C.radius

    x=sqrt(max(d*d-r*r,0))
    theta=asin(r/d)

    return [Line(P,P+x*v.rotate(theta)),Line(P,P+x*v.rotate(-theta))]

def Common_Tangent_between_Circle_and_Circle(C,D):
    """ 円 C,D の共通接線を求める."""

    r=C.radius; s=D.radius
    d=abs(C.center-D.center)

    X=[]

    K=Circle(Point(),r)
    if compare(d,abs(r-s))>=0:
        a=r*(r-s)/d
        b=sqrt(max(0,r*r-a*a))

        X.append(Tangent_to_Circle_on_Point(Point(a,b),K))
        X.append(Tangent_to_Circle_on_Point(Point(a,-b),K))
    if compare(d,abs(r+s))>=0:
        a=r*(r+s)/d
        b=sqrt(max(0,r*r-a*a))

        X.append(Tangent_to_Circle_on_Point(Point(a,b),K))
        X.append(Tangent_to_Circle_on_Point(Point(a,-b),K))

    F=Translation_and_Rotate_Affine_Determine(Point(),Point(d,0),C.center,D.center)
    return [F[l] for l in X]

#=== 2つの円の位置関係を求める.
def Relationship_between_Circle_and_Circle(C: Circle, D:Circle) -> int:
    """ 2 つの円 C, D の位置関係を求める (返り値となる整数は 2 つの円の共通接線の本数と一致する).

    Args:
        C (Circle):
        D (Circle):

    Returns:
        int:
            4: 離れている
            3: 外接
            2: 交わっている
            1: 内接
            0: 含んでいる
    """

    d=abs(C.center-D.center)
    r=C.radius; s=D.radius

    alpha=compare(d,r+s)
    if alpha==1:
        return 4
    elif alpha==0:
        return 3
    else:
        beta=compare(d,abs(r-s))
        if beta==1:
            return 2
        elif beta==0:
            return 1
        else:
            return 0

#=== 共通部分
def Circles_Intersection_Area(C: Circle, D: Circle) -> float:
    """ 2つの円 C, D の共通部分の面積を求める.

    Args:
        C (Circle): 円
        D (Circle): 円

    Returns:
        float: 円 C と円 D の共通部分の面積
    """

    d = abs(C.center - D.center)
    r = C.radius
    s = D.radius

    if compare(d, r + s) == 1:
        # 2 つは離れている
        return 0

    if compare(d, abs(r - s)) == -1:
        # 一方が他方を含んでいる
        a = min(r, s)
        return pi * a * a

    alpha = acos((d * d + r * r - s * s) / (2 * d * r))
    beta = acos((d * d - r * r + s * s) / (2 * d * s))

    X = r *r * alpha
    Y = s * s * beta
    Z = d * r * sin(alpha)
    return X + Y - Z
