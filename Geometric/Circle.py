class Circle():
    __slots__=["P","r","id"]

    ep=1e-9
    def __init__(self,Center:Point,Radius:float):
        """ 2点 P を中心とする半径 r の円を生成する.

        P: Point
        r>=0
        """
        assert Radius>=0

        self.P=Center
        self.r=Radius
        self.id=4

    def __str__(self):
        return "[Circle] Center: {}, Radius: {}".format(self.P,self.r)

    __repr__=__str__

    def __contains__(self,P):
        return abs(abs(P-self.P)-self.r)<self.ep

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
