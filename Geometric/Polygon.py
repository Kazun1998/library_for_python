from Point import *

class Polygon:
    __slots__ = ("vertices",)

    def __init__(self,*Points):
        self.vertices=list(Points)

    def __str__(self):
        return f"[Polygon] " + ", ".join(map(repr,self.vertices))

    __repr__ = __str__

    def area(self):
        S = 0
        p = self.vertices
        for i in range(len(p) - 1):
            S += p[i].det(p[i+1])
        S += p[-1].det(p[0])
        return abs(S) / 2

def Convex_Hull(S,online=False):
    """ S の凸包を求める.

    [Input]
    S: 点のリスト
    online: 辺上の点を認めるか.
    """

    from collections import deque

    T=sorted(S)

    #上側
    U=[]
    for p in T[::-1]:
        while len(U)>=2:
            m=iSP(U[-2],U[-1],p)
            if m==-1 or (not online and m==2):
                U.pop()
            else:
                break
        U.append(p)

    #下側
    L=[]
    for q in T:
        while len(L)>=2:
            m=iSP(L[-2],L[-1],q)
            if m==-1 or (not online and m==2):
                L.pop()
            else:
                break
        L.append(q)

    return Polygon(*(U+L[1:-1]))

def is_Convex(P: Polygon,rigit=True):
    """ 多角形 P が凸かどうかを判定する.

    P: Polygon
    right: True のとき, 辺上の点を認めない.
    """

    pass
