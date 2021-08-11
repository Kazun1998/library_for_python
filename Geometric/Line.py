from Point import *
class Line():
    __slots__=["P","Q","id"]

    ep=1e-9
    def __init__(self,P,Q):
        """2点 P, Q (P!=Q) を通る直線を生成する.


        P,Q: Point
        """
        assert P!=Q
        self.P=P
        self.Q=Q
        self.id=3

    def __str__(self):
        return "[Line] {}, {}".format(P,Q)

    __repr__=__str__

    def __eq__(self,other):
        pass

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

    a=L.P; b=L.Q; c=M.P; d=M.Q
    k=(c-a).det(d-c)/(b-a).det(d-c)
    return a+k*(b-a)
    

def is_Parallel(L,M):
    """2つの直線 (線分) L,M が平行かどうかを判定する.

    L,M: 直線 or 線分
    """

    u=L.Q-L.P; v=M.Q-M.P
    return compare(u.det(v),0,max(L.ep,M.ep))==0

def is_Orthogonal(L,M):
    """2つの直線 (線分) L,M が直行するかどうかを判定する.

    L,M: 直線 or 線分
    """

    u=L.Q-L.P; v=M.Q-M.P
    return compare(u.dot(v),0,max(L.ep,M.ep))==0
