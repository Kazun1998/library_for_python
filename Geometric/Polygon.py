from Point import *

class Polygon:
    __slots__=["vertices","id"]
    ep=1e-9

    def __init__(self,*Points):
        self.vertices=list(Points)
        self.id=7

    def __str__(self):
        return "[Polygon] "+", ".join(map(repr,self.vertices))

    __repr__=__str__

    def area(self):
        S=0
        p=self.vertices
        for i in range(len(p)-1):
            S+=p[i].det(p[i+1])
        S+=p[-1].det(p[0])
        return abs(S)/2

def Convex_Hull(S: list[Point], online = False) -> Polygon:
    """ S の凸包を求める

    Args:
        S (list[Point]): 点集合
        online (bool, optional): False のとき, 内角が 180 度になるのを許容しない. Defaults to False.

    Returns:
        Polygon: S の凸包
    """

    def cover(reverse_flag):
        vertices = []
        for P in (reversed(S) if reverse_flag else S):
            if not online and vertices and vertices[-1] == P:
                continue

            while len(vertices)>=2:
                m = iSP(vertices[-2], vertices[-1], P)
                if m == -1 or (not online and m == 2):
                    vertices.pop()
                else:
                    break
            vertices.append(P)
        return vertices

    S.sort()

    #上側
    upper = cover(True)

    #下側
    lower = cover(False)

    return Polygon(*(upper + lower[1:-1]))

def is_Convex(P: Polygon,rigit=True):
    """ 多角形 P が凸かどうかを判定する.

    P: Polygon
    right: True のとき, 辺上の点を認めない.
    """

    pass
