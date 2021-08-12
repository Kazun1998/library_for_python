from Point import *
class Segment():
    __slots__=["begin","end","id"]

    ep=1e-9
    def __init__(self,P,Q):
        """2点 P, Q (P!=Q) を端点とする線分を生成する.


        P,Q: Point
        """
        assert P!=Q
        self.begin=P
        self.end=Q
        self.id=2

    def __str__(self):
        return "[Segment] {}, {}".format(self.begin,self.end)

    __repr__=__str__

    def __eq__(self,other):
        pass

    def __contains__(self,point):
        return iSP(self.begin,self.end,point)==2

    def vectorize(self):
        return self.end-self.begin

    def counter_vectorize(self):
        return self.begin-self.end

class Line():
    __slots__=["begin","end","id"]

    ep=1e-9
    def __init__(self,P,Q):
        """2点 P, Q (P!=Q) を通る直線を生成する.

        P,Q: Point
        """
        assert P!=Q
        self.begin=P
        self.end=Q
        self.id=3

    def __str__(self):
        return "[Line] {}, {}".format(self.begin,self.end)

    __repr__=__str__

    def __eq__(self,other):
        a=self.begin; b=self.end; c=other.begin; d=other.end
        return (b-a).det(c-d)==0 and (b-a).det(c-a)==0

    def __contains__(self,point):
        return abs(iSP(self.begin,point,self.end))!=1

    def vectorize(self):
        return self.end-self.begin

    def counter_vectorize(self):
        return self.begin-self.end

def Line_from_General_Form(a,b,c):
    """ ax+by+c=0 という形の直線を生成する.

    a,b,c: int or float ((a,b) neq (0,0))
    """

    assert (a!=0) or (b!=0)

    k=sqrt(a*a+b*b)

    if b==0:
        x=-c/a; y=0
    else:
        x=0; y=-c/b

    return Line(Point(x,y),Point(x-b/k, y+a/k))

#=== 交差判定
def has_Intersection_between_Segment_and_Segment(L,M,endpoint=True):
    """ 線分 L,M が交わるかどうかを判定する.

    L,M: 直線
    """

    a=L.begin; b=L.end; c=M.begin; d=M.end
    if not(iSP(a,b,c)*iSP(a,b,d)<=0 and iSP(c,d,a)*iSP(c,d,b)<=0):
        return False

    if endpoint:
        return True

def has_Intersection_between_Line_and_Segment(L,M,endpoint=True):
    """ 直線 L と線分 M が交わるかどうかを判定する.

    L: 直線
    M: 線分
    """

    a=L.begin; b=L.end; c=M.begin; d=M.end
    return iSP(a,b,c)*iSP(a,b,d)<=0

def has_Intersection_between_Line_and_Line(L,M):
    """ 直線 L,M が交わるかどうかを判定する.

    L,M: 直線
    """

    return compare(L.vectorize().det(M.vectorize()),0,max(L.ep,M.ep))!=0

def Intersection_between_Line_and_Line(L,M,Mode=False):
    """ 直線 L,M の交点を求める.

    L,M: 直線
    Mode=False: 交点が一意に定まらない場合エラーを吐く.
    Mode=True: 一致する場合, True, 交点が存在しない場合 False を返す.
    """

    if L==M:
        if Mode:
            return True
        else:
            assert 0,"直線が一致します"
    if is_Parallel(L,M):
        if Mode:
            return False
        else:
            assert 0,"交点が存在ません"

    a=L.begin; b=L.end; c=M.begin; d=M.end
    k=(c-a).det(d-c)/(b-a).det(d-c)
    return a+k*(b-a)

#=== 2直線の関係
def is_Parallel(L,M):
    """2つの直線 (線分) L,M が平行かどうかを判定する.

    L,M: 直線 or 線分
    """

    u=L.vectorize(); v=M.vectorize()
    return compare(u.det(v),0,max(L.ep,M.ep))==0

def is_Orthogonal(L,M):
    """2つの直線 (線分) L,M が直行するかどうかを判定する.

    L,M: 直線 or 線分
    """

    u=L.vectorize(); v=M.vectorize()
    return compare(u.dot(v),0,max(L.ep,M.ep))==0


#=== 点との距離
def Distance_betweem_Point_and_Segment(P,L):
    """ 点 P と線分 L の距離を求める.

    """

    A=L.begin; B=L.end
    if Angle_Type(P,A,B)==-1:
        return abs(P-A)
    elif Angle_Type(P,B,A)==-1:
        return abs(P-B)
    else:
        v=L.vectorize()
        return abs((P-L.begin).det(v)/abs(v)) 

def Distance_betweem_Point_and_Line(P,L):
    """ 点 P と直線 L の距離を求める.

    """

    v=L.vectorize()
    return abs((P-L.begin).det(v)/abs(v))

#=== 線同士の距離
def Distance_betweem_Line_and_Line(L,M):
    """ 2直線 L,M の距離を求める.

    L,M: 直線
    """

    if is_Parallel(L,M):
        return Distance_betweem_Point_and_Line(L.begin,M)
    else:
        return 0

def Distance_betweem_Line_and_Segment(L,M):
    """ 直線 L と線分 M の距離を求める.

    L: 直線, M: 線分
    """

    if has_Intersection_between_Line_and_Segment(L,M):
        return 0
    else:
        return min(
            Distance_betweem_Point_and_Line(M.begin, L),
            Distance_betweem_Point_and_Line(M.end, L)
            )

def Distance_betweem_Segment_and_Segment(L,M):
    """ 2線分 L,M の距離を求める.

    L,M: 線分
    """

    if has_Intersection_between_Segment_and_Segment(L,M):
        return 0

    return min(
        Distance_betweem_Point_and_Segment(L.begin,M),
        Distance_betweem_Point_and_Segment(L.end  ,M),
        Distance_betweem_Point_and_Segment(M.begin,L),
        Distance_betweem_Point_and_Segment(M.end  ,L)
        )
